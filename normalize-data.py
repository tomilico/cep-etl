import os
import pandas as pd


class NormalizeData:
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir  # save the files from bronze (csv & JSON)
        self.output_dir = output_dir  # save with parquet
        os.makedirs(self.output_dir, exist_ok=True)  # make sure that the output dir exists

    def convert_columns_to_string(self, df):
        # converte colunas do tipo list para string para permitir drop_duplicates
        for col in df.columns:
            if df[col].apply(lambda x: isinstance(x, list)).any():
                df[col] = df[col].apply(lambda x: str(x) if isinstance(x, list) else x)
        return df

    def load_df_from_file(self, file, ext):
        input_path = os.path.join(self.input_dir, file)

        if ext.lower() == ".csv":
            df = pd.read_csv(input_path)
        elif ext.lower() == ".json":
            try:
                df = pd.read_json(input_path)
            except ValueError:
                df = pd.read_json(input_path, lines=True)
        else:
            return None  # optional safety

        return df

    def normalize_data(self):
        for file in os.listdir(self.input_dir):
            name, ext = os.path.splitext(file)
            # 1. Skip files that aren't supported
            df = self.load_df_from_file(file, ext)
            if df is None:
                print(f"Skipping {file}: Unsupported file format.")
                continue

            output_path = os.path.join(self.output_dir, f"{name}.parquet")

            df = self.convert_columns_to_string(df)
            df = df.drop_duplicates().reset_index(drop=True)


            df.to_parquet(output_path, index=False)
            print(f"File {file} has been normalized and saved into {output_path}")


if __name__ == "__main__":
    normalize_data = NormalizeData(input_dir='1-bronze-raw', output_dir='2-silver-validated')
    normalize_data.normalize_data()
