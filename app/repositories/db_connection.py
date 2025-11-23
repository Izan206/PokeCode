import sqlite3

def get_connection():
    conn = sqlite3.connect("data/pokemons.db")
    conn.row_factory=sqlite3.Row #Esto hara que lo que se devuelvan sean listas de diccionarios
    return conn