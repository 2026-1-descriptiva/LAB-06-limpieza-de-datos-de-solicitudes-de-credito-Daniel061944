"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.

    El archivo limpio debe escribirse en:
    "files/output/solicitudes_de_credito.csv"
    """

    from pathlib import Path
    import pandas as pd

    input_file = Path("files/input/solicitudes_de_credito.csv")
    output_dir = Path("files/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(input_file, sep=";")

    df = df.drop(columns=["Unnamed: 0"], errors="ignore")

    df["sexo"] = df["sexo"].str.strip().str.lower()

    df["tipo_de_emprendimiento"] = (
        df["tipo_de_emprendimiento"]
        .str.strip()
        .str.lower()
    )

    df["idea_negocio"] = (
        df["idea_negocio"]
        .str.strip()
        .str.lower()
        .str.replace("-", " ", regex=False)
        .str.replace("_", " ", regex=False)
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )

    df["barrio"] = (
        df["barrio"]
        .str.lower()
        .str.replace("-", " ", regex=False)
        .str.replace("_", " ", regex=False)
        .str.replace(r"\s+", " ", regex=True)
    )

    df["línea_credito"] = (
        df["línea_credito"]
        .str.strip()
        .str.lower()
        .str.replace("-", " ", regex=False)
        .str.replace("_", " ", regex=False)
        .str.replace(".", " ", regex=False)
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )

    df["monto_del_credito"] = (
        df["monto_del_credito"]
        .str.strip()
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.replace(".00", "", regex=False)
        .str.strip()
    )

    def limpiar_fecha(fecha):
        partes = str(fecha).split("/")

        if len(partes[0]) == 4:
            year, month, day = partes
        else:
            day, month, year = partes

        return f"{int(year):04d}-{int(month):02d}-{int(day):02d}"

    df["fecha_de_beneficio"] = df["fecha_de_beneficio"].apply(limpiar_fecha)

    df = df.dropna()
    df = df.drop_duplicates()

    df.to_csv(
        output_dir / "solicitudes_de_credito.csv",
        sep=";",
        index=False,
    )


if __name__ == "__main__":
    pregunta_01()