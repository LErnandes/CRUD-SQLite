import sqlite3
p_nome = input('Nome: ')
try:
    with open('pref.db', 'r') as f:
        conn = sqlite3.connect('pref.db')

        cursor = conn.cursor()
        
        cursor.execute("""
INSERT INTO preferencias (nome)
VALUES (?);
""", (p_nome,))
        
        cursor.execute("""
SELECT * FROM preferencias;
""")
        for linha in cursor.fetchall():
            print(linha)
        conn.close()
        
except IOError:
    conn = sqlite3.connect('pref.db')

    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE preferencias
        (nome varchar(30) NOT NULL)""")
    print('Tabela criada com sucesso.')
    cursor.execute("""
INSERT INTO preferencias (nome)
VALUES (?);
""", (p_nome,))
    cursor.execute("""
SELECT * FROM preferencias;
""")
    for linha in cursor.fetchall():
            print(linha)

    conn.close()


