from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from data_viz.models import School,Student,Summary,Class,Answers,Assessment_Areas,Award,Subject



# Create your views here.
award_data = Award.objects.all()
assessment_area_data = Assessment_Areas.objects.all()
answer_data = Answers.objects.all()
class_data = Class.objects.all()
school_data = School.objects.all()
student_data = Student.objects.all()
summary_data = Summary.objects.all()
subject_data = Subject.objects.all()


def get_query_set(entity_name):

    global award_data,assessment_area_data,answer_data,class_data,school_data,student_data,summary_data,subject_data

    if (entity_name == 'award'):
        return award_data
    elif (entity_name == 'assessmentareas'):
        return assessment_area_data
    elif (entity_name == 'class'):
        return class_data
    elif (entity_name == 'school'):
        return school_data
    elif (entity_name == 'students'):
        return student_data
    elif (entity_name == 'answer'):
        return answer_data
    elif (entity_name == 'subjects'):
        return subject_data
    elif (entity_name == 'summary'):
        return summary_data
    else:
        return None
    
def handle(request):

    global award_data,assessment_area_data,answer_data,class_data,school_data,student_data,summary_data,subject_data
    global student_data_index,summary_data_index
    category = request.GET.get("category" , "None")
    if (category == "None"):
        response = HttpResponse("empty category", content_type='text/plain')
        response.status_code = 400
        return response
    query_set = get_query_set(request.GET["category"] )
    if ( query_set == None):
        response = HttpResponse("category doesn't exist", content_type='text/plain')
        response.status_code = 400
        return response


    from_index = request.GET.get("from" , 0)
    to_index = request.GET.get("to" , 100)

    from_index = int(from_index)
    to_index = int(to_index)

    is_not_student_or_summary = (category != "students" and category != "summary")

    if (is_not_student_or_summary):
        query_set_data = query_set[:]
    else:
        query_set_data = query_set[from_index:to_index]

    data = serializers.serialize('json', query_set_data)

    return HttpResponse(data)




