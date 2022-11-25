import sqlite3

try:

    banco = sqlite3.connect('db.sqlite3')

    cursor = banco.cursor()

    # alterando um registro da tabela

    cursor.execute("UPDATE teacher_professor SET nome = 'Nelio Alves' WHERE id = 3")



    # cursor.execute("INSERT INTO teacher_professor VALUES (4,'Mayk Brito', 150, 'Instrutor focado em ajudar pessoas iniciantes na programação WEB. Ensina HTML, CSS, Javascript, SQL.', 'https://github.com/maykbrito.png')")

    banco.commit()
    banco.close()
    print("Foto alterada com sucesso.")

except sqlite3.Error as erro:
    print("Erro ao excluir: ", erro)
