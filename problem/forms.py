from django import forms


class ProblemForm(forms.Form):
    default_input = "46B E59 EA C1F 45E 63\n" \
                    "899 FFF 926 7AD C4E FFF\n" \
                    "E2E 323 6D2 976 83F C96\n" \
                    "9E9 A8B 9C1 461 F74 D05\n" \
                    "EDD E94 5F4 D1D D03 DE3\n" \
                    "89 925 CF9 CA0 F18 4D2"

    problem_input = forms.CharField(widget=forms.Textarea,
                                    initial=default_input)

    def is_valid(self):
        valid = super(ProblemForm, self).is_valid()
        if not valid:
            return valid
        problem_input = self.cleaned_data['problem_input']

        return validate_input(problem_input)


def validate_input(problem_input):
    """
    Validate the input matrix
    :param problem_input:
    :return: True if input is valid and can be parsed
    """
    rows = problem_input.splitlines()
    for idx, row in enumerate(rows):
        rows[idx] = row.split()

        for val in rows[idx]:
            try:
                int(val, 16)  # change to base 10
            except ValueError:
                return False

    # check if all rows have same size
    row_size = len(rows[0])
    for row in rows:
        if row_size != len(row):
            return False

    return True
