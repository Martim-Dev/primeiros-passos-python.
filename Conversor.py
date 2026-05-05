print("--- CONVERSOR INTERNACIONAL ---")

while True:
    entrada = input("\nValor em Euros (ou 'sair'): ").replace(',', '.')
    
    if entrada.lower() == 'sair':
        print("A fechar o programa...")
        break
        
    try:
        euros = float(entrada)
        taxa_dolar = 1.08
        
        print(f"Em Dólares: ${euros * taxa_dolar:.2f}")
        print(f"Na Finlândia: {euros:.2f}€")
        
    except ValueError:
        print("Erro: Escreve apenas números (ex: 10.50)")

