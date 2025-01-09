def dividir(conjunto):
  def conquistar(conjunto, indice, soma_atual, soma_total):
    if indice == len(conjunto): # Caso base: se não houver mais elementos
      return soma_atual == soma_total // 2
  
    # Tenta incluir o elemento atual no primeiro subconjunto
    if conquistar(conjunto, indice + 1, soma_atual + conjunto[indice], soma_total):
      return True
    # Tenta incluir o elemento atual no segundo subconjunto
    if conquistar(conjunto, indice + 1, soma_atual, soma_total):
      return True

    return False

  return conquistar(conjunto, 0, 0, sum(conjunto))
