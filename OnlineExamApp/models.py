from django.db import models

# Create your models here.
class Admin(models.Model):
	u_id=models.IntegerField()
	username=models.CharField(max_length=255)
	useremail=models.CharField(max_length=255)
	userpassword=models.CharField(max_length=255)
	userpassword_md5=models.CharField(max_length=255)
	user_status=models.IntegerField()
	area_permission=models.CharField(max_length=255)

class Batch(models.Model):
	b_id=models.IntegerField()
	batch_name=models.CharField(max_length=255)
	batch_time=models.TimeField(auto_now=True)
	batch_status=models.IntegerField()

class Center(models.Model):
	c_id=models.IntegerField()
	center_name=models.CharField(max_length=255)
	center_address=models.CharField(max_length=300)
	center_code=models.CharField(max_length=255)
	center_logo=models.CharField(max_length=255)
	location=models.CharField(max_length=255)
	phoneno=models.CharField(max_length=10)
	email=models.CharField(max_length=255)
	username=models.CharField(max_length=255)
	password=models.CharField(max_length=255)
	password_md5=models.CharField(max_length=255)
	theme_id=models.CharField(max_length=255)
	center_status=models.IntegerField()
	about_center=models.CharField(max_length=255)

class Category(models.Model):
	category_id=models.IntegerField()
	category_name=models.CharField(max_length=225)
	category_status=models.IntegerField()

class Subcategory(models.Model):
	subcategory_id=models.IntegerField()
	subcategory_name=models.CharField(max_length=255)
	subcategory_status=models.IntegerField()
	category1=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="subcategory")

class Subject(models.Model):
	subject_id=models.IntegerField()
	subject_name=models.CharField(max_length=255)
	subject_status=models.IntegerField()
	category2=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="subject1")
	subcategory1=models.ForeignKey(Subcategory,on_delete=models.CASCADE,related_name="subject2")
	
class Exam(models.Model):
	e_id=models.IntegerField()
	exam_name=models.CharField(max_length=255)
	exam_status=models.IntegerField()
	exam_date=models.DateField()
	exam_time=models.TimeField()
	exam_duration=models.CharField(max_length=255)
	neg_marks_status=models.IntegerField()
	negative_marks=models.IntegerField()
	time_reduction=models.IntegerField()
	passing_percentage=models.IntegerField()
	re_exam_day=models.IntegerField()
	terms_condition=models.TextField()
	result_show_on_mail=models.IntegerField()
	show_question=models.CharField(max_length=255)
	sort_order=models.CharField(max_length=255)
	category_id=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="exam1")
	subcategory_id=models.ForeignKey(Subcategory,on_delete=models.CASCADE,related_name="exam2")
	subject_id=models.ForeignKey(Subject,on_delete=models.CASCADE,related_name="exam3")
	center_id=models.ForeignKey(Center,on_delete=models.CASCADE,related_name="exam4")
	
class Practice_exam(models.Model):
	p_e_id=models.IntegerField()
	passing_percentage=models.IntegerField()
	re_exam_day=models.IntegerField()
	exam_name=models.CharField(max_length=255)
	exam_status=models.IntegerField()
	exam_duration=models.CharField(max_length=255)
	neg_mark_status=models.IntegerField()
	negative_marks=models.IntegerField()
	terms_condition=models.TextField()
	category_id=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="pexam1")
	subcategory_id=models.ForeignKey(Subcategory,on_delete=models.CASCADE,related_name="pexam2")
	center_id=models.ForeignKey(Center,on_delete=models.CASCADE,related_name="pexam3")
	subjects_id=models.ForeignKey(Subject,on_delete=models.CASCADE,related_name="pexam4")
	
	
class Student(models.Model):
	student_id=models.IntegerField()
	student_name=models.CharField(max_length=250)
	student_father=models.CharField(max_length=255)
	student_mother=models.CharField(max_length=255)
	student_dob=models.CharField(max_length=255)
	student_address=models.TextField()
	student_phone=models.CharField(max_length=255)
	student_email=models.CharField(max_length=255)
	user_name=models.CharField(max_length=255)
	password=models.CharField(max_length=255)
	student_status=models.IntegerField()
	category_id=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="student1")
	subcategory_id=models.ForeignKey(Subcategory,on_delete=models.CASCADE,related_name="student2")
	center_id=models.ForeignKey(Center,on_delete=models.CASCADE,related_name="student3")
	b_id=models.ForeignKey(Batch,on_delete=models.CASCADE,related_name="student4")
	
