import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass

def send_test_email(sender_email, password, smtp_server, port, use_ssl, recipient_email):
    """
    连接到SMTP服务器并发送一封测试邮件。

    :param sender_email: 发件人邮箱地址
    :param password: 邮箱密码或授权码
    :param smtp_server: SMTP 服务器地址
    :param port: SMTP 服务器端口
    :param use_ssl: 是否使用 SSL/TLS 直接连接 (True for port 465, False for 587/25)
    :param recipient_email: 收件人邮箱地址
    """
    # 1. 创建邮件对象
    message = MIMEMultipart("alternative")
    message["Subject"] = "SMTP 配置测试邮件 (SMTP Configuration Test)"
    message["From"] = sender_email
    message["To"] = recipient_email

    # 2. 构造邮件正文
    text_body = f"""
    你好!

    这是一封来自 Python SMTP 测试程序的邮件。
    发件人: {sender_email}
    
    如果你收到了这封邮件，说明你的SMTP配置是正确的。

    ---
    Hello!

    This is a test email from the Python SMTP test script.
    Sender: {sender_email}

    If you have received this email, your SMTP configuration is working correctly.

    ---
    测试配置信息:
    服务器 (Server): {smtp_server}
    端口 (Port): {port}
    使用SSL (SSL Mode): {'是 (Yes)' if use_ssl else '否 (No, using STARTTLS)'}
    """
    message.attach(MIMEText(text_body, "plain"))

    print("\n正在尝试连接到服务器并发送邮件...")

    # 3. 连接并发送
    try:
        # 根据 use_ssl 参数选择不同的连接方式
        if use_ssl:
            # 创建一个安全的SSL上下文并直接连接 (通常用于端口 465)
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, recipient_email, message.as_string())
        else:
            # 建立普通连接，然后升级到安全的TLS连接 (通常用于端口 587 或 25)
            with smtplib.SMTP(smtp_server, port) as server:
                server.starttls()  # 启用安全传输模式
                server.login(sender_email, password)
                server.sendmail(sender_email, recipient_email, message.as_string())

        print(f"✅ 邮件发送成功！请检查 '{recipient_email}' 的收件箱。")

    except smtplib.SMTPAuthenticationError:
        print("❌ 邮件发送失败: 认证错误。")
        print("   请检查你的用户名和密码（或授权码）是否正确。")
        print("   某些邮箱（如Gmail, QQ）需要使用专用的'应用密码'或'授权码'。")
    except smtplib.SMTPServerDisconnected:
        print("❌ 邮件发送失败: 服务器意外断开连接。")
        print("   可能是SSL/TLS设置与端口不匹配，请确认。")
    except ConnectionRefusedError:
        print("❌ 邮件发送失败: 连接被拒绝。")
        print("   请检查SMTP服务器地址和端口号是否正确，以及防火墙设置。")
    except Exception as e:
        print(f"❌ 邮件发送失败，发生未知错误: {e}")


if __name__ == "__main__":
    print("--- SMTP 发信配置测试工具 ---")
    print("本程序将从指定邮箱发送一封测试邮件到另一个邮箱。")

    # 获取用户输入
    smtp_server = input("请输入SMTP服务器地址 (e.g., smtp.gmail.com): ")
    port_str = input("请输入端口号 (e.g., 465 for SSL, 587 for TLS): ")
    sender_email = input("请输入你的邮箱地址 (Username/Sender): ")
    recipient_email = input("请输入收件人邮箱地址 (Recipient Email): ")
    # 使用 getpass 安全地输入密码
    password = getpass.getpass("请输入发件人邮箱的密码或授权码 (Password/App Password): ")
    ssl_input = input("连接是否使用 SSL? (是/否, y/n) [对于465端口填'是', 587端口填'否']: ").lower()

    # 数据处理
    try:
        port = int(port_str)
        use_ssl = ssl_input in ['y', 'yes', '是']
        
        # 调用发信函数
        send_test_email(sender_email, password, smtp_server, port, use_ssl, recipient_email)

    except ValueError:
        print("错误：端口号必须是一个数字。")
