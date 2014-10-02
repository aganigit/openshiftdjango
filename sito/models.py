from django.db import models
from image_cropping import ImageRatioField, ImageCropField

from taggit.managers import TaggableManager



# Create your models here.
class Categorie(models.Model):
    titolo = models.CharField(max_length=100)
    sottotitolo = models.CharField(max_length=250, null=True, blank=True)

    def __unicode__(self):
        return self.titolo

    class Meta:
        verbose_name_plural = "Categorie"

class Stagioni(models.Model):
    titolo = models.CharField(max_length=100)
    sottotitolo = models.CharField(max_length=250, null=True, blank=True)

    def __unicode__(self):
        return self.titolo

    class Meta:
        verbose_name_plural = "Stagioni"

class Immagini(models.Model):
    titolo = models.CharField(max_length=100, verbose_name="Titolo del Progetto:")
    image = models.ImageField(blank=True, null=True, upload_to='uploaded_images')
    didascalia = models.TextField(null=True, blank=True)
    cropping = ImageRatioField('image', '500x480')
    slider = ImageRatioField('image', '1170x500')
    thumb = ImageRatioField('image', '595x335')
    croppinguno = ImageRatioField('image', '1140x487')
    croppingdue = ImageRatioField('image', '198x132')
    croppingtre = ImageRatioField('image', '1199x674')
    croppingquattro = ImageRatioField('image', '500x469', verbose_name="Design Miniatura")
    croppingcinque = ImageRatioField('image', '1200x800', verbose_name="Design HD")
    croppingsei = ImageRatioField('image', '1200x1125', verbose_name="News")
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.titolo

    class Meta:
        verbose_name_plural = "Galleria Immagini"
        ordering = ['id']


class Video(models.Model):
    titolo = models.CharField("Titolo del Video:", max_length=100, null=True, blank=True)
    youtubeurl = models.CharField("Indirizzo url youtube:", max_length=100, null=True, blank=True)
    idyoutube = models.CharField("ID filmato:", max_length=100, null=True, blank=True)
    start = models.IntegerField(default=0, null=True, blank=True, verbose_name="Punto di Partenza del Filmato in secondi")
    embedded = models.TextField("Codice Embedded YouTube", null=True, blank=True)
    thumb = models.ImageField(upload_to='uploaded_thum_youtube', null=True, blank=True)
    link = models.CharField(max_length=100, null=True, blank=True)
    didascalia = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.titolo

    class Meta:
        verbose_name_plural = "Galleria Video YouTube - Vimeo"


class Rai(models.Model):
    titolo = models.CharField("Titolo del Video:", max_length=100, null=True, blank=True)
    raiurl = models.CharField("Indirizzo url youtube:", max_length=100, null=True, blank=True)
    idrai = models.CharField("ID filmato:", max_length=100, null=True, blank=True)
    start = models.IntegerField(default=0, null=True, blank=True, verbose_name="Punto di Partenza del Filmato in secondi")
    embedded = models.TextField("Codice Embedded YouTube", null=True, blank=True)
    thumb = models.ImageField(upload_to='uploaded_thum_youtube', null=True, blank=True)
    miniatura = ImageRatioField('thumb', '960x1280')
    cropping = ImageRatioField('thumb', '1135x304')
    link = models.CharField(max_length=100, null=True, blank=True)
    didascalia = models.TextField(null=True, blank=True)
    canale = models.CharField("Canale", max_length=100, null=True, blank=True)
    pub_date = models.DateTimeField('data puntata')

    def __unicode__(self):
        return self.titolo

    class Meta:
        verbose_name_plural = "Galleria Filmati Rai"


