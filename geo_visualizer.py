import plotly.graph_objects as go
from plotly.subplots import make_subplots
import requests

def get_full_geo_data(ip):
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=2).json()
        if r['status'] == 'success':
            return r['lat'], r['lon'], f"{r['city']}, {r['country']}"
    except: return None

def create_world_map(connections):
    # Creamos una cuadrícula: 1 fila, 2 columnas (Mapa y Lista)
    fig = make_subplots(
        rows=1, cols=2,
        column_widths=[0.75, 0.25], # 75% mapa, 25% lista lateral
        specs=[[{"type": "scattergeo"}, {"type": "table"}]]
    )

    my_lat, my_lon = 40.4168, -3.7038 # Origen: España
    
    ips_list = []
    locations_list = []

    for _, dst, _ in connections:
        geo = get_full_geo_data(dst)
        if geo:
            lat, lon, city_country = geo
            ips_list.append(dst)
            locations_list.append(city_country)
            
            # Dibujar línea en el Mapa (Columna 1)
            fig.add_trace(go.Scattergeo(
                lon = [my_lon, lon], lat = [my_lat, lat],
                mode = 'lines', line = dict(width = 1.5, color = '#00ff41'),
                opacity = 0.4, hoverinfo='none'
            ), row=1, col=1)

            # Dibujar Punto en el Mapa (Columna 1)
            fig.add_trace(go.Scattergeo(
                lon = [lon], lat = [lat], mode = 'markers',
                marker = dict(size = 8, color = '#00d4ff'),
                text = f"IP: {dst}<br>Loc: {city_country}", hoverinfo = 'text'
            ), row=1, col=1)

    # Añadir Tabla Lateral (Columna 2) con la información breve
    fig.add_trace(go.Table(
        header=dict(
            values=['<b>DIRECCIÓN IP</b>', '<b>PROCEDENCIA</b>'],
            fill_color='#00ff41', align='left', font=dict(color='black', size=12)
        ),
        cells=dict(
            values=[ips_list, locations_list],
            fill_color='#1a1a1a', align='left', font=dict(color='white', size=11),
            height=30
        )
    ), row=1, col=2)

    # Configuración de diseño profesional
    fig.update_layout(
        title=dict(text="NETVISUALIZER: GLOBAL MONITOR & IP LOG", font=dict(size=22, color="#00ff41")),
        paper_bgcolor = 'black',
        margin={"r":10,"t":50,"l":10,"b":10},
        showlegend = False,
        geo = dict(
            projection_type = 'miller', showland = True,
            landcolor = "#111", oceancolor = "#050505",
            showocean = True, bgcolor = "black"
        )
    )

    fig.write_html("mapa_mundial.html")
    print("\n[!] Dashboard con panel lateral generado en mapa_mundial.html")

if __name__ == "__main__":
    # Prueba con datos reales
    test = [("PC", "8.8.8.8", "USA"), ("PC", "142.250.184.14", "Spain")]
    create_world_map(test)

