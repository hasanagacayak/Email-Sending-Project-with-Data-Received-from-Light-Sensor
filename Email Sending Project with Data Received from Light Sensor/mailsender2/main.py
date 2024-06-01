import smtplib
import serial
import xlsxwriter
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

arduino = serial.Serial("COM3", 9600)
data_rx = arduino.readline()
current_time = datetime.now().strftime("%d-%m-%Y")
current_time2 = datetime.now().strftime("%d%m%Y")
excel = xlsxwriter.Workbook("data.xlsx")
excelSheet = excel.add_worksheet(f"{current_time2}")
excelSheet1 = excel.add_worksheet(f"{current_time}")
i = 1

def send_email(subject, body, sender_email, receiver_email, sender_pwd):
    smtp_server = 'smtp.office365.com'  # veya 'smtp.live.com' (Hotmail için)
    smtp_port = 587  # veya 465 (Hotmail için)

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_pwd)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("E-posta başarıyla gönderildi.")
    except Exception as e:
        print("E-posta gönderirken bir hata oluştu:", str(e))

# Kullanım örneği
def main():
    global i
    while i < 10:
        current_time1 = datetime.now().strftime("%H:%M:%S")
        # Arduino'dan veri okuma
        data = arduino.readline().decode().strip()
        excelSheet.write("A1", "Lümen")
        excelSheet.write("B1", "Tarih")
        excelSheet.write("C1", "Saat")
        data_value = int(data)
        if data_value > 500:
            sender_email = 'miaalarm666@hotmail.com'
            sender_password = 'miaalarm4207'
            receiver_email = 'umut.konyali@miateknoloji.com'
            subject = 'Uyarı E-posta'
            body = f'Yüksek ışık seviyesi, e-posta bu yüzden gönderiliyor. Lümen= {data_value}'
            send_email(subject, body, sender_email, receiver_email, sender_password)
            print("Tehlikeli Işık Değeri", "Lümen=", data)
        elif 200 < data_value <= 500:
            print("Normal Işık Değeri", "Lümen=", data)
        elif data_value <= 200:
            print("Düşük Işık Değeri", "Lümen=", data)

        excelSheet.write(f"A{i + 1}", data_value)
        excelSheet.write(f"B{i + 1}", current_time)
        excelSheet.write(f"C{i + 1}", current_time1)
        # print(f"Excel Hücresi: A{i + 1}, Değer: {data_value}")
        i = i + 1
    excel.close()

if __name__ == "__main__":
    main()
