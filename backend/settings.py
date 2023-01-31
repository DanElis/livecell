import environs

env = environs.Env()

HOST = env.str("HOST", "127.0.0.1")
PORT = env.int("PORT", 8000)
