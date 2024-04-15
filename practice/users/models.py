from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    nickname = models.CharField(max_length=10, null=True)
    image = models.ImageField(upload_to='prfile/',null=True)

    class Meta:
        db_table = 'profile' #장고가 마음대로 테이블 이름 정해서 만듦 이거 써주면 내가 지정한 이름으로 테이블 생성 
 
        def __str__(self): #출력시 nickname리턴해줌
            return self.nickname