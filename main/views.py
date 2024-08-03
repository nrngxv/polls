from django.shortcuts import render
from .forms import CreatePollForm
from .models import Poll
from django.shortcuts import redirect
from django.http import HttpResponse

def create(request):
    if request.method == "POST":
        form = CreatePollForm(request.POST)
        if form.is_valid(): # this checks for the POST
            # print(form.cleaned_data['question']) to check if POST is working and is valid
            form.save() #saves the question and options to the database
            return redirect("home") #then load home page
    else:
        form = CreatePollForm()

    context = {'form' : form }
    return render(request, "main/create.html", context)

def home(request):
    polls = Poll.objects.all() #fetches all the polls data
    context = {'polls' : polls}
    return render(request, "main/home.html", context)

def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id) #requestion objects with the respective poll id
    
    if request.method == "POST":
       selected_option = request.POST['poll']
       if selected_option == "option1":
           poll.option_one_count += 1
       elif selected_option == "option2":
           poll.option_two_count += 1
       elif selected_option == "option3":
           poll.option_three_count += 1
       else:
           return HttpResponse(400, "Invalid")
       
       poll.save()

       return redirect("results", poll.id) #saving the poll request and returing the home page
    context = {
        'poll': poll
    }
    return render(request, "main/vote.html", context)

#fetching result of the specifc poll id
def results(request, poll_id):
    poll = Poll.objects.get(pk = poll_id)
    context = {
        "poll" : poll
    }
    return render(request, "main/results.html", context)