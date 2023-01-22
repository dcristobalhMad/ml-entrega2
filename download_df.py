import kaggle

def auth_df():
    # Autenticando con la api de kaggle, se conecta gracias a las variables seteadas en gh actions
    print("Autenticando con la API de kaggle...")
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files('nathanlauga/nba-games', path='dataframes/', unzip=True)
    # Se descarga el dataframe descomprimido en la carpeta dataframes
    print("Descargado el dataframe en la carpeta dataframes")


def main():
    auth_df()

if __name__ == "__main__":
    main()