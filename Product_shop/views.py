import itertools
from Product_shop.forms import paginatorss
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from Product_shop.models import product_shop, collect_product, product_gallery
from django.views.generic import ListView,DetailView
# Create your views here.
# from tag_shop.models import tag_product
from collect_product.models import collect_product_type,collect_product,collect_product_main
from shopping_cart.forms import order_form
from favorite_prducts.forms import favorite_form
from django.core.paginator import Paginator
from ditails_product.models import color,size
from tag_shop.models import tag_product
from comment_product.forms import commentform
from comment_product.models import comment


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def list_view_women(request):


    order_filter_number_them = ''

    object_list=product_shop.objects.filter(product_Gender="women",product_active=True)
    collect_type = collect_product_type.objects.filter(product_shop__product_Gender__iexact='women')
    colors=color.objects.filter(product_shop__product_Gender__iexact='women')
    sugest=product_shop.objects.filter(product_Gender='women').order_by('-product_date').all()[:3]






    form=paginatorss(request.POST or None)
    if form.is_valid():
        page1=form.cleaned_data.get('page')
        order_filter_number_them =form.cleaned_data.get('filter_pro')
         # Show 25 contacts per page.
    else:
        page1 = 6
    paginator = Paginator(object_list, page1)


    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context= {'form':form, 'page_obj': page_obj,"collect_type":collect_type,'colors':colors,'sugest':sugest,'order_filter_number':order_filter_number_them}

    return render(request, 'products/List_view/List_view_women.html',context)

def list_view_men(request):
    order_filter_number_them = ''

    object_list=product_shop.objects.filter(product_Gender="men",product_active=True)
    collect_type = collect_product_type.objects.filter(product_shop__product_Gender__iexact='men')
    colors = color.objects.filter(product_shop__product_Gender__iexact='men')
    sugest=product_shop.objects.filter(product_Gender='men').order_by('-product_date').all()[:3]

    form = paginatorss(request.POST or None)
    if form.is_valid():
        page1 = form.cleaned_data.get('page')
        order_filter_number_them = form.cleaned_data.get('filter_pro')
        # Show 25 contacts per page.
    else:
        page1 = 6
    paginator = Paginator(object_list, page1)


    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context= {'form':form, 'page_obj': page_obj,"collect_type":collect_type,'colors':colors,'sugest':sugest,'order_filter_number':order_filter_number_them}

    return render(request, 'products/List_view/List_view_men.html',context)

def list_view_kids(request):
    order_filter_number_them = ''

    object_list=product_shop.objects.filter(product_Gender="kids",product_active=True)
    collect_type = collect_product_type.objects.filter(product_shop__product_Gender__iexact='kids')
    colors = color.objects.filter(product_shop__product_Gender__iexact='kids')
    sugest=product_shop.objects.filter(product_Gender='kids').order_by('-product_date').all()[:3]

    form = paginatorss(request.POST or None)
    if form.is_valid():
        page1 = form.cleaned_data.get('page')
        order_filter_number_them = form.cleaned_data.get('filter_pro')
        # Show 25 contacts per page.
    else:
        page1 = 6
    paginator = Paginator(object_list, page1)


    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context= {'form':form, 'page_obj': page_obj,"collect_type":collect_type,'colors':colors,'sugest':sugest,'order_filter_number':order_filter_number_them}

    return render(request, 'products/List_view/List_view_kids.html',context)


