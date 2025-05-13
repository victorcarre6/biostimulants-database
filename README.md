# biostimulants-database
An open-source repository for biostimulants and active compounds from biosources, including data curation and cheminformatics tools.

This project aims to support researchers and companies working on sustainable agriculture by providing a structured, data-rich resource for biostimulant discovery and characterization.  

---

## Project Objectives  

- **Data Collection** – Gather and organize information on biostimulants from scientific literature, patents, and open databases.  
- **Chemical Characterization** – Document chemical structures, properties, and mechanisms of action for each compound.
- **Easy access** – Provide an accessible, searchable database for biostimulants and related compounds with an API.

- **Data-Driven Insights** – Use as a database for [Biostimulant Formulation Predictor](https://github.com/victorcarre6/biostimulant-formulation-predictor) : to predict the efficacy and optimal formulation of biostimulants via machine learning.


---

## Current Status  

Done :
- **Project Structure** – Initial project structure created (data, src, notebooks, docs, examples, tests).  
- **Basic Data Set** – Sample data file added (`data/sample_data.csv`) as a starting point.  

Ongoing :
- **First Scripts** – Initial Python scripts for data collection and managment are being developed. 

Planned :
- **Data Vizualisation** – Develop data visualization tools to highlight outliers and trends
- **Prediction Integration** – Start [the prediction project](https://github.com/victorcarre6/biostimulant-formulation-predictor)  

---

## Getting Started  

### Prerequisites  

To run the code locally, you'll need the following packages (see `requirements.txt` for details):  
```bash
rdkit  
pubchempy  
pandas  
numpy  
scikit-learn  
matplotlib  
seaborn  
jupyter  
