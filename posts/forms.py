from wtforms import Form, StringField, TextAreaField

class PostForm(Form):
    title = StringField('Title')
    subtitle_full = StringField('Subtitle Full')
    subtitle_short = TextAreaField('Subtitle Short')
    claim = TextAreaField('Claim')
    url = TextAreaField('Url')
    thumnail = TextAreaField('Thumnail link')
    rating_tag = StringField('Tag')
    rating_img = TextAreaField('Rating Image Link')
    rating_text = StringField('Rating Label')
    author = StringField('Author')
    date = StringField('Date')
    true_info = TextAreaField('What\'s True')
    false_info = TextAreaField('What\'s False')
    ctx_info = TextAreaField('Context')
    origin = TextAreaField('Origin')