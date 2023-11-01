# Write your MySQL query statement below
SELECT Students.student_id, Students.student_name, Subjects.subject_name, IF(Examinations.subject_name is null, 0, count(*)) attended_exams
FROM Students
CROSS JOIN Subjects
LEFT JOIN Examinations ON Examinations.subject_name = Subjects.subject_name and Examinations.student_id = Students.student_id
GROUP BY Students.student_id, Subjects.subject_name
ORDER BY Students.student_id ASC
