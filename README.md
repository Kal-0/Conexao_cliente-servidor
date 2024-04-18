# Projeto de simulação da conexão cliente-servidor

Projeto realizado na cadeira de infraestrutura de comunicação (Redes) do curso de Ciência da Computação da C.E.S.A.R School.

## 🎯 Objetivo geral

Desenvolver uma aplicação cliente-servidor capaz de, na camada de aplicação, fornecer um transporte confiável de dados considerando um canal com perdas de dados e erros.

## 🚀💻⚙️ Funcionalidade especificas

- Soma de verificação para garantir integralidade dos dados enviados (checksum)
- Reenvio de pacotes em caso de perda
- Flag para simular time-limit-exceeded
- Número de sequência para garantir ordem de entrega
- Reconhecimento positivo de pacotes entregues
- Reconhecimento negativo de pacotes não entregues
- Janela e paralelismo

## 📦🔧🔨 Executando o projeto

Utilizamos a versão 3.12.0 do Python para o desenvolvimento

## Manual de Utilização
### 1° clone o repositório ou copie os arquivos ".py"
### 2° execute o server.py
execute esse comando no terminal no diretório dos arquivos
```
py server.py
```
### 3° execute o client.py
execute esse comando no terminal no diretório dos arquivos
```
py client.py
```
### 4° selecione um metodo de envio no terminal do client
### 5° envie mensagens ao servidor
### 6° para simular um pacote corrompido escreva a mensagem:
```
Tchecksum
```


## 📚📖🔍 Referências

- [KUROSE, J. F. e ROSS, K. - Redes de Computadores e a Internet - 8ª Ed., Pearson, 2021.](https://www.amazon.com.br/Redes-computadores-Internet-James-Kurose/dp/8582605587)
