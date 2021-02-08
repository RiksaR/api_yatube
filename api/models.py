from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import UniqueConstraint

User = get_user_model()


class Group(models.Model):
    """A model for managing groups
    """
    title = models.CharField(
        'Заголовок группы',
        max_length=200,
        help_text='Введите название группы длиной не более 200 символов',
    )

    def __str__(self):
        """ Return a string representation
        """
        return f'Группа: {self.title}'


class Post(models.Model):
    """A model for managing posts
    """
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Название группы',
        help_text='Вы можете выбрать группу для этого поста',
        blank=True,
        null=True,
    )

    def __str__(self):
        """ Return a string representation
        """
        return self.text


class Comment(models.Model):
    """A model for managing comments
    """
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True,
    )

    def __str__(self):
        """ Return a string representation
        """
        return self.text


class Follow(models.Model):
    """A model for managing subscriptions
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='the user who subscribes',
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='the user to subscribe to',
    )

    class Meta:
        constraints = [UniqueConstraint(
            fields=['user', 'following'],
            name='unique_following',
        )]

    def __str__(self):
        """ Return a string representation
        """
        return f'Пользователь {self.user} подписан на {self.following}'
