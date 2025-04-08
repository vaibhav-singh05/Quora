from django.shortcuts import render, redirect, get_object_or_404
from core.models import Profile, Contact, Question, Answer, Like
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.
def index(request):
    query = request.GET.get('q')
    if query:
        questions = Question.objects.filter(
            Q(title__icontains=query) | Q(desc__icontains=query)
        ).order_by('-date')
    else:
        questions = Question.objects.all().order_by('-date')

    return render(request, 'index.html', {'questions': questions})


def about(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'about.html')


def contact(request):
    if request.user.is_anonymous:
        return redirect('/login')

    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        state = request.POST.get('state')
        contact = Contact(firstname=firstname, lastname=lastname, mobile=mobile, email=email, state=state, date=datetime.today())
        contact.save()
        messages.success(request, "Your details have been sent!")
    return render(request, 'contact.html')


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('/login')


def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            messages.warning(request, "Email already exists")
            return redirect('register')

        if Profile.objects.filter(mobile=mobile).exists():
            messages.warning(request, "Mobile number already exists")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        profile = Profile(user=user, mobile=mobile)
        profile.save()
        messages.success(request, "You have registered successfully")
    return render(request, 'register.html')


@login_required
def posting(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        question = Question(title=title, desc=desc, user=request.user, date=datetime.today())
        question.save()
        messages.success(request, "Successfully posted your question!")
    return render(request, 'posting.html')


@login_required
def like_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    existing_like = Like.objects.filter(user=request.user, answer=answer)
    
    if existing_like.exists():
        existing_like.delete()
    else:
        Like.objects.create(user=request.user, answer=answer)

    return redirect('question_detail', question_id=answer.question.id)


@login_required
def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = Answer.objects.filter(question=question).order_by('-created_at')
    return render(request, 'question_detail.html', {'question': question, 'answers': answers})

@login_required
def submit_answer(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            answer = Answer(content=content, user=request.user, question=question)
            answer.save()
            messages.success(request, "Answer submitted successfully!")
    
    return redirect('question_detail', question_id=question.id)


@login_required
def my_profile(request):
    try:
        user_profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        messages.error(request, "Profile not found.")
        return redirect('home')

    user_questions = Question.objects.filter(user=request.user)
    user_answers = Answer.objects.filter(user=request.user)

    return render(request, 'my_profile.html', {
        'user_profile': user_profile,
        'user_questions': user_questions,
        'user_answers': user_answers,
    })


@login_required
def update_profile(request):
    try:
        user_profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        messages.error(request, "Profile does not exist.")
        return redirect('my_profile')

    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        bio = request.POST.get('bio')

        if profile_pic:
            user_profile.profile_pic = profile_pic
        if bio:
            user_profile.bio = bio

        user_profile.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('my_profile')

    return render(request, 'update_profile.html', {'user_profile': user_profile})

