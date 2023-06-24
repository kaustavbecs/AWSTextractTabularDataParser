from textractcaller.t_call import call_textract, Textract_Features
from textractprettyprinter.t_pretty_print import Pretty_Print_Table_Format, Textract_Pretty_Print, get_string

# Change this to point to your file
input_document = 'Statement.jpg'

textract_json = call_textract(input_document=input_document, features=[Textract_Features.FORMS, Textract_Features.TABLES])
print(get_string(textract_json=textract_json,
               table_format=Pretty_Print_Table_Format.csv,
               output_type=[Textract_Pretty_Print.TABLES, Textract_Pretty_Print.FORMS]))