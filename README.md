# Backend de E-Commerce com Django Rest Framework

Este é o repositório do backend de um aplicativo de e-commerce desenvolvido com Django Rest Framework. Ele fornece uma API para gerenciar produtos, carrinhos de compra, pedidos de compras e usuários.

## Sobre o Projeto
O intuito desse projeto é tentar simular o backend de um e-commerce para desenvolvimento próprio. Ele foi criado com o objetivo de aprender e praticar os conceitos de desenvolvimento de API REST utilizando o Django Rest Framework.

## Recursos

- Cadastro e login de usuários
- Listagem de produtos
- Adição de produtos ao carrinho de compras
- Atualização de quantidades de produtos no carrinho
- Remoção de produtos do carrinho
- Finalização de pedidos

## Configuração

Siga estas etapas para configurar e executar o projeto localmente:

1. Clone este repositório:

```bash
  git clone https://github.com/WWWNINIWWW/backend-ecommerce.git
```
2. Entre no seu repositorio

```bash
  cd seu-repositorio
```
3. Crie e entre no seu ambiente virtual

```bash
   python -m venv venv
   venv\Scripts\activate
```
4. Instale as dependências
```bash
   pip install -r requirements.txt
```
5. Execute as migrações do banco de dados

```bash
   python manage.py migrate
```
6. Inicie o servidor

```bash
   python manage.py runserver
```
## Testes da API
Você pode usar o arquivo JSON exportado do Insomnia para testar as funcionalidades da API: <br>
[![Run in Insomnia}](https://insomnia.rest/images/run.svg)](https://insomnia.rest/run/?label=Ecommerce%20API&uri=https%3A%2F%2Fgithub.com%2FWWWNINIWWW%2Fbackend-ecommerce%2Fblob%2Fmaster%2Finsomnia.json)



