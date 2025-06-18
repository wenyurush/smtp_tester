# SMTP 发信配置测试工具

这是一个简单的命令行Python脚本，用于测试您的SMTP（简单邮件传输协议）配置是否正确。它通过引导您输入必要的参数（服务器、端口、用户名、密码等），然后尝试发送一封测试邮件，来验证您的设置。

This is a simple command-line Python script designed to test your SMTP (Simple Mail Transfer Protocol) configuration. It guides you through entering the necessary parameters (server, port, username, password, etc.) and then attempts to send a test email to verify your settings.

## ✨ 主要功能 (Features)

- **交互式输入**: 通过命令行提示，引导用户输入所有必需的配置信息。
- **安全密码输入**: 使用 `getpass` 模块输入密码，密码不会在屏幕上明文显示。
- **灵活的收发件人**: 支持自定义发件人和收件人邮箱地址。
- **协议自适应**: 能够根据端口和用户的选择，自动处理 `SSL` (如端口465) 和 `STARTTLS` (如端口587) 两种安全连接方式。
- **清晰的反馈**: 无论发送成功还是失败，都会提供明确的提示信息，帮助定位问题。
- **零依赖**: 仅使用Python标准库，无需安装任何第三方包。

## 📋 环境要求 (Prerequisites)

- **Python 3.x**

## 🚀 如何使用 (How to Use)

1.  **下载脚本**:
    将脚本代码保存为一个文件，例如 `smtp_test.py`。

2.  **打开终端**:
    打开您的命令行工具（例如 Windows 的 `CMD` 或 `PowerShell`，macOS/Linux 的 `Terminal`）。

3.  **运行脚本**:
    在终端中，导航到脚本所在的目录，并运行以下命令：
    ```bash
    python smtp_test.py
    ```

4.  **输入配置信息**:
    根据屏幕上的提示，依次输入您的SMTP配置。以下是一个示例过程：

    ```
    --- SMTP 发信配置测试工具 ---
    本程序将从指定邮箱发送一封测试邮件到另一个邮箱。
    请输入SMTP服务器地址 (e.g., smtp.gmail.com): smtp.qq.com
    请输入端口号 (e.g., 465 for SSL, 587 for TLS): 465
    请输入你的邮箱地址 (Username/Sender): your-email@qq.com
    请输入收件人邮箱地址 (Recipient Email): recipient@example.com
    请输入发件人邮箱的密码或授权码 (Password/App Password): 
    连接是否使用 SSL? (是/否, y/n) [对于465端口填'是', 587端口填'否']: y

    正在尝试连接到服务器并发送邮件...
    ✅ 邮件发送成功！请检查 'recipient@example.com' 的收件箱。
    ```

## ⚠️ 重要提示 (Important Notes)

### 1. 授权码 (App Password / Authorization Code)

出于安全原因，大多数主流邮箱服务商（如Gmail, QQ, 163等）不再允许直接使用您的登录密码通过第三方客户端访问SMTP服务。您必须在邮箱的网页设置中，开启 `IMAP/SMTP` 服务，并生成一个专用的 **授权码** (或称 **应用专用密码**)。

**在脚本中输入密码时，请使用此授权码，而不是您的邮箱登录密码！**

### 2. SSL vs. STARTTLS

这是最常见的配置混淆点。请确保您的端口号和SSL选项匹配：

- **使用 SSL (端口 465)**:
  - 连接从一开始就是加密的。
  - 当脚本提示 `连接是否使用 SSL?` 时，您应该输入 `是` 或 `y`。

- **使用 STARTTLS (端口 587 或 25)**:
  - 连接以明文开始，然后通过 `STARTTLS` 命令升级为加密连接。
  - 当脚本提示 `连接是否使用 SSL?` 时，您应该输入 `否` 或 `n`。
 ## 🔍 错误排查 (Troubleshooting)

- **`SMTPAuthenticationError`**:
  - **原因**: 认证失败。
  - **解决方法**: 检查您的用户名（邮箱地址）和密码（**授权码**）是否完全正确。确认您使用的是授权码而不是登录密码。

- **`ConnectionRefusedError` 或 `SMTPServerDisconnected`**:
  - **原因**: 连接问题。
  - **解决方法**:
    1.  检查您的SMTP服务器地址和端口号是否正确。
    2.  确认您的 `SSL/STARTTLS` 设置与端口号匹配（见上文）。
    3.  检查您的网络连接或防火墙设置是否阻止了对外端口的访问。

- **其他 `Exception`**:
  - **原因**: 可能存在其他网络问题或服务商的临时限制。
  - **解决方法**: 仔细阅读错误信息，或在网上搜索该错误代码。


> Forged in human-AI light.
