# Automação de Cadastro de Produtos (RPA com Python)

Script de RPA que lê uma base de produtos em CSV e cadastra cada item, campo a
campo, num sistema web — sem intervenção manual. Feito durante meus estudos
de automação em Python (ambiente de prática do curso Intensivão Python, da
Hashtag Treinamentos), aplicando o mesmo raciocínio que uso hoje pra
automação de processos operacionais no trabalho.

## O que ele resolve

Cadastro manual, campo a campo, é repetitivo, sujeito a erro de digitação e
não escala. Com uma base de ~290 produtos (`produtos.csv`), o script:

1. Abre o navegador e faz login no sistema
2. Lê a base com `pandas`
3. Para cada linha, preenche o formulário (código, marca, tipo, categoria,
   preço unitário, custo, observação) e envia o cadastro
4. Trata o campo `obs` como opcional — pula a escrita quando ele vem vazio
   (`pandas.isna`), em vez de escrever `"nan"` no formulário

## Stack

| ferramenta | papel |
|---|---|
| `pandas` | leitura e iteração da base de dados (CSV → linhas a processar) |
| `pyautogui` | controle de mouse e teclado — simula a digitação humana |
| `python-dotenv` | carrega as credenciais de um `.env` local, fora do código |

## Como rodar

```bash
pip install -r requirements.txt
cp .env.example .env    # preencha com suas credenciais
python codigo.py
```

`pegar_posicao.py` é o utilitário auxiliar usado pra mapear as coordenadas de
clique antes de rodar o script principal — ele só imprime a posição atual do
mouse após 5 segundos, pra dar tempo de posicionar sobre o campo certo.

## Decisões técnicas e limitações conhecidas

Documentar o que não está perfeito é parte de mostrar maturidade técnica, não
só o que funciona:

- **Dependência de coordenada de tela fixa** (`pyautogui.click(x=652, y=356)`
  pra abrir o primeiro campo). Funciona porque o layout do sistema de treino
  é estável, mas é o ponto mais frágil do script — qualquer mudança de
  resolução ou layout quebra a automação. Num RPA de produção, isso seria
  substituído por seleção de elemento por atributo/seletor, não por
  coordenada.
- **Sem tratamento de exceção ou retry.** Se uma linha falhar no meio do
  preenchimento, o script não percebe e segue pra próxima. Próximo passo
  natural seria logar cada cadastro (sucesso/falha) e permitir retomar de
  onde parou.
- **Credenciais fora do código.** Na versão original o login estava
  hardcoded no script — foi corrigido para variável de ambiente via
  `python-dotenv` antes de publicar este repositório.

## Próximos passos

- Adicionar log de execução (quantos cadastrados, quantos falharam, quando)
- Trocar os cliques por coordenada fixa por seleção de elemento, onde o
  sistema permitir
- Empacotar como função reutilizável, com testes (`pytest`) cobrindo o
  tratamento de campo opcional
