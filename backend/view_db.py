import sqlite3


def view_database():
    try:
        conn = sqlite3.connect('blog.db')
        cursor = conn.cursor()

        print("=" * 60)
        print("博客系统数据库查看工具")
        print("=" * 60)

        # 查看所有表
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print(f"\n数据库中的表: {[table[0] for table in tables]}")

        # 查看用户表
        print("\n" + "=" * 60)
        print("【用户表】users")
        print("=" * 60)

        cursor.execute("SELECT id, username, email, is_active, created_at FROM users;")
        users = cursor.fetchall()

        if users:
            for i, user in enumerate(users, 1):
                print(f"\n用户 {i}:")
                print(f"  ID: {user[0]}")
                print(f"  用户名: {user[1]}")
                print(f"  邮箱: {user[2]}")
                print(f"  是否活跃: {'是' if user[3] else '否'}")
                print(f"  创建时间: {user[4]}")
        else:
            print("暂无用户数据")

        # 查看文章表
        print("\n" + "=" * 60)
        print("【文章表】posts")
        print("=" * 60)

        cursor.execute("SELECT id, title, content, author_id, created_at FROM posts;")
        posts = cursor.fetchall()

        if posts:
            for i, post in enumerate(posts, 1):
                print(f"\n文章 {i}:")
                print(f"  ID: {post[0]}")
                print(f"  标题: {post[1]}")
                print(f"  内容预览: {post[2][:50]}..." if len(post[2]) > 50 else f"  内容: {post[2]}")
                print(f"  作者ID: {post[3]}")
                print(f"  创建时间: {post[4]}")
        else:
            print("暂无文章数据")

        # 查看评论表
        print("\n" + "=" * 60)
        print("【评论表】comments")
        print("=" * 60)

        cursor.execute("SELECT id, content, author_id, post_id, created_at FROM comments;")
        comments = cursor.fetchall()

        if comments:
            for i, comment in enumerate(comments, 1):
                print(f"\n评论 {i}:")
                print(f"  ID: {comment[0]}")
                print(f"  内容预览: {comment[1][:30]}..." if len(comment[1]) > 30 else f"  内容: {comment[1]}")
                print(f"  作者ID: {comment[2]}")
                print(f"  文章ID: {comment[3]}")
                print(f"  创建时间: {comment[4]}")
        else:
            print("暂无评论数据")

        conn.close()

    except sqlite3.Error as e:
        print(f"数据库错误: {e}")
    except Exception as e:
        print(f"其他错误: {e}")


if __name__ == "__main__":
    view_database()