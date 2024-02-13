from django.db import models

# Create your models here.
class Contact(models.Model):
    Q_CHOICES = (
        ('general_query', 'General Query'),
        ('return', 'Return'),
        ('complaint', 'Complaint'),
    )

    # The type of query used
    q_type = models.CharField(max_length=14, choices=Q_CHOICES)
    order_number = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    message = models.TextField(max_length=3000, null=False, blank=False)

    def __str__(self):
        return self.email
