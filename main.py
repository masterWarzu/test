x = input("Введите выражение для вычисления без пробелов и нажмите Enter: ")

compiled_expression = compile(x, "string", "eval")

print(eval(compiled_expression))