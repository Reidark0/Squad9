# Vamos iniciar o Trabalho aqui.
# Tomem cuidado para mexer só na parte de vocês para não quebrar o programa
# Se não forem mexer sozinhos usem branchs para codar e depois façam o merge.
# Não economizem nos commits, pode fazer vários sem medo.
# 
# Nos Commits escrevam no início:
# "feature: " ao adicionar coisas
# "edit: " se editarem alguma coisa, sem adicionar nada
# "fix: se consetarem algum problema no código "
# "Style: " se a mudança for na aparencia do código
# e descrevam oque você fez.
# 
# Lembrem de Dar git pull antes de começar a codar pra editar o código mais recente

print('Bem-vindo à Barbearia 90S')
nome = (input('Qual seu nome? '))
print('Olá', nome)

servicos = 1
agendamento = 2
duvidas = 3
sair = 4

print('1. Serviços')
print('2. Agendamento')
print('3. Dúvidas')
print('4. Sair')

selecione = (int(input(f'Escolha uma opção para começar:' )))

if (selecione == 1):

       resposta = int((input(f'Qual serviço você gostaria?\n{1} Corte de cabelo.\n{2} Barba e cabelo.\n{3} Completo: Barba, cabelo\n bigode e sobrancelha\nDigite o número do serviço: ')))
       print(f'Você escolheu o serviço', resposta)

       confirmacao = input('Agendar? (sim/não): ')

       while (confirmacao == 'sim') or (confirmacao == 'nao'):
              if confirmacao == 'sim':
                dia = input(f'{1} terça-feira\n{2} quarta-feira\n{3} quinta-feira\n{4} sexta-feira\n{5} sábado\n Qual dia gostaria de agendar?')
                hora = input('Qual horário gostaria de agendar? ')
                print(f'Você está agendado para: ', dia, hora)
                break

if (selecione == 3):
       resposta2 = input(f'O que você gostaria de saber?\n{1} Dia e horário de funcionamento\n{2} Localização\n{3} Formas de pagamento\n Selecione uma opção:')
if resposta2 == 1: 
       print('Funcionamos de segunda à sexta das 9h às 21h')
elif resposta2 == 2:
       print('Estamos localizados na Rua das Palmeiras, 33')