class Practice_exam_status(models.Model):
	pid=models.IntegerField()
	exam_date=models.DateField()
	status=models.IntegerField()
	starttime=models.CharField(max_length=255)
	endtime=models.CharField(max_length=255)
	noofattempts=models.IntegerField(max_length=255)
	pass_or_fail=models.CharField(max_length=255)
	student_id=models.ForeignKey(Student,on_delete=models.CASCADE,related_name="practice")
	exams_id=models.ForeignKey(Exam,on_delete=models.CASCADE,related_name="practice2")
	
	

class Question(models.Model):
	q_id=models.IntegerField()
	question=models.CharField(max_length=255)
	typeofquestion=models.CharField(max_length=255)
	option_a=models.CharField(max_length=255)
	option_b=models.CharField(max_length=255)
	option_c=models.CharField(max_length=255)
	option_d=models.CharField(max_length=255)
	correct_ans=models.CharField(max_length=255)
	question_status=models.IntegerField(max_length=2)
	marks=models.IntegerField()
	subject_id=models.ForeignKey(Subject,on_delete=models.CASCADE,related_name="question1")
	category_id=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="question2")
	subcategory_id=models.ForeignKey(Subcategory,on_delete=models.CASCADE,related_name="question3")
	

class Main_answer(models.Model):
	m_a_id=models.IntegerField()
	ans=models.CharField(max_length=255)
	marks=models.IntegerField()
	category_id=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="answer1")
	subcategory_id=models.ForeignKey(Subcategory,on_delete=models.CASCADE,related_name="answer2")
	subject_id=models.ForeignKey(Subject,on_delete=models.CASCADE,related_name="aswer3")
	exam_id=models.ForeignKey(Exam,on_delete=models.CASCADE,related_name="answer4")
	question_id=models.ForeignKey(Question,on_delete=models.CASCADE,related_name="answer5")
	student_id=models.ForeignKey(Student,on_delete=models.CASCADE,related_name="answer6")


class Practice_question(models.Model):
	p_q_id=models.IntegerField()
	question=models.CharField(max_length=255)
	typeofquestion=models.CharField(max_length=255)
	option_a=models.CharField(max_length=255)
	option_b=models.CharField(max_length=255)
	option_c=models.CharField(max_length=255)
	option_d=models.CharField(max_length=255)
	correct_ans=models.CharField(max_length=255)
	question_status=models.IntegerField(max_length=2)
	marks=models.IntegerField()
	p_e_id=models.ForeignKey(Practice_exam,on_delete=models.CASCADE,related_name="pquestion")

class Practice_answer(models.Model):
	p_a_id=models.IntegerField()
	ans=models.CharField(max_length=255)
	marks=models.IntegerField()
	examdate=models.DateField()
	correct_ans=models.CharField(max_length=255)
	typeofquestion=models.CharField(max_length=255)
	exam_id=models.ForeignKey(Center,on_delete=models.CASCADE,related_name="panswer1")
	question_id=models.ForeignKey(Question,on_delete=models.CASCADE,related_name="panswer2")
	student_id=models.ForeignKey(Student,on_delete=models.CASCADE,related_name="panswer3")
	
class Notice(models.Model):
	n_id=models.IntegerField()
	notice=models.TextField()
	notice_subject=models.CharField(max_length=255)
	notice_date=models.DateField()
	status=models.IntegerField()     
    
class Noticestudent(models.Model):
    ns_id=models.IntegerField()
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE,related_name="Noticestudent")
    notice_id=models.ForeignKey(Notice,on_delete=models.CASCADE,related_name="Notice1")
    center_id=models.ForeignKey(Center,on_delete=models.CASCADE,related_name="Noticestudent1")
    notice_date=models.DateField()
    
class Noticecenter(models.Model):
    nc_id=models.IntegerField() 
    center_id=models.ForeignKey(Center,on_delete=models.CASCADE,related_name="Noticecenter1") 
    notice_id=models.ForeignKey(Notice,on_delete=models.CASCADE,related_name="Notice2") 
    notice_date=models.DateField()
    
class Main_exam_status(models.Model):
    main_id=models.IntegerField()
    exam_id=models.ForeignKey(Exam,on_delete=models.CASCADE,related_name="practice_status")   
    status=models.IntegerField()
    starttime=models.CharField(max_length=255) 
    endtime=models.CharField(max_length=255)
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE,related_name="studentid")
    noofattempts=models.IntegerField()
    pass_or_fail=models.CharField(max_length=255)
    user_score=models.DecimalField(max_digits=10, decimal_places=3)
    passing_score=models.DecimalField(max_digits=10, decimal_places=3)
    total_score=models.DecimalField(max_digits=10, decimal_places=3)
    total_question=models.IntegerField()    
    negative_mark=models.IntegerField()
