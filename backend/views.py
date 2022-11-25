_AG='site name updated'
_AF='is_external'
_AE='is_visibled'
_AD='order_menu'
_AC='file_path_doc'
_AB='phone'
_AA='email'
_A9='designation'
_A8='location'
_A7='one_record_only'
_A6='notes'
_A5='address'
_A4='Link'
_A3='Name (en)'
_A2='Name (id)'
_A1='document'
_A0='related_link'
_z='video_gallery'
_y='photo_gallery'
_x='social_media'
_w='alert'
_v='daily_alert'
_u='form not valid '
_t='slide_show'
_s='agency'
_r='pages'
_q='greeting'
_p='events'
_o='article'
_n='news'
_m='Content (en)'
_l='Content (id)'
_k='announcement'
_j='logo'
_i='menu'
_h='Jumlah Foto'
_g='Title (en)'
_f='Title (id)'
_e='Foto'
_d='file_path'
_c='link'
_b='categories'
_a='language'
_Z='Update'
_Y='tags'
_X='delete'
_W='form_edit'
_V='save_edit'
_U='update.html'
_T='form_add'
_S='save_add'
_R='create.html'
_Q='Action'
_P='updated_at'
_O='uuid'
_N='photo'
_M='icon'
_L='status'
_K='str_file_path'
_J='content'
_I='en'
_H='POST'
_G='form'
_F='name'
_E='title'
_D='active_page'
_C=None
_B=False
_A='id'
from core.common import get_agency_info
from django.contrib import messages
from django.db.models import F,OuterRef,Subquery,Count
from django.http import JsonResponse
from django.shortcuts import get_object_or_404,redirect,render
from django.urls import reverse_lazy
from django.utils.text import Truncator
from django.views.generic import TemplateView
from django_outbox import msgbox
from django_outbox.common import get_natural_datetime,get_site_id,get_template
from education.models import *
from core.models import Photo,Agency,AgencyTranslation,Service
from parler.utils.context import switch_language
from parler.views import TranslatableCreateView,TranslatableUpdateView
from django.contrib.sites.models import Site
from parler.utils import get_active_language_choices
from parler.utils.conf import LanguagesSetting
from django.http import Http404
from menu.models import *
from menu.menus import Menus
from .forms import *
from core.forms import PhotoForm
mMsgBox=msgbox.ClsMsgBox()
def save_tags(tag_list,obj_master):
	i=0
	while i<len(tag_list):tag=Tags.objects.get(id=tag_list[i]);obj_master.tags.add(tag);i+=1
class IndexView(TemplateView):
	site_id=_C
	def get(self,request,*args,**kwargs):self.site_id=get_site_id(request);template=get_template(self.site_id,is_frontend=_B);print('template = ',template);self.template_name=template+'index.html';return super(IndexView,self).get(request,*(args),**kwargs)
	def get_context_data(self,*args,**kwargs):context=super(IndexView,self).get_context_data(*(args),**kwargs);context[_D]='dashboard';return context
class TagsView(TemplateView):
	site_id=_C
	def get(self,request,*args,**kwargs):self.site_id=get_site_id(request);template=get_template(self.site_id,is_frontend=_B);self.template_name=template+'tags.html';return super(TagsView,self).get(request,*(args),**kwargs)
	def get_context_data(self,*args,**kwargs):context=super(TagsView,self).get_context_data(*(args),**kwargs);context[_D]=_Y;return context
def tags_ajax(request):
	site_id=get_site_id(request);obj=Tags();obj.set_current_language(_I);subquery=Subquery(TagsTranslation.objects.filter(master_id=OuterRef(_A),language_code=_A).values(_F));lang=obj.get_current_language();obj2=Tags.objects.language(lang).filter(site_id=site_id).annotate(name_id=subquery);lst=[]
	for i in obj2:res={};res[_M]=_C;res[_O]=i.uuid;res[_P]=i.updated_at;res[_A2]=Truncator(i.name_id).chars(20);res[_A3]=Truncator(i.name).chars(20);res[_Z]=get_natural_datetime(i.updated_at);res[_Q]=_C;lst.append(res)
	return JsonResponse(lst,safe=_B)
def tags_create(request):
	context={};context[_D]=_Y;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_R
	if request.method==_H:
		form=TagsForm(request.POST)
		if form.is_valid():
			tmp=Tags.objects.filter(translations__name=request.POST.get(_F))
			if tmp:messages.info(request,mMsgBox.get('file_exists'));context[_G]=TagsForm()
			else:post=Tags.objects.language(_A).create(name=request.POST.get(_F));post.set_current_language(_I);post.name=request.POST.get(_F);post.save();messages.info(request,mMsgBox.get(_S,request.POST.get(_F)));return redirect(reverse_lazy(_Y))
	else:messages.info(request,mMsgBox.get(_T));context[_G]=TagsForm()
	return render(request,template,context)
def tags_update(request,uuid):
	context={};context[_D]=_Y;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_U;data=Tags.objects.filter(site_id=site_id,uuid=uuid);post=get_object_or_404(data)
	if request.method==_H:
		form=TagsForm(request.POST,instance=post)
		if form.is_valid():lang=request.POST.get(_a);obj=data.get();obj.set_current_language(lang);obj.name=request.POST.get(_F);obj.save();messages.info(request,mMsgBox.get(_V,request.POST.get(_F)));return redirect(reverse_lazy(_Y))
	else:messages.info(request,mMsgBox.get(_W));context[_G]=TagsForm(instance=post)
	return render(request,template,context)
def tags_delete(request,uuid):context={};site_id=get_site_id(request);data=Tags.objects.filter(site_id=site_id,uuid=uuid);post=get_object_or_404(data);tmp=post.name;post.delete();messages.info(request,mMsgBox.get(_X,tmp));return redirect(reverse_lazy(_Y))
class LogoView(TemplateView):
	site_id=_C
	def get(self,request,*args,**kwargs):self.site_id=get_site_id(request);template=get_template(self.site_id,is_frontend=_B);self.template_name=template+'logo.html';return super(LogoView,self).get(request,*(args),**kwargs)
	def get_context_data(self,*args,**kwargs):context=super(LogoView,self).get_context_data(*(args),**kwargs);context[_A7]=True;context[_D]=_j;return context
def logo_ajax(request):
	site_id=get_site_id(request);subquery=Subquery(Photo.objects.filter(object_id=OuterRef(_A),content_type__model=_j).values(_d));obj2=Logo.objects.filter(site_id=site_id).distinct().annotate(file_path=subquery).annotate(jml=Count(subquery));lst=[]
	for i in obj2:res={};res[_M]=_C;res[_O]=i.uuid;res[_P]=i.updated_at;res['Name']=Truncator(i.name).chars(20);res[_h]=i.jml;res[_e]=i.file_path;res[_Z]=get_natural_datetime(i.updated_at);res[_Q]=_C;lst.append(res)
	return JsonResponse(lst,safe=_B)
def logo_create(request):
	context={};context[_D]=_j;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_R
	if request.method==_H:
		form=LogoForm(request.POST);photo=PhotoForm(request.POST)
		if form.is_valid():post=form.save();Photo.objects.create(content_object=post,file_path=request.POST.get(_K));messages.info(request,mMsgBox.get(_S,request.POST.get(_F)));return redirect(reverse_lazy(_j))
	else:messages.info(request,mMsgBox.get(_T));context[_G]=LogoForm();context[_N]=PhotoForm()
	return render(request,template,context)
def logo_update(request,uuid):
	context={};context[_D]=_j;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_U;data=Logo.objects.filter(site_id=site_id,uuid=uuid);post=get_object_or_404(data);post_photo=post.photo.all()
	if post_photo:post_photo=post_photo.get()
	if request.method==_H:
		form=LogoForm(request.POST,instance=post);photo=PhotoForm(request.POST,instance=post_photo)
		if form.is_valid():
			post=form.save()
			if photo.is_valid():
				if request.POST.get(_K):post.photo.clear();Photo.objects.create(content_object=post,file_path=request.POST.get(_K))
			messages.info(request,mMsgBox.get(_V,request.POST.get(_F)));return redirect(reverse_lazy(_j))
	else:messages.info(request,mMsgBox.get(_W));context[_G]=LogoForm(instance=post);context[_N]=PhotoForm(instance=post_photo)
	return render(request,template,context)
