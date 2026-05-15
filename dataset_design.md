
# Desenho do Dataset

## 1. Unidade de análise

Cada linha representa um usuário exposto a uma imagem de produto durante uma campanha de e-commerce.

## 2. Colunas do dataset

- user_id
- image_type
- gender
- age_group
- customer_type
- page_views
- clicks
- time_on_page
- converted
- purchase_value

## 3. Tipos de dados

- user_id: número inteiro, identificador único do usuário.
- image_type: texto, indicando o tipo de imagem exibida para o usuário.
- gender: texto, indicando o gênero do cliente.
- age_group: texto, indicando a faixa etária do cliente.
- customer_type: texto, indicando se o cliente é novo ou recorrente.
- page_views: número inteiro, indicando quantas vezes o usuário visualizou a página.
- clicks: número inteiro/binário, indicando se o usuário clicou ou não.
- time_on_page: número decimal, indicando o tempo do usuário na página em segundos.
- converted: número inteiro/binário, indicando se o usuário realizou compra ou não.
- purchase_value: número decimal, indicando o valor da compra. Caso não haja conversão, o valor será 0.

## 4. Regras de simulação

O dataset será simulado com usuários distribuídos aleatoriamente entre dois grupos de teste:

- Grupo A: imagem de estúdio
- Grupo B: imagem lifestyle

Cada usuário terá atributos como gênero, faixa etária e tipo de cliente. As métricas de clique, tempo na página, conversão e valor de compra serão geradas de forma probabilística, considerando que cada tipo de imagem pode ter uma performance diferente.

A imagem lifestyle terá uma probabilidade ligeiramente maior de clique e conversão, simulando a hipótese de que esse tipo de imagem gera mais engajamento e vendas.

## 5. Relação esperada entre imagem e conversão

Espera-se que usuários expostos a imagens lifestyle apresentem maior taxa de conversão do que usuários expostos a imagens de estúdio.

A hipótese é que imagens lifestyle ajudam o cliente a visualizar melhor o produto em contexto real de uso, aumentando a intenção de compra.

## 6. Possíveis vieses ou limitações

- Os dados serão simulados, portanto não representam necessariamente o comportamento real de consumidores.
- A primeira versão do projeto terá apenas duas variantes visuais.
- A simulação pode simplificar fatores importantes, como preço, marca, categoria do produto e sazonalidade.
- Diferenças entre segmentos podem ser artificiais, pois serão definidas manualmente na geração dos dados.
- O projeto inicial não analisará imagens reais, apenas o impacto associado ao tipo de imagem.
