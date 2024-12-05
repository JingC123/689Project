import os
from leetcode_env.environment import LeetCodeEnv
from leetcode_env.types import LeetCodeSubmission, ProgrammingLanguage

leetcode_session = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMjU0NTY3OSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImIyZTFjNDg0OTI0NTIxNmU0MzVlYmI0YzdlZTIyZjgxNWJhZDU4OGIxNDQ3ZGUzYzk2MmVmOTY1ZmU2OWY3YWQiLCJpZCI6MjU0NTY3OSwiZW1haWwiOiJqaW5nY2FvMjMzM0BnbWFpbC5jb20iLCJ1c2VybmFtZSI6ImppbmdjYW8yMzMzIiwidXNlcl9zbHVnIjoiamluZ2NhbzIzMzMiLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS5jb20vdXNlcnMvamluZ2NhbzIzMzMvYXZhdGFyXzE1Nzg1MjQyNTQucG5nIiwicmVmcmVzaGVkX2F0IjoxNzI5MjE5MzUwLCJpcCI6IjE2NS45MS4xMy4zOCIsImlkZW50aXR5IjoiMTY0NTNkNmUyNjgzYjg4MDBkZWQyYTI3YzdmNTk1ZDkiLCJzZXNzaW9uX2lkIjo3NTcwOTk5MCwiZGV2aWNlX3dpdGhfaXAiOlsiOTg2MTQzMzY5YmQyZDRmNzU4NzJhYzg4YzE0Y2ExMmEiLCIxNjUuOTEuMTMuMzgiXX0._TLShqyZF_nNq8UD3_g1YR2CUFLhJhowJXoowYDyl4Q"
csrf_token ="mrpa7bjpXBtAeTMY2NR4T9p0pTy2QPwEtMmahGSqAMoYqPzCtzYvNOXm4eXG2uAb"
class LeetCodeTester(object):

    def __init__(self):
        self.env = LeetCodeEnv(cooldown=15, leetcode_session=leetcode_session, csrf_token=csrf_token)
        self.lang_dict = {
            "python3": ProgrammingLanguage.PYTHON3,
            "java": ProgrammingLanguage.JAVA,
            "cpp": ProgrammingLanguage.CPP,
        }

    def test(self, code: str, task_id: str, language: str) -> tuple[bool, dict]:
        lang = self.lang_dict.get(language)
        sub = LeetCodeSubmission(code=code, lang=lang, question_slug=task_id)
        status, reward, done, submission_result = self.env.step(sub)
        return reward, submission_result

if __name__ == '__main__':

    tester = LeetCodeTester()
    task_id = "make-number-of-distinct-characters-equal"
    code = "class Solution:\n\n    def insertAndRemove(self, mp, toInsert..."  # abbreviated
    print(tester.test(code, task_id, "python3"))