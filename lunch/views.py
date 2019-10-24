from django.shortcuts import render
from rest_framework import viewsets
from lunch.serializers import PlanSerializer
from lunch.models import Plan, Student
from django.views.generic.base import TemplateView
from django.utils import timezone
import datetime
from django.views.generic import View
from django.http import JsonResponse

# Create your views here.

class PlanViewSet(viewsets.ModelViewSet):
    
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class LunchView(TemplateView):
    
    template_name = "lunch/lunchview.html"
    
    def _context_helper(self, date, context):
        start_week = date - datetime.timedelta(date.weekday())
        Plan.objects.create_lunch_plan_for_week_starting(start_week)
        
        end_week = start_week + datetime.timedelta(4)
        days = list()
        for i in range(0, 5):
            weekday = start_week + datetime.timedelta(i)
            obj = ( weekday, 
                    Plan.objects.filter(date=weekday, lunch="H"), 
                    Plan.objects.filter(date=weekday, lunch="C")
                  )
            days.append(obj)
        context['thisweek'] = days
        context['start'] = start_week
        context['end'] = end_week
        context['students'] = Student.objects.all()
        context['show_next'] = True
        return context
        
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        date = timezone.now()
        return self._context_helper(date, context)

class NextWeekPlan(LunchView):
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        date = timezone.now() + datetime.timedelta(7)
        context = self._context_helper(date, context)
        context['show_next'] = False
        return context

class SwitchPlan(View):
    
    def post(self, request, pk, *args, **kwargs):
        
        plan = Plan.objects.get(pk = pk)
        print(request.POST)
        switch_to = request.POST.get('status')
        try:
            plan.lunch = switch_to
            plan.save()
        
            return JsonResponse({'status': 'ok'})
        except:
            return JsonResponse({'status': 'fail'})
            
    
    