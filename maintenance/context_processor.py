from .models import Category, SubCategory, LandScape1


def nav_bar(request):
    try:
        category = Category.objects.filter(is_screen=False)
        return {'category': category}

    except Category.DoesNotExist:
        return {}


def sub_nav_bar(request):
    try:
        sub_cat = SubCategory.objects.all()
        sub_cat_count = sub_cat.count()
        return {'sub_cat': sub_cat, 'sub_cat_count': sub_cat_count}

    except SubCategory.DoesNotExist:
        return {}


def landscape(request):
    try:
        landscape1 = LandScape1.objects.get(id=1)

        return {'lanscape1': landscape1}
    except LandScape1.DoesNotExist:
        return {}
