
# this class will be get called for the purpose of getting personal info of cricketer
def get_personal_data(personal_data,personal_data_lst):
    for i in personal_data:
        personal_data_lst.append(i.get_text())
        print(i)

    print("Personal Data ", personal_data_lst)