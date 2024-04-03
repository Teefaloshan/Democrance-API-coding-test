from django.db import models
#Part1
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

#Part2
class Policy(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quote_amount = models.DecimalField(max_digits=8, decimal_places=2)
    state = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_state_history(self):
        return PolicyStateHistory.objects.filter(policy=self).order_by('-timestamp')
    
class PolicyStateHistory(models.Model):
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    state = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)


   