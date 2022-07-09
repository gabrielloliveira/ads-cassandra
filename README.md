# ads-cassandra
Trabalho da disciplina Tópicos avançados em Análise e Desempenho de Software

## TRABALHO 02 – Implementação de Gerador de Carga Sintética

## DESCRIÇÃO DO TRABALHO
Vocês em duplas deverão implementar um sistema distribuído cliente/servidor 
As duas máquinas podem ser dois notebooks, ou um notebook e um smartphone, a maneira que achar mais interessante.
O serviço provido pelo servidor é salvar um arquivo em no banco de dados Cassandra. 


Do lado do cliente você deve ser capaz de gerar e salvar **N** arquivos de tamanho **Z** automaticamente e enviar de forma sequencial, configurando a taxa de envio (arq/segundos). Perceba que você tem 3 parâmetros que deverão ser facilmente configurados.

Seu sistema deverá ser monitorado em termos de três métricas, de preferência salvando em arquivo de log: 
tempo médio de resposta (MRT), 
consumo de memória, 
consumo de CPU.

No final do dia da apresentação do trabalho deverão enviar um relatório (aprox 5 pgns)
