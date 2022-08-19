import smtplib
from email.message import EmailMessage


def alert_system(product, link):
    """email_id = "vishal_sharma704@yahoo.com"
    email_pass = "@Billu704"

    msg = EmailMessage()
    msg['Subject'] = "Price Drop Alert"
    msg['From'] = email_id
    msg['To'] = "vishal_sharma704@yahoo.com" # receiver address
    msg.set_content(f"Hey, price of {product} dropped!\n{link}")

    with smtplib.SMTP_SSL("smtp.yahoo.com", 465) as smtp:
        smtp.login(email_id, email_pass)
        smtp.send_message(msg)"""
        
    # your Gmail account 
    import smtplib
    
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    
    # start TLS for security
    s.starttls()
    
    # Authentication Your Email Address That You Used IN Solution 1
    s.login("vs704.vs@gmail.com", "okvlxfrsbnmwcdql")
    
    # message to be sent
    message = "Hey, price of " + product + " dropped!" + "\n" + link
    
    # sending the mail
    s.sendmail("vs704.vs@gmail.com", "vs704.vs@gmail.com", message)
    
    # terminating the session
    s.quit()