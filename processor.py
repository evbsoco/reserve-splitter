from pathlib import Path
import pandas as pd


def process_file(filepath):
    """
    Splits an Excel reserve file into:
      - One Excel workbook with a sheet for each unique 'z new' value
      - One CSV per elevation level
    """

    filepath = Path(filepath)

    # Example:
    # "A1B1 RESERVE.xlsx" -> "A1B1"
    title = filepath.stem.replace(" RESERVE", "")

    # Output workbook
    output_file = filepath.parent / f"{title} RESERVE_split.xlsx"

    # Output CSV folder
    output_dir = filepath.parent / title
    output_dir.mkdir(exist_ok=True)

    # Read Excel
    df = pd.read_excel(filepath)

    # Get unique z values
    z_values = sorted(df["z new"].dropna().unique())

    # Create workbook and CSVs
    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:

        for z in z_values:

            df_z = df[df["z new"] == z]

            sheet_name = str(int(z))

            df_z.to_excel(writer, sheet_name=sheet_name, index=False)
            df_z.to_csv(output_dir / f"{sheet_name}.csv", index=False)

    return f"Finished {title}"