<h1 id="readme-top"> Desafio: A Lista de Compras 📝</h2>

_Read this in other languages:_  
[_English_](./translations/README-EN.md)  

![licence mit](https://img.shields.io/badge/licence-MIT-blue.svg)  ![status](https://img.shields.io/badge/status-em_desenvolvimento-green)  

<details>
  <summary><b>Conteúdo</b></summary>
  <ol>
    <li>
      <a href="#about-the-project">Sobre o Projeto</a>
      <ul>
        <li><a href="#features">Funcionalidades</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Iniciando o Projeto</a>
      <ul>
        <li><a href="#prerequisites">Pré-requisitos</a></li>
        <li><a href="#installation">Instalação</a></li>
      </ul>
    </li>
    <li><a href="#usage">Caso de Uso</a></li>
    <li><a href="#contributing">Contribuições</a>
    <ul>
        <li><a href="#how-do-it">Como Fazer</a></li>
      </ul>
    </li>
    <li><a href="#license">Licença</a></li>
    <a></li>
  </ol>
</details> 

<h2 id="about-the-project"><p align="center">Sobre o Projeto</p></h2>

Este aplicativo foi desenvolvido em [Python](https://www.python.org/), permite que o usuário gerencie uma lista de compras com permissão para adicionar, remover e pesquisar os produtos adicionados nela. Requisito para aprovação no Desafio de Aprendizagem do Módulo 3 do curso [_Pensamento Computacional com Python_](https://ticemtrilhas.org.br/trail/b201ce44-d4ff-4f3c-a201-22f0d2c17991), da [TIC em trilhas](https://ticemtrilhas.org.br).

<p align="right">(<a href="#readme-top">voltar ao início</a>)</p>

<h3 id="features">Funcionalidades</h3>

1. **Menu de Opções:** O sistema deve fornecer um menu de opções para o usuário interagir. As opções devem ser as seguintes:  
   - A. Adicionar produto  
   - B. Remover produto  
   - C. Pesquisar produto  
   - D. Sair do programa  

2. **Adicionar Produto:** O usuário deve poder adicionar um novo produto à lista de compras. O sistema deve solicitar informações sobre o nome, unidade de medida, quantidade e descrição do produto. As opções de unidade devem ser:  
   - A. Quilograma  
   - B. Grama  
   - C. Litro  
   - D. Mililitro  
   - E. Unidade  
   - F. Metro  
   - G. Centímetro  
   
   **Essas opções devem aparecer quando o sistema perguntar a unidade de medida.**  

3. **Controle de ID Automático:** O sistema deve atribuir automaticamente um ID único para cada produto adicionado à lista.  

4. **Remover Produto:** O usuário deve poder remover um produto da lista com base no ID do produto. O sistema deve solicitar o ID do produto que o usuário deseja remover.  

5. **Pesquisar Produtos por Nome:** O usuário deve poder pesquisar produtos na lista com base no nome ou parte do nome. O sistema deve exibir os resultados correspondentes e fornecer a contagem total de produtos encontrados.  

6. **Listar Todos os Produtos:** O sistema deve ser capaz de exibir todos os produtos presentes na lista de compras, se houver. Contudo, o menu não deve mostrar uma opção de “Listar produtos”. A exibição deverá ocorrer toda vez que o menu principal for executado, acima dele.  

7. **Cabeçalho do Aplicativo:** Deve ser exibido um cabeçalho ao iniciar o aplicativo para fornecer uma saudação e indicar que é uma Lista de Compras Simples.  

8. **Feedback de Ação:** Após a execução de uma ação (como adicionar ou remover um produto), o sistema deve fornecer feedback indicando o resultado da ação.  

9. **Tratamento de Entradas Inválidas:** O sistema deve ser capaz de lidar com entradas inválidas do usuário e fornecer mensagens de erro apropriadas para orientar o usuário.  

10. **Encerramento do Programa:** O usuário deve poder encerrar o programa de forma adequada, escolhendo a opção de saída no menu.  

<p align="right">(<a href="#readme-top">voltar ao início</a>)</p>

<h2 id="getting-started"><p align="center">Iniciando a Aplicação</p></h2>
<h3 id="prerequisites">Pré-requisitos</h3>

- IDE [Visual Studio Code 1.98.2](https://ode.visualstudio.com/download)
- Extensão [Pylance _v2025.3.2_](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- Extensão [Python _v2025.2.0_](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

<h3 id="installation">Instalação</h3>

1. No Terminal, clone o repositório: 

   ```bash
        git clone https://github.com/gabrielasams/a-lista-de-compras.git
   ```
2. Abra a pasta com os arquivos do repositório na IDE recomendada.
3. Execute no Terminal da própria IDE.

<p align="right">(<a href="#readme-top">voltar ao início</a>)</p>

<h2 id="usage"><p align="center">Caso de Uso</p></h2>
_EM CONSTRUÇÃO_

<p align="right">(<a href="#readme-top">voltar ao início</a>)</p>

<h2 id="contributing"><p align="center">Contribuições</p></h2>
<h3 id="how-do-it">Como Fazer</h3>
Saiba como sugerir melhorias e correções:

1. Faça um _fork_ do repositório.
2. Crie sua _feature branch_: `git checkout -b my-new-feature`.
3. Adicione os arquivos para mudança:  `git add .`.
4. _Commit_ suas mudanças: `git commit -m "Add some feature"`.
5. Envie para a _branch_: `git push origin my-new-feature`.
6. Envie uma _pull request_.

- Adicione um título e/ou uma descrição para que fique clara qual sua sugestão para o sistema :).

**Depois que seu _pull request_ estiver unido ao repositório, você pode apagar sua _branch_ com segurança.** 

<h2 id="license"><p align="center">Licença</p></h2>

Distribuido sob a [MIT License](https://www.github.com/gabrielasams/a-lista-de-compras/blob/main/LICENSE). Acesse para mais informação.

Copyright © 2025 - A Lista de Compras

<p align="right">(<a href="#readme-top">voltar ao início</a>)</p>
