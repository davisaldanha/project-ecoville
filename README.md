# project-ecoville
Project to complete the Object Oriented Programming course with Python in the technical course in Systems Development at Senac Ceará.


--

### 🌱 **Desafio: Sistema de Gestão de Resíduos Sustentáveis**

#### 📌 **Contextualização da Situação Problema**  
A cidade de Ecoville enfrenta um grande problema na gestão de resíduos sólidos. Muitos cidadãos não sabem como descartar corretamente seus resíduos, o que leva a um acúmulo desnecessário de lixo em aterros sanitários. Para resolver essa questão, a prefeitura deseja criar um sistema digital que ajude a **classificar resíduos**, **calcular o impacto ambiental do descarte incorreto** e **incentivar práticas sustentáveis** por meio de um programa de pontos ecológicos.  

#### 🎯 **Requisitos Funcionais do Sistema**  

1. **Classe `Residuo`**  
   - Representa um item descartável.  
   - Contém atributos como **nome**, **tipo** (`reciclável`, `orgânico`, `perigoso`, etc.), **peso em kg**.  
   - Método especial (`__str__`) para exibir detalhes do resíduo.  

2. **Classe `Coleta`**  
   - Gerencia o descarte dos resíduos.  
   - Possui uma lista de resíduos descartados corretamente.  
   - Método especial (`__len__`) para retornar o número total de resíduos cadastrados.  
   - Método especial (`__getitem__`) para acessar resíduos pelo índice.  

3. **Classe `Usuario`** 🏡  
   - Representa um cidadão que utiliza o sistema.  
   - Contém atributos como **nome**, **endereço**, **pontuação ecológica**.  
   - Método especial (`__eq__`) para comparar usuários com base na **pontuação sustentável**.  

4. **Classe `EstacaoReciclagem`** 🔄  
   - Representa um **ponto de coleta** de resíduos na cidade.  
   - Contém atributos como **localização** e **tipos de resíduos aceitos**.  
   - Método especial (`__contains__`) para verificar se um tipo de resíduo é aceito na estação.  

5. **Sistema de Pontuação Sustentável**  
   - Cada resíduo descartado corretamente gera **pontos ecológicos**.  
   - Criar um método `__add__` na classe `Residuo`, que permita **somar os pontos dos resíduos** para incentivar práticas sustentáveis.  

#### 🏆 **Atividade para ser realizada**  
O desafio consiste em:  
1. **Implementar as classes `Residuo`, `Coleta`, `Usuario` e `EstacaoReciclagem`** com os métodos especiais descritos.  
2. Criar um pequeno programa que instancie objetos dessas classes e teste suas funcionalidades.  
3. Adicionar uma funcionalidade extra para exibir **sugestões de descarte correto** dependendo do tipo de resíduo.


### 🔋 **Desafio: Sistema Inteligente de Gestão de Energia Residencial**  

#### 📌 **Contextualização da Situação Problema**  
O consumo excessivo de eletricidade em residências tem levado ao aumento da demanda por energia, causando impactos ambientais como maior emissão de carbono. Para resolver esse problema, as empresas de energia desejam desenvolver um sistema inteligente que monitore e otimize o consumo de eletricidade em tempo real, recomendando boas práticas e alternativas sustentáveis.  

#### 🎯 **Requisitos Funcionais do Sistema**  

1. **Classe `Dispositivo`**  
   - Representa um aparelho eletrônico da casa.  
   - Contém atributos como **nome**, **potência (W)** e **tempo médio de uso diário (horas)**.  
   - Método especial (`__str__`) para exibir detalhes do dispositivo.  

2. **Classe `Residencia`**  
   - Gerencia os dispositivos em uma casa.  
   - Possui uma lista de dispositivos elétricos cadastrados.  
   - Método especial (`__len__`) para contar o número total de aparelhos na residência.  
   - Método especial (`__getitem__`) para acessar um dispositivo pelo índice.  

3. **Classe `PainelSolar`** 🌞  
   - Representa um **sistema de energia solar** instalado na residência.  
   - Contém atributos como **capacidade de geração (kWh)** e **eficiência média**.  
   - Método especial (`__sub__`) para calcular a economia de energia proporcionada pelos painéis solares.  

4. **Classe `RelatorioEnergetico`** 📊  
   - Calcula o consumo total da residência e sugere maneiras de reduzir o gasto energético.  
   - Método especial (`__call__`) para processar os dados dos dispositivos e gerar um relatório personalizado.  
   - Exibe recomendações como troca de lâmpadas por LED, uso de sensores de presença, entre outras dicas.  

#### 🏆 **Atividade para ser realizada**  
O desafio consiste em:  
1. **Implementar as classes `Dispositivo`, `Residencia`, `PainelSolar` e `RelatorioEnergetico`** com os métodos especiais descritos.  
2. Criar um pequeno programa que instancie objetos dessas classes e simule uma residência com dispositivos elétricos e painéis solares.  
3. Adicionar funcionalidades extras, como alerta de **pico de consumo** e sugestões para reduzir gastos.  
