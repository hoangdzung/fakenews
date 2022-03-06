from app import db 
from models import *
import pickle
import sys 
from tqdm import tqdm 

data = pickle.load(open(sys.argv[1],'rb'))
data = [{k: v if v is not None else '' for k,v in data_dict.items() } for data_dict in data] 
db.create_all()

for data_dict in tqdm(data):
    p = Post(title=data_dict['title'],
            subtitle_full=data_dict['subtitle_full'],
            subtitle_short=data_dict['subtitle_short'],
            claim=data_dict['claim'],
            url=data_dict['url'],
            thumnail=data_dict['thumnail'],
            rating_tag=data_dict['label_tag'],
            rating_img=data_dict['rating_img'],
            rating_text=data_dict['rating_text'],
            author=data_dict['author'],
            date=data_dict['date'],
            true_info=data_dict['true'],
            false_info=data_dict['false'],
            ctx_info=data_dict['ctx'],
            origin=data_dict['origin']
            )
    db.session.add(p)
    db.session.commit()
