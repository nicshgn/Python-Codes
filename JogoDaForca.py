Palavra1 = "goianesia"
LetrasDescobertas = ["_"] * len(Palavra1)
Tentativas = 6
palpite = []

print("Jogue forca e descubra a fruta favorita de joão:)")

while Tentativas > 0 and "_" in LetrasDescobertas:
  print("Palavra: ", " ".join(LetrasDescobertas))
  print("Tentativas restantes: ", Tentativas)
  SuaTentativa = input("Digite uma letra para tentar adivinhar: \n\n").lower()

  if SuaTentativa in palpite:
    print("VOCE JA USOU ESSA LETRA, USA OUTRA LETRAAAA")
    continue

  palpite.append(SuaTentativa)

  if SuaTentativa in Palavra1.lower():
    for i in range(len(Palavra1)):
      if Palavra1[i] == SuaTentativa:
        LetrasDescobertas[i] = SuaTentativa
    print("ACERTOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOUUUUUUUUUUUUU!!!!!!!!")
  else:
    print("Errou seu animal >:( dica: (sua dica aqui) ")
    Tentativas -= 1

  if Tentativas == 0:
    print("Perdeu! A palavra era: ", Palavra1)
    
 if "_" not in LetrasDescobertas:
   print("PARABENS AAAAAAAAAA\n")
   print("A palavra era: ", Palavra1)
