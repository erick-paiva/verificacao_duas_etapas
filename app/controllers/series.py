from http import HTTPStatus
from flask import jsonify, request
from app.models.series_model import Serie


def verifica_valores(keys: list):
    chaves_permitidas = ["serie", "seasons",
                         "released_date", "genre", "imdb_rating"]

    chaves_erradas = [
        error_key for error_key in keys if not error_key in chaves_permitidas]
    
    chaves_faltantes = [key for key in chaves_permitidas if not key in keys]
    
    if chaves_erradas:
        return {"Error": {
            "Você passou chaves incorretas !": chaves_erradas
        }}

    if chaves_faltantes:
        return {"Error": {
            "Você não passou todas as chaves !": chaves_faltantes
        }}


def add_serie():
    Serie.create_table_if_not_exits()

    data = request.get_json()
    chaves_verificadas = verifica_valores(list(data.keys()))
    if chaves_verificadas:
        return jsonify(chaves_verificadas), HTTPStatus.BAD_REQUEST

    serie = Serie(data)
    try:
        inserted_serie = serie.create_serie()
    except:
        return {"error": f"a serie {data['serie']} ja foi adcionada!"}, HTTPStatus.NOT_ACCEPTABLE

    serialized_serie = Serie.serialize(inserted_serie)

    return serialized_serie, HTTPStatus.CREATED


def obter_todas_series():
    Serie.create_table_if_not_exits()
    todas_series = Serie.obter_uma_ou_varias_series()
    serialized = [Serie.serialize(serie) for serie in todas_series]

    return jsonify(serialized)


def obter_uma_serie(serie_id: int):
    Serie.create_table_if_not_exits()
    serie = Serie.obter_uma_ou_varias_series(serie_id)
    if not serie:
        return {"error": f"Não foi possivel encontrar uma serie com o id {serie_id}"}, HTTPStatus.NOT_FOUND
    serialized = Serie.serialize(serie)
    return jsonify(serialized), HTTPStatus.OK
