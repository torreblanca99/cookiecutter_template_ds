# DS Cookiecutter template 🍪 ✂️
This repository contains a template for Data Science projects. This template is used with Cookiecutter.

[[Link to Cookiecutter]](https://www.cookiecutter.io/)


## Project Structure 📁
 When you use this template, your projects will have the following structure:
```
├── LICENSE            <- MIT License of the project
├── README.md          <- The top-level README for Data Scientists using this project (project documentation).
│
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks.
│
│
│
├── poetry.toml   <- Files with the libraries and requirements using Poetry,
├── poetry.lock   <- it creates a virtual environment and manage all libraries.
|
├── .pre-commit-config.yaml   <- Basic precommit hooks.
|
├── .gitignore  <- Basic gitignore file
│
└── {{ cookiecutter.module_name }}   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes {{ cookiecutter.module_name }} a Python module
    │
```

## Usage 🚀
To get started with this template, you need Cookiecutter and Poetry (for viraual environments and libraries) Follow these steps:
1. **Intall** cookiecutter:
```bash
pip install cookiecutter
```
2. **Use** template:
```bash
cookiecutter https://github.com/torreblanca99/cookiecutter_template_ds.git
```
3. **Set** names: here ypu have to specifie the names for the following parts (they have default values):
```json
{
    "full_name": "Julio Torreblanca",
    "repo_name": "DS Repo",
    "module_name": "module_name",
    "project_short_description": "Template.",
    "version": "1.0.0",
    "version_python": "3.12"
}
```
4. **Install** Poetry:
```bash
pip install poetry
```
5. Create **Viraul Enviroment** and **install** libraries with Poetry:
```bash
poetry install
```
