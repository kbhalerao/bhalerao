from django.test import TestCase, Client
from lunch.models import Student, Plan
from django.utils import timezone
from lunch.serializers import StudentSerializer, PlanSerializer
import datetime
from django.urls import reverse


# Create your tests here.
class PlanTestCase(TestCase):
    def setUp(self):
        pass
    
    def test_create_student(self):
    
        s = Student.objects.create(name="Aaron")
        self.assertNotEqual(s.pk, None)
    
    def test_create_plan(self):
        
        s = Student.objects.create(name="Karena")
        p = Plan.objects.create(student = s, 
                                date = timezone.now().date(), 
                                lunch = "H")
        self.assertIsNotNone(p.id)
        self.assertEqual(p.date, timezone.now().date())
    
    def test_ensure_plan(self):
        
        s = Student.objects.create(name="Samarth")
        date = timezone.now()
        start_week = date - datetime.timedelta(date.weekday())
        Plan.objects.create_lunch_plan_for_week_starting(start_week)
        self.assertEqual(Plan.objects.all().count(), 5)
        
        Plan.objects.create_lunch_plan_for_week_starting(start_week)
        self.assertEqual(Plan.objects.all().count(), 5)
        

class SerializerTests(TestCase):
    
    def setUp(self):
        self.s = Student.objects.create(name="Karena")
        self.p = Plan.objects.create(student = self.s, 
                                     date = timezone.now().date(), 
                                     lunch = "H")
                                
    def test_student_serializer(self):
    
        s_ser = StudentSerializer(self.s)
        self.assertEqual(s_ser.data['name'], "Karena")
    
    def test_plan_serializer(self):
        p_ser = PlanSerializer(self.p)


class APITests(TestCase):
    
    def setUp(self):
        self.s = Student.objects.create(name="Karena")
        self.p = Plan.objects.create(student = self.s, 
                                     date = timezone.now().date(), 
                                     lunch = "H")
    
    def test_view(self):
        
        url = "/"
        client = Client()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.s.name.encode(), response.content)                         
    
    def test_switch_plan(self):
        
        url = reverse("switch_plan", kwargs={'pk': self.p.pk})
        client = Client()
        
        response = client.post(url, {'status': 'C'})
        self.assertEqual(response.status_code, 200)
        self.p.refresh_from_db()
        self.assertEqual(self.p.lunch, "C")
    
        
        response = client.post(url, {'status': 'H'})
        self.assertEqual(response.status_code, 200)
        self.p.refresh_from_db()
        self.assertEqual(self.p.lunch, "H")
        
        
        
        
        