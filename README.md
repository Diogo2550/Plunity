# Plunity

Projeto particular criado para permitir uma criação mais componentizada de jogos utilizando a framework PPlay ([site](http://www2.ic.uff.br/pplay/)) criada pela UFF.

O seu nome é uma trocadilho com a *Game Engine Unity* pois a criação do Plunity será inspirado pela mesma.

---
## Como instalar
Para instalar basta clonar este repositório e rodar o comando 

> python main.py

na pasta do projeto para executar o app padrão.

---
## Como utilizar
Ainda não há uma maneira correta de como se deverá ser utilizado pois o *framework* ainda está engatinhando e seus *scripts core* não foram finalizados. A ideia final, porém, é que, assim como a *Unity*, seu game tenha centenas de *gameobjects* e cada *gameobject* tenha seu comportamento encapsulado dentro de si e possua o auxilio de componentes pré prontos para implementação de ações padrões, como gravidade e colisão.

---
## Classes padrões

### core.GameObject
Classe que deverá ser herdada por TODOS os *gameobjects* presentes em cena. Ela proporcionará o uso de componentes padrões da *framework* assim como proporcionará métodos padrões que poderão ser editados para a customização do comportamento de seu objeto.

No momento, alguns métodos já estão disponíveis para uso:

**def _start(self):**
Método chamado na inicialização do jogo. Atributos e parâmetros inicias, como a posição inicial do objeto em cena, devem ser adicionados aqui.

**def _update(self):**
Método executado antes do fim de cada frame do jogo, utilizado para atualizar o comportamento de um objeto em cena.

**def _afterUpdated(self):**
Método chamado após a execução do *_update*, ainda não possui muita ultilidade.

**def setPosition(self, position):**
Método que recebe um Vector2 e define a posição do objeto em cena.

**def addComponent(self, componentType):**
Um dos principais métodos da classe GameObject. Permite a adição de componentes que alteração o comportamento *ingame* de um determinado objeto. Componentes são scripts que herdam da classe core.Component.

**def getComponent(self, componentType):**
Permite obter um determinado tipo de componente que está presente no *gameobject*. Muito útil para modificar o comportamento de uma componente e tornar seu jogo mais customizado.