from django.db import models
from django.utils import timezone
import datetime
'''여기서 정의된 모델(데이터베이스 테이블)은 migrate 명령을 이용하여
실제 데이터 베이스에 적용할 수 있다

*migrate 사용 순서
1. 모델을 변경(models.py)
2. python manage.py makemigrations<앱명> (변경사항에 대한 migration을 만들기)
3. python manage.py migration (데이터베이스에 적용)

sql을 확인하기위해서는 sqlmigrate명령어 사용
'''

# Create your models here.
class Question(models.Model):
	question_txt = models.CharField(max_length=200)#schema 최대길이
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_txt
	
	def published_recently(self):
		return self.pub_date >= timezone.now()-datetime.timedelta(days=1)


class Choice(models.Model):
	question= models.ForeignKey(Question, on_delete=models.CASCADE)#ForeignKey=>관계설정
	choice_text=models.CharField(max_length=200)
	votes =models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text

# Django 모델 API (데이터를 추가/갱신/조회) Django는 ORM모델을 사용 object relational mapper
# insert : 객체 생성 후에 save()함수를 이용하여 새 객체를 insert한다
# select : Django 모델 클래스에 대해 objects라는 Manager 객체를 자도으로 추가한다.
	# objects는 django.db.models.Manager 이다. 이 매니저 객체를 이용해서 데이터 필터링 할 수 있고, 기타 여러기능들을 사용 할 수 있다
	# 데이터를 읽어올 떄 바로 이 매니저 객체를 사용하였음(모델클래스.objects)
	# all() : 테이블 데이터를 모두 가져온다. Question.objects.all()
	# get() : 하나의 row만을 가져올 때 사용하는 메소드이다.Primary Key를 가져올 때는 Question.Objects.get(pk =1)
	# filter() : 특정 조건을 이용하여 Row들을 가져오기 위한 메소드
	# exclude() : filter와 반대되는 개념, 특정 조건을 제외한 나머지 Row들을 가져오기 위한 메소드
	# count() : 데이터의 갯수(row 수)를 세기위한 메소드
	# order_by() : 데이터를 특정 키에 따라 정렬하기 위한 메소드, 정렬키를 인수로 사용하는데
		#-가  붙으면 내림차순이 된다.
		#Question.objects.order_by('-id','aa')
	# distinct() : 증복된 값은 하나로만 표시하기 위한 메소드, SQL의 SELECT DISTINCT와 같은 기능
	# rows = User.objects.distinct('name')
	# first() : 여러개의 데이터중에서 처음에 있는 row만을 리텅한다.
		#rows = User.objects.order_by('name').first
		#위 겨로가는 저열된 레코드 중에서 가장 첫번째 row가 리턴값이 된다
	#last() : 여러개의 데이터 중에서 마지막 row만을 리턴한다

	##위의 메소드들은 실제데이터 결과를 직접 리턴하기보다는 Django에서 제공하는 쿼리 표현식(Query set)의 형태로 리턴한다.
	##여러 메소드들을 체인처럼 연결해서 사용할 수 있다.

	##row = User.objects.filter(name = 'Lee').order_by('-id').first()

#update : 수정할 row객체를 얻은 후에 변경할 필드를 수정한다. 수정한 후에는 save() 메소드를 호출한다. 
#SQL의 UPDATE가 실행되어 테이블에 데이터가 갱신된다

#delete: Row객체를 얻어온 후에 delete()메소드를 호출한다. delete메소드에 의해서 바로 데이터베이스의 레코드(row)가 삭제된다.

#python manage.py createsuperuser 관리자 만들기.