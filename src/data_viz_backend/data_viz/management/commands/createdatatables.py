import pandas as pd 
from sqlite3 import connect
import os

from django.core.management.base import BaseCommand



class Command(BaseCommand):
    

    def handle(self , *args , **options):

        archives_path = os.path.join(os.getcwd() , 'archives')

        summary_entity = pd.read_csv(os.path.join(archives_path,'summary_archive'),
                         compression='gzip')
        assessment_area_entity = pd.read_csv(os.path.join(archives_path,'assessment_area_archive'),
                         compression='gzip')
        answer_entity = pd.read_csv(os.path.join(archives_path,'answers_archive'),
                         compression='gzip')
        class_entity = pd.read_csv(os.path.join(archives_path,'class_archive'),
                         compression='gzip')
        
        student_entity = pd.read_csv(os.path.join(archives_path,'student_archive'),
                         compression='gzip')
        
        subject_entity = pd.read_csv(os.path.join(archives_path,'subjects_archive'),
                         compression='gzip')
        
        award_entity = pd.read_csv(os.path.join(archives_path,'award_archive'),
                         compression='gzip')
        
        school_entity = pd.read_csv(os.path.join(archives_path,'schools_archive'),
                         compression='gzip')
        
        conn = connect("db.sqlite3")
        summary_entity.to_sql('data_viz_summary' , conn,if_exists='replace' , index=False)
        answer_entity.to_sql('data_viz_answers' , conn,if_exists='replace' , index=False)
        student_entity.to_sql('data_viz_student' , conn,if_exists='replace' , index=False)
        school_entity.to_sql('data_viz_school' , conn,if_exists='replace' , index=False)
        class_entity.to_sql('data_viz_class' , conn,if_exists='replace' , index=False)
        assessment_area_entity.to_sql('data_viz_assessment_areas' , conn,if_exists='replace' , index=False)
        award_entity.to_sql('data_viz_award' , conn,if_exists='replace' , index=False)
        subject_entity.to_sql('data_viz_subject' , conn,if_exists='replace' , index=False)

        
