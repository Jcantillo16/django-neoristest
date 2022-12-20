from django.db import models
# Create your models here.

class TituloBancario(models.Model):
    idtitulo = models.CharField(max_length=4)
    titulo = models.CharField(max_length=100, null=True, blank=True )
    clasificacion = models.CharField(max_length=100)
    valor = models.IntegerField()
    fecha_creacion = models.DateField()
    fecha_vencimiento = models.DateField()
    pagocuota = models.CharField(max_length=1)

    class Meta:
        db_table = 'titulo_bancario'

    def __str__(self):
        return f"""
        idtitulo: {self.idtitulo}
        titulo: {self.titulo}
        clasificacion: {self.clasificacion}
        valor: {self.valor}
        fecha_creacion: {self.fecha_creacion}
        fecha_vencimiento: {self.fecha_vencimiento}
        pagocuota: {self.pagocuota}
        """


    def __repr__(self):
        return f"""
        idtitulo: {self.idtitulo}
        titulo: {self.titulo}
        clasificacion: {self.clasificacion}
        valor: {self.valor}
        fecha_creacion: {self.fecha_creacion}
        fecha_vencimiento: {self.fecha_vencimiento}
        pagocuota: {self.pagocuota}
        """