def logo_delete(request,uuid):context={};site_id=get_site_id(request);data=Logo.objects.filter(site_id=site_id,uuid=uuid);post=get_object_or_404(data);tmp=post.name;post.delete();messages.info(request,mMsgBox.get(_X,tmp));return redirect(reverse_lazy(_j))
class AnnouncementView(TemplateView):
	site_id=_C
	def get(self,request,*args,**kwargs):self.site_id=get_site_id(request);template=get_template(self.site_id,is_frontend=_B);self.template_name=template+'announcement.html';return super(AnnouncementView,self).get(request,*(args),**kwargs)
	def get_context_data(self,*args,**kwargs):context=super(AnnouncementView,self).get_context_data(*(args),**kwargs);context[_D]=_k;return context
def announcement_ajax(request):
	site_id=get_site_id(request);obj=Announcement();obj.set_current_language(_I);subquery1=Subquery(AnnouncementTranslation.objects.filter(master_id=OuterRef(_A),language_code=_A).values(_E));subquery2=Subquery(AnnouncementTranslation.objects.filter(master_id=OuterRef(_A),language_code=_A).values(_J));subquery_foto=Subquery(Photo.objects.filter(object_id=OuterRef(_A),content_type__model=_k).values(_d));lang=obj.get_current_language();obj2=Announcement.objects.language(lang).filter(site_id=site_id).annotate(title_id=subquery1).annotate(content_id=subquery2).annotate(file_path=subquery_foto).annotate(jml=Count(subquery_foto));lst=[]
	for i in obj2:res={};res[_M]=_C;res[_O]=i.uuid;res[_P]=i.updated_at;res[_f]=Truncator(i.title_id).chars(20);res[_g]=Truncator(i.title).chars(20);res[_l]=Truncator(i.content_id).chars(20);res[_m]=Truncator(i.content).chars(20);res[_h]=i.jml;res[_e]=i.file_path;res[_Z]=get_natural_datetime(i.updated_at);res[_Q]=_C;lst.append(res)
	return JsonResponse(lst,safe=_B)
def announcement_create(request):
	context={};context[_D]=_k;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_R
	if request.method==_H:
		form=AnnouncementForm(request.POST);photo=PhotoForm(request.POST)
		if form.is_valid():post=Announcement.objects.language(_A).create(title=request.POST.get(_E),content=request.POST.get(_J),categories_id=request.POST.get(_b),status=request.POST.get(_L));post.set_current_language(_I);post.title=request.POST.get(_E);post.content=request.POST.get(_J);post.save();save_tags(request.POST.getlist(_Y),post);Photo.objects.create(content_object=post,file_path=request.POST.get(_K));messages.info(request,mMsgBox.get(_S,request.POST.get(_E)));return redirect(reverse_lazy(_k))
	else:messages.info(request,mMsgBox.get(_T));context[_G]=AnnouncementForm();context[_N]=PhotoForm()
	return render(request,template,context)
def announcement_update(request,uuid):
	context={};context[_D]=_k;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_U;data=Announcement.objects.filter(site_id=site_id,uuid=uuid);post=get_object_or_404(data);post_photo=post.photo.all()
	if post_photo:post_photo=post_photo.get()
	if request.method==_H:
		form=AnnouncementForm(request.POST,instance=post);photo=PhotoForm(request.POST,instance=post_photo)
		if form.is_valid():
			lang=request.POST.get(_a);obj=data.get();obj.set_current_language(lang);obj.title=request.POST.get(_E);obj.content=request.POST.get(_J);obj.categories_id=request.POST.get(_b);obj.status=request.POST.get(_L);obj.save();obj.tags.clear();save_tags(request.POST.getlist(_Y),obj)
			if photo.is_valid():
				if request.POST.get(_K):post.photo.clear();Photo.objects.create(content_object=post,file_path=request.POST.get(_K))
			messages.info(request,mMsgBox.get(_V,request.POST.get(_E)));return redirect(reverse_lazy(_k))
	else:messages.info(request,mMsgBox.get(_W));context[_G]=AnnouncementForm(instance=post);context[_N]=PhotoForm(instance=post_photo)
	return render(request,template,context)
def announcement_delete(request,uuid):context={};site_id=get_site_id(request);data=Announcement.objects.filter(site_id=site_id,uuid=uuid);post=get_object_or_404(data);tmp=post.title;post.delete();messages.info(request,mMsgBox.get(_X,tmp));return redirect(reverse_lazy(_k))
class NewsView(TemplateView):
	site_id=_C
	def get(self,request,*args,**kwargs):self.site_id=get_site_id(request);template=get_template(self.site_id,is_frontend=_B);self.template_name=template+'news.html';return super(NewsView,self).get(request,*(args),**kwargs)
	def get_context_data(self,*args,**kwargs):context=super(NewsView,self).get_context_data(*(args),**kwargs);context[_D]=_n;return context
def news_ajax(request):
	site_id=get_site_id(request);obj=News();obj.set_current_language(_I);subquery1=Subquery(NewsTranslation.objects.filter(master_id=OuterRef(_A),language_code=_A).values(_E));subquery2=Subquery(NewsTranslation.objects.filter(master_id=OuterRef(_A),language_code=_A).values(_J));subquery_foto=Subquery(Photo.objects.filter(object_id=OuterRef(_A),content_type__model=_n).values(_d));lang=obj.get_current_language();obj2=News.objects.language(lang).filter(site_id=site_id).annotate(title_id=subquery1).annotate(content_id=subquery2).annotate(file_path=subquery_foto).annotate(jml=Count(subquery_foto));lst=[]
	for i in obj2:res={};res[_M]=_C;res[_O]=i.uuid;res[_P]=i.updated_at;res[_f]=Truncator(i.title_id).chars(20);res[_g]=Truncator(i.title).chars(20);res[_l]=Truncator(i.content_id).chars(20);res[_m]=Truncator(i.content).chars(20);res[_h]=i.jml;res[_e]=i.file_path;res[_Z]=get_natural_datetime(i.updated_at);res[_Q]=_C;lst.append(res)
	return JsonResponse(lst,safe=_B)
def news_create(request):
	context={};context[_D]=_n;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_R
	if request.method==_H:
		form=NewsForm(request.POST);photo=PhotoForm(request.POST)
		if form.is_valid():post=News.objects.language(_A).create(title=request.POST.get(_E),content=request.POST.get(_J),categories_id=request.POST.get(_b),status=request.POST.get(_L));post.set_current_language(_I);post.title=request.POST.get(_E);post.content=request.POST.get(_J);post.save();save_tags(request.POST.getlist(_Y),post);Photo.objects.create(content_object=post,file_path=request.POST.get(_K));messages.info(request,mMsgBox.get(_S,request.POST.get(_E)));return redirect(reverse_lazy(_n))
	else:messages.info(request,mMsgBox.get(_T));context[_G]=NewsForm();context[_N]=PhotoForm()
	return render(request,template,context)
def news_update(request,uuid):
	context={};context[_D]=_n;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_U;data=News.objects.filter(site_id=site_id,uuid=uuid);post=get_object_or_404(data);post_photo=post.photo.all()
	if post_photo:post_photo=post_photo.get()
	if request.method==_H:
		form=NewsForm(request.POST,instance=post);photo=PhotoForm(request.POST,instance=post_photo)
		if form.is_valid():
			lang=request.POST.get(_a);obj=data.get();obj.set_current_language(lang);obj.title=request.POST.get(_E);obj.content=request.POST.get(_J);obj.categories_id=request.POST.get(_b);obj.status=request.POST.get(_L);obj.save();obj.tags.clear();save_tags(request.POST.getlist(_Y),obj)
			if photo.is_valid():
				if request.POST.get(_K):post.photo.clear();Photo.objects.create(content_object=post,file_path=request.POST.get(_K))
			messages.info(request,mMsgBox.get(_V,request.POST.get(_E)));return redirect(reverse_lazy(_n))
	else:messages.info(request,mMsgBox.get(_W));context[_G]=NewsForm(instance=post);context[_N]=PhotoForm(instance=post_photo)
	return render(request,template,context)
