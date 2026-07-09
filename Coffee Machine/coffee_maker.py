from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name", ["pikachu","squitle","charmder"])
table.add_column("type", ["electric","water","fire"])
table.align = "r"
print(table)