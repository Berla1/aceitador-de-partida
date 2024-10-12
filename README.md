
# Match Acceptor

Este repositório contém um projeto desenvolvido para automatizar a aceitação de partidas em jogos online, nesse caso League of Legends. A ferramenta é capaz de detectar a janela de confirmação de partida e automaticamente aceitar o jogo, otimizando o tempo do usuário.

## Funcionalidades

- **Detecção automática**: O sistema detecta a janela de confirmação de partida em tempo real.
- **Automação de Aceitação**: Quando uma nova partida é encontrada, a confirmação é feita automaticamente, sem necessidade de interação manual.
- **Customização**: Configurações ajustáveis para diversos jogos.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal utilizada.
- **OpenCV**: Para captura e processamento de imagem.
- **PyAutoGUI**: Para automação da interface gráfica, clicando automaticamente no botão de confirmação.
- **Time**: Para controle de intervalos e timing na automação.

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/Berla1/aceitador-de-partida.git
    cd aceitador-de-partida
    ```

2. Execute o projeto:
    ```bash
    python main.py
    ```

## Como usar

1. Execute o script e certifique-se de que a janela do jogo está visível.
2. O script irá monitorar automaticamente a tela e aceitar a partida assim
   que a janela de confirmação aparecer.

