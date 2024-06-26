import re

import aiosqlite


# D:\Projects\BOTS\bot_pioneer\data\districts.db
def get_db_path():
    return r'C:\Users\IT2.UMFC-KO\PycharmProjects\bot\bot_pioneer\data\districts.db'


async def insert_user(district_id, user_id, user_name, user_firstname, user_lastname):
    async with aiosqlite.connect(get_db_path()) as conn:
        await conn.execute(
            'INSERT INTO users (district_id, user_id, user_name, user_nickname, role) SELECT ?, ?, ?, ?, ?'
            'WHERE NOT EXISTS ('
            'SELECT 1 FROM users '
            'WHERE user_id = ?)',
            (district_id, user_id, user_name, f"{user_firstname} {user_lastname}", "admin", user_id))
        await conn.commit()


async def select_userid(district_id):
    async with aiosqlite.connect(get_db_path()) as conn:
        cursor = await conn.execute("SELECT user_id FROM users WHERE district_id = ?", (district_id,))
        data = await cursor.fetchall()
        return [row[0] for row in data]


async def select_admins_same_district(admin_id):
    async with aiosqlite.connect(get_db_path()) as conn:
        cursor = await conn.execute("SELECT district_id FROM users WHERE user_id = ?", (admin_id,))
        current_admin_district = await cursor.fetchone()

        if current_admin_district:
            current_district_id = current_admin_district[0]
            cursor = await conn.execute("SELECT user_id FROM users WHERE district_id = ?", (current_district_id,))
            return [row[0] for row in await cursor.fetchall()]
    return []


async def delete_admin(admin_id):
    async with aiosqlite.connect(get_db_path()) as conn:
        await conn.execute("DELETE FROM users WHERE user_id = ?", (admin_id,))
        await conn.commit()


# DELETE FROM users WHERE user_id = ?
async def add_order_info(district_id, order_number, order_description, from_user, data_time):
    async with aiosqlite.connect(get_db_path()) as conn:
        await conn.execute('''INSERT INTO orders (district_id, order_description, from_user, order_number, time)
                              VALUES (?, ?, ?, ?, ?)''',
                           (district_id, order_description, from_user, order_number, data_time))
        await conn.commit()


async def add_worker(who_take_order, order_number):
    async with aiosqlite.connect(get_db_path()) as conn:
        await conn.execute('''UPDATE orders
                              SET who_take_order = ?
                              WHERE order_number = ?''', (who_take_order, convert_string_to_int(str(order_number))))
        await conn.commit()


def convert_string_to_int(input_string):
    return re.sub(r'\D', '', input_string)


async def store_order_number(order_number):
    async with aiosqlite.connect(get_db_path()) as conn:
        await conn.execute("DELETE FROM order_number")
        await conn.execute("INSERT INTO order_number (order_number) VALUES (?)", (order_number,))
        await conn.commit()


async def get_order_number():
    async with aiosqlite.connect(get_db_path()) as conn:
        cursor = await conn.execute("SELECT order_number FROM order_number")
        data = await cursor.fetchall()
        return [row[0] for row in data]


async def get_order_info(district_id):
    await clear_db()
    async with aiosqlite.connect(get_db_path()) as conn:
        cursor = await conn.execute("SELECT * FROM orders WHERE district_id = ? ORDER BY id DESC LIMIT 10;",
                                    (district_id,))
        results = await cursor.fetchall()
    return list(results)


async def clear_db():
    async with aiosqlite.connect(get_db_path()) as conn:
        cursor = await conn.execute('SELECT COUNT(*) FROM orders')
        count = (await cursor.fetchone())[0]
        if count > 1000:
            await conn.execute('''
                               DELETE FROM orders
                               WHERE id NOT IN (
                                   SELECT id FROM orders
                                   ORDER BY id DESC
                                   LIMIT ?
                               )
                               ''', (count // 2,))
            await conn.commit()


def check_none_string(text):
    return "" if text is None else text