def news_delete(request,uuid):context={};site_id=get_site_id(request);data=News.objects.filter(site_id=site_id,uuid=uuid);post=get_object_or_404(data);tmp=post.title;post.delete();messages.info(request,mMsgBox.get(_X,tmp));return redirect(reverse_lazy(_n))
class ArticleView(TemplateView):
	site_id=_C
	def get(self,request,*args,**kwargs):self.site_id=get_site_id(request);template=get_template(self.site_id,is_frontend=_B);self.template_name=template+'article.html';return super(ArticleView,self).get(request,*(args),**kwargs)
	def get_context_data(self,*args,**kwargs):context=super(ArticleView,self).get_context_data(*(args),**kwargs);context[_D]=_o;return context
def article_ajax(request):
	site_id=get_site_id(request);obj=Article();obj.set_current_language(_I);subquery1=Subquery(ArticleTranslation.objects.filter(master_id=OuterRef(_A),language_code=_A).values(_E));subquery2=Subquery(ArticleTranslation.objects.filter(master_id=OuterRef(_A),language_code=_A).values(_J));subquery_foto=Subquery(Photo.objects.filter(object_id=OuterRef(_A),content_type__model=_o).values(_d));lang=obj.get_current_language();obj2=Article.objects.language(lang).filter(site_id=site_id).annotate(title_id=subquery1).annotate(content_id=subquery2).annotate(file_path=subquery_foto).annotate(jml=Count(subquery_foto));lst=[]
	for i in obj2:res={};res[_M]=_C;res[_O]=i.uuid;res[_P]=i.updated_at;res[_f]=Truncator(i.title_id).chars(20);res[_g]=Truncator(i.title).chars(20);res[_l]=Truncator(i.content_id).chars(20);res[_m]=Truncator(i.content).chars(20);res[_h]=i.jml;res[_e]=i.file_path;res[_Z]=get_natural_datetime(i.updated_at);res[_Q]=_C;lst.append(res)
	return JsonResponse(lst,safe=_B)
def article_create(request):
	context={};context[_D]=_o;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_R
	if request.method==_H:
		form=ArticleForm(request.POST);photo=PhotoForm(request.POST)
		if form.is_valid():post=Article.objects.language(_A).create(title=request.POST.get(_E),content=request.POST.get(_J),categories_id=request.POST.get(_b),status=request.POST.get(_L));post.set_current_language(_I);post.title=request.POST.get(_E);post.content=request.POST.get(_J);post.save();save_tags(request.POST.getlist(_Y),post);Photo.objects.create(content_object=post,file_path=request.POST.get(_K));messages.info(request,mMsgBox.get(_S,request.POST.get(_E)));return redirect(reverse_lazy(_o))
	else:messages.info(request,mMsgBox.get(_T));context[_G]=ArticleForm();context[_N]=PhotoForm()
	return render(request,template,context)
def article_update(request,uuid):
	context={};context[_D]=_o;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_U;data=Article.objects.filter(site_id=site_id,uuid=uuid);post=get_object_or_404(data);post_photo=post.photo.all()
	if post_photo:post_photo=post_photo.get()
	if request.method==_H:
		form=ArticleForm(request.POST,instance=post);photo=PhotoForm(request.POST,instance=post_photo)
		if form.is_valid():
			lang=request.POST.get(_a);obj=data.get();obj.set_current_language(lang);obj.title=request.POST.get(_E);obj.content=request.POST.get(_J);obj.categories_id=request.POST.get(_b);obj.status=request.POST.get(_L);obj.save();obj.tags.clear();save_tags(request.POST.getlist(_Y),obj)
			if photo.is_valid():
				if request.POST.get(_K):post.photo.clear();Photo.objects.create(content_object=post,file_path=request.POST.get(_K))
			messages.info(request,mMsgBox.get(_V,request.POST.get(_E)));return redirect(reverse_lazy(_o))
	else:messages.info(request,mMsgBox.get(_W));context[_G]=ArticleForm(instance=post);context[_N]=PhotoForm(instance=post_photo)
	return render(request,template,context)
def article_delete(request,uuid):context={};site_id=get_site_id(request);data=Article.objects.filter(site_id=site_id,uuid=uuid);post=get_object_or_404(data);tmp=post.title;post.delete();messages.info(request,mMsgBox.get(_X,tmp));return redirect(reverse_lazy(_o))
class EventsView(TemplateView):
	site_id=_C
	def get(self,request,*args,**kwargs):self.site_id=get_site_id(request);template=get_template(self.site_id,is_frontend=_B);self.template_name=template+'events.html';return super(EventsView,self).get(request,*(args),**kwargs)
	def get_context_data(self,*args,**kwargs):context=super(EventsView,self).get_context_data(*(args),**kwargs);context[_D]=_p;return context
def events_ajax(request):
	site_id=get_site_id(request);obj=Events();obj.set_current_language(_I);subquery1=Subquery(EventsTranslation.objects.filter(master_id=OuterRef(_A),language_code=_A).values(_E));subquery2=Subquery(EventsTranslation.objects.filter(master_id=OuterRef(_A),language_code=_A).values(_J));subquery_foto=Subquery(Photo.objects.filter(object_id=OuterRef(_A),content_type__model=_p).values(_d));lang=obj.get_current_language();obj2=Events.objects.language(lang).filter(site_id=site_id).annotate(title_id=subquery1).annotate(content_id=subquery2).annotate(file_path=subquery_foto).annotate(jml=Count(subquery_foto));lst=[]
	for i in obj2:res={};res[_M]=_C;res[_O]=i.uuid;res[_P]=i.updated_at;res[_f]=Truncator(i.title_id).chars(20);res[_g]=Truncator(i.title).chars(20);res[_l]=Truncator(i.content_id).chars(20);res[_m]=Truncator(i.content).chars(20);res[_h]=i.jml;res[_e]=i.file_path;res[_Z]=get_natural_datetime(i.updated_at);res[_Q]=_C;lst.append(res)
	return JsonResponse(lst,safe=_B)
def events_create(request):
	context={};context[_D]=_p;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_R
	if request.method==_H:
		form=EventsForm(request.POST);photo=PhotoForm(request.POST)
		if form.is_valid():post=Events.objects.language(_A).create(title=request.POST.get(_E),content=request.POST.get(_J),location=request.POST.get(_A8),categories_id=request.POST.get(_b),status=request.POST.get(_L),date=request.POST.get('date'),time=request.POST.get('time'));post.set_current_language(_I);post.title=request.POST.get(_E);post.content=request.POST.get(_J);post.location=request.POST.get(_A8);post.save();save_tags(request.POST.getlist(_Y),post);Photo.objects.create(content_object=post,file_path=request.POST.get(_K));messages.info(request,mMsgBox.get(_S,request.POST.get(_E)));return redirect(reverse_lazy(_p))
	else:messages.info(request,mMsgBox.get(_T));context[_G]=EventsForm();context[_N]=PhotoForm()
	return render(request,template,context)
def events_update(request,uuid):
	context={};context[_D]=_p;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_U;data=Events.objects.filter(site_id=site_id,uuid=uuid);post=get_object_or_404(data);post_photo=post.photo.all()
	if post_photo:post_photo=post_photo.get()
	if request.method==_H:
		form=EventsForm(request.POST,instance=post);photo=PhotoForm(request.POST,instance=post_photo)
		if form.is_valid():
			lang=request.POST.get(_a);obj=data.get();obj.set_current_language(lang);obj.title=request.POST.get(_E);obj.content=request.POST.get(_J);obj.location=request.POST.get(_A8);obj.categories_id=request.POST.get(_b);obj.status=request.POST.get(_L);obj.date=request.POST.get('date');obj.time=request.POST.get('time');obj.save();obj.tags.clear();save_tags(request.POST.getlist(_Y),obj)
			if photo.is_valid():
				if request.POST.get(_K):post.photo.clear();Photo.objects.create(content_object=post,file_path=request.POST.get(_K))
			messages.info(request,mMsgBox.get(_V,request.POST.get(_E)));return redirect(reverse_lazy(_p))
	else:messages.info(request,mMsgBox.get(_W));context[_G]=EventsForm(instance=post);context[_N]=PhotoForm(instance=post_photo)
	return render(request,template,context)
