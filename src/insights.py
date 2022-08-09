from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    job_types = set()
    for job in jobs_list:
        job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    jobs_list = read(path)
    industries = set()
    for job in jobs_list:
        if job["industry"] != "":
            industries.add(job["industry"])
    return industries


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    jobs_list = read(path)
    salaries = set()
    errors = set()
    for job in jobs_list:
        try:
            salaries.add(int(job["max_salary"]))
        except ValueError:
            errors.add(job["max_salary"])
    return max(salaries)


def get_min_salary(path):
    jobs_list = read(path)
    salaries = set()
    errors = set()
    for job in jobs_list:
        try:
            salaries.add(int(job["min_salary"]))
        except ValueError:
            errors.add(job["max_salary"])
    return min(salaries)


def check_inputs(min_salary, max_salary, salary):
    if type(salary) != int and type(salary) != float:
        raise ValueError
    if type(min_salary) != int and type(min_salary) != float:
        raise ValueError
    if type(max_salary) != int and type(max_salary) != float:
        raise ValueError
    if min_salary > max_salary:
        raise ValueError


def matches_salary_range(job, salary):
    try:
        check_inputs(job["min_salary"], job["max_salary"], salary)
        return job["min_salary"] <= salary <= job["max_salary"]
    except KeyError:
        raise ValueError


def filter_by_salary_range(jobs, salary):
    filtered_list = list()
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_list.append(job)
        except ValueError:
            pass
    return filtered_list
