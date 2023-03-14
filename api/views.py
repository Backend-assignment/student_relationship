from django.shortcuts import render
from .models import Student,Contact
from django.http import JsonResponse,HttpRequest

# Create view for Student
def get_student(request:HttpRequest)->JsonResponse:
    """
    Get all student
    """
    students = Student.objects.all()
    data = {
        'results':[]
    }
    for student in students:
        contact = student.contact # Get contact of student
        data['results'].append({
            'first_name':student.first_name,
            'last_name':student.last_name,
            'phone':contact.phone,
            'address':contact.address
           
        })

    return JsonResponse(data)

# Create view for Contact

def get_contact(request:HttpRequest)->JsonResponse:
    """
    Get all contact
    """
    contacts = Contact.objects.filter(address='Samarqand')
    data = {
        'results':[]
    }
    for contact in contacts:
        # student = contact.student # Get student of contact
        student= Student.objects.get(contact=contact)
        data['results'].append({
  
            'phone':contact.phone,
            'address':contact.address,
            'first_name':student.first_name,
            'last_name':student.last_name
           
        })

    return JsonResponse(data)
    