def events_delete(request,uuid):context={};site_id=get_site_id(request);data=Events.objects.filter(site_id=site_id,uuid=uuid);post=get_object_or_404(data);tmp=post.title;post.delete();messages.info(request,mMsgBox.get(_X,tmp));return redirect(reverse_lazy(_p))
class SlideShowView(TemplateView):
	site_id=_C
	def get(self,request,*args,**kwargs):self.site_id=get_site_id(request);template=get_template(self.site_id,is_frontend=_B);self.template_name=template+'slide_show.html';return super(SlideShowView,self).get(request,*(args),**kwargs)
	def get_context_data(self,*args,**kwargs):context=super(SlideShowView,self).get_context_data(*(args),**kwargs);context[_D]=_t;return context
def slideshow_ajax(request):
	site_id=get_site_id(request);lst=[];obj=SlideShow();obj.set_current_language(_I);subquery1=Subquery(SlideShowTranslation.objects.filter(master_id=OuterRef(_A),language_code=_A).values(_E));subquery2=Subquery(SlideShowTranslation.objects.filter(master_id=OuterRef(_A),language_code=_A).values(_J));subquery_foto=Subquery(Photo.objects.filter(object_id=OuterRef(_A),content_type__model='slideshow').values(_d)[:1]);lang=obj.get_current_language();obj2=SlideShow.objects.language(lang).filter(site_id=site_id).distinct().annotate(title_id=subquery1).annotate(content_id=subquery2).annotate(file_path=subquery_foto)
	for i in obj2:res={};res[_M]=_C;res[_O]=i.uuid;res[_P]=i.updated_at;res[_f]=Truncator(i.title_id).chars(20);res[_g]=Truncator(i.title).chars(20);res[_l]=Truncator(i.content_id).chars(20);res[_m]=Truncator(i.content).chars(20);res[_e]=i.file_path;res[_Z]=get_natural_datetime(i.updated_at);res[_Q]=_C;lst.append(res)
	return JsonResponse(lst,safe=_B)
def slideshow_create(request):
	context={};context[_D]=_t;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_R
	if request.method==_H:
		form=SlideShowForm(request.POST);photo=PhotoForm(request.POST)
		if form.is_valid():post=SlideShow.objects.language(_A).create(title=request.POST.get(_E),content=request.POST.get(_J),link=request.POST.get(_c),status=request.POST.get(_L));post.set_current_language(_I);post.title=request.POST.get(_E);post.content=request.POST.get(_J);post.save();Photo.objects.create(content_object=post,file_path=request.POST.get(_K));messages.info(request,mMsgBox.get(_S,request.POST.get(_E)));return redirect(reverse_lazy(_t))
		else:print(_u);context[_G]=SlideShowForm();context[_N]=PhotoForm()
	else:messages.info(request,mMsgBox.get(_T));context[_G]=SlideShowForm();context[_N]=PhotoForm()
	return render(request,template,context)
def slideshow_update(request,uuid):
	context={};context[_D]=_t;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_U;data=SlideShow.objects.filter(site_id=site_id,uuid=uuid);post=get_object_or_404(data);post_photo=post.photo.first()
	if request.method==_H:
		form=SlideShowForm(request.POST,instance=post);photo=PhotoForm(request.POST,instance=post_photo)
		if form.is_valid():
			lang=request.POST.get(_a);obj=data.get();obj.set_current_language(lang);obj.title=request.POST.get(_E);obj.content=request.POST.get(_J);obj.link=request.POST.get(_c);obj.status=request.POST.get(_L);obj.save()
			if request.POST.get(_K):Photo.objects.create(content_object=obj,file_path=request.POST.get(_K))
			else:print('photo not valid')
			messages.info(request,mMsgBox.get(_V,request.POST.get(_E)));return redirect(reverse_lazy(_t))
	else:messages.info(request,mMsgBox.get(_W));context[_G]=SlideShowForm(instance=post);context[_N]=PhotoForm(instance=post_photo)
	return render(request,template,context)
def slideshow_delete(request,uuid):context={};site_id=get_site_id(request);data=SlideShow.objects.filter(site_id=site_id,uuid=uuid);post=get_object_or_404(data);tmp=post.title;post.delete();messages.info(request,mMsgBox.get(_X,tmp));return redirect(reverse_lazy(_t))
class DailyAlertView(TemplateView):
	site_id=_C
	def get(self,request,*args,**kwargs):self.site_id=get_site_id(request);template=get_template(self.site_id,is_frontend=_B);self.template_name=template+'daily_alert.html';return super(DailyAlertView,self).get(request,*(args),**kwargs)
	def get_context_data(self,*args,**kwargs):context=super(DailyAlertView,self).get_context_data(*(args),**kwargs);context[_D]=_v;return context
def dailyalert_ajax(request):
	site_id=get_site_id(request);lst=[];obj=DailyAlert();obj.set_current_language(_I);subquery1=Subquery(DailyAlertTranslation.objects.filter(master_id=OuterRef(_A),language_code=_A).values(_w));lang=obj.get_current_language();obj2=DailyAlert.objects.language(lang).filter(site_id=site_id).annotate(alert_id=subquery1)
	for i in obj2:res={};res[_M]=_C;res[_O]=i.uuid;res[_P]=i.updated_at;res['Alert (id)']=Truncator(i.alert_id).chars(20);res['Alert (en)']=Truncator(i.alert).chars(20);res[_A4]=Truncator(i.link).chars(20);res[_Z]=get_natural_datetime(i.updated_at);res[_Q]=_C;lst.append(res)
	return JsonResponse(lst,safe=_B)
def dailyalert_create(request):
	context={};context[_D]=_v;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_R
	if request.method==_H:
		form=DailyAlertForm(request.POST)
		if form.is_valid():post=DailyAlert.objects.language(_A).create(alert=request.POST.get(_w),link=request.POST.get(_c),status=request.POST.get(_L));post.set_current_language(_I);post.alert=request.POST.get(_w);post.save();messages.info(request,mMsgBox.get(_S,request.POST.get(_w)));return redirect(reverse_lazy(_v))
		else:print(_u);context[_G]=DailyAlertForm()
	else:messages.info(request,mMsgBox.get(_T));context[_G]=DailyAlertForm()
	return render(request,template,context)
def dailyalert_update(request,uuid):
	context={};context[_D]=_v;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_U;data=DailyAlert.objects.filter(site_id=site_id,uuid=uuid);post=get_object_or_404(data)
	if request.method==_H:
		form=DailyAlertForm(request.POST,instance=post)
		if form.is_valid():lang=request.POST.get(_a);obj=data.get();obj.set_current_language(lang);obj.alert=request.POST.get(_w);obj.link=request.POST.get(_c);obj.status=request.POST.get(_L);obj.save();messages.info(request,mMsgBox.get(_V,request.POST.get(_w)));return redirect(reverse_lazy(_v))
	else:messages.info(request,mMsgBox.get(_W));context[_G]=DailyAlertForm(instance=post)
	return render(request,template,context)
def dailyalert_delete(request,uuid):context={};site_id=get_site_id(request);data=DailyAlert.objects.filter(site_id=site_id,uuid=uuid);post=get_object_or_404(data);tmp=post.alert;post.delete();messages.info(request,mMsgBox.get(_X,tmp));return redirect(reverse_lazy(_v))
class GreetingView(TemplateView):
	site_id=_C
	def get(self,request,*args,**kwargs):self.site_id=get_site_id(request);template=get_template(self.site_id,is_frontend=_B);self.template_name=template+'greeting.html';return super(GreetingView,self).get(request,*(args),**kwargs)
	def get_context_data(self,*args,**kwargs):context=super(GreetingView,self).get_context_data(*(args),**kwargs);context[_A7]=True;context[_D]=_q;return context
def greeting_ajax(request):
	site_id=get_site_id(request);obj=Greeting();obj.set_current_language(_I);subquery1=Subquery(GreetingTranslation.objects.filter(master_id=OuterRef(_A),language_code=_A).values(_E));subquery2=Subquery(GreetingTranslation.objects.filter(master_id=OuterRef(_A),language_code=_A).values(_J));subquery_foto=Subquery(Photo.objects.filter(object_id=OuterRef(_A),content_type__model=_q).values(_d));lang=obj.get_current_language();obj2=Greeting.objects.language(lang).filter(site_id=site_id).annotate(title_id=subquery1).annotate(content_id=subquery2).annotate(file_path=subquery_foto).annotate(jml=Count(subquery_foto));lst=[]
	for i in obj2:res={};res[_M]=_C;res[_O]=i.uuid;res[_P]=i.updated_at;res[_f]=Truncator(i.title_id).chars(20);res[_g]=Truncator(i.title).chars(20);res[_l]=Truncator(i.content_id).chars(20);res[_m]=Truncator(i.content).chars(20);res[_h]=i.jml;res[_e]=i.file_path;res[_Z]=get_natural_datetime(i.updated_at);res[_Q]=_C;lst.append(res)
	return JsonResponse(lst,safe=_B)
