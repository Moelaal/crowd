
import imp
from projectMenu import create_project,view_project,viewAll_project,deleteAll_project

def profileChoose():
    while True:
        print('__________________________________')
        print('Choose one of the following:\n1-Create new project\n2-view project \n3-View All projects\n4-Delete project \n5-Exits')
        choose = int(input('choose 1,2,3,4,5: '))

        if choose == 1:
            create_project()
        elif choose == 2:
            view_project()
        elif choose == 3:
            viewAll_project()
        elif choose == 4:
            deleteAll_project()
        elif choose == 5:
            break


