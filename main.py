from engine import sniff, IP, get_ip_location
from geo_visualizer import create_world_map # Usamos solo el mapa mundial mejorado
import sys

captured_data = []

def monitor_callback(packet):
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        
        # Filtramos tráfico local para que el mapa sea profesional
        if not ip_dst.startswith(("192.", "127.", "10.")):
            location = get_ip_location(ip_dst)
            
            # Formato para el mapa: (Origen, Destino, Localización)
            connection = ("Mi_PC", ip_dst, location)
            
            if connection not in captured_data:
                captured_data.append(connection)
                print(f"[+] Conexión detectada: {ip_src} -> {ip_dst} ({location})")

print("="*50)
print("NETVISUALIZER: CAPTURANDO TRÁFICO REAL")
print("Navega por internet y pulsa Ctrl+C para ver el mapa final.")
print("="*50)

try:
    # Captura paquetes (puedes quitar 'count' para captura infinita)
    sniff(prn=monitor_callback, store=False, count=50)
except KeyboardInterrupt:
    pass

if captured_data:
    print("\nGenerando mapa mundial con panel lateral...")
    create_world_map(captured_data)
else:
    print("\nNo se detectó tráfico externo.")