def greeting_create(request):
	context={};context[_D]=_q;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_R
	if request.method==_H:
		form=GreetingForm(request.POST);photo=PhotoForm(request.POST)
		if form.is_valid():post=Greeting.objects.language(_A).create(title=request.POST.get(_E),content=request.POST.get(_J),name=request.POST.get(_F),designation=request.POST.get(_A9),status=request.POST.get(_L));post.set_current_language(_I);post.title=request.POST.get(_E);post.content=request.POST.get(_J);post.name=request.POST.get(_F);post.designation=request.POST.get(_A9);post.save();save_tags(request.POST.getlist(_Y),post);Photo.objects.create(content_object=post,file_path=request.POST.get(_K));messages.info(request,mMsgBox.get(_S,request.POST.get(_E)));return redirect(reverse_lazy(_q))
	else:messages.info(request,mMsgBox.get(_T));context[_G]=GreetingForm();context[_N]=PhotoForm()
	return render(request,template,context)
def greeting_update(request,uuid):
	context={};context[_D]=_q;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_U;data=Greeting.objects.filter(site_id=site_id,uuid=uuid);post=get_object_or_404(data);post_photo=post.photo.all()
	if post_photo:post_photo=post_photo.get()
	if request.method==_H:
		form=GreetingForm(request.POST,instance=post);photo=PhotoForm(request.POST,instance=post_photo)
		if form.is_valid():
			lang=request.POST.get(_a);obj=data.get();obj.set_current_language(lang);obj.title=request.POST.get(_E);obj.content=request.POST.get(_J);obj.name=request.POST.get(_F);obj.designation=request.POST.get(_A9);obj.status=request.POST.get(_L);obj.save()
			if photo.is_valid():
				if request.POST.get(_K):post.photo.clear();Photo.objects.create(content_object=post,file_path=request.POST.get(_K))
			messages.info(request,mMsgBox.get(_V,request.POST.get(_E)));return redirect(reverse_lazy(_q))
	else:messages.info(request,mMsgBox.get(_W));context[_G]=GreetingForm(instance=post);context[_N]=PhotoForm(instance=post_photo)
	return render(request,template,context)
def greeting_delete(request,uuid):context={};site_id=get_site_id(request);data=Greeting.objects.filter(site_id=site_id,uuid=uuid);post=get_object_or_404(data);tmp=post.title;post.delete();messages.info(request,mMsgBox.get(_X,tmp));return redirect(reverse_lazy(_q))
class PagesView(TemplateView):
	site_id=_C
	def get(self,request,*args,**kwargs):self.site_id=get_site_id(request);template=get_template(self.site_id,is_frontend=_B);self.template_name=template+'pages.html';return super(PagesView,self).get(request,*(args),**kwargs)
	def get_context_data(self,*args,**kwargs):context=super(PagesView,self).get_context_data(*(args),**kwargs);context[_D]=_r;return context
def pages_ajax(request):
	site_id=get_site_id(request);obj=Pages();obj.set_current_language(_I);subquery1=Subquery(PagesTranslation.objects.filter(master_id=OuterRef(_A),language_code=_A).values(_E));subquery2=Subquery(PagesTranslation.objects.filter(master_id=OuterRef(_A),language_code=_A).values(_J));subquery_foto=Subquery(Photo.objects.filter(object_id=OuterRef(_A),content_type__model=_r).values(_d));lang=obj.get_current_language();obj2=Pages.objects.language(lang).filter(site_id=site_id).annotate(title_id=subquery1).annotate(content_id=subquery2).annotate(file_path=subquery_foto).annotate(jml=Count(subquery_foto));lst=[]
	for i in obj2:res={};res[_M]=_C;res[_O]=i.uuid;res[_P]=i.updated_at;res[_f]=Truncator(i.title_id).chars(20);res[_g]=Truncator(i.title).chars(20);res[_l]=Truncator(i.content_id).chars(20);res[_m]=Truncator(i.content).chars(20);res[_h]=i.jml;res[_e]=i.file_path;res[_Z]=get_natural_datetime(i.updated_at);res[_Q]=_C;lst.append(res)
	return JsonResponse(lst,safe=_B)
def pages_create(request):
	context={};context[_D]=_r;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_R
	if request.method==_H:
		form=PagesForm(request.POST);photo=PhotoForm(request.POST)
		if form.is_valid():post=Pages.objects.language(_A).create(title=request.POST.get(_E),content=request.POST.get(_J),menu_id=request.POST.get(_i),status=request.POST.get(_L));post.set_current_language(_I);post.title=request.POST.get(_E);post.content=request.POST.get(_J);post.save();save_tags(request.POST.getlist(_Y),post);Photo.objects.create(content_object=post,file_path=request.POST.get(_K));messages.info(request,mMsgBox.get(_S,request.POST.get(_E)));return redirect(reverse_lazy(_r))
	else:messages.info(request,mMsgBox.get(_T));context[_G]=PagesForm();context[_N]=PhotoForm()
	return render(request,template,context)
def pages_update(request,uuid):
	context={};context[_D]=_r;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_U;data=Pages.objects.filter(site_id=site_id,uuid=uuid);post=get_object_or_404(data);post_photo=post.photo.all()
	if post_photo:post_photo=post_photo.get()
	if request.method==_H:
		form=PagesForm(request.POST,instance=post);photo=PhotoForm(request.POST,instance=post_photo)
		if form.is_valid():
			lang=request.POST.get(_a);obj=data.get();obj.set_current_language(lang);obj.title=request.POST.get(_E);obj.content=request.POST.get(_J);obj.menu_id=request.POST.get(_i);obj.status=request.POST.get(_L);obj.save();obj.tags.clear();save_tags(request.POST.getlist(_Y),obj)
			if photo.is_valid():
				if request.POST.get(_K):post.photo.clear();Photo.objects.create(content_object=post,file_path=request.POST.get(_K))
			messages.info(request,mMsgBox.get(_V,request.POST.get(_E)));return redirect(reverse_lazy(_r))
	else:messages.info(request,mMsgBox.get(_W));context[_G]=PagesForm(instance=post);context[_N]=PhotoForm(instance=post_photo)
	return render(request,template,context)
def pages_delete(request,uuid):context={};site_id=get_site_id(request);data=Pages.objects.filter(site_id=site_id,uuid=uuid);post=get_object_or_404(data);tmp=post.title;post.delete();messages.info(request,mMsgBox.get(_X,tmp));return redirect(reverse_lazy(_r))
class SocialMediaView(TemplateView):
	site_id=_C
	def get(self,request,*args,**kwargs):self.site_id=get_site_id(request);template=get_template(self.site_id,is_frontend=_B);self.template_name=template+'social_media.html';return super(SocialMediaView,self).get(request,*(args),**kwargs)
	def get_context_data(self,*args,**kwargs):context=super(SocialMediaView,self).get_context_data(*(args),**kwargs);context[_D]=_x;return context
def socialmedia_ajax(request):
	site_id=get_site_id(request);obj2=SocialMedia.objects.filter(site_id=site_id);lst=[]
	for i in obj2:res={};res[_M]=_C;res[_O]=i.uuid;res[_P]=i.updated_at;res['Kind']=i.kind;res[_A4]=Truncator(i.link).chars(30);res[_Z]=get_natural_datetime(i.updated_at);res[_Q]=_C;lst.append(res)
	return JsonResponse(lst,safe=_B)
def socialmedia_create(request):
	context={};context[_D]=_x;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_R
	if request.method==_H:
		form=SocialMediaForm(request.POST)
		if form.is_valid():post=form.save();messages.info(request,mMsgBox.get(_S,request.POST.get(_c)));return redirect(reverse_lazy(_x))
	else:messages.info(request,mMsgBox.get(_T));context[_G]=SocialMediaForm()
	return render(request,template,context)