def product_detail(request, *args, **kwargs):



    selected_product_id = kwargs['productId']
    order_forms=order_form(request.POST or None,initial={'product_id':selected_product_id})
    favorite_forms=favorite_form(request.POST or None,initial={'product_id':selected_product_id})



    order_forms_comment=commentform(request.POST or None,initial={'id_comment':selected_product_id})


    product = product_shop.objects.get_by_id(selected_product_id)

    if product is None or not product.product_active:
        raise Http404('محصول مورد نظر یافت نشد')

    sugest=product_shop.objects.get_queryset().filter(collect__product_shop=product).distinct().order_by('product_date')
    grouped_galleries_sugest = list(my_grouper(4, sugest))


    tag=tag_product.objects.get_queryset().filter(product_shop=selected_product_id)
    colors=color.objects.get_queryset().filter(product_shop=selected_product_id)
    sizes=size.objects.get_queryset().filter(product_shop=selected_product_id)


    galleries = product_gallery.objects.filter(product_id=selected_product_id)
    comment_massage=comment.objects.filter(product_id=selected_product_id)
    len_massage=len(comment_massage)


    grouped_galleries = list(my_grouper(3, galleries))

    if request.user.is_authenticated:
        product.product_visit +=1
        product.save()


    context = {
        'object': product,
        'grouped_gallery': grouped_galleries,
        'sugest':grouped_galleries_sugest,
        'tag':tag,
        'basket':order_forms,
        'favorite':favorite_forms,
        'comment_form':order_forms_comment,
        'color':colors,
        'size':sizes,
        'comment_massage':comment_massage,
        'len_massage':len_massage,

    }

    return render(request, 'products/Detail_view.html', context)

class search(ListView):
    paginate_by = 6
    template_name = 'products/List_view/List_view_women.html'

    def get_queryset(self):

        request=self.request
        query=request.GET.get('q')
        if query is not None:
            return product_shop.objects.search(query)

        return product_shop.objects.get_product_active()


def product_collect_men(request,**kwargs):

    collect_main=collect_product_main.objects.filter(product_shop__product_Gender__iexact='men').distinct()
    collect=collect_product.objects.filter(product_shop__product_Gender__iexact='men').distinct()

    contex={"collect":collect,'collect_main':collect_main}

    return render(request, 'products/collect/collect_partial_men.html', contex)

def product_collect_women(request,**kwargs):
    collect_type=collect_product_type.objects.filter(product_shop__product_Gender__iexact='women').distinct()
    collect_main = collect_product_main.objects.filter(product_shop__product_Gender__iexact='women').distinct()
    collect = collect_product.objects.filter(product_shop__product_Gender__iexact='women').distinct()

    contex = {"collect": collect, 'collect_main': collect_main}

    return render(request, 'products/collect/collect_partial_women.html', contex)

def product_collect_kids(request,**kwargs):
    collect_type = collect_product_type.objects.filter(product_shop__product_Gender__iexact='kids').distinct()
    collect_main = collect_product_main.objects.filter(product_shop__product_Gender__iexact='kids').distinct()
    collect = collect_product.objects.filter(product_shop__product_Gender__iexact='kids').distinct()

    contex = {"collect": collect, 'collect_type': collect_type, 'collect_main': collect_main}

    return render(request, 'products/collect/collect_partial_kids.html', contex)



class collect_product_types_men(ListView):
    paginate_by = 6

    template_name = 'products/List_view/List_view_women.html'

    def get_queryset(self):
        collect_name = self.kwargs["category_name_type"]

        category = collect_product_type.objects.filter(name_collect_product_type__iexact=collect_name,product_shop__product_Gender__iexact='men')
        if category is None:
            raise Http404("صفحه مورد نظر یافت نشد")

        return product_shop.objects.get_product_category_type(collect_name,gender='men')


class collect_product_types_women(ListView):
    paginate_by = 6

    template_name = 'products/List_view/List_view_women.html'

    def get_queryset(self):
        collect_name = self.kwargs["category_name_type"]

        category = collect_product_type.objects.filter(name_collect_product_type__iexact=collect_name,product_shop__product_Gender__iexact='women')
        if category is None:
            raise Http404("صفحه مورد نظر یافت نشد")

        return product_shop.objects.get_product_category_type(collect_name,gender='women')


class collect_product_types_kids(ListView):
        paginate_by = 6

        template_name = 'products/List_view/List_view_kids.html'

        def get_queryset(self):
            collect_name = self.kwargs["category_name_type"]

            category = collect_product_type.objects.filter(name_collect_product_type__iexact=collect_name,
                                                           product_shop__product_Gender__iexact='kids')
            if category is None:
                raise Http404("صفحه مورد نظر یافت نشد")

            return product_shop.objects.get_product_category_type(collect_name,gender='kids')


