def dividir(conjunto):
  conjunto.sort(reverse=True)   # Ordena o conjunto em ordem decrescente

  subconjunto1 = []
  subconjunto2 = []
  soma1 = 0
  soma2 = 0

  for elemento in conjunto:
    if soma1 <= soma2:  # Adiciona o elemento ao subconjunto com a menor soma
      subconjunto1.append(elemento)
      soma1 += elemento
    else:
      subconjunto2.append(elemento)
      soma2 += elemento

  return soma1 == soma2