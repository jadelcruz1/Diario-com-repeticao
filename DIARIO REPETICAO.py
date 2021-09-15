#COLOCAR COMENTARIO

Data = input('Digite a data do documento:') # informar aqui a data do documento que deu origem ao lançamento contábil.

Debito = int(input('Digite a conta debito:')) # aqui será inserido conta cotábil débito (ATIVO OU DESPESA).

Credito = int(input('Digite a conta credito:')) # aqui será inserido conta cotábil crédito (passivo OU receita).

Valor = float(input('Digite o valor:'))# o valor será o expresso em documento fiscal ou contabil.

Historico = input('Digite a que se refere o lançamento:') # esse historico é a para informar  qual documento deu origem ao lançamento (NF, Contrato,  NF de serviço, DARF, etc).


while (Debito != Credito): # estrutura de repetição criada para repetir lancamentos contabeis - finalidade gerar livros razão e Diario.
    print('{}'.format(Data))
    print( 'Debito {}' .format(Debito))
    print('Credito {}' .format(Credito))
    print('R$ {}' .format(Valor))
    print('Vr ref pagamento de {}' .format(Historico))
    break # break inserido para que não gere loop inifnito, desde que satisfeita a condição. Assim evito de colocar um contador nao algoritimo que não vem ao caso.

else:  # aqui essa condição foi para que as contas debito e credito não sejam iguai, pois o balancete irá ter ATIVO diferente de Passivo.
    print('conta debito não pode ser igual a debito')