def socialmedia_update(request,uuid):
	context={};context[_D]=_x;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_U;data=SocialMedia.objects.filter(site_id=site_id,uuid=uuid);post=get_object_or_404(data)
	if request.method==_H:
		form=SocialMediaForm(request.POST,instance=post)
		if form.is_valid():post=form.save();messages.info(request,mMsgBox.get(_V,request.POST.get(_c)));return redirect(reverse_lazy(_x))
	else:messages.info(request,mMsgBox.get(_W));context[_G]=SocialMediaForm(instance=post)
	return render(request,template,context)
def socialmedia_delete(request,uuid):context={};site_id=get_site_id(request);data=SocialMedia.objects.filter(site_id=site_id,uuid=uuid);post=get_object_or_404(data);tmp=post.link;post.delete();messages.info(request,mMsgBox.get(_X,tmp));return redirect(reverse_lazy(_x))
class PhotoGalleryView(TemplateView):
	site_id=_C
	def get(self,request,*args,**kwargs):self.site_id=get_site_id(request);template=get_template(self.site_id,is_frontend=_B);self.template_name=template+'photo_gallery.html';return super(PhotoGalleryView,self).get(request,*(args),**kwargs)
	def get_context_data(self,*args,**kwargs):context=super(PhotoGalleryView,self).get_context_data(*(args),**kwargs);context[_D]=_y;return context
def photogallery_ajax(request):
	site_id=get_site_id(request);lst=[];obj=PhotoGallery();obj.set_current_language(_I);subquery1=Subquery(PhotoGalleryTranslation.objects.filter(master_id=OuterRef(_A),language_code=_A).values(_E));subquery_foto=Subquery(Photo.objects.filter(object_id=OuterRef(_A),content_type__model='photogallery').values(_d));lang=obj.get_current_language();obj2=PhotoGallery.objects.language(lang).filter(site_id=site_id).annotate(title_id=subquery1).annotate(file_path=subquery_foto).annotate(jml=Count(subquery_foto))
	for i in obj2:res={};res[_M]=_C;res[_O]=i.uuid;res[_P]=i.updated_at;res[_f]=Truncator(i.title_id).chars(20);res[_g]=Truncator(i.title).chars(20);res[_h]=i.jml;res[_e]=i.file_path;res[_Z]=get_natural_datetime(i.updated_at);res[_Q]=_C;lst.append(res)
	return JsonResponse(lst,safe=_B)
def photogallery_create(request):
	context={};context[_D]=_y;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_R
	if request.method==_H:
		form=PhotoGalleryForm(request.POST);photo=PhotoForm(request.POST)
		if form.is_valid():post=PhotoGallery.objects.language(_A).create(title=request.POST.get(_E),status=request.POST.get(_L));post.set_current_language(_I);post.title=request.POST.get(_E);post.save();Photo.objects.create(content_object=post,file_path=request.POST.get(_K));messages.info(request,mMsgBox.get(_S,request.POST.get(_E)));return redirect(reverse_lazy(_y))
		else:print(_u);context[_G]=PhotoGalleryForm();context[_N]=PhotoForm()
	else:messages.info(request,mMsgBox.get(_T));context[_G]=PhotoGalleryForm();context[_N]=PhotoForm()
	return render(request,template,context)
def photogallery_update(request,uuid):
	context={};context[_D]=_y;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_U;data=PhotoGallery.objects.filter(site_id=site_id,uuid=uuid);post=get_object_or_404(data);post_photo=post.photo.all()
	if post_photo:post_photo=post_photo.get()
	if request.method==_H:
		form=PhotoGalleryForm(request.POST,instance=post);photo=PhotoForm(request.POST,instance=post_photo)
		if form.is_valid():
			lang=request.POST.get(_a);obj=data.get();obj.set_current_language(lang);obj.title=request.POST.get(_E);obj.status=request.POST.get(_L);obj.save()
			if photo.is_valid():
				if request.POST.get(_K):post.photo.clear();Photo.objects.create(content_object=post,file_path=request.POST.get(_K))
			messages.info(request,mMsgBox.get(_V,request.POST.get(_E)));return redirect(reverse_lazy(_y))
	else:messages.info(request,mMsgBox.get(_W));context[_G]=PhotoGalleryForm(instance=post);context[_N]=PhotoForm(instance=post_photo)
	return render(request,template,context)
def photogallery_delete(request,uuid):context={};site_id=get_site_id(request);data=PhotoGallery.objects.filter(site_id=site_id,uuid=uuid);post=get_object_or_404(data);tmp=post.title;post.delete();messages.info(request,mMsgBox.get(_X,tmp));return redirect(reverse_lazy(_y))
class VideoGalleryView(TemplateView):
	site_id=_C
	def get(self,request,*args,**kwargs):self.site_id=get_site_id(request);template=get_template(self.site_id,is_frontend=_B);self.template_name=template+'video_gallery.html';return super(VideoGalleryView,self).get(request,*(args),**kwargs)
	def get_context_data(self,*args,**kwargs):context=super(VideoGalleryView,self).get_context_data(*(args),**kwargs);context[_D]=_z;return context
def videogallery_ajax(request):
	site_id=get_site_id(request);lst=[];obj=VideoGallery();obj.set_current_language(_I);subquery1=Subquery(VideoGalleryTranslation.objects.filter(master_id=OuterRef(_A),language_code=_A).values(_E));lang=obj.get_current_language();obj2=VideoGallery.objects.language(lang).filter(site_id=site_id).annotate(title_id=subquery1)
	for i in obj2:res={};res[_M]=_C;res[_O]=i.uuid;res[_P]=i.updated_at;res[_f]=Truncator(i.title_id).chars(20);res[_g]=Truncator(i.title).chars(20);res['Embed']=Truncator(i.embed).chars(30);res[_Z]=get_natural_datetime(i.updated_at);res[_Q]=_C;lst.append(res)
	return JsonResponse(lst,safe=_B)
def videogallery_create(request):
	context={};context[_D]=_z;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_R
	if request.method==_H:
		form=VideoGalleryForm(request.POST)
		if form.is_valid():post=VideoGallery.objects.language(_A).create(title=request.POST.get(_E),embed=request.POST.get('embed'),status=request.POST.get(_L));post.set_current_language(_I);post.title=request.POST.get(_E);post.save();messages.info(request,mMsgBox.get(_S,request.POST.get(_E)));return redirect(reverse_lazy(_z))
		else:print(_u);context[_G]=VideoGalleryForm()
	else:messages.info(request,mMsgBox.get(_T));context[_G]=VideoGalleryForm()
	return render(request,template,context)
def videogallery_update(request,uuid):
	context={};context[_D]=_z;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_U;data=VideoGallery.objects.filter(site_id=site_id,uuid=uuid);post=get_object_or_404(data)
	if request.method==_H:
		form=VideoGalleryForm(request.POST,instance=post)
		if form.is_valid():lang=request.POST.get(_a);obj=data.get();obj.set_current_language(lang);obj.title=request.POST.get(_E);obj.embed=request.POST.get('embed');obj.status=request.POST.get(_L);obj.save();messages.info(request,mMsgBox.get(_V,request.POST.get(_E)));return redirect(reverse_lazy(_z))
	else:messages.info(request,mMsgBox.get(_W));context[_G]=VideoGalleryForm(instance=post)
	return render(request,template,context)
def videogallery_delete(request,uuid):context={};site_id=get_site_id(request);data=VideoGallery.objects.filter(site_id=site_id,uuid=uuid);post=get_object_or_404(data);tmp=post.title;post.delete();messages.info(request,mMsgBox.get(_X,tmp));return redirect(reverse_lazy(_z))
class RelatedLinkView(TemplateView):
	site_id=_C
	def get(self,request,*args,**kwargs):self.site_id=get_site_id(request);template=get_template(self.site_id,is_frontend=_B);self.template_name=template+'related_link.html';return super(RelatedLinkView,self).get(request,*(args),**kwargs)
	def get_context_data(self,*args,**kwargs):context=super(RelatedLinkView,self).get_context_data(*(args),**kwargs);context[_D]=_A0;return context