class collect_product_main_men(ListView):
    paginate_by = 6

    template_name = 'products/List_view/List_view_men.html'

    def get_queryset(self):
        collect_name = self.kwargs["category_name_type"]
        category=collect_product_main.objects.filter(name_collect_product_main__iexact=collect_name,product_shop__product_Gender__iexact='men').distinct()
        if category is None:
            raise Http404("صفحه مورد نظر یافت نشد")
        return product_shop.objects.get_product_category_main(collect_name,gender='men')


class collect_product_main_women(ListView):
    paginate_by = 6

    template_name = 'products/List_view/List_view_women.html'

    def get_queryset(self):
        collect_name = self.kwargs["category_name_type"]
        category = collect_product_main.objects.filter(name_collect_product_main__iexact=collect_name,
                                                       product_shop__product_Gender__iexact='women')
        if category is None:
            raise Http404("صفحه مورد نظر یافت نشد")

        return product_shop.objects.get_product_category_main(collect_name,gender='women')

class collect_product_main_kids(ListView):
    paginate_by = 6

    template_name = 'products/List_view/List_view_kids.html'

    def get_queryset(self):
        collect_name = self.kwargs["category_name_type"]
        category = collect_product_main.objects.filter(name_collect_product_main__iexact=collect_name,
                                                       product_shop__product_Gender__iexact='kids')
        if category is None:
            raise Http404("صفحه مورد نظر یافت نشد")

        return product_shop.objects.get_product_category_main(collect_name,gender='kids')


class collect_product_men(ListView):

    paginate_by = 6

    template_name = 'products/List_view/List_view_men.html'

    def get_queryset(self):
        collect_name = self.kwargs["category_name_type"]

        category = collect_product.objects.filter(name_collect_product__iexact=collect_name,product_shop__product_Gender__iexact='men')
        if category is None:
            raise Http404("صفحه مورد نظر یافت نشد")

        return product_shop.objects.get_product_category(collect_name,gender='men')


class collect_product_women(ListView):
    paginate_by = 6

    template_name = 'products/List_view/List_view_women.html'

    def get_queryset(self):
        collect_name = self.kwargs["category_name_type"]

        category = collect_product.objects.filter(name_collect_product__iexact=collect_name,product_shop__product_Gender__iexact='women')
        if category is None:
            raise Http404("صفحه مورد نظر یافت نشد")

        return product_shop.objects.get_product_category(collect_name,gender='women')

class collect_product_kids(ListView):
    paginate_by = 6

    template_name = 'products/List_view/List_view_kids.html'

    def get_queryset(self):
        collect_name = self.kwargs["category_name_type"]

        category = collect_product.objects.filter(name_collect_product__iexact=collect_name,product_shop__product_Gender__iexact='kids')
        if category is None:
            raise Http404("صفحه مورد نظر یافت نشد")

        return product_shop.objects.get_product_category(collect_name,gender='kids')

def filter_women(request):

    collect_type = collect_product_type.objects.filter(product_shop__product_Gender__iexact='women')
    product_shops = product_shop.objects.filter(product_Gender="women",product_active=True)

    contacx={"collect_type":collect_type,'product_filter':product_shops}

    return render(request,'products/List_view/List_view_women.html',contacx)


def filter_men(request):
    collect_type = collect_product_type.objects.filter(product_shop__product_Gender__iexact='men')
    product_shops = product_shop.objects.filter(product_Gender="men", product_active=True)
    price=product_shops.order_by('-price_discount').all()
    contacx = {"collect_type": collect_type, 'product_filter': product_shops,'price':price}

    return render(request, 'products/List_view/List_view_men.html', contacx)


def filter_kids(request):
    collect_type = collect_product_type.objects.filter(product_shop__product_Gender__iexact='kids')
    product_shops = product_shop.objects.filter(product_Gender="kids", product_active=True)

    contacx = {"collect_type": collect_type, 'product_filter': product_shops}

    return render(request, 'products/List_view/List_view_kids.html', contacx)

