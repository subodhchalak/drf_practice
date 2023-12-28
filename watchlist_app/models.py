# django imports
from django.db import models
from django.contrib.auth.models import User

# in app imports
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator
)

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
    name = models.CharField(  
        max_length = 100,
        blank = False,
        null = False,
        # unique = True
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


#---------------------------------------------------------------------------
#                            Review
#---------------------------------------------------------------------------


class Review(models.Model):
    """
    It's a model to save the review of watchlists
    """
    reviewer = models.ForeignKey(
        to = User,
        on_delete = models.CASCADE,
        related_name = 'review',
        default = None,
        blank = False
    )
    watchlist = models.ForeignKey(
        to = Watchlist,
        on_delete = models.CASCADE,
        related_name = 'review'
    )
    rating = models.PositiveIntegerField(
        validators = [MinValueValidator(1), MaxValueValidator(5)]
    )
    description = models.CharField(
        max_length = 250,
        blank = False,
        null = False
    )
    is_active = models.BooleanField(
        default = True
    )
    created_at = models.DateTimeField(
        auto_now_add = True
    )
    updated_at = models.DateTimeField(
        auto_now = True
    )

    def __str__(self):
        return str(self.reviewer)
    
    class Meta:
        ordering = ('-id', )