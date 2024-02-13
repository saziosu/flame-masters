from django.db import models

# Create your models here.
class Contact(models.Model):
    """
    A model to store contact form entries
    """
    Q_CHOICES = (
        ('general_query', 'General Query'),
        ('return', 'Return'),
        ('complaint', 'Complaint'),
    )

    # The type of query used
    reason = models.CharField(max_length=14, choices=Q_CHOICES)
    order_number = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        # order the contact form posts on when they were created
        # newest first
        ordering = ['-created_on']

    def __str__(self):
        return self.email
