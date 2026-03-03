def outer_scope():
    my_enclosing_var = "enclosing"


    def inner_scope():
        my_inner_var = "inner"

        print(my_enclosing_var)

module_scope = "global"