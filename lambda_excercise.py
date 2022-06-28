\
#Lambda Excercise 1
import functools

#Consider the List

prog_lang = [('Python', 3.8),
    ('Java', 13),
    ('JavaScript', 2019),
    ('Scala', 2.13)]


#1. Sort the list by each language's version in ascending order.
#[('Scala', 2.13), ('Python', 3.8), ('Java', 13), ('JavaScript', 2019)]
def sort_lang_asc(prog_lang):
    return sorted(prog_lang, key = lambda x: x[1])
print(sort_lang_asc(prog_lang))
#2. Sort the list by the length of the name of each language in descending order.
#[('JavaScript', 2019), ('Python', 3.8), ('Scala', 2.13), ('Java', 13)]
def sort_leng_desc(prog_lang):
    return sorted(prog_lang, key = lambda x: (len(x[0]), x[0]) ,reverse=True)
print(sort_leng_desc(prog_lang))
#3. Filter the list so that it only contains languages with 'a' in it.
#[('Java', 13), ('JavaScript', 2019), ('Scala', 2.13)]
def filter_a(prog_lang):
    return list(filter(lambda x: 'a' in x[0], prog_lang))
print(filter_a(prog_lang))
#4. Filter the list so that it only contains languages whose version is in integer form.
#[('Java', 13), ('JavaScript', 2019)]
def filter_int(prog_lang):
    return list(filter(lambda x: type(x[1]) == int, prog_lang))
print(filter_int(prog_lang))

#5. Transform the list so that it contains the tuples in the form,
#("language in all lower case", length of the language string)
#[('python', 6), ('java', 4), ('javascript', 10), ('scala', 5)]
def trans_list(prog_lang):
    return tuple(zip(list(map(lambda x: x[0].lower(),prog_lang)),list(map(lambda x:len(str(x[0])),prog_lang))))
print(trans_list(prog_lang))
#6. Generate a tuple in the form,
#("All languages separated by commas","All versions separated by commas")
#('Python,Java,JavaScript,Scala', '3.8,13,2019,2.13')

def tupl_comma(prog_lang):
    return functools.reduce(lambda x,y: x+y, prog_lang)+functools.reduce(lambda x,y: y+x, prog_lang)
print(tupl_comma(prog_lang))