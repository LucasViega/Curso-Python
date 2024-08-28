"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 61 # velocidade atual do carro
local_carro = 101 # local em que o carro está na estrada


RADA_1 = 60 # Velocidade máxima radar 1
LOCAL_1 = 100 # Local onde o radar 1 está
RADAR_RANGE = 1 # A distancia onde o radar pega

velocidade_carro_passou_radar_1 = velocidade > RADA_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1

if velocidade_carro_passou_radar_1:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1:
    print('carro multado em radar 1')