def relatedlink_ajax(request):
	site_id=get_site_id(request);lst=[];obj=RelatedLink();obj.set_current_language(_I);subquery1=Subquery(RelatedLinkTranslation.objects.filter(master_id=OuterRef(_A),language_code=_A).values(_F));lang=obj.get_current_language();obj2=RelatedLink.objects.language(lang).filter(site_id=site_id).annotate(name_id=subquery1)
	for i in obj2:res={};res[_M]=_C;res[_O]=i.uuid;res[_P]=i.updated_at;res[_A2]=Truncator(i.name_id).chars(20);res[_A3]=Truncator(i.name).chars(20);res[_A4]=Truncator(i.link).chars(30);res[_Z]=get_natural_datetime(i.updated_at);res[_Q]=_C;lst.append(res)
	return JsonResponse(lst,safe=_B)
def relatedlink_create(request):
	context={};context[_D]=_A0;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_R
	if request.method==_H:
		form=RelatedLinkForm(request.POST)
		if form.is_valid():post=RelatedLink.objects.language(_A).create(name=request.POST.get(_F),link=request.POST.get(_c),status=request.POST.get(_L));post.set_current_language(_I);post.name=request.POST.get(_F);post.save();messages.info(request,mMsgBox.get(_S,request.POST.get(_F)));return redirect(reverse_lazy(_A0))
		else:print(_u);context[_G]=RelatedLinkForm()
	else:messages.info(request,mMsgBox.get(_T));context[_G]=RelatedLinkForm()
	return render(request,template,context)
def relatedlink_update(request,uuid):
	context={};context[_D]=_A0;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_U;data=RelatedLink.objects.filter(site_id=site_id,uuid=uuid);post=get_object_or_404(data)
	if request.method==_H:
		form=RelatedLinkForm(request.POST,instance=post)
		if form.is_valid():lang=request.POST.get(_a);obj=data.get();obj.set_current_language(lang);obj.name=request.POST.get(_F);obj.link=request.POST.get(_c);obj.status=request.POST.get(_L);obj.save();messages.info(request,mMsgBox.get(_V,request.POST.get(_F)));return redirect(reverse_lazy(_A0))
	else:messages.info(request,mMsgBox.get(_W));context[_G]=RelatedLinkForm(instance=post)
	return render(request,template,context)
def relatedlink_delete(request,uuid):context={};site_id=get_site_id(request);data=RelatedLink.objects.filter(site_id=site_id,uuid=uuid);post=get_object_or_404(data);tmp=post.name;post.delete();messages.info(request,mMsgBox.get(_X,tmp));return redirect(reverse_lazy(_A0))
class DocumentView(TemplateView):
	site_id=_C
	def get(self,request,*args,**kwargs):self.site_id=get_site_id(request);template=get_template(self.site_id,is_frontend=_B);self.template_name=template+'document.html';return super(DocumentView,self).get(request,*(args),**kwargs)
	def get_context_data(self,*args,**kwargs):context=super(DocumentView,self).get_context_data(*(args),**kwargs);context[_D]=_A1;return context
def document_ajax(request):
	site_id=get_site_id(request);lst=[];obj=Document();obj.set_current_language(_I);subquery1=Subquery(DocumentTranslation.objects.filter(master_id=OuterRef(_A),language_code=_A).values(_F));subquery2=Subquery(DocumentTranslation.objects.filter(master_id=OuterRef(_A),language_code=_A).values(_J));lang=obj.get_current_language();obj2=Document.objects.language(lang).filter(site_id=site_id).annotate(name_id=subquery1).annotate(content_id=subquery2)
	for i in obj2:res={};res[_M]=_C;res[_O]=i.uuid;res[_P]=i.updated_at;res[_A2]=Truncator(i.name_id).chars(20);res[_A3]=Truncator(i.name).chars(20);res['content (id)']=Truncator(i.content_id).chars(30);res['content (en)']=Truncator(i.content).chars(30);res[_Z]=get_natural_datetime(i.updated_at);res[_Q]=_C;lst.append(res)
	return JsonResponse(lst,safe=_B)
def document_create(request):
	context={};context[_D]=_A1;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_R
	if request.method==_H:form=DocumentForm(request.POST,request.FILES);print('form=',form);post=Document.objects.language(_A).create(name=request.POST.get(_F),content=request.POST.get(_J),file_path_doc=request.POST.get(_AC),status=request.POST.get(_L));post.set_current_language(_I);post.name=request.POST.get(_F);post.content=request.POST.get(_J);post.save();messages.info(request,mMsgBox.get(_S,request.POST.get(_F)));return redirect(reverse_lazy(_A1))
	else:messages.info(request,mMsgBox.get(_T));context[_G]=DocumentForm()
	return render(request,template,context)
def document_update(request,uuid):
	context={};context[_D]=_A1;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_U;data=Document.objects.filter(site_id=site_id,uuid=uuid);post=get_object_or_404(data)
	if request.method==_H:
		form=DocumentForm(request.POST,request.FILES,instance=post)
		if form.is_valid():lang=request.POST.get(_a);obj=data.get();obj.set_current_language(lang);obj.name=request.POST.get(_F);obj.content=request.POST.get(_J);obj.file_path_doc=request.POST.get(_AC);obj.status=request.POST.get(_L);obj.save();messages.info(request,mMsgBox.get(_V,request.POST.get(_F)));return redirect(reverse_lazy(_A1))
	else:messages.info(request,mMsgBox.get(_W));context[_G]=DocumentForm(instance=post)
	return render(request,template,context)
def document_delete(request,uuid):context={};site_id=get_site_id(request);data=Document.objects.filter(site_id=site_id,uuid=uuid);post=get_object_or_404(data);tmp=post.name;post.delete();messages.info(request,mMsgBox.get(_X,tmp));return redirect(reverse_lazy(_A1))
class MenuView(TemplateView):
	site_id=_C
	def get(self,request,*args,**kwargs):self.site_id=get_site_id(request);template=get_template(self.site_id,is_frontend=_B);self.template_name=template+'menu.html';return super(MenuView,self).get(request,*(args),**kwargs)
	def get_context_data(self,*args,**kwargs):context=super(MenuView,self).get_context_data(*(args),**kwargs);context[_D]=_i;return context
def get_menu_group(site_id):
	A='Frontend Site ';site_name=Site.objects.get(pk=site_id).domain;menugroup=MenuGroup.objects.filter(site=site_id,kind=1);print('menugroup = ',menugroup)
	if menugroup:return menugroup[0].id
	else:
		lang1=get_active_language_choices()[0];lang2=_A
		if lang1==_A:lang2=_I
		post=MenuGroup.objects.language(lang1).create(site_id=site_id,kind=1,name=A+site_name);post.set_current_language(lang2);post.name=A+site_name;post.save();return post.id
def menu_ajax(request):
	A='Name (';site_id=get_site_id(request);group_id=get_menu_group(site_id);print('group_id = ',group_id);lst=[]
	if group_id:
		lang=get_active_language_choices()[0];lang2=_A
		if lang==_A:lang2=_I
		menu=Menus(menu_group=group_id,kinds=1,site_id=site_id)
		if menu:
			obj2=menu.get_menus();print(obj2)
			for i in obj2:
				tmp='';lvl=i['level']
				while lvl>0:tmp+='<i class="fa fa-long-arrow-right"></i> &nbsp;&nbsp;&nbsp;&nbsp; ';lvl-=1
				res={};res[_M]=_C;res[_O]=i[_O];res[_P]=_C;res[A+lang+')']=Truncator(i[_F]).chars(20);res[A+lang2+')']=Menu.objects.language(lang2).get(pk=i[_A]).name;res['Tree']=tmp+Truncator(i[_F]).chars(20);res[_A4]=Truncator(i[_c]).chars(30);res['Icon']=Truncator(i[_M]).chars(30);res[_Q]=_C;lst.append(res)
	return JsonResponse(lst,safe=_B)
def menu_create(request):
	context={};context[_D]=_i;site_id=get_site_id(request);group_id=get_menu_group(request.user.id);menu_group=MenuGroup.objects.get(id=group_id);template=get_template(site_id,is_frontend=_B)+_R
	if request.method==_H:
		form=MenuForm(request.POST)
		if form.is_valid():form_clean=form.cleaned_data;print(form_clean);post=Menu.objects.language(_A).create(name=form_clean[_F],parent_id=request.POST.get('parent'),link=form_clean[_c],order_menu=form_clean[_AD],icon=form_clean[_M],is_visibled=form_clean[_AE],is_external=form_clean[_AF]);post.menu_group.add(menu_group);post.set_current_language(_I);post.name=form_clean[_F];post.save();messages.info(request,mMsgBox.get(_S,request.POST.get(_F)));return redirect(reverse_lazy(_i))
		else:print(_u);context[_G]=MenuForm()
	else:messages.info(request,mMsgBox.get(_T));context[_G]=MenuForm()
	return render(request,template,context)
