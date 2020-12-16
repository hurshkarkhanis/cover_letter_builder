optional_name = input('name of person you know at company, leave blank if none: '.upper())
print()
company_name = input('company name: '.upper())
print()
job_title = input('job title: '.upper())
print()
skill_1 = input('FIRST SKILL TO SHOWCASE (ex: i learned about { ____ }) ')
print()
skill_2 = input('SECOND SKILL TO SHOWCASE: (ex: and { ____ }) ')
print()
summarize_relavent_project = input('SUMMARIZE PROJECT: (ex: my project is about { _____ }) ')
print()
technical_skills = input('TECHNICAL SKILLS USED: (ex: this project uses { ____ and ____ }) ')
print()
what_it_does = input('WHAT YOUR PROJECT DOES IN DETAIL (write a lot here): ')




if optional_name == '':
    one = 'To the recruiting team at ' + company_name + ','
else:
    one = 'To ' + optional_name + ' and the recruiting team at ' + company_name + ','


two = 'The ' + job_title + ' role at ' + company_name + ' is a perfect fit for me.'

three = 'After graduating college with a finance degree this year, I decided to jump into the world of data by learning about ' + skill_1 + ' and ' + skill_2 + ","

four = 'both of which are required for the role as per the job description. I have done so by working on a number of projects, specifically one about ' + summarize_relavent_project

five = 'This project uses ' + technical_skills + ' to ' + what_it_does + ','
six = 'something I know will come in handy in the ' + job_title + ' role.'

seven = 'In addition to my technical skills, I also have leadership experience. In college, I served as a resident advisor, where I mentored a group of fifty freshman'

eight =  'students during their first year of college. As part of this role, I also collaborated with campus partners to put on initiatives about the importance of money management and'
nine = 'political participation, since it happened to be an election year.'

ten = 'I am confident that both my technical and soft skills make me a perfect fit for the ' + job_title + ' role.'

eleven = 'You can contact me at the links below. Looking forward to connecting,'


twelve = 'Hursh Karkhanis'

thirteen = 'Website: ​https://www.hurshkarkhanis.com/'
fourteen = 'Email: ​karkhanis.hursh@gmail.com'


lines = [one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen]

for line in lines:
    print(line)
    print('\n')
