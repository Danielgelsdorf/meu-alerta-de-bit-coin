import smtplib
import email.message
import time
import requests as req
from datetime import datetime
def main():
    now = datetime.now()
    print('atualisado em ',now.day,now.month,now.year,'as',now.hour,now.minute)
    
    dolar=req.get("http://economia.awesomeapi.com.br/json/last/USD-BRL")
    cotacao=dolar.json()
    final=float(cotacao['USDBRL']['bid'])
    print('O dólar atual está em: R$',final)
    bit=req.get('https://www.mercadobitcoin.net/api/BTC/ticker/')
    cota=bit.json()
    fim=float(cota['ticker']['sell'])
    print("a cotação atual de venda do bit coin é:R$",fim)
    def enviar_email(fim,final):
        corpo_email = f"""
        <h1> veja aqui as cotações</h1>
        <p> pode vender seus bit coins</p>
        <p> cotação atual do dólar{final}, cotação atual do bit{fim}</p>
        """
        msg = email.message.Message()
        msg['Subject'] = "posso vender minhas cripto"
        msg['From'] = 'gelsdorfdaniel@gmail.com'
        msg['To'] = 'afonsodaniel985@gmail.com'
        password = 'fvrcygrtsprebrhy'
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email )
        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        # Login Credentials for sending the mail
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print('Email enviado')
    if fim > 130000:
        enviar_email(fim,final)
i=1
while i > 0:
    main()
    time.sleep(100)
    main()
