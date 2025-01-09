import time
from algoritmos import divisao, guloso

def main():
  # Define o conjunto de entrada
  conjunto = [8, 3, 4, 12, 21]
  # conjunto = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, -1, -2, -3, -4]
  # conjunto = [i for i in range(-25, 50)]
  
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