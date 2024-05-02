from utils.db import db
class Ubigeo(db.Model):
    __tablename__ = 'ubigeo'
    idubigeo = db.Column(db.String(100), primary_key=True)
    departamento = db.Column(db.String(255))
    provincia = db.Column(db.String(255))
    distrito = db.Column(db.String(255))
    superficie = db.Column(db.Integer)
    altitud = db.Column(db.Integer)
    latitud = db.Column(db.Integer)
    longitud = db.Column(db.Integer)


    def __init__(self, idubigeo, departamento, provincia,distrito, superficie,altitud, latitud,longitud):
        self.idubigeo = idubigeo
        self.departamento = departamento
        self.provincia = provincia
        self.distrito = distrito
        self.superficie = superficie
        self.altitud = altitud
        self.latitud = latitud
        self.longitud = longitud