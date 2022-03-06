from flask import Blueprint, render_template
from flask import request, redirect, url_for
from flask_security import login_required
from models import Post
from .forms import PostForm
from app import db 

posts = Blueprint('posts',__name__,template_folder='templates') 

@posts.route('/create',methods=['POST','GET'])
@login_required
def post_create():
    form = PostForm()
    if request.method == 'POST':
        title = request.form.get('title')
        subtitle_full = request.form.get('subtitle_full')
        subtitle_short = request.form.get('subtitle_short')
        claim = request.form.get('claim')
        url = request.form.get('url')
        thumnail = request.form.get('thumnail')
        rating_tag = request.form.get('rating_tag')
        rating_img = request.form.get('rating_img')
        rating_text = request.form.get('rating_text')
        author = request.form.get('author')
        true_info = request.form.get('true_info')
        false_info = request.form.get('false_info')
        ctx_info = request.form.get('ctx_info')
        origin = request.form.get('origin')
          
        try:
            post = Post(title=title,
            subtitle_full=subtitle_full,
            subtitle_short=subtitle_short,
            thumnail=thumnail,
            rating_tag=label_tag,
            rating_img=rating_img,
            rating_text=rating_text,
            author=author,
            date=date,
            true_info=true,
            false_info=false,
            ctx_info=ctx,
            origin=origin
            )
            db.session.add(post)
            db.session.commit()
        except:
            print("Can't add post to db")
        
        return redirect(url_for('posts.post_detail', slug=post.slug))
    
    return render_template('posts/post_create.html',form=form)

@posts.route('/')
def posts_list():
    q = request.args.get('q')
    print("q:",q)
    if q:
        posts = Post.query.filter(Post.title.contains(q) |
                Post.origin.contains(q))
    else:
        posts = Post.query.order_by(Post.created.desc())

    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1 
    
    pages = posts.paginate(page=page, per_page=10)

    return render_template('posts/posts.html', posts=posts, pages=pages)

@posts.route('/<slug>')
def post_detail(slug):
    q = request.args.get('q')
    print("q:",q)
    if q:
        full_url = url_for('posts.posts_list', **request.args)
        return redirect(full_url)

    post = Post.query.filter(Post.slug==slug).first_or_404()
    return render_template('posts/post_detail.html', post=post)

@posts.route('/<slug>/edit', methods=['POST','GET'])
@login_required
def post_update(slug):
    post = Post.query.filter(Post.slug==slug).first_or_404()
    if request.method == 'POST':
        form = PostForm(formdata=request.form, obj=post)
        form.populate_obj(post)
        db.session.commit()
        return redirect(url_for('posts.post_detail', slug=post.slug))
    form = PostForm(obj=post)
    return render_template('posts/edit.html', post=post, form=form)
