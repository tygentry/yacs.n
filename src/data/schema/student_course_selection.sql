DROP TABLE student_course_selection;
CREATE TABLE student_course_selection(
	user_id LONG INT,
	semester varchar(255),
	crn varchar(255);

	primary key(user_id, semester)
);	