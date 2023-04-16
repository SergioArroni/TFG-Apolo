# **Aquiles**: Sistema inteligente de monitorización  y detección de ataques basados en inteligencia artificial

## Descripción

Diseño de un sistema inteligente que, mediante el uso de técnicas de Machine Learning se encarga de la monitorización del tráfico en una red, capaz de detectar intrusos (IDS) y ataques generados mediante técnicas de inteligencia artificial (AML).

* **Autor:** Sergio Arroni Del Riego
* **Tutor:** Antonio Payá González
* **Tutor:** Vicente García Díaz

![Aquiles](documentation/Figures/Aquiles.png)

## Estrucutra del proyecto

```bash
├── documentation
│   ├── Chapters
│   │   ├── Capítulo_*.tex
│   ├── Appendices
│   │   ├── Apéndice_*.tex
│   ├── Figures
│   │   ├── **/*.png
│   ├── main.tex
│   ├── main.pdf
│   ├── Biblio.bib
├── environment
│   ├── **/*
├── research_src
│   ├── 00-datasets
│   ├── 01-intrusion_detection_systems
│   ├── 02-aml_attacks
│   ├── 03-aml_defenses
│   ├── shared
│   ├── results
├── README.md
├── LICENSE
└── .gitignore
```

## Documentación

La memoria del Trabajo de Fin de Grado se encuentra en el directorio `documentation` y se ha generado mediante el uso de LaTeX. Para generar el archivo PDF, primero es necesario asegurarse de tener instalado un compilador de LaTeX en su ordenador. Una vez que se tiene el compilador, se puede utilizar el siguiente comando desde la línea de comandos para compilar el archivo main.tex:

```bash
pdflatex main.tex
```

## Environment

Para la demo que se utilizará en el Trabajo de Fin de Grado, de ha desarrollado un entorno que simula una red de ordenadores conectados a través de una red local. Este entorno se encuentra en el directorio `environment` y se ha desarrollado mediante el uso de Docker y Docker-Compose. Para poder utilizar el entorno, primero es necesario asegurarse de tener instalado Docker y Docker-Compose en su ordenador. Una vez que se tiene instalado Docker y Docker-Compose, se puede utilizar el siguiente comando desde la línea de comandos para levantar el entorno:

```bash
docker-compose up -d
```

## Research Source Code

El código fuente de la investigación se encuentra en el directorio `research_src`.

## Licencia

Este proyecto está bajo la licencia Apache License 2.0 - ver el archivo [LICENSE](LICENSE) para más detalles.
