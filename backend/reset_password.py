import sqlite3
from backend.auth import get_password_hash


def reset_password(username, new_password):
    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()

    # 生成新密码的哈希
    hashed_password = get_password_hash(new_password)

    # 更新用户密码
    cursor.execute(
        "UPDATE users SET hashed_password = ? WHERE username = ?",
        (hashed_password, username)
    )

    if cursor.rowcount > 0:
        conn.commit()
        print(f"✓ 用户 '{username}' 密码已重置为: {new_password}")
        print(f"新密码哈希: {hashed_password}")
    else:
        print(f"✗ 用户 '{username}' 不存在")

    conn.close()


if __name__ == "__main__":
    username = input("请输入要重置密码的用户名: ")
    new_password = input("请输入新密码: ")
    reset_password(username, new_password)