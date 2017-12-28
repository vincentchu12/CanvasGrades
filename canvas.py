from canvasapi import Canvas
from config import API_KEY, API_URL, SIS_ID, ID_TYPE

canvas = Canvas(API_URL, API_KEY)

user = canvas.get_user(SIS_ID, ID_TYPE)

user_id = user.id

all_courses = user.get_courses()

for c in all_courses:
    try:
        if c.access_restricted_by_date == True: # old course
            pass
    except AttributeError:
        if c.enrollments[0]['type'] == 'student':
            course_id = c.id
            course_name = c.name
            assignments = c.get_assignments()
            assignment_groups = c.list_assignment_groups()
            print(course_name)
            for group in assignment_groups:
                group_id = group.id
                group_name = group.name
                group_weight = group.group_weight                
                print("{}: {}%".format(group_name.upper(), group_weight))
                for assignment in assignments:
                    if(assignment.assignment_group_id == group.id):
                        assignment_id = assignment.id
                        assignment_name = assignment.name
                        assignment_points = assignment.points_possible
                        submission = c.get_submission(assignment_id, user_id)
                        submission_status = submission.workflow_state
                        submission_score = submission.score
                        if submission_status == 'unsubmitted':
                            pass
                        elif submission_status == 'submitted':
                            pass
                        elif submission_status == 'graded':
                            pass
                        elif submission_status == 'pending_review':
                            pass
                        print("{} ({}/{})".format(assignment_name, submission_score, assignment_points))
                print()
            print()

    
    #     print(c.enrollemnts[0]['role'])
    #     #print(repr(c))
    #     # for group in c.list_assignment_groups():
    #     #     print("{}: Weight {}%".format(group.name, group.group_weight))
    #     #     for assignment in c.get_assignments():
    #     #         print(assignment.name, assignment.assignment_group_id, assignment.points_possible)
    #     # print('\n')
    # except:
    #     pass
