import pandas as pd

# =========================
# CONFIG
# =========================
INPUT_FILE = "dataset sem agregação.xlsx"

# =========================
# FATO_BALANCE
# =========================
def gerar_fato():
    df_raw = pd.read_excel(INPUT_FILE, header=None)

    header = df_raw.iloc[0]
    df = df_raw.iloc[1:].copy()

    df.rename(columns={0: "Descrição"}, inplace=True)

    # extrair anos
    anos = []
    for val in header[1:]:
        try:
            anos.append(int(str(val)[:4]))
        except:
            anos.append(None)

    df.columns = ["Descrição"] + anos
    df["Descrição"] = df["Descrição"].astype(str).str.strip()

    registos = []

    for i in range(df.shape[0]):
        descricao = df.iloc[i, 0]

        if descricao == "" or pd.isna(descricao):
            continue

        for j in range(1, df.shape[1]):
            ano = df.columns[j]
            valor = df.iloc[i, j]

            if ano is None:
                continue

            if valor is None or str(valor).strip() == "":
                continue

            valor_str = str(valor).replace(" ", "").replace(",", ".")

            try:
                valor_num = float(valor_str)
            except:
                continue

            for mes in range(1, 13):
                data = pd.Timestamp(year=ano, month=mes, day=1)

                registos.append({
                    "Descrição": descricao,
                    "data": data,
                    "ano_mes": data.strftime("%Y-%m"),
                    "valor": valor_num
                })

    fato = pd.DataFrame(registos)
    fato.to_csv("fato_balance_final.csv", index=False, encoding="utf-8-sig")

    print("✔ fato_balance gerada")


# =========================
# DIM_DATA
# =========================
def gerar_dim_data():
    df = pd.read_excel(INPUT_FILE, header=0)

    colunas = pd.Series(df.columns[1:]).astype(str)
    anos = colunas.str.extract(r'(\d{4})')[0].dropna().astype(int)
    anos = anos.drop_duplicates().sort_values()

    datas = []
    for ano in anos:
        for mes in range(1, 13):
            datas.append(pd.Timestamp(year=ano, month=mes, day=1))

    dim_data = pd.DataFrame({"data": datas})

    dim_data["ano"] = dim_data["data"].dt.year
    dim_data["mes"] = dim_data["data"].dt.month
    dim_data["mes_nome"] = dim_data["data"].dt.strftime("%b")
    dim_data["trimestre"] = dim_data["data"].dt.quarter
    dim_data["ano_mes"] = dim_data["data"].dt.to_period("M").astype(str)

    dim_data.to_csv("dim_data_final.csv", index=False)

    print("✔ dim_data gerada")


# =========================
# DIM_CONTA
# =========================
def gerar_dim_conta():
    df = pd.read_excel(INPUT_FILE, header=None)

    header = df.iloc[0]
    df = df[1:]
    df.columns = ["Descrição"] + list(header[1:])

    df["Descrição"] = df["Descrição"].astype(str).str.strip()
    df = df.dropna(subset=["Descrição"])

    dim_conta = df[["Descrição"]].drop_duplicates().copy()

    def extrair_categoria(desc):
        if "(" in desc and ")" in desc:
            contexto = desc.split("(")[1].replace(")", "").strip()
            partes = [p.strip() for p in contexto.split("-")]

            categoria = partes[0] if len(partes) >= 1 else None
            subcategoria = partes[1] if len(partes) >= 2 else None
        else:
            categoria = None
            subcategoria = None

        return pd.Series([categoria, subcategoria])

    dim_conta[["Categoria", "Subcategoria"]] = dim_conta["Descrição"].apply(extrair_categoria)

    def classificar_tipo(desc):
        desc = desc.lower()
        if any(p in desc for p in [
            "base monetária",
            "depósitos",
            "passivos",
            "capital",
            "empréstimos passivos",
            "responsabilidades"
        ]):
            return "Passivo"
        return "Activo"

    dim_conta["Tipo"] = dim_conta["Descrição"].apply(classificar_tipo)

    dim_conta = dim_conta[
        ["Descrição", "Tipo", "Categoria", "Subcategoria"]
    ].sort_values("Descrição")

    dim_conta.to_csv("dim_conta_final.csv", index=False)

    print("✔ dim_conta gerada")


# =========================
# MAIN
# =========================
def main():
    gerar_dim_conta()
    gerar_dim_data()
    gerar_fato()

    print("✔ Pipeline completo executado")


if __name__ == "__main__":
    main()