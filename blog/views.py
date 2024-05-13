from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse

import logging

from .models import Post

from django.http import Http404

# Pagination
from django.core.paginator import Paginator

from .form import ContactForm
# Create your views here.
# Static Demo data
# posts=[
#         {'id':1,'title':'Post 1','content':'Content of Post 1'},
#         {'id':2,'title':'Post 2','content':'Content of Post 2'},
#         {'id':3,'title':'Post 3','content':'Content of Post 3'},
#         {'id':4,'title':'Post 4','content':'Content of Post 4'},
#     ]


def index(request):
    blog_title="Latest Post"
    # getting static data
    all_posts=Post.objects.all()
    
    paginator=Paginator(all_posts,5)
    page_number=request.GET.get('page')
    page_object=paginator.get_page(page_number)
    return render(request,'blog/index.html',{'blog_title':blog_title,'page_obj':page_object})




def detail(request,slug):
    # getting static data
    # post=next((item for item in posts if item['id']==int(post_id)),None)
    
    
    
    # Handling error
    try:
        post=Post.objects.get(slug=slug)
        related_post=Post.objects.filter(category=post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404("Page Does Not Exits")
    
    # getting data from model by post id 
    # logger=logging.getLogger("TESTING")
    # logger.debug(f'Post variable is {post}')
    
    return render(request,'blog/detail.html',{'post':post,'related_posts':related_post})

def contact(request):
    return HttpResponse("Contact Page")

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_redirect(request):
    return HttpResponse("This is the new  url")


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        logger = logging.getLogger("TESTING")
        if form.is_valid():
            logger.debug(f'POST Data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}')
            #send email or save in database
            success_message = 'Your Email has been sent!'
            return render(request,'blog/contact.html', {'form':form,'success_message':success_message})
        else:
            logger.debug('Form validation failure')
        return render(request,'blog/contact.html', {'form':form, 'name': name, 'email':email, 'message': message})
    return render(request,'blog/contact.html')

def about_view(request):
    # about_content = AboutUs.objects.first().content
    return render(request,'blog/about.html')