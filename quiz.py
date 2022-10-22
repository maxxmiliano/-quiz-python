#iniciando mini projeto quiz
print("olá esse um  mini quiz")

resp_usuario = input("Vamos responder o quiz? (s/n)")

if resp_usuario != "s":
    quit()
score = 0

print("começando...")   
print("Qual o maior país do mundo ? \n (a) China\n (b) Rússia\n (c) Canadá\n (d) Mônaco")
resposta_1 = input("resposta: ")

if resposta_1 == "B":
    print("correto! ")
    score = score+1 
else:
    print("incorreto! ")

  
print("Quais as duas datas que são comemoradas em novembro?\n (a) Independencia do Brasil e dia da Bandeira\n (b) Proclamação da República e dia Nacional da consciência negra\n (c) Dia de Finados e Dia nacional do livro\n (d) black Friday e dia da arvore  ")

resposta_2 = input("resposta: ")

if resposta_2 == "B":
    print("correto! ")
    score = score+1
else:
    print("incorreto! ")    
    
print("Em qual local da Ásia o português é lingua oficial?\n (a) Macau\n (b) Índia\n (c) Filipinas\n (d) Moçanbique")

resposta_3 = input("resposta: ")

if resposta_3 == "a":
    print("correto! ")
    score = score+1
else:
    print("incorreto! ")    

print(f"Quiz acabou...Sua pontuação é: {score}/2")
