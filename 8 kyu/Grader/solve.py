def grader(score):
    return {score < 0.6 or score > 1: 'F',
            0.9 <= score <= 1: 'A',
            0.8 <= score < 0.9: 'B',
            0.7 <= score < 0.8: 'C',
            0.6 <= score < 0.7: 'D'}[True]
