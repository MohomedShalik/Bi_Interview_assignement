from django.core.management.base import BaseCommand
import zipfile
import pandas as pd 
from sqlite3 import connect
import os
import pathlib



class Command(BaseCommand):


    def handle(self , *args , **options):


        tmp_dir_path = os.path.join(os.getcwd(), "tmp")
        arch_dir_path = os.path.join(os.getcwd(), "archives")
        interview_dataset_path = os.path.join(tmp_dir_path,"Interview_dataset.zip")
        csv_dataset_path = os.path.join(tmp_dir_path,"Ganison_dataset")


        if (not os.path.exists(arch_dir_path)):
            os.makedirs(arch_dir_path)

        if not (os.path.exists(csv_dataset_path)):
            with zipfile.ZipFile(interview_dataset_path, 'r') as zip_ref:
                print("extracting csv files from zip file")
                zip_ref.extractall(tmp_dir_path)
        
        df_appended = self.load_dataframe_from_csv(csv_dataset_path)
        df_appended["Fullname"] = df_appended['First Name'].astype(str) +" "+ df_appended["Last Name"]
        df_appended.drop(columns=['First Name', 'Last Name'] , inplace=True)
        
        student_entity = df_appended[['StudentID','Fullname']].copy()
        student_entity.drop_duplicates(inplace=True)
        student_entity.rename(columns = {'StudentID':'id', 'Fullname' : 'student_name'}, inplace = True)
        
        award_entity = df_appended[['award']].copy()
        award_entity.drop_duplicates(inplace=True)
        award_entity.insert(0 , 'id' , range(1, 1 + len(award_entity)))
        award_entity.rename(columns = {'award':'award_name'}, inplace = True)

        school_entity = df_appended[['school_name']].copy()
        school_entity.drop_duplicates(inplace=True)
        school_entity.insert(0, 'id', range(1, 1 + len(school_entity)))

        class_entity = df_appended[['Class']].copy()
        class_entity.drop_duplicates(inplace=True)
        class_entity["id"] =class_entity["Class"].str.split(" ").str[1]
        class_entity.rename(columns = {'Class':'class_name'}, inplace = True)
        
        assessment_area_entity = df_appended[['Assessment Areas']].copy()
        assessment_area_entity.drop_duplicates(inplace=True)
        assessment_area_entity.insert(0 , 'id' , range(1, 1 + len(assessment_area_entity)))
        assessment_area_entity.rename(columns = {'Assessment Areas':'assessment_area_name'}, inplace = True)

        s_answer = df_appended[['Answers']].copy()
        c_answer = df_appended[['Correct Answers']].copy()
        s_answer.drop_duplicates(inplace=True)
        c_answer.drop_duplicates(inplace=True)
        c_answer.rename(columns = {'Correct Answers':'Answers'}, inplace = True)
        answer_entity = pd.concat([s_answer , c_answer])
        answer_entity.drop_duplicates(inplace=True)
        answer_entity.rename(columns = {'Answers':'answer'}, inplace = True)
        answer_entity.sort_values(by=["answer"],inplace=True)
        answer_entity.insert(0 , 'id' , range(1, 1 + len(answer_entity)))

        subject_entity = df_appended[['Subject']].copy()
        subject_entity.drop_duplicates(inplace=True)
        subject_entity.sort_values(by="Subject" , inplace=True)
        subject_entity.insert(0 , 'id' , range(1, 1 + len(subject_entity)))
        subject_entity.rename(columns = {'Subject':'subject_name'}, inplace = True)

        summary_entity = df_appended

        drop_columns = ["Question Number" , "Subject Contents" ,'sydney_correct_count_percentage','sydney_average_score',
               'student_total_assessed','student_area_assessed_score','total_area_assessed_score'
               ,'average_score','school_percentile','strength_status','participant_count','high_distinct_count', 'distinct_count', 'credit_count'
               ,]
        summary_entity.drop(columns=drop_columns,inplace=True)
        summary_entity.drop(columns=["Fullname"],inplace=True)
        summary_entity.rename(columns = {'StudentID':'student_id'}, inplace = True)
        summary_entity["year_level_name"] = "Year " + summary_entity['year'].astype(str) +" Level "+ summary_entity["Year Level"].astype(str)
        summary_entity.drop(columns=["year" , "Year Level"] , inplace=True)
        summary_entity['correct_answer_id'] = summary_entity['Correct Answers'].map(answer_entity.set_index('answer')['id'])

        rename_columns = { 'school_name':'school_id', 'Class' : 'class_id' , 
                          'award':'award_id' , "Subject" : "subject_id" , 
                          "Answers" :"answer_id" ,"Correct Answers" : "correct_answer",
                          "Assessment Areas" : "assessment_area_id"}
        
        summary_entity.rename(columns = rename_columns, inplace = True)
        summary_entity['school_id'] = summary_entity['school_id'].map(school_entity.set_index('school_name')['id'])
        summary_entity['subject_id'] =  summary_entity['subject_id'].map(subject_entity.set_index('subject_name')['id'])
        summary_entity['answer_id'] = summary_entity['answer_id'].map(answer_entity.set_index('answer')['id'])
        summary_entity['assessment_area_id'] = summary_entity['assessment_area_id'].map(assessment_area_entity.set_index('assessment_area_name')['id'])  
        summary_entity['award_id'] = summary_entity['award_id'].map(award_entity.set_index('award_name')['id'])
        summary_entity['class_id'] = summary_entity['class_id'].map(class_entity.set_index('class_name')['id'])
        summary_entity.insert(0 , 'id' , range(1, 1 + len(summary_entity)))
          

        summary_entity.to_csv(os.path.join(arch_dir_path,'summary_archive'),compression="gzip",index=False)
        student_entity.to_csv(os.path.join(arch_dir_path,'student_archive'),compression="gzip",index=False)
        class_entity.to_csv(os.path.join(arch_dir_path,'class_archive'),compression="gzip",index=False)
        answer_entity.to_csv(os.path.join(arch_dir_path,'answers_archive'),compression="gzip",index=False)
        assessment_area_entity.to_csv(os.path.join(arch_dir_path,'assessment_area_archive'),compression="gzip",index=False)
        subject_entity.to_csv(os.path.join(arch_dir_path,'subjects_archive'),compression="gzip",index=False)
        award_entity.to_csv(os.path.join(arch_dir_path,'award_archive'),compression="gzip",index=False)
        school_entity.to_csv(os.path.join(arch_dir_path,'schools_archive'),compression="gzip",index=False)

        
    def load_dataframe_from_csv(self,csv_files_parent_dir):

        csv_files = [os.path.join(csv_files_parent_dir , file) for file in os.listdir(csv_files_parent_dir)]
        df_appended = pd.DataFrame()
        for file in csv_files:
            df = pd.read_csv(file)
            if (df.columns[-1] == "awarDistinction"):
                df.rename(columns = {'awarDistinction':'award'}, inplace = True)
            df_appended = pd.concat([df_appended , df]);
        del df
        return df_appended




        




            
