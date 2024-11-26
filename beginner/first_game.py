print("Bem-vindo ao jogo pequeno aventureiro")
name = input("Como te chamas? ")
age = int(input("Quantos anos tens? "))

print("Olá", name, "tens", age, "anos")

health = 10

def check_health():
  if health <= 0:
      print("Perdeste o jogo... Mais sorte na próxima vez!")
      return True
  return False

if age >= 8:
  print("Boa! Tens idade para jogar!")

  wants_to_play = input("Queres jogar seu maluquitos bons? ").lower()
  if wants_to_play == "sim":
    print("Boa! Vamos começar!")
    print("Tens", health, "pontos de vida")
    
    left_or_right = input("Primeira escolha... Esquerda ou Direita? ").lower()
    if left_or_right == "esquerda":

      answer = input("Boa, seguis-te o caminho e chegas-te a um rio... Vais nadar ou esperar um barco? ").lower()

      if answer == "esperar um barco":
        print("O barco tinha um buraco e foi ao fundo. Conseguis-te nadar, mas perdes-te 5 pontos de vida")
        health -= 5
        if check_health():
          exit()
          
      elif answer == "nadar":
        print("Oh não! Conseguis-te atravessar, mas foste mordido por um peixe e perdes-te 5 pontos de vida")
        health -= 5
        if check_health():
          exit()
          
      answer = input("Chegas-te a um castelo. Vais entrar ou seguir o caminho? ").lower()
      if answer == "seguir o caminho":
        print("Foste atacado por cães e perdes-te 5 pontos de vida.")
        health -= 5
        health -= 5
        if check_health():
          exit()
          
      else:
        print("Muito bem! Entras-te no castelo e ganhas-te o jogo!!!")
          
    else:
      print("Caíste e perdeste...")

  else:
    print("Até uma próxima pequeno aventureiro!")

else:
  print("Desculpa, mas não tens idade para jogar!")