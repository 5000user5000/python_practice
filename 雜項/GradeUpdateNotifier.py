import requests
import hashlib
import smtplib
from email.mime.text import MIMEText
import time
import os

score_url = "https://if163.aca.ntu.edu.tw/eportfolio/student/CourseSem.asp" #epo的網址
login_ur = score_url  #和score_url 相同，因為使用這網頁會先跳轉到登入介面，之後會跳回首頁。所以得用score_url 再跳轉一次

email_config = {
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'sender_email': 'xxx@gmail.com',
    'sender_password': 'gmail 應用程式的密碼，要先二階段認證',
    'recipient_email': '收件者的email'
}

login_credentials = {
    'username': '學校登入成績的使用者名稱',
    'password': '帳號'
}


def read_previous_content():
    # 从文件或数据库中读取之前的网页内容
    print("开始读取之前的网页内容")
    with open('previous_content.txt', 'r') as file:  #也可以用json
        content = file.read()
    return content

def save_current_content(content):
    # 将当前的网页内容保存到文件或数据库中
    print("开始保存当前网页内容")
    content_hash = hashlib.md5(content.encode()).hexdigest()  # 使用MD5算法计算网页内容的哈希值，以便后续比较。且必須先encode
    with open('previous_content.txt', 'w') as file:
        file.write(content_hash)

def login_to_website():
    # 使用提供的凭据登录到成绩网页
    print("开始登录")
    session = requests.Session()
    
    login_data = {
        'username': login_credentials['username'],
        'password': login_credentials['password']
    }
    
    response = session.post(login_ur, data=login_data)

    print("登录成功")
    print(response.status_code)
    # 检查登录是否成功，可以根据具体情况判断
    if response.status_code == 200:
        return session
    else:
        raise Exception('登录失败')

def check_grades_update(session):
    # 使用会话对象或Cookie等来检查成绩是否有更新
    print("开始检查成绩是否更新")
    response = session.get(score_url)
    current_content = response.text

    if os.path.isfile("previous_content.txt") == False:
        save_current_content(current_content)
        return False

    previous_content = read_previous_content()
    
    if previous_content != hashlib.md5(current_content.encode()).hexdigest():
        return True
    else:
        return False

def send_email_notification(subject, message):
    print("开始发送邮件")
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = email_config['sender_email']
    msg['To'] = email_config['recipient_email']

    with smtplib.SMTP(email_config['smtp_server'], email_config['smtp_port']) as server:
        server.starttls()
        server.login(email_config['sender_email'], email_config['sender_password'])
        server.sendmail(email_config['sender_email'], [email_config['recipient_email']], msg.as_string())

def main():
    print("开始运行")
    session = login_to_website()

    
    # 检查是否有更新，如果有则发送邮件通知
    # while True:
    #     if check_grades_update(session):
    #         subject = "学校成绩已更新"
    #         message = "你的学校成绩已经更新，请登录查看。"
    #         send_email_notification(subject, message)

    #         response = session.get(score_url)
    #         current_content = response.text
    #         save_current_content(current_content)

    #     time.sleep(3600)  # 每隔一小时检查一次更新

    # 仅检查一次
    if check_grades_update(session):
        subject = "学校成绩已更新"
        message = "你的学校成绩已经更新，请登录查看。"
        send_email_notification(subject, message) #有可能會被當作垃圾郵件，所以去垃圾桶查看

        response = session.get(score_url)
        current_content = response.text
        save_current_content(current_content)

if __name__ == "__main__":
    main()