def menu_update(request,uuid):
	context={};context[_D]=_i;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_U;data=Menu.objects.filter(uuid=uuid);post=get_object_or_404(data)
	if request.method==_H:
		form=MenuForm(request.POST,instance=post)
		if form.is_valid():form_clean=form.cleaned_data;print(form_clean);lang=request.POST.get(_a);obj=data.get();obj.set_current_language(lang);obj.name=form_clean[_F];obj.parent_id=request.POST.get('parent');obj.link=form_clean[_c];obj.order_menu=form_clean[_AD];obj.icon=form_clean[_M];obj.is_visibled=form_clean[_AE];obj.is_external=form_clean[_AF];obj.save();messages.info(request,mMsgBox.get(_V,request.POST.get(_F)));return redirect(reverse_lazy(_i))
	else:messages.info(request,mMsgBox.get(_W));context[_G]=MenuForm(instance=post)
	return render(request,template,context)
def menu_delete(request,uuid):context={};site_id=get_site_id(request);data=Menu.objects.filter(uuid=uuid);post=get_object_or_404(data);tmp=post.name;post.delete();messages.info(request,mMsgBox.get(_X,tmp));return redirect(reverse_lazy(_i))
def site_name_update(site_id,name):site=Site.objects.get(id=site_id);site.name=name;site.save()
class AgencyView(TemplateView):
	site_id=_C
	def get(self,request,*args,**kwargs):self.site_id=get_site_id(request);template=get_template(self.site_id,is_frontend=_B);self.template_name=template+'agency.html';return super(AgencyView,self).get(request,*(args),**kwargs)
	def get_context_data(self,*args,**kwargs):context=super(AgencyView,self).get_context_data(*(args),**kwargs);context[_D]=_s;context[_A7]=True;return context
def agency_ajax(request):
	site_id=get_site_id(request);obj=Agency();obj.set_current_language(_I);service=Service.objects.filter(site_id=site_id).values_list(_s,flat=True);subquery1=Subquery(AgencyTranslation.objects.filter(master_id=OuterRef(_A),language_code=_A).values(_A5));subquery2=Subquery(AgencyTranslation.objects.filter(master_id=OuterRef(_A),language_code=_A).values(_A6));lang=obj.get_current_language();obj2=Agency.objects.language(lang).filter(id=service[0]).annotate(address_id=subquery1).annotate(notes_id=subquery2);lst=[]
	for i in obj2:res={};res[_M]=_C;res[_O]=i.uuid;res[_P]=i.updated_at;res['Name']=Truncator(i.name).chars(20);res['Address (id)']=Truncator(i.address_id).chars(20);res['Address (en)']=Truncator(i.address).chars(20);res['Description (id)']=Truncator(i.notes_id).chars(20);res['Description (en)']=Truncator(i.notes).chars(20);res[_AA]=i.email;res[_AB]=i.phone;res[_Z]=get_natural_datetime(i.updated_at);res[_Q]=_C;lst.append(res)
	return JsonResponse(lst,safe=_B)
def agency_create(request):
	context={};context[_D]=_s;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_R
	if request.method==_H:
		form=AgencyForm(request.POST)
		if form.is_valid():post=Agency.objects.language(_A).create(address=request.POST.get(_A5),notes=request.POST.get(_A6),name=request.POST.get(_F),email=request.POST.get(_AA),phone=request.POST.get(_AB),fax=request.POST.get('fax'),whatsapp=request.POST.get('whatsapp'),status=request.POST.get(_L));post.set_current_language(_I);post.address=request.POST.get(_A5);post.notes=request.POST.get(_A6);post.save();site_name_update(site_id,request.POST.get(_F));print(_AG);messages.info(request,mMsgBox.get(_S,request.POST.get(_F)));return redirect(reverse_lazy(_s))
	else:messages.info(request,mMsgBox.get(_T));context[_G]=AgencyForm()
	return render(request,template,context)
def agency_update(request,uuid):
	context={};context[_D]=_s;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_U;data=Agency.objects.filter(uuid=uuid);post=get_object_or_404(data)
	if request.method==_H:
		form=AgencyForm(request.POST,instance=post)
		if form.is_valid():lang=request.POST.get(_a);obj=data.get();obj.set_current_language(lang);obj.address=request.POST.get(_A5);obj.notes=request.POST.get(_A6);obj.name=request.POST.get(_F);obj.email=request.POST.get(_AA);obj.phone=request.POST.get(_AB);obj.fax=request.POST.get('fax');obj.whatsapp=request.POST.get('whatsapp');obj.status=request.POST.get(_L);obj.save();print('site name begin update');site_name_update(site_id,request.POST.get(_F));print(_AG);messages.info(request,mMsgBox.get(_V,request.POST.get(_F)));return redirect(reverse_lazy(_s))
	else:messages.info(request,mMsgBox.get(_W));context[_G]=AgencyForm(instance=post)
	return render(request,template,context)
def agency_delete(request,uuid):context={};site_id=get_site_id(request);data=Agency.objects.filter(uuid=uuid);post=get_object_or_404(data);tmp=post.name;post.delete();messages.info(request,mMsgBox.get(_X,tmp));return redirect(reverse_lazy(_s))
class CategoriesView(TemplateView):
	site_id=_C
	def get(self,request,*args,**kwargs):self.site_id=get_site_id(request);template=get_template(self.site_id,is_frontend=_B);self.template_name=template+'categories.html';return super(CategoriesView,self).get(request,*(args),**kwargs)
	def get_context_data(self,*args,**kwargs):context=super(CategoriesView,self).get_context_data(*(args),**kwargs);context[_D]=_b;return context
def categories_ajax(request):
	site_id=get_site_id(request);obj=Categories();obj.set_current_language(_I);subquery1=Subquery(CategoriesTranslation.objects.filter(master_id=OuterRef(_A),language_code=_A).values(_F));lang=obj.get_current_language();obj2=Categories.objects.language(lang).filter(site_id=site_id).annotate(name_id=subquery1);lst=[]
	for i in obj2:res={};res[_M]=_C;res[_O]=i.uuid;res[_P]=i.updated_at;res[_A2]=Truncator(i.name_id).chars(20);res[_A3]=Truncator(i.name).chars(20);res[_Z]=get_natural_datetime(i.updated_at);res[_Q]=_C;lst.append(res)
	return JsonResponse(lst,safe=_B)
def categories_create(request):
	context={};context[_D]=_b;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_R
	if request.method==_H:
		form=CategoriesForm(request.POST)
		if form.is_valid():post=Categories.objects.language(_A).create(name=request.POST.get(_F));post.set_current_language(_I);post.name=request.POST.get(_F);post.save();messages.info(request,mMsgBox.get(_S,request.POST.get(_F)));return redirect(reverse_lazy(_b))
	else:messages.info(request,mMsgBox.get(_T));context[_G]=CategoriesForm()
	return render(request,template,context)
def categories_update(request,uuid):
	context={};context[_D]=_b;site_id=get_site_id(request);template=get_template(site_id,is_frontend=_B)+_U;data=Categories.objects.filter(uuid=uuid);post=get_object_or_404(data)
	if request.method==_H:
		form=CategoriesForm(request.POST,instance=post)
		if form.is_valid():lang=request.POST.get(_a);obj=data.get();obj.set_current_language(lang);obj.name=request.POST.get(_F);obj.save();messages.info(request,mMsgBox.get(_V,request.POST.get(_F)));return redirect(reverse_lazy(_b))
	else:messages.info(request,mMsgBox.get(_W));context[_G]=CategoriesForm(instance=post)
	return render(request,template,context)
def categories_delete(request,uuid):context={};site_id=get_site_id(request);data=Categories.objects.filter(uuid=uuid);post=get_object_or_404(data);tmp=post.name;post.delete();messages.info(request,mMsgBox.get(_X,tmp));return redirect(reverse_lazy(_b))