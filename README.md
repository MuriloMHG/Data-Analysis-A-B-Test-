# PT-BR

## Pipeline de Testes A/B para Ativos Visuais

### 1. Visão Geral do Projeto

Empresas de e-commerce investem altos valores na produção de imagens de produtos, como fotos de estúdio e imagens lifestyle, mas muitas vezes não possuem evidências estatísticas sobre qual estilo visual realmente gera melhor desempenho de marketing.

Este projeto simula e analisa um teste A/B comparando dois tipos de imagens de produto:

- **Imagens de estúdio**
- **Imagens lifestyle**

O objetivo é avaliar qual tipo de imagem apresenta melhor desempenho em métricas importantes de marketing, como taxa de cliques, taxa de conversão, tempo na página e receita média por usuário.

### 2. Problema de Negócio

Times de marketing e criação frequentemente tomam decisões visuais com base em estética, intuição ou preferência de marca. Porém, essas decisões podem impactar diretamente o engajamento dos usuários, a conversão e a receita.

Este projeto busca responder à seguinte pergunta:

> Imagens lifestyle performam melhor do que imagens de estúdio em termos de engajamento e resultados de negócio?

### 3. Dataset

O dataset utilizado neste projeto foi simulado para fins de aprendizado, experimentação e demonstração de metodologia.

Cada linha representa um usuário exposto a uma imagem de produto durante uma campanha de e-commerce.

#### Principais Colunas

| Coluna             | Descrição                                                        |
| ------------------ | ------------------------------------------------------------------ |
| `user_id`        | Identificador único do usuário                                   |
| `image_type`     | Tipo de imagem exibida para o usuário:`studio` ou `lifestyle` |
| `gender`         | Gênero do usuário                                                |
| `age_group`      | Faixa etária do usuário                                          |
| `customer_type`  | Tipo de cliente: novo ou recorrente                                |
| `clicks`         | Indica se o usuário clicou ou não                                |
| `converted`      | Indica se o usuário realizou compra ou não                       |
| `time_on_page`   | Tempo gasto na página, em segundos                                |
| `purchase_value` | Valor de compra gerado pelo usuário                               |

### 4. Metodologia

O projeto segue um pipeline simples de análise de testes A/B:

1. Simular dados de marketing em nível de usuário.
2. Calcular métricas principais por tipo de imagem.
3. Comparar o desempenho entre imagens de estúdio e imagens lifestyle.
4. Aplicar testes estatísticos de hipótese.
5. Gerar arquivos processados para análise e relatório.

#### Métricas analisadas

- Taxa de cliques, ou CTR
- Taxa de conversão
- Tempo médio na página
- Receita média por usuário
- Receita total

#### Testes estatísticos utilizados

| Métrica             | Teste utilizado                |
| -------------------- | ------------------------------ |
| CTR                  | Teste Z para duas proporções |
| Taxa de conversão   | Teste Z para duas proporções |
| Tempo na página     | Teste T de Welch               |
| Receita por usuário | Teste T de Welch               |

### 5. Principais Resultados

| Métrica                    |           Lifestyle | Estúdio |    Lift |
| --------------------------- | ------------------: | -------: | ------: |
| CTR                         |              11,07% |    8,63% | +28,27% |
| Taxa de conversão          |               4,89% |    4,04% | +21,19% |
| Tempo médio na página     |              45,39s |   37,78s |       - |
| Receita média por usuário | R$ 6,68 | R$ 5,22 |  +27,98% |         |

### 6. Resultados dos Testes Estatísticos

| Métrica             | Teste                          |   P-valor | Significativo |
| -------------------- | ------------------------------ | --------: | ------------- |
| CTR                  | Teste Z para duas proporções | 0,0000419 | Sim           |
| Taxa de conversão   | Teste Z para duas proporções |    0,0382 | Sim           |
| Tempo na página     | Teste T de Welch               |   < 0,001 | Sim           |
| Receita por usuário | Teste T de Welch               |   0,00999 | Sim           |

Considerando um nível de significância de 5%, todas as métricas testadas apresentaram diferenças estatisticamente significativas entre os dois tipos de imagem.

