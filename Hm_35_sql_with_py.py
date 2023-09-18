import sqlite3

# Создание базы данных и подключение к ней
with sqlite3.connect('shopIT.db') as con:
    cur = con.cursor()

    # Создание таблицы "Компьютеры"
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Computers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            
            type VARCHAR(255) NOT NULL,
            brand VARCHAR(255) NOT NULL,
            price DECIMAL(10, 2) NOT NULL
        );
    ''')

    # Вставка данных в таблицу "Компьютеры"
    cur.execute('''
        INSERT INTO Computers (type, brand, price)
        
        VALUES
            ('ноутбук', 'HP', 45000.00),
            ('стационарный компьютер', 'Dell', 55000.00),
            ('моноблок', 'HP', 42000.00),
            ('ноутбук', 'Lenovo', 32000.00),
            ('стационарный компьютер', 'HP', 48000.00);
    ''')

    # Запросы и вывод результатов
    print("Все компьютеры бренда 'HP':")
    cur.execute('SELECT * FROM Computers WHERE UPPER(brand) = "HP";')
    for row in cur.fetchall():
        print(row)

    print("\nКомпьютеры стоимостью более 40000:")
    cur.execute('SELECT * FROM Computers WHERE price > 40000;')
    for row in cur.fetchall():
        print(row)

    print("\nКомпьютеры типа 'ноутбук' и стоимостью менее 30000:")
    cur.execute('SELECT * FROM Computers WHERE type = "ноутбук" AND price < 30000;')
    for row in cur.fetchall():
        print(row)