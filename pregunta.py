"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
from fuzzywuzzy import fuzz, process
from datetime import datetime

def clean_data():

    df = pd.read_csv('solicitudes_credito.csv', sep = ';', index_col = [0])
    df_clean = df.copy()
    df_clean = df.drop_duplicates(keep='last')
    df_clean = df_clean.dropna(axis = 0, how = "any")
    sex_valid_names = ['femenino', 'masculino']

    min_threshold = 80

    for valid_name in sex_valid_names:

        potential_matches = process.extract(
            valid_name,
            df_clean.sexo,
            limit=df_clean.shape[0],
        )

        for potential_match in potential_matches:

            if potential_match[1] >= min_threshold:

                df_clean.loc[df_clean.sexo == potential_match[0], "sexo_"] = valid_name

    df_clean['sexo'] = df_clean['sexo_']
    df_clean = df_clean.drop(columns = ['sexo_'])

    tipo_emp_valid_names = ['industria', 'comercio', 'servicio', 'agropecuaria']

    min_threshold = 80

    for valid_name in tipo_emp_valid_names:

        potential_matches = process.extract(
            valid_name,
            df_clean.tipo_de_emprendimiento,
            limit=df_clean.shape[0],
        )

        for potential_match in potential_matches:

            if potential_match[1] >= min_threshold:

                df_clean.loc[df_clean.tipo_de_emprendimiento == potential_match[0], "tipo_de_emprendimiento_"] = valid_name

    df_clean['tipo_de_emprendimiento'] = df_clean['tipo_de_emprendimiento_']
    df_clean = df_clean.drop(columns = ['tipo_de_emprendimiento_'])

    df_clean.idea_negocio = df_clean.idea_negocio.str.replace('-',' ')
    df_clean.idea_negocio = df_clean.idea_negocio.str.replace('_',' ')
    df_clean.idea_negocio = df_clean.idea_negocio.str.strip()
    df_clean.idea_negocio = df_clean.idea_negocio.str.lower()

    df_clean.barrio = df_clean.barrio.str.replace('-',' ')
    df_clean.barrio = df_clean.barrio.str.replace('_',' ')
    df_clean.barrio = df_clean.barrio.str.strip()
    df_clean.barrio = df_clean.barrio.str.lower()

    df_clean.comuna_ciudadano = df_clean.comuna_ciudadano.astype('int')

    def fecha(data_fecha):

        try:
            df_clean_fecha = datetime.strptime(data_fecha, '%d/%m/%Y')
        
        except:
            df_clean_fecha = datetime.strptime(data_fecha, '%Y/%m/%d')

        return df_clean_fecha

    df_clean.fecha_de_beneficio = df_clean.fecha_de_beneficio.map(fecha)

    df_clean.monto_del_credito = df_clean.monto_del_credito.str.replace('$', '')
    df_clean.monto_del_credito = df_clean.monto_del_credito.str.replace(',', '')
    df_clean.monto_del_credito = df_clean.monto_del_credito.str.strip()
    df_clean.monto_del_credito = pd.to_numeric(df_clean.monto_del_credito)
    df_clean.monto_del_credito = df_clean.monto_del_credito.astype('int')

    df_clean.línea_credito = df_clean.línea_credito.str.replace('-', ' ')
    df_clean.línea_credito = df_clean.línea_credito.str.replace('_', ' ')
    df_clean.línea_credito = df_clean.línea_credito.str.strip()
    df_clean.línea_credito = df_clean.línea_credito.str.lower()
    df_clean.línea_credito = df_clean.línea_credito.replace({'soli diaria': 'solidaria'})
    df_clean = df_clean.drop_duplicates(keep='last')

    #
    # Inserte su código aquí
    #

    return df_clean
