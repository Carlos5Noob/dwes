grupos = {
    "chirigotas": {
        "Los Yesterday": {
            "preliminares": [9.1, 9.3, 9.0, 9.2],
            "cuartos": [9.4, 9.2, 9.1, 9.3],
            "semifinal": [9.6, 9.5, 9.4, 9.5],
            "final": [9.7, 9.6, 9.8, 9.7]
        },
        "Er Chele Vara": {
            "preliminares": [8.5, 8.6, 8.7, 8.9],
            "cuartos": [8.9, 8.8, 8.6, 8.7]
        }
    },
    "comparsas": {
        "Los Ángeles Caídos": {
            "preliminares": [9.5, 9.6, 9.7, 9.8],
            "cuartos": [9.7, 9.6, 9.8, 9.9],
            "semifinal": [9.8, 9.9, 9.8, 9.9],
            "final": [9.9, 9.9, 9.8, 9.8]
        },
        "Los Millonarios": {
            "preliminares": [9.3, 9.4, 9.5, 9.6],
            "cuartos": [9.6, 9.5, 9.7, 9.8],
            "semifinal": [9.7, 9.6, 9.7, 9.8]
        }
    },
    "coros": {
        "La Trinidad": {
            "preliminares": [9.0, 9.1, 9.2, 9.3],
            "cuartos": [9.3, 9.4, 9.5, 9.6],
            "semifinal": [9.5, 9.6, 9.7, 9.8],
            "final": [9.7, 9.8, 9.9, 9.8]
        },
        "El Batallón Fletilla": {
            "preliminares": [8.8, 8.9, 9.0, 9.1],
            "cuartos": [9.0, 9.1, 9.2, 9.3],
            "semifinal": [9.2, 9.3, 9.4, 9.5]
        }
    },
    "cuartetos": {
        "Tres notas Musicales": {
            "preliminares": [9.2, 9.3, 9.1, 9.4],
            "cuartos": [9.4, 9.5, 9.3, 9.6],
            "semifinal": [9.5, 9.6, 9.7, 9.6],
            "final": [9.7, 9.8, 9.6, 9.7]
        },
        "Ser o no Ser": {
            "preliminares": [8.7, 8.8, 8.9, 8.6],
            "cuartos": [8.9, 9.0, 8.8, 8.9]
        }
    }
}


def calcula_media_puntuaciones(grupos, ag=None, fase=None):
    """
    Calcula las medias de cada agrupación para cada fase, y la media general de todas las fases en las que participó la agrupación.
    Permite filtrar por agrupación y fase específicas.
    :param grupos: Diccionario que contiene las modalidades y agrupaciones con sus respectivas puntuaciones.
    :param ag: Nombre de la agrupación para la cual calcular las medias. Si no se especifica, calcula para todas (opcional).
    :param fase: Fase específica para calcular la media. Si no se especifica, calcula para todas las fases (opcional).
    :return: Un diccionario con las agrupaciones y sus medias de puntuación total.
    """
    resultados = {}

    for modalidad, agrupaciones in grupos.items():
        for nombre_agrupacion, fases in agrupaciones.items():
            # Si se proporciona el argumento 'ag' y no coincide con el nombre de la agrupación, continuar
            if ag and ag.lower() not in nombre_agrupacion.lower():
                continue

            medias_fases = []
            for nombre_fase, puntuaciones in fases.items():
                # Si se proporciona una fase y no coincide con el nombre de la fase, continuar
                if fase and nombre_fase.lower() != fase.lower():
                    continue

                # Calculamos la media de las puntuaciones por cada fase
                media_fase = round(sum(puntuaciones) / len(puntuaciones), 2)
                medias_fases.append(media_fase)

            if medias_fases:
                # Calculamos la media total de todas las fases del concurso
                media_total = round(sum(medias_fases) / len(medias_fases), 2)
                resultados[nombre_agrupacion] = media_total

    return resultados


# Ejemplo de uso
media_todas_las_agrupaciones = calcula_media_puntuaciones(grupos)
print(f"La media de todas las agrupaciones es: {media_todas_las_agrupaciones}")

media_yesterday = calcula_media_puntuaciones(grupos, ag="Yesterday")
print(f"La media de 'Los Yesterday' es: {media_yesterday}")

media_cuartos = calcula_media_puntuaciones(grupos, fase="cuartos")
print(f"La media de todas las agrupaciones en cuartos es: {media_cuartos}")