from django.db import models

# Create your models here.

class SourceMaster(models.Model):
    Source_ID = models.AutoField(primary_key=True)
    Source_name = models.CharField(max_length=100)
    Rate_per_candidate = models.BigIntegerField()
    Contact_no = models.BigIntegerField()
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    Employee_id = models.CharField(max_length=100, blank = True, null = True)
    Date_of_Entry = models.DateTimeField("Created At", auto_now_add=True)


class CourseMaster(models.Model):
    Course_ID = models.AutoField(primary_key=True)
    Course_Name = models.CharField(max_length=100)
    Fees = models.BigIntegerField()

class call_mast(models.Model):
    Candidate_ID = models.AutoField(primary_key=True)
    Candidate_name = models.CharField(max_length=255)
    Contact_number = models.CharField(max_length=255)
    Email_id=models.CharField(max_length=255)
    Interested_area=models.CharField(max_length=255)
    Source_name = models.ForeignKey(SourceMaster,db_column='Source_ID',to_field='Source_ID',related_name='+',default=1, on_delete=models.CASCADE)
    Receiving_date=models.DateField()
    class Meta:
        db_table="calling master"

class call_trans(models.Model):
    Transaction_id = models.AutoField(primary_key=True)
    Candidate_ID = models.ForeignKey(call_mast, db_column='Candidate_ID',to_field='Candidate_ID',related_name='+',default=1, on_delete=models.CASCADE)
    Feedback=models.CharField(max_length=100)
    Next_Call_Date=models.DateField()
    Next_Call_Time=models.TimeField()
    Cofirm=models.CharField(max_length=100)
    Call_Date=models.DateField()
    Call_Time=models.TimeField()
    class Meta:
        db_table="calling transaction"

class CandidateTrainingMaster(models.Model):
    Training_ID = models.AutoField(primary_key=True)
    Candidate_ID = models.ForeignKey(call_mast, db_column='Candidate_ID',to_field='Candidate_ID',related_name='+',default=1, on_delete=models.CASCADE)
    canname = models.CharField(max_length=100)
    ContactNo = models.BigIntegerField()
    email = models.EmailField()
    qualification = models.CharField(max_length=250, )
    idProofName = models.CharField(max_length=250)
    idProofNo = models.CharField(max_length=250)
    dateOfBirth = models.DateField()
    Course_ID = models.ForeignKey(CourseMaster,db_column='Course_ID',to_field='Course_ID',related_name='+',default=1, on_delete=models.CASCADE) 
    Placement = models.CharField(max_length=250)
    callId = models.IntegerField()
    Address = models.TextField()
    parentName = models.CharField(max_length=250)
    offerId = models.IntegerField() 
    ParentCont = models.CharField(max_length=250)
    dateOfReg = models.DateField()
    Status = models.CharField(max_length=250)
    paymentDueDay = models.DateField()
    noOfInstallments = models.IntegerField()
    Date_of_entry  = models.DateTimeField("Created At", auto_now_add=True)

class training_trans(models.Model):
    Payment_ID = models.AutoField(primary_key=True)
    Candidate_name=models.CharField(max_length=100)
    Date_of_transaction=models.DateField()
    Course_ID = models.ForeignKey(CourseMaster,db_column='Course_ID',to_field='Course_ID',related_name='+',default=1, on_delete=models.CASCADE) 
    Course_amount=models.CharField(max_length=100)
    Payment_mode=models.CharField(max_length=100)
    Amount_deposited=models.CharField(max_length=100)
    Bank_transaction_id=models.CharField(max_length=20)
    Bank_account_number=models.CharField(max_length=20)
    Cheque_number=models.CharField(max_length=100)
    Warning_level=models.CharField(max_length=100)
    Payment_status=models.CharField(max_length=100)
    Reason_for_nonPayment=models.CharField(max_length=100)
    class Meta:
        db_table="training transaction"