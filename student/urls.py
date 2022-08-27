from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('student/',views.student,name='student'),
    path('studentlogin/',views.studentlogin,name='studentlogin'),
    path('applyleave/',views.applyleave,name='applyleave'),
    path('teacherlogin/',views.teacherlogin,name='teacherlogin'),
    path('parentlogin/',views.parentlogin,name='parentlogin'),
    path('parentreg/',views.parentreg,name='parentreg'),
    path('addevent/',views.addevent,name='addevent'),
    path('studlog/',views.studlog,name='studlog'),
    path('studhome/',views.studhome,name='studhome'),
    path('parlog/',views.parlog,name='parlog'),
    path('parenthome/',views.parenthome,name='parenthome'),
    path('parentview/',views.parentview,name='parentview'),
    path('teachhome/',views.teachhome,name='teachhome'),
    path('teachlog/',views.teachlog,name='teachlog'),
    path('viewevent/',views.viewevent,name='viewevent'),
    path('viewleave/',views.viewleave,name='viewleave'),
    path('approvleave/<int:id>',views.approvleave,name='approvleave'),
    path('delete/<int:id>',views.delete,name="delete"),
    path('approvedleave/',views.approvedleave,name='approvedleave'),
    path('viewstudent/',views.viewstudent,name='viewstudent'),
    path('detailleave/',views.detailleave,name='detailleave'),
    path('logoutuser/',views.logoutuser,name='logoutuser'),
    path('sapprovedleave/',views.sapprovedleave,name='sapprovedleave'),

]
