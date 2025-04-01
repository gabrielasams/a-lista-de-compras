
<h1 id="readme-top">Challenge: The Shopping List 📝</h2>

![license mit](https://img.shields.io/badge/license-MIT-blue.svg)  ![status](https://img.shields.io/badge/status-finished-green)  

<details>
  <summary><b>Content</b></summary>
  <ol>
    <li>
      <a href="#about-the-project">About the Project</a>
      <ul>
        <li><a href="#features">Features</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a>
    <ul>
        <li><a href="#how-do-it">How to Do</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <a></li>
  </ol>
</details> 

<h2 id="about-the-project"><p align="center">About the Project</p></h2>

This application was developed in [Python](https://www.python.org/) and allows the user to manage a shopping list with permission to add, remove and search for existent products. Requirement for approval at the Learning Challenge of Module 3 of the [_Pensamento Computacional com Python_](https://ticemtrilhas.org.br/trail/b201ce44-d4ff-4f3c-a201-22f0d2c17991) course, from [TIC em trilhas](https://ticemtrilhas.org.br).

<p align="right">(<a href="#readme-top">Return to top</a>)</p>

<h3 id="features">Features</h3>

1. **Options Menu:** The system should provide a menu of options for the user to interact with. The options should be as follows: 
- A. Add product 
- B. Remove product 
- C. Search for product 
- D. Exit the system

2. **Add Product:** The user must be able to add a new product to the shopping list. The system must request information about the name, unit of measurement, quantity and description of the product. The unit options must be: 
- A. Kilogram 
- B. Gram 
- C. Liter 
- D. Milliliter 
- E. Unit 
- F. Meter 
- G. Centimeter 
   
   **These options should appear when the system asks for the unit of measurement.** 

3. **Automatic ID Control:** The system should automatically assign a unique ID to each product added to the list.

4. **Remove Product:** The user should be able to remove a product from the list based on the product ID. The system should prompt for the product ID that the user wants to remove.

5. **Search Products by Name:** The user should be able to search for products in the list based on the name or part of the name. The system should display the matching results and provide the total count of products found.

6. **List All Products:** The system must be able to display all products present in the shopping list, if any. However, the menu must not show a “List Products” option. The display must occur every time the main menu is executed, above it.

7. **Application Header:** A header should be displayed when the application starts to provide a greeting and indicate that it is a Simple Shopping List.

8. **Action Feedback:** After performing an action (such as adding or removing a product), the system should provide feedback indicating the result of the action.

9. **Handling Invalid Input:** The system must be able to handle invalid user input and provide appropriate error messages to guide the user.  

10. **System Shutdown:** The user must be able to shut down the system properly by choosing the exit option from the menu.

<p align="right">(<a href="#readme-top">Return to top</a>)</p>

<h2 id="getting-started"><p align="center">Getting Started</p></h2>
<h3 id="prerequisites">Prerequisites</h3>

- IDE [Visual Studio Code 1.98.2](https://ode.visualstudio.com/download)
- Extension [Pylance _v2025.3.2_](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- Extension [Python _v2025.2.0_](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

<h3 id="installation">Installation</h3>

1. In Terminal, clone the repository:

   ```bash
        git clone https://github.com/gabrielasams/a-lista-de-compras.git
   ```
2. Open the folder with the repository files in the recommended IDE.
3. Run it in the IDE's own Terminal.

<p align="right">(<a href="#readme-top">Return to top</a>)</p>

<h2 id="contributing"><p align="center">Contributing</p></h2>
<h3 id="how-do-it">How to Do</h3>
Learn how to suggest improvements and corrections:

11. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Add files changed:  `git add .`
4. Commit your changes: `git commit -m "Add some feature"`
5. Push to the branch: `git push origin my-new-feature`
6. Submit a pull request

- Add a title and/or one description that let clear your suggestion :).

**After your pull request is merged, you can safely delete your branch.**

<h2 id="license"><p align="center">License</p></h2>

Distributed under the [MIT License](https://www.github.com/gabrielasams/a-lista-de-compras/blob/main/LICENSE). Visit for more information.

Copyright © 2025 - The Shopping List

<p align="right">(<a href="#readme-top">Return to top</a>)</p>