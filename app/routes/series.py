from flask import Blueprint
from app.controllers import add_serie, obter_todas_series, obter_uma_serie

bp_series = Blueprint("series", __name__, url_prefix="/series")

bp_series.post("")(add_serie) 
bp_series.get("")(obter_todas_series) 
bp_series.get("<int:serie_id>")(obter_uma_serie) 