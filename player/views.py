from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from player.models import *
from django.db.models import Q
from pprint import pprint
from django.http import Http404
import  operator
from functools import reduce


# Create your views here.

# top_player_names
# top_player_pictures
# top_teams

def index(request):
    try:
        res = {}
        res['top_players'] = Player.objects.all()[:5]
        res['top_teams'] = Team.objects.all()[:5]
        res['recent_matchs'] = Match.objects.all().order_by('-date')[:5]
        res['leagues']=League.objects.all()
        template = loader.get_template('player/index.html')
    except:
        raise Http404("Oops! Resource doesn't exist. If you believe this is a bug or error, contact\
         maijj6@mail2.sysu.edu.cn please.")
    return HttpResponse(template.render(res, request))


def player_detail(request, player_api_id):
    try:
        res = {}
        template = loader.get_template('player/player.html')
        res['info'] = Player.objects.filter(player_api_id=player_api_id)[0]
        res['detail_info'] = PlayerAttributes.objects.filter(player_api_id=player_api_id)[0]
    except:
        raise Http404("Oops! Resource doesn't exist. If you believe this is a bug or error, contact\
         maijj6@mail2.sysu.edu.cn please.")

    return HttpResponse(template.render(res, request))


def match_detail(request, match_id):
    try:
        res = {}
        template = loader.get_template('player/match.html')
        res['info'] = Match.objects.filter(id=match_id)[0]

        res['info'].home_team_api_id=Team.objects.filter(team_api_id=res['info'].home_team_api_id)[0]
        res['info'].away_team_api_id=Team.objects.filter(team_api_id=res['info'].away_team_api_id)[0]

        res['info'].home_player_1_id = Player.objects.filter(player_api_id=res['info'].home_player_1_id)[0]
        res['info'].home_player_2_id = Player.objects.filter(player_api_id=res['info'].home_player_2_id)[0]
        res['info'].home_player_3_id = Player.objects.filter(player_api_id=res['info'].home_player_3_id)[0]
        res['info'].home_player_4_id = Player.objects.filter(player_api_id=res['info'].home_player_4_id)[0]
        res['info'].home_player_5_id = Player.objects.filter(player_api_id=res['info'].home_player_5_id)[0]
        res['info'].home_player_6_id = Player.objects.filter(player_api_id=res['info'].home_player_6_id)[0]
        res['info'].home_player_7_id = Player.objects.filter(player_api_id=res['info'].home_player_7_id)[0]
        res['info'].home_player_8_id = Player.objects.filter(player_api_id=res['info'].home_player_8_id)[0]
        res['info'].home_player_9_id = Player.objects.filter(player_api_id=res['info'].home_player_9_id)[0]
        res['info'].home_player_10_id = Player.objects.filter(player_api_id=res['info'].home_player_10_id)[0]
        res['info'].home_player_11_id = Player.objects.filter(player_api_id=res['info'].home_player_11_id)[0]

        res['info'].away_player_1_id = Player.objects.filter(player_api_id=res['info'].away_player_1_id)[0]
        res['info'].away_player_2_id = Player.objects.filter(player_api_id=res['info'].away_player_2_id)[0]
        res['info'].away_player_3_id = Player.objects.filter(player_api_id=res['info'].away_player_3_id)[0]
        res['info'].away_player_4_id = Player.objects.filter(player_api_id=res['info'].away_player_4_id)[0]
        res['info'].away_player_5_id = Player.objects.filter(player_api_id=res['info'].away_player_5_id)[0]
        res['info'].away_player_6_id = Player.objects.filter(player_api_id=res['info'].away_player_6_id)[0]
        res['info'].away_player_7_id = Player.objects.filter(player_api_id=res['info'].away_player_7_id)[0]
        res['info'].away_player_8_id = Player.objects.filter(player_api_id=res['info'].away_player_8_id)[0]
        res['info'].away_player_9_id = Player.objects.filter(player_api_id=res['info'].away_player_9_id)[0]
        res['info'].away_player_10_id = Player.objects.filter(player_api_id=res['info'].away_player_10_id)[0]
        res['info'].away_player_11_id = Player.objects.filter(player_api_id=res['info'].away_player_11_id)[0]

    except:
        raise Http404("Oops! Resource doesn't exist. If you believe this is a bug or error, contact\
         maijj6@mail2.sysu.edu.cn please.")

    return HttpResponse(template.render(res, request))


def team_detail(request, team_api_id):
    res = {}
    template = loader.get_template('player/team.html')
    try:
        res['info'] = Team.objects.filter(team_api_id=team_api_id)[0]
        res['detail_info'] = TeamAttributes.objects.filter(team_api_id=team_api_id)[0]
        res['recent_matchs'] = Match.objects.filter(
            Q(home_team_api=team_api_id) | Q(away_team_api=team_api_id)).order_by('-date')[:5]
        for match in res['recent_matchs']:
            match.date=match.date[:-9]
    except:
        raise Http404("Oops! Resource doesn't exist. If you believe this is a bug or error, contact\
         maijj6@mail2.sysu.edu.cn please.")

    return HttpResponse(template.render(res, request))

def league_detail(request,league_id):
    res = {}
    template = loader.get_template('player/league.html')
    try:
        res['all_matchs'] = Match.objects.filter(league=league_id).order_by('-date')
        for match in res['all_matchs']:
            match.date=match.date[:-9]
    except:
        raise Http404("Oops! Resource doesn't exist. If you believe this is a bug or error, contact\
         maijj6@mail2.sysu.edu.cn please.")

    return HttpResponse(template.render(res, request))


# Handle search
def player_search(request):
    #result = table.objects.filter(string__contains='pattern')
    try:
        res={}
        template=loader.get_template('player/player_result.html')
        search_term=request.POST.get('player_input').split()
        if search_term:
            res['cache']=search_term
            print(Player.objects.filter(player_name__contains='messi'))
            res['result']=Player.objects.filter(reduce(operator.or_,(Q(player_name__icontains=x) for x in search_term)))
            if res['result'].count()>=100:
                res['error']="Warning : Too many results ! Show only the first 100 results ! Use more precise keywords."
                res['result']=res['result'][:100]
            elif not res['result']:
                res['error']='Nothing to show here.'
        else:
            res['error']="Please input some thing. Nothing to show here."

        return HttpResponse(template.render(res,request))
    except:
        raise Http404("Oops! Resource doesn't exist. If you believe this is a bug or error, contact\
         maijj6@mail2.sysu.edu.cn please.")


def team_search(request):
    try:
        res={}
        template=loader.get_template('player/team_result.html')
        search_term=request.POST.get('team_input').split()
        if search_term:
            res['cache']=search_term
            res['result']=Team.objects.filter(reduce(operator.and_,(Q(team_long_name__icontains=x) for x in search_term)))
            if res['result'].count()>=100:
                res['error']="Warning : Too many results ! Show only the first 100 results ! Use more precise keywords."
                res['result']=res['result'][:100]
            elif not res['result']:
                res['error']='Nothing to show here.'
        else:
            res['error']="Please input some thing. Nothing to show here."
        return HttpResponse(template.render(res,request))
    except:
        raise Http404("Oops! Resource doesn't exist. If you believe this is a bug or error, contact\
         maijj6@mail2.sysu.edu.cn please.")



