alex = {}

alex['first'] = 'Alex'
alex['last'] = 'Wang'

olive = {'first':'Olive','last':'Wu'}

print(alex,olive)

people = [alex,olive]
people.append({'first':'Adam','last':'Rollo'})
print(people)

presenters = people[0:1]
print(presenters)