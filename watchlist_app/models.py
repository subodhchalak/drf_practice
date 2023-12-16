from django.db import models

# Create your models here.

#---------------------------------------------------------------------------
#                            Movie
#---------------------------------------------------------------------------

class Movie(models.Model):
    name = models.name = models.CharField(
        max_length = 100,
    )
    description = models.CharField(
        max_length = 300,
        blank = True,
        null = True
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