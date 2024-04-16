from django.shortcuts import render

posts = [
    {
    'author':'Masba Uddin ',
    'Title':'Blog Post 1',
    'content':'First post content',
    },
     {
    'author':'Uddin ',
    'Title':'Blog Post 1',
    'content':'First post content',
    }
]



def home(request):
    context = {
        'posts': posts
    }
    return render(request,'blog/home.html',context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})


