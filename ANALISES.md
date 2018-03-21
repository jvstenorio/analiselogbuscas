# Análises

## Análise 1: Perfil das buscas por voos executivos

### 1) Qual é a análise:

O objetivo dessa análise é usar os dados sobre as buscas por voos executivos para entender melhor a demanda por esse tipo de voo. 

### 2) Motivação da análise:

Os voos executivos possuem as tarifas mais altas entre os voos comerciais, é fundamental para o negócio entender a demanda desse tipo de voo, para melhorar a experiência de busca e desenvolver a marca nesse segmento.


### 3) Como executar:

Devemos recuperar os registros sobre voos executivos no log de buscas, em seguida vamos extrair algumas informações desses dados como: quais são os destinos e origens mais procurados, qual o tempo médio da busca, qual a duração média da viagem, qual a relação entre as origens e os destinos mais procurados e quais são as companhias aéreas preferidas para cada destino. As informações extraídas serão apresentadas através de visualizações de dados que possibilitem responder as questões necessárias para entender o perfil das buscas por esse tipo de voo.

## Análise 2: Destinos preferidos para viagens com crianças

### 1) Qual é a análise:

O objetivo dessa análise é descobrir os destinos preferidos para viagens com crianças e identificar padrões que influenciam o cliente na escolha de um destino ou uma companhia aérea. 

### 2) Motivação da análise:

Essa análise tem impacto relevante no negócio e na construção da marca, pois existe uma alta demanda por viagens de férias com crianças. Identificar padrões nas buscas por esse tipo de viagem, possibilita o desenvolvimento de estratégias para melhorar o suporte em períodos de alta temporada, bem como minimizar os riscos com as companhias aéreas.

### 3) Como executar:

Primeiramente, devemos filtrar o log de buscas para manter apenas as viagens com crianças. Depois devemos identificar os destinos preferidos, usando métodos para agrupar os dados e contar as buscar. Com os destinos preferidos identificados, devemos extrair algumas características desses destinos como: companhia aéreas favoritas, duração média da viagem, duração média da busca, quantidade de melhores preços, entre outros. Observando as características extraídas, podemos construir um perfil sobre as buscas para esse tipo de viagem, bem como encontrar padrões que diferenciam destinos preferidos dos demais. Os resultados dessa análise podem ser apresentados através de visualizações de dados.

## Análise 3: Quando as pessoas buscam passagens internacionais?

### 1) Qual é a análise: 

O objetivo é realizar uma análise temporal das buscas por viagens com destinos internacionais, para identificar padrões de horários e dias onde as pessoas mais buscam por esse tipo de voo.

### 2) Motivação da análise:

Entender o comportamento das buscas por viagens internacionais é fundamental para o negócio, tendo em vista que esse tipo de viagem representa uma grande parcela do lucro no mercado de voos comerciais. Essa análise permite que sejam criadas estratégias para suportar e impulsionar as buscas, nos dias e horários com maior demanda por esse tipo de voo.

### 3) Como executar:

Devemos filtrar os dados para manter apenas as viagens internacionais e extrair a quantidade de buscas realizadas em determinadas faixas de horários e dias. Com as informações extraídas, devemos usar algum método de mineração de padrões frequentes para identificar conjuntos de dias e horários com maior número de buscas. Nos casos onde desejamos analisar apenas um destino internacional específico, essa mesma análise também pode ser feita usando apenas as buscas com destinos para os países desejados.

