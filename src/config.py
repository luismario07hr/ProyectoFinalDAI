import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# --- AÑADE ESTAS DOS LÍNEAS PARA DEPURAR ---
print(f"-> DEBUG URL: '{SUPABASE_URL}'")
print(f"-> DEBUG KEY: '{SUPABASE_KEY[:10]}...'")
# -------------------------------------------

if not SUPABASE_URL or not SUPABASE_KEY:
    raise RuntimeError(
        "Faltan SUPABASE_URL o SUPABASE_KEY. Copie .env.example como .env y complete los valores."
    )