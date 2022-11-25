import sqlite3

try: 

    banco = sqlite3.connect('db.sqlite3')
    
    cursor = banco.cursor()

    # excluindo um registro da tabela
    cursor.execute("DELETE FROM teacher_professor WHERE id = 1")

    banco.commit()
    banco.close()
    print("Registro excluido com sucesso.")

except sqlite3.Error as erro:
    print("Erro ao excluir: ",erro)