class Vimeo(models.Model):
    titolo = models.CharField("Titolo del Video:", max_length=100, null=True, blank=True)
    url = models.CharField("Indirizzo url youtube:", max_length=100, null=True, blank=True)
    idvideo = models.CharField("ID filmato:", max_length=100, null=True, blank=True)
    start = models.IntegerField(default=0, null=True, blank=True, verbose_name="Punto di Partenza del Filmato in secondi")
    embedded = models.TextField("Codice Embedded YouTube", null=True, blank=True)
    thumb = models.ImageField(upload_to='uploaded_thum_youtube', null=True, blank=True)
    miniatura = ImageRatioField('thumb', '960x1280')
    cropping = ImageRatioField('thumb', '1135x304')
    link = models.CharField(max_length=100, null=True, blank=True)
    didascalia = models.TextField(null=True, blank=True)
    pub_date = models.DateTimeField('date puntata')

    def __unicode__(self):
        return self.titolo

    class Meta:
        verbose_name_plural = "Galleria Filmati Unconventional30"

class Ricettario(models.Model):
    titolo = models.CharField("Titolo:", max_length=100, null=True, blank=True)
    titolo_menu = models.CharField("Titolo Menu:", max_length=100, null=True, blank=True)
    stagione = models.ForeignKey(Stagioni, null=True, blank=True)
    body = models.TextField(null=True, blank=True, verbose_name="Descrizione")
    #body = RichTextField(null=True, blank=True, verbose_name="Descrizione")
    image = models.ImageField(blank=True, null=True, upload_to='uploaded_images')
    miniatura = ImageRatioField('image', '960x1280')
    cropping = ImageRatioField('image', '1135x304')
    video = models.ManyToManyField(Video, null=True, blank=True, verbose_name="Seleziona Video")
    pub_date = models.DateTimeField('date published')
    tags = TaggableManager(verbose_name="Parole chiave", blank=True)
    
    def __unicode__(self):
        return self.titolo


class Post(models.Model):
    titolo = models.CharField("Titolo:", max_length=100, null=True, blank=True)
    titolo_menu = models.CharField("Titolo Menu:", max_length=100, null=True, blank=True)
    categoria = models.ForeignKey(Categorie, null=True, blank=True)
    revhome = models.BooleanField('Home Gallery', 
                                    default=False, 
                                    help_text="Mostra IMG nella slide in home")
    body = models.TextField(null=True, blank=True, verbose_name="Descrizione")
    #body = RichTextField(null=True, blank=True, verbose_name="Descrizione")
    image = models.ImageField(blank=True, null=True, upload_to='uploaded_images')
    blog = models.BooleanField('Blog', 
    								default=False, 
                                    help_text="Attiva Pagina Standard")
    pagvideo = models.BooleanField('Pagina Video',
    								default=False,
                                    help_text="Attiva Pagina Video")
    pagvimeo = models.BooleanField('Pagina Unconventional30',
                                    default=False,
                                    help_text="Attiva Pagina Video Unconventional30")
    pagrai = models.BooleanField('Pagina Video Rai',
                                    default=False,
                                    help_text="Attiva Pagina Video Rai")
    pagrice = models.BooleanField('Pagina Ricettario',
                                    default=False,
                                    help_text="Attiva Pagina Ricettario")
    miniatura = ImageRatioField('image', '960x1280')
    cropping = ImageRatioField('image', '1170x500')
    galleria = models.ManyToManyField(Immagini, null=True, blank=True,
                                        verbose_name="Seleziona Immagini Galleria",
                                        help_text="Carica Immagini")
    video = models.ManyToManyField(Video, null=True, blank=True, 
                                        verbose_name="Seleziona Video",
                                        help_text="Carica Immagini")
    rai = models.ManyToManyField(Rai, null=True, blank=True,
                                        verbose_name="Video Rai",
                                        help_text="Carica Filmati della RAI")
    vimeo = models.ManyToManyField(Vimeo, null=True, blank=True,
                                        verbose_name="Video Unconventional30",
                                        help_text="Carica Filmati della tv Unconventional30")
    pub_date = models.DateTimeField('date published')
    tags = TaggableManager(verbose_name="Parole chiave", blank=True)
    
    def __unicode__(self):
        return self.titolo
