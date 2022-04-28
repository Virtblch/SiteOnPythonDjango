from django.http import Http404
from django.shortcuts import render
from django.core.paginator import Paginator
from linuxbash.models import Post, SubCategory, Category


# Формирование блока меню
def menu(url):
    menu = [];
    try:
        for categ in Category.objects.all():
            menu.append('<div class="category">' + categ.categHumanName + ':</div>')
            for subcateg in SubCategory.objects.filter(keyCateg=categ):
                # Ссылка на главную страницу есть в шапке сайта, в меню не нужна
                if subcateg.subCategName != 'main':
                    menu.append(
                        '<div class="subcategory"><a href=' + url + '/' + subcateg.subCategName + '>' + subcateg.subCategHumanName + '</a></div>')
        return menu
    except:
        raise Http404


# Формирование поста главной страницы сайта
# Пост главной страницы должен иметь подкатегорию "main"
def index_page(requests):
    try:
        # Для главной страницы только посты подкатегории 'main'
        sc = SubCategory.objects.filter(subCategName='main')
        # Абсолютный путь к главной странице сайта (для формирования ссылок меню)
        absurl = requests.scheme + '://' + requests.META['HTTP_HOST']
        # Передача данных(меню, статья) в html-шаблон (шаблоны в папке templates)
        return render(requests, 'post.html',
                      {'menus': menu(absurl), 'posts': Post.objects.filter(keyCateg=sc[0])})
    except:
        raise Http404


# Формирование списка постов на странице подкатегорий
# на основании передаваемой из urls.py подкатегории(subCateg),
# имеющейся в открываемой ссылке.
def category_page(requests, subCateg):
    try:
        # Фильтрация подкатегорий на основе url (в переменной subCateg часть url)
        sc = SubCategory.objects.filter(subCategName=subCateg)
        #.all - .get_queryset().order_by('id')
        # Посты подкатегории
        posts = Post.objects.get_queryset().order_by('id').filter(keyCateg=sc[0])
        # Пагинация с использованием класса django Paginator (разбивка по n-статей на страницу,
        # в templates/category.html перемещение по страницам: '<< previous page 2 of 3 next >>')
        # Число выводимых на страницу постов:
        paginator = Paginator(posts, 7)
        page_number = requests.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # Абсолютный путь к главной странице сайта (для формирования ссылок меню)
        absurl = requests.scheme + '://' + requests.META['HTTP_HOST']
        # Передача данных(меню, список статей) в html-шаблон (шаблоны в папке templates)
        return render(requests, 'category.html',
                      {'menus': menu(absurl), 'posts': page_obj})
    except:
        raise Http404


# Формирование поста.
# Пост определяется отбором по сохраненному в постах полю URL
# на основании передаваемой из urls.py ссылки.
# Пример: переход по ссылке /mtext/101-cuneiform.html
# из urls.py передается urlInt=101 и urlSlug=cuneiform,
# собирается "101-cuneiform", сравнивается с полем URL в постах.
def post_page(requests, subCateg, urlInt, urlSlug):
    try:
        # Фильтрация по полю url на основе собственно url
        # Пример: /mtext/101-cuneiform.html
        url = str(urlInt) + '-' + urlSlug
        # Абсолютный путь к главной странице сайта (для формирования ссылок меню)
        absurl = requests.scheme + '://' + requests.META['HTTP_HOST']
        # Передача данных(меню, статья) в html-шаблон (шаблоны в папке templates)
        return render(requests, 'post.html', {'menus': menu(absurl), 'posts': Post.objects.filter(url=url)})
    except:
        raise Http404
