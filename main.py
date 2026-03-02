import time
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import database
import config

def enviar_correo(lista_tareas):
    cuerpo = "🔔 RECORDATORIO DE TAREAS PENDIENTES 🔔\n\n"
    for nombre, desc in lista_tareas:
        cuerpo += f"📌 {nombre}: {desc}\n"
    
    msg = MIMEText(cuerpo)
    msg['Subject'] = f"Aviso por Hora - {datetime.now().strftime('%H:%M')}"
    msg['From'] = config.EMAIL_EMISOR
    msg['To'] = config.EMAIL_DESTINO

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(config.EMAIL_EMISOR, config.PASSWORD_APP)
            server.send_message(msg)
        print(f"[{datetime.now().strftime('%H:%M')}] Correo enviado a {config.EMAIL_DESTINO}")
    except Exception as e:
        print(f"Error al enviar: {e}")

if __name__ == "__main__":
    database.inicializar_db()
    print("🚀 Sistema de avisos iniciado. No cierres esta ventana.")
    
    while True:
        tareas = database.obtener_pendientes()
        if tareas:
            enviar_correo(tareas)
        else:
            print("Zzz... No hay tareas pendientes.")
            
        time.sleep(config.INTERVALO_AVISO)