# 账号数据结构: {"用户名": ["用户名", "密码", "状态"], ...}
accounts = {}

try:
    # 读取账号数据
    with open("数据.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:  # 确保不是空行
                parts = line.split(",")
                if len(parts) == 3:  # 确保每行有3个部分
                    accounts[parts[0]] = parts
                else:
                    print(f"警告: 忽略格式不正确的行: {line}")

    print("当前账号数据:", accounts)  # 调试用

    # 用户登录逻辑
    while True:
        try:
            user = input("Username (输入q退出):").strip()
            if user.lower() == 'q':
                break

            if user not in accounts:
                print("该用户未注册...")
                continue

            # 检查账号状态 (假设"1"是正常，"0"是锁定)
            if accounts[user][2] == "0":
                print("该账号已被锁定，请联系管理员")
                continue

            # 密码尝试
            count = 0
            while count < 3:
                try:
                    password = input("Password:").strip()
                    if password == accounts[user][1]:
                        print(f"Welcome {user}...登录成功...")
                        break  # 退出密码输入循环
                    else:
                        count += 1
                        remaining_attempts = 3 - count
                        if remaining_attempts > 0:
                            print(f"密码错误，还剩{remaining_attempts}次尝试")
                        else:
                            print("密码错误次数过多，账号将被锁定")

                except KeyboardInterrupt:
                    print("\n操作已取消")
                    break
                except Exception as e:
                    print(f"发生错误: {e}")
                    break

            # 如果输错3次密码，锁定账号
            if count == 3:
                accounts[user][2] = "0"  # 锁定账号
                print(f"账号 {user} 已被锁定")

                # 更新文件
                try:
                    with open("数据.txt", "w") as f:
                        for username in accounts:
                            account = accounts[username]
                            f.write(f"{account[0]},{account[1]},{account[2]}\n")
                except Exception as e:
                    print(f"无法保存账号状态: {e}")

        except KeyboardInterrupt:
            print("\n操作已取消")
            continue
        except Exception as e:
            print(f"发生错误: {e}")
            continue

except FileNotFoundError:
    print("错误: 账号文件1.txt不存在")
except Exception as e:
    print(f"程序初始化错误: {e}")

print("程序退出")
