from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models


User = get_user_model()


class News(models.Model):
    """News model."""

    title = models.CharField(
        verbose_name="Заголовок",
        max_length=255,
    )
    slug = models.SlugField(
        verbose_name="url новости",
        blank=True,
        max_length=255,
        unique=True,
    )
    thumbnail = models.ImageField(
        verbose_name="Изображение",
        blank=True,
        upload_to="images/thumbnails/%Y/%m/%d/",
        validators=[
            FileExtensionValidator(
                allowed_extensions=("png", "jpg", "webp", "jpeg", "gif"),
            ),
        ],
    )
    description = models.TextField(
        verbose_name="Описание новости",
    )
    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время добавления",
    )
    time_update = models.DateTimeField(
        auto_now=True,
        verbose_name="Время обновления",
    )
    author = models.ForeignKey(
        to=User,
        verbose_name="Автор",
        on_delete=models.SET_DEFAULT,
        related_name="author_post",
        default=1,
    )

    class Meta:
        """Sorting, model name in the admin panel, table with data."""

        db_table = "app_news"
        ordering = ["-time_create"]
        indexes = [models.Index(fields=["-time_create"])]
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__thumbnail = self.thumbnail if self.pk else None

    def __str__(self):
        """Return the string representation of the object as the news title."""
        return self.title
