from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

class Bootcamp(models.Model):
    title = models.CharField(
        _('Titre'),
        max_length=100,
        help_text=_('Titre complet du bootcamp')
    )
    duration = models.CharField(
        _('Durée'),
        max_length=50,
        help_text=_('Ex: 12 semaines, 3 mois')
    )
    price = models.DecimalField(
        _('Prix'),
        max_digits=10,
        decimal_places=2,
        help_text=_('Prix en FCFA')
    )
    next_session = models.DateField(
        _('Prochaine session'),
        help_text=_('Date de début de la prochaine session')
    )
    description = models.TextField(
        _('Description'),
        help_text=_('Détails complets du programme')
    )
    is_active = models.BooleanField(
        _('Actif'),
        default=True,
        help_text=_('Ce bootcamp est-il actuellement disponible ?')
    )

    class Meta:
        verbose_name = _('Bootcamp')
        verbose_name_plural = _('Bootcamps')
        ordering = ['next_session']

    def __str__(self):
        return f"{self.title} - {self.next_session}"

class Lead(models.Model):
    class Status(models.TextChoices):
        NEW = 'NEW', _('Nouveau')
        CONTACTED = 'CONTACTED', _('Contacté')
        REGISTERED = 'REGISTERED', _('Inscrit')
        REJECTED = 'REJECTED', _('Non intéressé')

    phone_regex = RegexValidator(
        regex=r'^(77|76|70|78|75|33)\d{7}$',
        message=_("Format: 77|76|70|78 suivi de 7 chiffres")
    )

    name = models.CharField(
        _('Nom complet'),
        max_length=100
    )
    email = models.EmailField(
        _('Email')
    )
    phone = models.CharField(
        _('Téléphone'),
        max_length=20,
        validators=[phone_regex]
    )
    message = models.TextField(
        _('Message'),
        blank=True,
        help_text=_('Pourquoi êtes-vous intéressé ?')
    )
    bootcamp = models.ForeignKey(
        Bootcamp,
        on_delete=models.CASCADE,
        verbose_name=_('Bootcamp'),
        related_name='leads'
    )
    status = models.CharField(
        _('Statut'),
        max_length=20,
        choices=Status.choices,
        default=Status.NEW
    )
    created_at = models.DateTimeField(
        _('Date de création'),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        _('Dernière modification'),
        auto_now=True
    )
    updated_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Modifié par'),
        related_name='updated_leads'
    )

    class Meta:
        verbose_name = _('Lead')
        verbose_name_plural = _('Leads')
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f"{self.name} - {self.get_status_display()} ({self.bootcamp.title})"

    def save(self, *args, **kwargs):
        """Enregistre qui a modifié le lead"""
        if self.pk and not self.updated_by:
            # Logique pour enregistrer l'utilisateur actuel
            pass
        super().save(*args, **kwargs)