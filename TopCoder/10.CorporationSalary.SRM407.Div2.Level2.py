class CorporationSalary:
    def total_salary(self, relations):
        members = self.convert_relations(relations)
        salaries = [0 for _ in members]
        while 0 in salaries:
            for i, v in enumerate(salaries):
                if v == 0:
                    if len(members[i]) == 0:
                        salaries[i] = 1
                    else:
                        member_salary = [salaries[j] for j in members[i]]
                        if not 0 in member_salary:
                            salaries[i] = sum(member_salary)
        return(sum(salaries))

    def convert_relations(self, string_array):
        result = [[] for _ in string_array]
        for i, line in enumerate(string_array):
            for j, v in enumerate(line):
                if v == 'Y':
                    result[i].append(j)
        return result;

cor = CorporationSalary()

problems = [["N"],
            ["NNYN", "NNYN", "NNNN", "NYYN"],
            ["NNNNNN","YNYNNY","YNNNNY","NNNNNN","YNYNNN","YNNYNN"],
            ["NYNNYN","NNNNNN","NNNNNN","NNYNNN","NNNNNN","NNNYYN"],
            ["NNNN","NNNN","NNNN","NNNN"]]

for one in problems:
    print(cor.total_salary(one))