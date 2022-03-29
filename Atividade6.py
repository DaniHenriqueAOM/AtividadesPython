nm_vdr = str(input("Digite o nome do vendedor: "))
cd_peca = int(input("Digite o código da peça: "))
p_unt_peca = float(input("Digite o valor unitário da peça: "))
qtd_vnd = int(input("Digite a quantidade vendida: "))

com_vdr = (qtd_vnd * p_unt_peca)
com_vdr = com_vdr * 0.05

print(f"\nidentificação do vendedor: {nm_vdr}\nTotal vendido: {qtd_vnd}\nValor da comissão: {com_vdr}")
