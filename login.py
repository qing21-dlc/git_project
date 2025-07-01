def login():
    """基础登录函数"""
    # 预存储的有效凭据（实际应用中应从数据库读取）
    valid_credentials = {
        "admin": "Admin@123",  # 用户名: 密码
        "user1": "Passw0rd!",
        "test_user": "Test#2023"
    }

    # 获取用户输入
    username = input("请输入用户名: ").strip()
    password = input("请输入密码: ").strip()

    # 验证逻辑
    if not username or not password:
        print("\n错误：用户名和密码不能为空！")
        return False
    
    if username in valid_credentials:
        if password == valid_credentials[username]:
            print(f"\n✅ 登录成功！欢迎回来，{username}！")
            return True
        else:
            print("\n❌ 密码错误！")
    else:
        print("\n❌ 用户名不存在！")
    
    return False

# 测试登录函数
if __name__ == "__main__":
    print("=== 系统登录 ===")
    login()
