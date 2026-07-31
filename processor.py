from pathlib import Path
import pandas as pd
import sys


def process_file(filepath):
    filepath = Path(filepath)

    # Example:
    # "A1B1 RESERVE.xlsx" -> "A1B1"
    title = filepath.stem.replace(" RESERVE", "")

    # ---------------- Determine application folder ----------------

    if getattr(sys, "frozen", False):
        # Running as EXE
        app_dir = Path(sys.executable).parent
    else:
        # Running from Python
        app_dir = Path(__file__).resolve().parent

    # ---------------- Outputs folder ----------------

    output_root = app_dir / "outputs"
    output_root.mkdir(exist_ok=True)

    # Output workbook
    output_file = output_root / f"{title} RESERVE_split.xlsx"

    # Output CSV folder
    output_dir = output_root / title
    output_dir.mkdir(exist_ok=True)

    # ---------------- Read Excel ----------------

    df = pd.read_excel(filepath)

    z_values = sorted(df["z"].dropna().unique())

    # ---------------- Write outputs ----------------

    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:

        for z in z_values:

            df_z = df[df["z"] == z]

            sheet_name = str(int(z))

            df_z.to_excel(writer, sheet_name=sheet_name, index=False)

            df_z.to_csv(
                output_dir / f"{sheet_name}.csv",
                index=False
            )

    return output_file