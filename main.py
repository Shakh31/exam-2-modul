from functions import register, log_in, add_todo, remove_todo, update_todo

k = int(input("Sign up/in(0/1): "))

if k == 0:
    register()
else:
    log_in()
