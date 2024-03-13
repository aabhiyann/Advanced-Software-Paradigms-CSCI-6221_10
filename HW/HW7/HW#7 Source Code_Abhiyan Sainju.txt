% Instructions:
% 1. Load students grades:
%    Use the predicate load_students_grades to load a list of student grades.
%    Example: load_students_grades([['John Smith',100,100,100,100,100,100],['Marry Lou',90,90,90,90,90,90],['Nicole Scott',85,85,80,80,80,80]]).
% 2. Show a students grade:
%    Use the predicate show_student_grade to display a specific student grade.
%    Example: show_student_grade('Nicole Scott').

% 3. Show all students with a specific grade:
%    Use the predicate show_allstudents to display all students with a specific grade.
%    Example: show_allstudents('A').


% Define the grading scale (facts)
point_letter(90, 'A').
point_letter(85, 'A-').
point_letter(80, 'B+').
point_letter(75, 'B').
point_letter(70, 'B-').
point_letter(65, 'C+').
point_letter(60, 'C').
point_letter(1, 'F').

% Predicate to load students grades
load_students_grades(StudentsGrades) :-
    insert_students_grades(StudentsGrades).

% Predicate to insert students grades
insert_students_grades([]).
insert_students_grades([[Student, HW1, HW2, HW3, MidTerm, Final, Project]|Other]) :-
    assertz(student_grade(Student, HW1, HW2, HW3, MidTerm, Final, Project)),
    insert_students_grades(Other).

% Predicate to calculate the overall score
calculate_overall_score(HW1, HW2, HW3, MidTerm, Final, Project, OverallScore) :-
    TotalHW is (HW1 + HW2 + HW3) / 3,
    TotalExam is (MidTerm + Final) / 2,
    OverallScore is 0.2 * TotalHW + 0.4 * TotalExam + 0.4 * Project.

% Predicate to convert point grade to letter grade
overallscore_to_letter_grade(PointGrade, LetterGrade) :-
    point_letter(Score, LetterGrade),
    PointGrade >= Score,
    \+ (point_letter(NextScore, _), PointGrade >= NextScore, NextScore > Score).

% Predicate to query a students letter grade by name
show_student_grade(Student) :-
    student_grade(Student, HW1, HW2, HW3, MidTerm, Final, Project),
    calculate_overall_score(HW1, HW2, HW3, MidTerm, Final, Project, OverallScore),
    overallscore_to_letter_grade(OverallScore, Grade),
    format('~w: ~w~n', [Student, Grade]).

% Predicate to query students by letter grade
show_allstudents(Grade) :-
    findall(Student, (student_grade(Student, HW1, HW2, HW3, MidTerm, Final, Project),
                      calculate_overall_score(HW1, HW2, HW3, MidTerm, Final, Project, OverallScore),
                      overallscore_to_letter_grade(OverallScore, Grade)),
            StudentsWithGrade),
    (   StudentsWithGrade = []
    ->  format('No students have a letter grade of ~w~n', [Grade])
    ;   forall(member(Student, StudentsWithGrade),
               format('~w: ~w~n', [Student, Grade]))
    ).


