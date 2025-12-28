from scapy.all import sniff, IP
import requests

# Diccionario para no repetir consultas a la API (caché)
geo_cache = {}

def get_ip_location(ip):
    """Consulta la ubicación de una IP externa"""
    if ip in geo_cache:
        return geo_cache[ip]
    
    # Filtramos IPs privadas (tu casa) para no gastar la API
    if ip.startswith(("192.", "10.", "172.")):
        return "Local Network"

    try:
        # Usamos una API gratuita de geolocalización
        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        if response['status'] == 'success':
            location = f"{response['city']}, {response['country']}"
            geo_cache[ip] = location
            return location
    except:
        return "Unknown"
    return "External"

def process_packet(packet):
    """Función que se ejecuta por cada paquete capturado"""
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        
        # Si el destino no es tu red local, geolocalizamos
        if not ip_dst.startswith("192."):
            location = get_ip_location(ip_dst)
            print(f"[+] Conexión detectada: {ip_src} -> {ip_dst} ({location})")

print("--- NetVisualizer Activo ---")
print("Capturando tráfico... (Presiona Ctrl+C para detener)")


sniff(prn=process_packet, store=False, count=100)