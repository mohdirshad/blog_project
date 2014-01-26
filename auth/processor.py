import time
from calendar import month_name

from auth.models import UserProfile
from blog.models import Post



def current_user(req): 
    try:
        if req.user.is_superuser:
            superUP=UserProfile()
            superUP.user=req.user
            superUP.image=None
            return {'UP':superUP, 'page': str(req.get_full_path()).strip()}
        else:
            return {'UP':UserProfile.objects.get(user=req.user),
                    'page': str(req.get_full_path()).strip()}
    except:
        return {'page': str(req.get_full_path()).strip()}


def mkmonth_lst(req):
    """ Make a list of months to show archive links"""
    months = []
    all = Post.objects.filter().dates('pub_date','month',order='DESC')[:6]
    for e in all:
        months.append([month_name[e.month], e.year])
    return {'months':months}







