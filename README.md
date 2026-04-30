# 📊 Panorama Monetário de Angola

Projeto de análise de dados económicos com foco no panorama monetário de Angola, utilizando Python para transformação de dados e Power BI para visualização.

---

## 🎯 Objetivo

* Transformar dados brutos em formato analítico
* Construir um modelo estrela (Data Warehouse)
* Criar dashboards para análise temporal

---

## 🏗️ Modelo de Dados

O projeto segue um modelo estrela composto por:

* **dim_conta** → classificação das contas
* **dim_data** → dimensão temporal (mensal)
* **fato_balance** → valores monetários

---

## ⚙️ Engenharia de Dados

Os dados originais estavam em formato não estruturado (wide format e agregados por ano).

Principais transformações:

* Reconstrução do cabeçalho
* Conversão e limpeza dos valores
* Expansão de dados anuais para granularidade mensal
* Criação de dimensões e tabela facto

---

## 🛠️ Tecnologias

* Python (Pandas)
* Power BI
* Excel

---

## ▶️ Como executar

1. Instalar dependências:

```
pip install pandas openpyxl
```

2. Executar o script:

```
python transformacao.py
```

3. Importar os ficheiros no Power BI

---

## 📂 Estrutura do Projeto

```
├── dataset sem agregação.xlsx
├── transformacao.py
├── dim_conta_final.csv
├── dim_data_final.csv
├── fato_balance_final.csv
└── README.md
```

---

## 📊 Dashboard
<img width="1509" height="845" alt="image" src="https://github.com/user-attachments/assets/c9575b3f-c46f-4d18-aae7-958c51dfea24" />


<img width="1511" height="849" alt="image" src="https://github.com/user-attachments/assets/3a248491-99d0-4bb7-ac45-7e395ba9bb99" />

<img width="1508" height="841" alt="image" src="https://github.com/user-attachments/assets/e25d3982-4513-4239-b39d-5c61bcc12831" />

<img width="1511" height="847" alt="image" src="https://github.com/user-attachments/assets/0a0132d1-e472-40de-bc84-0cb750186c0f" />




## 💡 Nota Técnica

Os dados estavam originalmente agregados por ano.
Foi necessário expandir para granularidade mensal para permitir análises temporais mais detalhadas.

---

## 🚀 Resultado

Modelo de dados estruturado e pronto para análise, permitindo identificar tendências, variações e padrões no sistema monetário.
