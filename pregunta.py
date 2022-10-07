"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
from datetime import datetime

def clean_data():

    df = pd.read_csv('solicitudes_credito.csv', sep = ';', index_col = [0])
    df_clean = df.copy()
    df_clean = df.drop_duplicates(keep='last')
    df_clean = df_clean.dropna(axis = 0, how = "any")
    ###########
    df_clean.sexo = df_clean.sexo.str.lower()
    df_clean.tipo_de_emprendimiento = df_clean.tipo_de_emprendimiento.str.lower()
    ####################
    df_clean.barrio = df_clean.barrio.str.replace('-',' ')
    df_clean.barrio = df_clean.barrio.str.replace('_',' ')
    df_clean.barrio = df_clean.barrio.str.strip()
    df_clean.barrio = df_clean.barrio.str.lower()
    dict_barrio = {'antonio nari¿o': 'antonio nariño', 'bel¿n': 'belen'}
    df_clean.barrio.replace(dict_barrio, inplace = True, regex = True)
    ##############
    df_clean.idea_negocio = df_clean.idea_negocio.str.replace('-',' ')
    df_clean.idea_negocio = df_clean.idea_negocio.str.replace('_',' ')
    df_clean.idea_negocio = df_clean.idea_negocio.str.strip()
    df_clean.idea_negocio = df_clean.idea_negocio.str.lower()

    ##############
    df_clean.comuna_ciudadano = df_clean.comuna_ciudadano.astype('int')

    ##############
    df_clean.monto_del_credito = df_clean.monto_del_credito.str.replace('$', '')
    df_clean.monto_del_credito = df_clean.monto_del_credito.str.replace(',', '')
    df_clean.monto_del_credito = df_clean.monto_del_credito.str.strip()
    df_clean.monto_del_credito = pd.to_numeric(df_clean.monto_del_credito)
    df_clean.monto_del_credito = df_clean.monto_del_credito.astype('int')

    ##############
    df_clean.línea_credito = df_clean.línea_credito.str.replace('-', ' ')
    df_clean.línea_credito = df_clean.línea_credito.str.replace('_', ' ')
    df_clean.línea_credito = df_clean.línea_credito.str.strip()
    df_clean.línea_credito = df_clean.línea_credito.str.lower()

    ##################
    def fecha(data_fecha):
        try:
            df_clean_fecha = datetime.strptime(data_fecha, '%d/%m/%Y')
            
        except:
            df_clean_fecha = datetime.strptime(data_fecha, '%Y/%m/%d')

        return df_clean_fecha

    df_clean.fecha_de_beneficio = df_clean.fecha_de_beneficio.map(fecha)
    
    df_clean = df_clean.drop_duplicates(keep='last')

    return df_clean
