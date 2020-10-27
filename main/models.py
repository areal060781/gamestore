from django.db import models


class GamePlatform(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class GameManager(models.Manager):
    def get_highlighted(self):
        return self.filter(highlighted=True)

    def get_no_highlighted(self):
        return self.filter(highlighted=False)

    def get_by_platform(self, platform):
        return self.filter(gameplatform__name__iexact=platform)


class Game(models.Model):
    class Meta:
        ordering = ['-highlighted', 'name']

    name = models.CharField(max_length=100)
    release_year = models.IntegerField(null=True)
    developer = models.CharField(max_length=100)
    published_by = models.CharField(max_length=100)

    image = models.ImageField(
        upload_to='images/',
        default='images/placeholder.png',
        max_length=100
    )

    gameplatform = models.ForeignKey(GamePlatform, null=False, on_delete=models.CASCADE)

    highlighted = models.BooleanField(default=False)

    objects = GameManager()

    def __str__(self):
        return f'{self.gameplatform.name} - {self.name}'
