from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required
from .models import Book, IssuedItem, Author
from django.db.models import Q
from datetime import date
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect





def home(request):
    return render(request,'home.html')


def register(request):
    if(request.method == 'POST'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if(password1 == password2):
            if(User.objects.filter(username=username).exists()):
                messages.info(request,'Username already exist')
                return redirect('register')
            elif(User.objects.filter(email=email).exists()):
                messages.info(request,'Email already registered')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password not matches')
            return redirect('register')
    else:
        return render(request,'register.html')
    

def login(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if(user is not None):
            auth.login(request,user)
            return redirect('home')
       
        else:
            messages.info(request,'Invalid Credential')
            return redirect('login')

    else:
        return render(request,'login.html')
    
# @login_required(login_url='login')
# def issue(request):
#     if(request.method == 'POST'):
#         book_id = request.POST['book_id']
#         current_book = Book.objects.get(id=book_id)
#         book = Book.objects.filter(id=book_id)
#         issue_item = IssuedItem.objects.create(user_id=request.user,book_id=current_book)
#         issue_item.save()
#         # book.update(quantity = book[0].quantity-1)
#         messages.success(request, 'Book issued successfully.')
#     my_items = IssuedItem.objects.filter(user_id = request.user,return_date__isnull=True).values_list('book_id')
#     books = Book.objects.exclude(id__in=my_items)
#
#     return render(request,'issue_item.html',{'books':books})
#
# def search_book(request):
#     data = Book.objects.all()
#     if request.method == 'POST':
#         search = request.POST['query']
#         if search != None:
#             search_data = Book.objects.filter(book_name__icontains=search)
#         context = {
#             'data': search_data
#         }
#         return render(request, 'issue_item.html', context)
#     return render(request, 'issue_item.html',{'book':data})

@login_required(login_url='login')
def issue(request):
    data = Book.objects.all()
    books = None
    search_data = None

    if request.method == 'POST':
        book_id = request.POST['book_id']
        current_book = Book.objects.get(id=book_id)
        issue_item = IssuedItem.objects.create(user_id=request.user, book_id=current_book)
        issue_item.save()
        messages.success(request, 'Book issued successfully.')

    if request.method == 'GET':
        search = request.GET.get('query')
        if search:
            search_data = Book.objects.filter(book_name__icontains=search)
            # search_data = Book.objects.filter(
            #     Q(book_name__icontains=search) | Q(author_name__icontains=search)
            # )
        else:
            my_items = IssuedItem.objects.filter(user_id=request.user, return_date__isnull=True).values_list('book_id')
            books = Book.objects.exclude(id__in=my_items)

    return render(request, 'issue_item.html', {'books': books, 'data': search_data})



@login_required(login_url='login')
def return_item(request):
    if(request.method == 'POST'):
        book_id = request.POST['book_id']
        current_book = Book.objects.get(id=book_id)
        book = Book.objects.filter(id=book_id)
        
        issue_item = IssuedItem.objects.filter(user_id=request.user,book_id=current_book,return_date__isnull=True)
        issue_item.update(return_date=date.today())
        messages.success(request, 'Book returned successfully.')

    my_items = IssuedItem.objects.filter(user_id = request.user,return_date__isnull=True).values_list('book_id')
    
    books = Book.objects.exclude(~Q(id__in=my_items))
    params = {'books':books}
    return render(request,'return_item.html',params)


@login_required(login_url='login')
def history(request):
    my_items = IssuedItem.objects.filter(user_id=request.user).order_by('-issue_date')
    paginator = Paginator(my_items,10) 
    page_number = request.GET.get('page')
    show_data_final = paginator.get_page(page_number)
    return render(request,'history.html',{'books':show_data_final})


def logout(request):
    auth.logout(request)
    return redirect('/')




def librarian(request):
    data = Book.objects.all()
    return render(request,'librarian.html',  {'books': data})



def addbookview(request):

    return render(request, 'addbook.html')


def addbook(request):
    if request.method == 'POST':
        b = request.POST['Book_Name']
        a = request.POST['Author_Name']
        s = request.POST['Subject']
        print(b, a, s)
        book = Book()

        book.book_name = b
        book.author_name = a
        book.subject = s
        book.save()
        return HttpResponseRedirect('librarian')


def editbook(request):
    if request.method == 'POST':
        b = request.POST['Book_Name']
        a = request.POST['Author_Name']
        s = request.POST['Subject']

        book = Book.objects.get(id=request.POST['bookid'])

        book.book_name = b
        book.author_name = a
        book.subject = s
        book.save()
        return HttpResponseRedirect('librarian')


def editbookview(request):
    book = Book.objects.get(id=request.GET['bookid'])
    return render(request, 'editbook.html', {'book': book})



def deletebookview(request):
    book = Book.objects.get(id=request.GET['bookid'])
    book.delete()
    return HttpResponseRedirect('librarian')
   

