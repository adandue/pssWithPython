import random
import string
import secrets

def generar_contraseña_segura(longitud=12):
    """
    Genera una contraseña segura con los siguientes requisitos:
    - Al menos 12 caracteres (por defecto)
    - Al menos una letra mayúscula
    - Al menos una letra minúscula
    - Al menos un número
    - Al menos un carácter especial
    - Evita patrones predecibles
    """
    
    if longitud < 12:
        raise ValueError("La longitud mínima debe ser 12 caracteres")
    
    # Definir conjuntos de caracteres
    minusculas = string.ascii_lowercase
    mayusculas = string.ascii_uppercase
    numeros = string.digits
    especiales = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Palabras comunes a evitar (lista básica)
    palabras_comunes = [
        'password', 'contraseña', '123456', 'qwerty', 'admin', 'login',
        'usuario', 'welcome', 'hello', 'hola', 'casa', 'amor', 'familia'
    ]
    
    # Patrones secuenciales a evitar
    secuencias_prohibidas = [
        'abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz',
        '123', '234', '345', '456', '567', '678', '789', '890',
        'qwe', 'wer', 'ert', 'rty', 'tyu', 'yui', 'uio', 'iop',
        'asd', 'sdf', 'dfg', 'fgh', 'ghj', 'hjk', 'jkl',
        'zxc', 'xcv', 'cvb', 'vbn', 'bnm'
    ]
    
    def contiene_secuencia_prohibida(contraseña):
        """Verifica si la contraseña contiene secuencias prohibidas"""
        contraseña_lower = contraseña.lower()
        for secuencia in secuencias_prohibidas:
            if secuencia in contraseña_lower:
                return True
        return False
    
    def contiene_palabra_común(contraseña):
        """Verifica si la contraseña contiene palabras comunes"""
        contraseña_lower = contraseña.lower()
        for palabra in palabras_comunes:
            if palabra in contraseña_lower:
                return True
        return False
    
    def tiene_repeticiones_excesivas(contraseña):
        """Verifica si hay más de 2 caracteres consecutivos iguales"""
        for i in range(len(contraseña) - 2):
            if contraseña[i] == contraseña[i+1] == contraseña[i+2]:
                return True
        return False
    
    def es_contraseña_segura(contraseña):
        """Valida que la contraseña cumpla todos los requisitos de seguridad"""
        # Verificar longitud
        if len(contraseña) < longitud:
            return False
        
        # Verificar que contenga al menos un carácter de cada tipo
        tiene_minuscula = any(c in minusculas for c in contraseña)
        tiene_mayuscula = any(c in mayusculas for c in contraseña)
        tiene_numero = any(c in numeros for c in contraseña)
        tiene_especial = any(c in especiales for c in contraseña)
        
        if not (tiene_minuscula and tiene_mayuscula and tiene_numero and tiene_especial):
            return False
        
        # Verificar que no contenga patrones inseguros
        if (contiene_secuencia_prohibida(contraseña) or 
            contiene_palabra_común(contraseña) or 
            tiene_repeticiones_excesivas(contraseña)):
            return False
        
        return True
    
    # Generar contraseña hasta obtener una segura
    max_intentos = 1000
    intentos = 0
    
    while intentos < max_intentos:
        # Asegurar que tenemos al menos un carácter de cada tipo
        contraseña = [
            secrets.choice(minusculas),
            secrets.choice(mayusculas),
            secrets.choice(numeros),
            secrets.choice(especiales)
        ]
        
        # Completar con caracteres aleatorios
        todos_caracteres = minusculas + mayusculas + numeros + especiales
        for _ in range(longitud - 4):
            contraseña.append(secrets.choice(todos_caracteres))
        
        # Mezclar la contraseña para evitar patrones
        random.shuffle(contraseña)
        contraseña_str = ''.join(contraseña)
        
        # Verificar si es segura
        if es_contraseña_segura(contraseña_str):
            return contraseña_str
        
        intentos += 1
    
    raise Exception("No se pudo generar una contraseña segura después de múltiples intentos")

def evaluar_fortaleza_contraseña(contraseña):
    """
    Evalúa la fortaleza de una contraseña existente
    """
    puntuacion = 0
    feedback = []
    
    # Longitud
    if len(contraseña) >= 12:
        puntuacion += 2
    elif len(contraseña) >= 8:
        puntuacion += 1
    else:
        feedback.append("La contraseña es demasiado corta")
    
    # Tipos de caracteres
    if any(c.islower() for c in contraseña):
        puntuacion += 1
    else:
        feedback.append("Falta al menos una letra minúscula")
    
    if any(c.isupper() for c in contraseña):
        puntuacion += 1
    else:
        feedback.append("Falta al menos una letra mayúscula")
    
    if any(c.isdigit() for c in contraseña):
        puntuacion += 1
    else:
        feedback.append("Falta al menos un número")
    
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in contraseña):
        puntuacion += 1
    else:
        feedback.append("Falta al menos un carácter especial")
    
    # Diversidad de caracteres
    if len(set(contraseña)) >= len(contraseña) * 0.8:
        puntuacion += 1
    else:
        feedback.append("Tiene demasiados caracteres repetidos")
    
    # Clasificación de fortaleza
    if puntuacion >= 6:
        fortaleza = "Muy fuerte"
    elif puntuacion >= 4:
        fortaleza = "Fuerte"
    elif puntuacion >= 2:
        fortaleza = "Moderada"
    else:
        fortaleza = "Débil"
    
    return {
        'puntuacion': puntuacion,
        'fortaleza': fortaleza,
        'feedback': feedback
    }

# Función principal de demostración
def main():
    """Función principal que demuestra el uso del generador"""
    print("=== Generador de Contraseñas Seguras ===\n")
    
    # Generar algunas contraseñas de ejemplo
    longitudes = [12, 16, 20]
    
    for longitud in longitudes:
        print(f"Contraseña de {longitud} caracteres:")
        contraseña = generar_contraseña_segura(longitud)
        print(f"  {contraseña}")
        
        # Evaluar la contraseña generada
        evaluacion = evaluar_fortaleza_contraseña(contraseña)
        print(f"  Fortaleza: {evaluacion['fortaleza']} (Puntuación: {evaluacion['puntuacion']}/7)")
        print()
    
    # Ejemplo de evaluación de contraseñas débiles
    print("=== Evaluación de Contraseñas Débiles ===\n")
    contraseñas_ejemplo = [
        "123456",
        "password",
        "Contraseña1",
        "MiContraseña123!",
        "P@ssw0rd2024"
    ]
    
    for contraseña in contraseñas_ejemplo:
        evaluacion = evaluar_fortaleza_contraseña(contraseña)
        print(f"Contraseña: {contraseña}")
        print(f"Fortaleza: {evaluacion['fortaleza']} (Puntuación: {evaluacion['puntuacion']}/7)")
        if evaluacion['feedback']:
            print(f"Sugerencias: {', '.join(evaluacion['feedback'])}")
        print()

# Ejecutar el programa si se ejecuta directamente
if __name__ == "__main__":
    main()