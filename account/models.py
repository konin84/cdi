import email
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
# from django.core.validators import RegexValidator
# from patient.models import Patient

# phone_validator = RegexValidator(r"^(\+?\d{0,4})?\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{4}\)?)?$", "The phone number provided is invalid")


class UserAccountManager(BaseUserManager):
    use_in_migration =True

    def create_user(self , email, password = None):

        if not email or len(email) <= 0:   
            raise  ValueError("Email  is required in this field")
       
        if not password :
            raise ValueError("Password is must! Kindly provide a password")
          
        user = self.model(email=self.normalize_email(email),) 
    
        user.set_password(password)
        user.save(using = self._db)
        return user
      
    def create_superuser(self , email, password):
        user = self.create_user(
            email= self.normalize_email(email), 
            password = password)
        user.is_staff = True
        user.is_admin = True
        user.is_active = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):

    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        ACCOUNTANT = "ACCOUNTANT", 'Accountant'
        DOCTOR = "DOCTOR", 'Doctor'
        CASHIER = "CASHIER", 'Cashier',
        PATIENT = "PATIENT", 'Patient',
    
    class Gender(models.TextChoices):
        MALE = "MALE", 'Male'
        FEMELE = "FEMELE", 'Femele'
        OTHER = "OTHER", 'Autre'
        

    base_gender = Gender.MALE
    base_role = Role.ADMIN

    role = models.CharField(max_length=15, choices=Role.choices, default=base_role)
    email = models.EmailField(max_length=50, unique=True, verbose_name='email address')
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # The special permissions here
    is_accountant = models.BooleanField(default=False)
    is_cashier = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
   
    #Additional information
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=50)
    patient_id = models.IntegerField(null=True, blank=True)
    telephone = models.CharField(max_length=20, unique=True, blank=True, null=True)
    gender = models.CharField(max_length=15, choices=Gender.choices)
    # avatar = models.ImageField(null=True, default="images/avatar.svg", upload_to='images/users')
    createdon = models.DateTimeField(auto_now_add=True)
    

    # USERNAME_FIELD = "email"
    USERNAME_FIELD = "email"
        
  #  defining the manager for the UserAccount model
    objects = UserAccountManager()
      
    def __str__(self):
        return str(self.email)
        # return str(self.email)
      
    def has_perm(self , perm, obj = None):
        return self.is_admin
      
    def has_module_perms(self , app_label):
        return True
  
    def save(self , *args , **kwargs):
        if not self.role or self.role == None : 
            self.role = UserAccount.base_role
        return super().save(*args , **kwargs)
    

class AdministratorManager(models.Manager):
     
     
    def create_user(self , email , password = None):
        if not email or len(email) <= 0 : 
            raise  ValueError("Email field is required !")
        if not password :
            raise ValueError("Password is must !")
        email  = email.lower()
        user = self.model(
            email = email
        )

        user.set_password(password)
        user.save(using = self._db)
        return user
     
    def get_queryset(self , *args, **kwargs):
         
        queryset = super().get_queryset(*args , **kwargs)
        queryset = queryset.filter(role = UserAccount.Role.ADMIN)
        return queryset	

class Administrator(UserAccount):
    
	class Meta :
		proxy = True
	objects = AdministratorManager()
	
	def save(self , *args , **kwargs):
		self.role = UserAccount.Role.ADMIN
		self.is_admin = True
		self.is_active = True
		self.is_staff = True
        
		return super().save(*args , **kwargs)

class DoctorManager(models.Manager):
     
    def create_user(self , email , password = None):
         
        if not email or len(email) <= 0 : 
            raise  ValueError("Email field is required !")
        if not password :
            raise ValueError("Password is must !")
        email  = email.lower()
        user = self.model(
            email = email
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def get_queryset(self , *args, **kwargs):
    
        queryset = super().get_queryset(*args , **kwargs)
        queryset = queryset.filter(role = UserAccount.Role.DOCTOR)
        return queryset	

class Doctor(UserAccount):
    
        
    class Meta :
        proxy = True
    objects = DoctorManager()
    
    def save(self , *args , **kwargs):
        self.role = UserAccount.Role.DOCTOR
        self.is_doctor = True
        self.is_active = True
        self.is_staff= True
        return super().save(*args , **kwargs)

class AccountantManager(models.Manager):
     
    def create_user(self , email , password = None):
         
        if not email or len(email) <= 0 : 
            raise  ValueError("Email field is required !")
        if not password :
            raise ValueError("Password is must !")
        email  = email.lower()
        user = self.model(
            email = email
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    #  def get_full_name(self):
    #     return '%s %s' % (self.first_name, self.last_name)

    def get_queryset(self , *args, **kwargs):
        queryset = super().get_queryset(*args , **kwargs)
        queryset = queryset.filter(role = UserAccount.Role.ACCOUNTANT)
        return queryset	

class Accountant(UserAccount):
	class Meta :
		proxy = True
	objects = AccountantManager()
	
	def save(self , *args , **kwargs):
		self.role = UserAccount.Role.ACCOUNTANT
		self.is_accountant = True
		self.is_active = True
		self.is_staff = True
       
		return super().save(*args, **kwargs)

class CashierManager(models.Manager):
     
    def create_user(self , email , password = None):
         
        if not email or len(email) <= 0 : 
            raise  ValueError("Email field is required !")
        if not password :
            raise ValueError("Password is must !")
        email  = email.lower()
        user = self.model(email = email)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def get_queryset(self , *args, **kwargs):
        queryset = super().get_queryset(*args , **kwargs)
        queryset = queryset.filter(role = UserAccount.Role.CASHIER)
        return queryset	

class Cashier(UserAccount):
        
    class Meta :
        proxy = True
    objects = CashierManager()

    def save(self , *args , **kwargs):
        self.role = UserAccount.Role.CASHIER
        self.is_cashier = True
        self.is_active = True
        return super().save(*args, **kwargs)

class PatientManager(models.Manager):
     
    def create_user(self , email , password = None):
         
        if not email or len(email) <= 0 : 
            raise  ValueError("Email field is required !")
        if not password :
            raise ValueError("Password is must !")
        email  = email.lower()
        user = self.model(email = email)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def get_queryset(self , *args, **kwargs):
        queryset = super().get_queryset(*args , **kwargs)
        queryset = queryset.filter(role = UserAccount.Role.PATIENT)
        return queryset	

class Patient(UserAccount):
        
    class Meta :
        proxy = True
    objects = PatientManager()

    def save(self , *args , **kwargs):
        self.role = UserAccount.Role.PATIENT
        self.is_patient = True
        self.is_active = True

        return super().save(*args, **kwargs)




