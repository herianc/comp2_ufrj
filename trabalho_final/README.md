# Trabalho final da Disciplina de COMPUTAÇÃO 2 - UFRJ (Ainda incompleto)

**Ideia:** Jogo da Forca com tema sobre Geociências/Estatística. Jogo com três níveis de dificuldade (Fácil, Médio e Difícil) para cada tema; Sistema de pontuação do usuário com relação ao tempo de resposta e número de tentativas em cada palavra.

**(Abstração (classe, objeto e método)**
**Herança (simples ou múltipla)** - Classe mãe Tema com métodos de níveis de dificuldade. As classes Geociências e Estatística são filhas desta classe.
**Encapsulamento**: Pontuação do Jogador
**Polimorfismo** - As classes filhas terão palavras diferentes em cada método (dificuldades)
**Classe abstrata/interface** - Classe Tema que será molde para os temas do jogo (Geociências, Estatística); Classe Jogador  
**Tratamento de exceções** - Tratamento de entradas inválidas do jogador.
**Persistência de dados**: Armazenamento da pontuação do jogador
**Uso de bibliotecas diversas**: Biblioteca `time` para cronometrar o tempo de resposta do usuário/ `Tkinter` para interface gráfica
