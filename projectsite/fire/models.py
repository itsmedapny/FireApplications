from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Locations(BaseModel):
    name = models.CharField(max_length=150)
    latitude = models.DecimalField(
        max_digits=22, decimal_places=16, null=True, blank=True)
    longitude = models.DecimalField(
        max_digits=22, decimal_places=16, null=True, blank=True)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)  # can be in separate table
    country = models.CharField(max_length=150)  # can be in separate table
    
    
    def __str__(self):
        return f"{self.city}"


class Incident(BaseModel):
    SEVERITY_CHOICES = (
        ('Minor Fire', 'Minor Fire'),
        ('Moderate Fire', 'Moderate Fire'),
        ('Major Fire', 'Major Fire'),
    )
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    date_time = models.DateTimeField(blank=True, null=True)
    severity_level = models.CharField(max_length=45, choices=SEVERITY_CHOICES)
    description = models.CharField(max_length=250)
    
    
    def __str__(self):
        return f"{self.location}"


class FireStation(BaseModel):
    name = models.CharField(max_length=150)
    latitude = models.DecimalField(
        max_digits=22, decimal_places=16, null=True, blank=True)
    longitude = models.DecimalField(
        max_digits=22, decimal_places=16, null=True, blank=True)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)  # can be in separate table
    country = models.CharField(max_length=150)  # can be in separate table
    
    
    def __str__(self):
        return f"{self.name}"


class Firefighters(BaseModel):
    XP_RANK = (
        ('Veteran', 'Probationary Firefighter'),
        ('Firefighter I', 'Firefighter I'),
        ('Firefighter II', 'Firefighter II'),
        ('Firefighter III', 'Firefighter III'),
        ('Driver', 'Driver'),
        ('Captain', 'Captain'),
        ('Battalion Chief', 'Battalion Chief'),)
    XP_CHOICES = (
        ('Entry-Level Firefighters', 'Entry-Level Firefighters'),
        ('Junior Firefighters', 'Junior Firefighters'),
        ('Senior Firefighters', 'Senior Firefighters'),
        ('Company Officers', 'Company Officers'),
        ('Chief Officers', 'Chief Officers'),)
    
    name = models.CharField(max_length=150)
    rank = models.CharField(
        max_length=45, null=True, blank=True, choices=XP_RANK)
    experience_level = models.CharField(
        max_length=45, null=True, blank=True, choices=XP_CHOICES)
    station = models.CharField(max_length=45, null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.name}"


class FireTruck(BaseModel):
    truck_number = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    capacity = models.CharField(max_length=150)  
    station = models.ForeignKey(FireStation, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"{self.model}"


class WeatherConditions(BaseModel):
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=10, decimal_places=2)
    humidity = models.DecimalField(max_digits=10, decimal_places=2)
    wind_speed = models.DecimalField(max_digits=10, decimal_places=2)
    weather_description = models.CharField(max_length=150)
    
    
    def __str__(self):
        return f"{self.weather_description}"
    