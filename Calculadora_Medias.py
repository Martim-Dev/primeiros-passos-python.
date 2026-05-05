print("--- CALCULADORA DE MÉDIA ESCOLAR ---")

while True:
    try:
        # Pede as notas (usa .replace para aceitar vírgulas)
        nota1 = float(input("\nNota do 1º teste: ").replace(',', '.'))
        nota2 = float(input("Nota do 2º teste: ").replace(',', '.'))
        
        media = (nota1 + nota2) / 2
        
        print(f"A tua média final é: {media:.1f}")
        
        # Sistema de decisão
        if media >= 9.5:
            print("Resultado: Estás POSITIVO! 🎉")
        else:
            print("Resultado: Estás NEGATIVO. Estuda mais! 📚")
            
        continuar = input("\nQueres calcular outra média? (s/n): ")
        if continuar.lower() != 's':
            print("A fechar calculadora...")
            break
            
    except ValueError:
        print("Erro: Introduz apenas números (ex: 14.5)")

