from django.db import models

# Create your models here.


#---------------------------------------------------------------------------
#                            Platform
#---------------------------------------------------------------------------

class Platform(models.Model):
    name = models.CharField(
        max_length = 50,
        blank = False,
        null = False,
        unique = True
    )
    description = models.CharField(
        max_length = 300,
        blank = True,
        null = True
    )
    website = models.URLField(
        blank = False,
        null = True
    )
    created_at = models.DateTimeField(
        auto_now_add = True
    )
    updated_at = models.DateTimeField(
        auto_now = True
    )

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('-id', )


#---------------------------------------------------------------------------
#                               Watchlist
#---------------------------------------------------------------------------


class Watchlist(models.Model):
    """
    It's a model to save the Watchlists
    """
    platform = models.ForeignKey(
        to = Platform,
        on_delete = models.CASCADE,
        related_name = 'watchlist',
        blank = False,
        null = True
    )
    name = models.name = models.CharField(
        max_length = 100,
        blank = False,
        null = False,
        unique = True
    )
    description = models.CharField(
        max_length = 300,
        blank = True,
        null = False,
        default = None
    )
    is_active = models.BooleanField(
        verbose_name = "Status",
        default = True,
    )
    created_at = models.DateTimeField(
        auto_now_add = True
    )
    updated_at = models.DateTimeField(
        auto_now = True
    )

    def __str__(self):
        return self.name
     
    class Meta:
        ordering = ('-id', )