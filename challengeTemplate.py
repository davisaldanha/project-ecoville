class Residuo:
    def __init__(self, nome, tipo, peso, pontos):
        self.nome = nome
        self.tipo = tipo
        self.peso = peso
        self.pontos = pontos

    def __str__(self):
        return f"Resíduo: {self.nome} | Tipo: {self.tipo} | Peso: {self.peso}kg | Pontos: {self.pontos}"

    def __add__(self, other):
        return self.pontos + other.pontos


class Coleta:
    def __init__(self):
        self.residuos = []

    def adicionar_residuo(self, residuo):
        self.residuos.append(residuo)

    def __len__(self):
        return len(self.residuos)

    def __getitem__(self, index):
        return self.residuos[index]


class Usuario:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.pontos_ecologicos = 0

    def adicionar_pontos(self, pontos):
        self.pontos_ecologicos += pontos

    def __eq__(self, other):
        return self.pontos_ecologicos == other.pontos_ecologicos

    def __str__(self):
        return f"Usuário: {self.nome} | Endereço: {self.endereco} | Pontos Ecológicos: {self.pontos_ecologicos}"


class EstacaoReciclagem:
    def __init__(self, localizacao, tipos_aceitos):
        self.localizacao = localizacao
        self.tipos_aceitos = tipos_aceitos

    def __contains__(self, tipo_residuo):
        return tipo_residuo in self.tipos_aceitos

    def __str__(self):
        return f"Estação de Reciclagem em {self.localizacao} | Tipos aceitos: {', '.join(self.tipos_aceitos)}"

# Simulação do sistema
usuario1 = Usuario("Davi", "Fortaleza, CE")
estacao1 = EstacaoReciclagem("Centro", ["reciclável", "orgânico"])

residuo1 = Residuo("Garrafa PET", "reciclável", 0.5, 10)
residuo2 = Residuo("Casca de banana", "orgânico", 0.3, 5)

coleta = Coleta()
coleta.adicionar_residuo(residuo1)
coleta.adicionar_residuo(residuo2)

usuario1.adicionar_pontos(residuo1 + residuo2)

# Exibição de resultados
print(usuario1)
print(estacao1)
print(f"Total de resíduos cadastrados: {len(coleta)}")
print(f"Primeiro resíduo cadastrado: {coleta[0]}")
print(f"O resíduo '{residuo1.nome}' pode ser descartado na estação? {'Sim' if residuo1.tipo in estacao1 else 'Não'}")