### 7. Recomendação de Negócio

Os resultados simulados sugerem que imagens lifestyle superam imagens de estúdio nas principais métricas analisadas.

Com base nesta análise, a recomendação seria priorizar imagens lifestyle em campanhas e páginas de produto, especialmente quando o objetivo do negócio for aumentar engajamento, taxa de conversão e receita média por usuário.

No entanto, como o dataset é simulado, os resultados devem ser interpretados como uma demonstração da metodologia de testes A/B, e não como uma evidência direta para uma decisão real de negócio.

# EN

## A/B Testing Pipeline for Visual Assets

### 1. Project Overview

E-commerce companies invest heavily in product visuals, such as studio photos and lifestyle images, but they often lack statistical evidence about which visual style drives better marketing performance.

This project simulates and analyzes an A/B test comparing two types of product images:

- **Studio images**
- **Lifestyle images**

The goal is to evaluate which image type performs better across key marketing metrics such as click-through rate, conversion rate, time on page, and revenue per user.

### 2. Business Problem

Marketing and creative teams often make visual decisions based on aesthetics, intuition, or brand preference. However, these decisions can have a direct impact on user engagement, conversion, and revenue.

This project addresses the following question:

> Do lifestyle product images outperform studio product images in terms of user engagement and business outcomes?

### 3. Dataset

The dataset used in this project is simulated for learning and experimentation purposes.

Each row represents a user exposed to one product image during an e-commerce campaign.

#### Main Columns

| Column         | Description                                          |
| -------------- | ---------------------------------------------------- |
| user_id        | Unique user identifier                               |
| image_type     | Type of image shown to the user: studio or lifestyle |
| gender         | User gender                                          |
| age_group      | User age group                                       |
| customer_type  | New or returning customer                            |
| clicks         | Whether the user clicked                             |
| converted      | Whether the user purchased                           |
| time_on_page   | Time spent on the page in seconds                    |
| purchase_value | Purchase amount generated by the user                |

### 4. Methodology

The project follows a simple A/B testing pipeline:

1. Simulate user-level marketing data.
2. Calculate core marketing metrics by image type.
3. Compare performance between studio and lifestyle images.
4. Apply statistical hypothesis tests.
5. Generate processed outputs for reporting.

#### Metrics analyzed

- Click-through rate
- Conversion rate
- Average time on page
- Revenue per user
- Total revenue

#### Statistical tests

| Metric           | Test Used             |
| ---------------- | --------------------- |
| CTR              | Two-proportion Z-test |
| Conversion Rate  | Two-proportion Z-test |
| Time on Page     | Welch's t-test        |
| Revenue per User | Welch's t-test        |

### 5. Key Results

| Metric               |           Lifestyle |  Studio |    Lift |
| -------------------- | ------------------: | ------: | ------: |
| CTR                  |              11.07% |   8.63% | +28.27% |
| Conversion Rate      |               4.89% |   4.04% | +21.19% |
| Average Time on Page |              45.39s |  37.78s |       - |
| Revenue per User     | R$ 6.68 | R$ 5.22 | +27.98% |         |

### 6. Statistical Test Results

| Metric           | Test                  |   P-value | Significant |
| ---------------- | --------------------- | --------: | ----------- |
| CTR              | Two-proportion Z-test | 0.0000419 | Yes         |
| Conversion Rate  | Two-proportion Z-test |    0.0382 | Yes         |
| Time on Page     | Welch's t-test        |   < 0.001 | Yes         |
| Revenue per User | Welch's t-test        |   0.00999 | Yes         |

At a 5% significance level, all tested metrics showed statistically significant differences between the two image types.

### 7. Business Recommendation

The simulated results suggest that lifestyle images outperform studio images across all main performance metrics.

Based on this analysis, the recommendation is to prioritize lifestyle images in product campaigns and product pages, especially when the business goal is to increase user engagement, conversion rate, and revenue per user.

However, because this dataset is simulated, the results should be interpreted as a demonstration of A/B testing methodology rather than direct evidence for a real business decision.
