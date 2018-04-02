"""
Q: Given a dictionary that contains mapping of employee and his manager as a number
of (employee, manager) pairs like below.
{ "A", "C" },
{ "B", "C" },
{ "C", "F" },
{ "D", "E" },
{ "E", "F" },
 {“G”, “D”}
{ "F", "F" }

In this example C is manager of A,
C is also manager of B, F is manager
of C and so on.
Write a function to get names of all employees under each manager in the hierarchy
not just their direct reports. It may be assumed that an employee directly reports
to only one manager. In the above dictionary the root node/ceo is listed as
reporting to himself.
Output should be a Dictionary that contains following.
A - []
B - []
C - [A, B]
D - [G]
E - [D, G]
F - [A, B, C, D, E, G]
G - []

"""


def get_direct_emps_under_mgrs(emp_dict):
    mans_dir_emps = dict()
    for emp, man in emp_dict.items():
        if emp != man:
            mans_dir_emps.setdefault(man, []).append(emp)
    return mans_dir_emps


def all_emps_under_single_mgr(man, direct_emps_under_mgrs, result, man_emp):
    """

    :param mgr: string
        Particular manager under whom we want to find all employees.
    :param direct_emps_under_mgrs: directory
        Directory holding all direct employees under all managers.
        {'C': ['A', 'B'], 'F': ['C', 'E', 'F'], 'E': ['D'], 'D': ['G']}
    : param result: list
        All reporting employees
    :return:
    """
    if man not in direct_emps_under_mgrs:
        print("Here for %s" % man)
        return
    else:
        for emp in direct_emps_under_mgrs[man]:
            result.append(emp)
            all_emps_under_single_mgr(emp, direct_emps_under_mgrs, result, man_emp)


def employes_under_manager(emp_dict):
    direct_emps_under_mgrs = get_direct_emps_under_mgrs(emp_dict)
    man_emp = dict()
    for emp in emp_dict.keys():
        result = []
        all_emps_under_single_mgr(emp, direct_emps_under_mgrs, result, man_emp)
        man_emp[emp] = result
        print("********* %s" % man_emp)
    return man_emp


if __name__ == "__main__":
    emp_dict = {"A": "C", "B": "C", "C": "F", "D": "E", "E": "F", "G": "D",
                     "F": "F"}
    print(employes_under_manager(emp_dict))
