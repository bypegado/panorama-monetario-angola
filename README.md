# 📊 Panorama Monetário de Angola

Projeto de análise de dados económicos com foco no panorama monetário de Angola, utilizando Python para transformação de dados e Power BI para visualização.

---

## 🎯 Objetivo

- Transformar dados brutos em formato analítico  
- Construir um modelo estrela (Data Warehouse)  
- Criar dashboards para análise temporal e suporte à decisão  

---

## 🏗️ Modelo de Dados

O projeto segue um modelo dimensional (modelo estrela) composto por:

- **dim_conta** → classificação das contas  
- **dim_data** → dimensão temporal (mensal)  
- **fato_balance** → valores monetários  

---

## ⚙️ Engenharia de Dados

Os dados originais estavam em formato não estruturado (wide format e agregados por ano), exigindo um processo completo de transformação.

Principais etapas:

- Reconstrução do cabeçalho  
- Limpeza e normalização dos dados  
- Transformação para formato analítico  
- Expansão de dados anuais para granularidade mensal  
- Criação das tabelas dimensão e tabela facto  

---

## 🛠️ Tecnologias

- Python (Pandas)  
- Power BI  
- Excel  

---

## Dashboard
<img width="1420" height="796" alt="Screenshot 2026-05-02 220521" src="https://github.com/user-attachments/assets/21ff1a9f-8825-4d80-943d-20686f0d3596" />

<img width="1439" height="809" alt="Screenshot 2026-05-02 000447" src="https://github.com/user-attachments/assets/8e66afd0-0685-4544-81b9-16eca2b66937" />

<img width="1508" height="848" alt="Screenshot 2026-05-02 172314" src="https://github.com/user-attachments/assets/fc3efeca-2193-4877-9d30-c66af7debf53" />


## 💡 Nota Técnica

Os dados estavam originalmente agregados por ano.
Foi necessário expandir para granularidade mensal para permitir análises temporais mais detalhadas e consistentes.

🚀 Resultado

Modelo de dados estruturado e pronto para análise, permitindo:

Identificar tendências económicas
Analisar variações ao longo do tempo
Apoiar decisões com base em dados confiáveis
🔗 Acesso ao Dashboard

👉 Explore o dashboard interativo:
https://bit.ly/panorama_monetario_de_angola
