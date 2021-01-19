from common.database import Database

class TableContent():
    def __init__(self, options, preferences, priority, score):
        self.options=options
        self.preferences=preferences
        self.priority=priority
        self.score=score

    def add_option(self):
        opt=[]
        new_options= input("Please enter your options: ")
        while True:
            if new_options in opt:
                continue
            elif new_options != '':
                opt.append(new_options)
            else:
                break
            return opt


    def add_criteria(self):
        crt=[]
        new_criteria = input("Please enter your criterias: ") # how to make it possible to enter more options
        while True:
            if new_criteria in crt:
                continue
            elif new_criteria != '':
                crt.append(new_criteria)
                new_criteria = input("Please enter your criterias: ")
            else:
                break
            return crt  # connecting to priority? connecting to table?

    def add_priority(self):
        prio=[] # is one list enough, how will you recall the values with the same score?
        for i in crt:
            print(i)
            new_prio=input('Please enter your priority for this criteria: ')
            if 3>new_prio>0:
                if new_prio=2:
                    prio.append(new_prio)
                elif new_prio=3:
                    new_prio/3
                    prio.append(new_prio)
                else:
                    new_prio*3
                    prio.append(new_prio)
            else:
                return input('Please enter a number between 1 (highest priority) an 3 (lowest priority: ')

    def add_score(self):
        # how to make the input more flexible within the table -> eventbased programming?
        # call clean score method
        # two empty list?: opt1scr[] and opt2scr[] -> compare with prio[]


    #def clean_score():
        #csc = []
        #for i in scr[]:  # scr[] weigth already adjusted e.g. 1=-2, 6=2
            #for j in prio[]:  # prio[] weigth already adjusted e.g. 1=3
                #new_csc = i * j
                #csc.append(new_csc)

    #def sum_of_columns():
            #sum(csc)  # sum() is a very inefficient way to build the sum of a list

