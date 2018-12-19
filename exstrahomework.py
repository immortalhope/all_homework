#student (name, e-mail)
#food (name, price)
dataset = {
    "bob@kpi.ua":{
                    "person":{
                            "name":"Bob",
                            "email":"bob@kpi.ua"
                    },
                    "foods": {
                            "apple":[1.3,12.1],
                            "milk":[45]
                    }
    },
    "boba@kpi.ua":{
                    "person": {
                            "name": "Boba",
                            "email" : "boba@kpi.ua"
                     },
                    "foods": {"milk": [45]}
                }
}

"""
Завдання:
1. Написати рекурсивну функцію, що повертає список імен користувачів.
2. Написати звичайну функцію, що повертає назву продукту та скільки разів його купували.
3. Написати функцію, що виводить ім'я користувача та скільки він витратив на свою їжу.
"""

def namelist(dataset, emails, list_of_names):
    if len(dataset) == len(list_of_names):
        return list_of_names
    list_of_names.append(dataset[emails[0]]["person"]["name"])
    emails.pop(0)
    return namelist(dataset, emails, list_of_names)

list_of_names=[]
emails = []
for key in dataset:
    emails.append(key)
print(namelist(dataset, emails, list_of_names))


def foods_name(dataset, foodset = {}):
    for key in dataset:
        for elm in dataset[key]["foods"]:
            times = 0
            error = 0
            try:
                times = foodset[elm]
            except KeyError:
                error += 1
            foodset[elm] = times + len(dataset[key]["foods"][elm])
    return foodset

print (foods_name(dataset, foodset = {}))

def name_money(dataset):
    result = {}
    for key in dataset:
        food = dataset[key]["foods"]
        name = dataset[key]["person"]["name"]
        count = 0
        for elm in food:
            count += sum(food[elm])
            result[name] = count
    return result

print (name_money(dataset))