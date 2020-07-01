import random
from datetime import datetime
from django.shortcuts import render, redirect

def index(request):

    if not "gold" in request.session or "act" not in request.session:
        
        request.session['gold'] = 0
        request.session['act'] = []
    
    return render(request,"gold.html")

def reset(request):
    request.session.flush()
    return redirect('/')

GOLD_MAP = {
    "farm": (10,20),
    "cave": (5,10),
    "house": (2,5),
    "casino": (0,50)
    }
def process(request):
    if request.method == 'GET':
        return redirect('/')
    
    place = request.POST['place']
    place_now = GOLD_MAP[place]
    gold = random.randint(place_now[0],place_now[1])
    datime = datetime.now().strftime("%I:%M%p")
    message = f"You won {gold} from the {place}! at {datime}"
    request.session['gold'] += gold
    action = "win"

    if place == 'casino':
        if random.randint(0,1)>0:
            gold = gold * -1
            message = f"You went to the {place} and lost {gold} gold! at {datime}"
            action = "lose"
    
    request.session['act'].append({"message": message, "action": action})
    
    return redirect('/')