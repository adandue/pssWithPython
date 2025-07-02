import random
import string

# Lista de palabras comunes a evitar
COMMON_WORDS = [
    'password', 'admin', 'user', 'login', 'qwerty', 'abc123', '123456',
    'letmein', 'welcome', 'monkey', 'dragon', 'iloveyou', '111111'
]

# Función para detectar secuencias simples
def is_sequential(password):
    sequences = ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '0123456789']
    for seq in sequences:
        for i in range(len(seq) - 3):  # buscar secuencias de 4 caracteres o más
            if seq[i:i+4] in password:
                return True
    return False

# Generador de contraseñas seguras
def generate_secure_password(length=12):
    if length < 12:
        raise ValueError("La longitud mínima debe ser 12 caracteres.")

    while True:
        # Asegurar al menos un carácter de cada tipo
        password_chars = [
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]

        # Completar el resto aleatoriamente
        all_chars = string.ascii_letters + string.digits + string.punctuation
        password_chars += random.choices(all_chars, k=length - 4)
        random.shuffle(password_chars)
        password = ''.join(password_chars)

        # Verificaciones
        lower = any(c.islower() for c in password)
        upper = any(c.isupper() for c in password)
        digit = any(c.isdigit() for c in password)
        special = any(c in string.punctuation for c in password)
        not_common = all(word not in password.lower() for word in COMMON_WORDS)
        not_sequence = not is_sequential(password)

        if lower and upper and digit and special and not_common and not_sequence:
            return password

# Ejemplo de uso
print("Contraseña segura generada:", generate_secure_password())
