#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name = "John", job ="Admin"):
        self.set_name(name)
        self.set_job(job)
    
    def set_name(self, name):
        if not isinstance(name, str) or len(name) <= 0 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = name.title()

    def set_job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    def get_name(self):
        return self._name
    
    def get_job(self):
        return self._job

    name = property(get_name, set_name)
    job = property(get_job, set_job)
