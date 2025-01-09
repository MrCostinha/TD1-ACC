import time
from algoritmos import divisao, guloso

def main():
  # Define o conjunto de entrada
  conjunto = [2, 5, 3, 12, 9, 11]

  algoritmos = {
      "Divisão e Conquista": divisao.dividir,
      "Guloso": guloso.dividir,
  }
  
  soma_total = sum(conjunto)

  # Executa cada algoritmo e mede o tempo de execução
  for nome, algoritmo in algoritmos.items():
      if soma_total % 2 != 0:
        print("Não é possível dividir o conjunto com soma ímpar")
      else:
        inicio = time.time()
        resultado = algoritmo(conjunto.copy())  # Usa uma cópia do conjunto para cada algoritmo
        fim = time.time()
        tempo_execucao = fim - inicio
        print(f"{nome}: {resultado} (Tempo: {tempo_execucao:.6f} segundos)")

if __name__ == "__main__": # Executa a função main() se o script for executado diretamente
  main()