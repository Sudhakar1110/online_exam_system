import frappe

@frappe.whitelist()
def get_exam_questions(exam_name):
    questions = frappe.get_all(
        "Question",
        filters={"exam": exam_name},
        fields=[
            "question",
            "option_a",
            "option_b",
            "option_c",
            "option_d",
            "correct_answer",
            "marks"
        ]
    )

    return questions


@frappe.whitelist()
def submit_exam(student, exam, score):

    doc = frappe.get_doc({
        "doctype": "Exam Attempt",
        "student": student,
        "exam": exam,
        "score": score,
        "status": "Completed"
    })

    doc.insert(ignore_permissions=True)
    frappe.db.commit()

    return {
        "message": "Exam Submitted Successfully"
    }
