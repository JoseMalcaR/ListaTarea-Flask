instructions = [
    'DROP TABLE IF EXISTS "todo";',
    'DROP TABLE IF EXISTS "user";',
    """
    CREATE TABLE "user" (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(100) NOT NULL
    );
    """,
    """
    CREATE TABLE "todo" (
        id SERIAL PRIMARY KEY,
        created_by INT NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        description TEXT NOT NULL,
        completed BOOLEAN NOT NULL,
        FOREIGN KEY (created_by) REFERENCES "user"(id)
    );
    """

]