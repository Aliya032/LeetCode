
# Write your MySQL query statement below
select
    s1.student_id,
    s1.student_name,
    su1.subject_name,
    count(e1.subject_name) as attended_exams
from
     Students s1
cross join
    Subjects su1
left join
    Examinations e1
on
    s1.student_id = e1.student_id and su1.subject_name = e1.subject_name
group by
    su1.subject_name, s1.student_id
order by
    s1.student_id,
    su1.subject_name;

