# Алгоритм для произвольной БД с построением связей
# Компетенция - курс и курс - компетенция

def get_common_tags(tags1, tags2):
    common_tags = set(tags1).intersection(tags2)
    return common_tags, len(common_tags)

def get_linking_profession_to_competency(profession, set_of_competencies):
    matched_competencies = []
    for competency_id, competency in set_of_competencies.items():
        common_tags, weight = get_common_tags(profession['tags'], competency['tags'])
        if common_tags:
            matched_competencies.append(
                {'id': competency_id, 'name': competency['name'], 'tags': competency['tags'], 'weight': weight}
            )
    return matched_competencies

def get_linking_competency_to_course(competency, set_of_courses):
    matched_courses = []
    for course_id, course in set_of_courses.items():
        common_tags, weight = get_common_tags(competency['tags'], course['tags'])
        if common_tags:
            matched_courses.append(
                {'id': course_id, 'name': course['name'], 'tags': course['tags'], 'weight': weight, 'competency': competency, 'discipline_id': course['discipline_id']}
            )
    return matched_courses

def recommend_courses(profession_id, competencies, courses, discipline_id=None): # по умолчанию будем обозначать, что фильтра нет
    profession = professions[profession_id]
    matched_competencies = get_linking_profession_to_competency(profession, competencies)

    all_matched_courses = []
    for competency in matched_competencies:
        matched_courses = get_linking_competency_to_course(competency, courses)

        if discipline_id: # если был передан фильтр(на данный момент на принадлежность курсов дисциплине)
            matched_courses = list(filter(lambda x: x['discipline_id'] == discipline_id, matched_courses)) # проверяем, что в данной дисциплине есть ссылка на id курса
        for match_course in matched_courses:
            match_course['weight'] += competency['weight']
        all_matched_courses.extend(matched_courses)
    return sorted(all_matched_courses, key=lambda x: x['weight'], reverse=True)

def recommend_courses_for_profession(profession_id, competencies, courses):
    return recommend_courses(profession_id, competencies, courses)

#в рамках дисциплины должны выбрать наиболее подходящий из связанных с ней курсов
def recommend_course_for_discipline(discipline_id, profession_id, competencies, courses):
    return recommend_courses(profession_id, competencies, courses, discipline_id=discipline_id)

professions = {
    1: {'name': 'Data Scientist', 'tags': ['python', 'statistics', 'machine learning', 'programming basics', 'data analysis']},
    2: {'name': 'Web Developer', 'tags': ['html', 'css', 'javascript', 'react']},
    3: {'name': 'Backend Go Developer', 'tags': ['go']}
}

competencies = {
    1: {'name': 'Python Programming', 'tags': ['python', 'data analysis']},
    2: {'name': 'Frontend Development', 'tags': ['html', 'css', 'javascript']},
    3: {'name': 'Backend Development', 'tags': ['database']},
    4: {'name': 'Base Programming', 'tags': ['programming basics']},
    5: {'name': 'Data Science', 'tags': ['machine learning', 'statistics', 'data analysis']},
}

courses = {
    1: {'name': 'Introduction to Python', 'tags': ['programming basics'], 'discipline_id': None},
    2: {'name': 'Advanced Web Development', 'tags': ['javascript', 'react', 'html'], 'discipline_id': 1},
    3: {'name': 'Data Science Course', 'tags': ['python', 'machine learning', 'statistics', 'data analysis'], 'discipline_id': 1},
}

disciplines = {
    1: {'name': 'Современные языки программирования'}
}

# Тестируем функцию
profession_id = int(input('Id of the profession: '))
recommended_courses = recommend_courses_for_profession(profession_id, competencies, courses)

# Выводим список рекомендованных курсов
print(f'Профессия: {professions[profession_id]['name']}')
for recommended_course in recommended_courses:
    print(f"Компетенция: {recommended_course['competency']['name']}, Курс: {recommended_course['name']}, Вес: {recommended_course['weight']}")

print()

discipline_id = int(input('Id of the discipline: '))
discipline_courses = recommend_course_for_discipline(discipline_id, profession_id, competencies, courses)

print(f'Дисциплина: {disciplines[discipline_id]['name']}')
for discipline_course in discipline_courses:
    print(f"Курс: {discipline_course['name']} в рамках компетенции {discipline_course['competency']['name']} с весом {discipline_course['weight']}")