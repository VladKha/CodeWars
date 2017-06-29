def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) / 3
    return {90 <= score <= 100:	'A',
            80 <= score < 90:   'B',
            70 <= score < 80:	'C',
            60 <= score < 70:   'D',
            0  <= score < 60:	'F'}[True]
