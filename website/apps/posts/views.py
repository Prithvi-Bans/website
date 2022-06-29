from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

# Create your views here.

def PostLikeView(request, pk):
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	post.likes.add(request.user)
	return HttpResponseRedirect(reverse('postview'))

class PostListView(ListView):
	model = Post
	template_name = 'posts/postview.html'

	# def get_context_data(self, *args, **kwargs):
	# 	context = super().get_context_data()
	# 	totallikes = Post.totallikes(self)
	# 	context['totallikes'] = totallikes
	# 	return context 

class PostUserView(ListView):
	model = Post
	template_name = 'posts/postuserview.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		current_user = self.request.user
		context = Post.objects.filter(author = current_user)
		context = {'context':context}
		return context
		

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	form_class = PostForm
	# fields = ['post_title', 'post_text', 'post_image']
	success_url = '/post'
	
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(UpdateView):
	model = Post
	form_class = PostForm
	template_name = 'posts/postupdate.html'
	success_url = '/post'
	#fields = ['post_title', 'post_text', 'post_image']

class PostDeleteView(DeleteView):
	model = Post
	template_name = 'posts/postdelete.html'
	success_url = '/home/dashboard'