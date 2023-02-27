from django.db import models
from django.core.validators import RegexValidator

URL_VALIDATOR_MESSAGE = 'Not a valid URL.'
# URL_VALIDATOR = RegexValidator(regex='/^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$/',
#                                message=URL_VALIDATOR_MESSAGE)
URL_VALIDATOR = RegexValidator(regex='/^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)',
                               message=URL_VALIDATOR_MESSAGE)
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, )
    image = models.ImageField(upload_to='portfolio/images/')
    # url = models.URLField(blank=True, validators=[URL_VALIDATOR])
    url = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.title
