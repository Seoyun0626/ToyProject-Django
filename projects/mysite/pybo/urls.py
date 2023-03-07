from django.urls import path

from .views import base_views, question_views, answer_views, comment_views, vote_views

app_name='pybo' # URL별칭에서 중복문제 해결을위한 네임스페이스 과정

urlpatterns = [
    path('', base_views.index,name='index'), # config/urls.py에서 pybo/에 대해 처리 -> 빈 문자열 넘기기, /pybo/ = index
    path('<int:question_id>/', base_views.detail, name='detail'), # question_id에 값 저장된 후 views.detail 함수 실행, /pybo/2/ = detail
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify,
         name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete,
         name='question_delete'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),
    path('comment/create/question/<int:question_id>/', comment_views.comment_create_question,
         name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/', comment_views.comment_modify_question,
         name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>/', comment_views.comment_delete_question,
         name='comment_delete_question'),
    path('comment/create/answer/<int:answer_id>/', comment_views.comment_create_answer,
         name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', comment_views.comment_modify_answer,
         name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', comment_views.comment_delete_answer,
         name='comment_delete_answer'),
    # vote_views.py
    path('vote/question/<int:question_id>/', vote_views.vote_question, name='vote_question'),
]