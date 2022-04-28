import json

__data = []


def load_candidates_from_json(path):
    """

    :return:
    """
    global __data
    with open(path, 'r', encoding='utf-8') as file:
        __data = json.load(file)
    return __data


def get_candidate(candidate_id):
    """
Ищет кандидата по ID и возвращает словарь с информацие о кандидате

    """
    for candidate in __data:
        if candidate['id'] == candidate_id:
            return {
                'name': candidate['name'],
                'position': candidate['position'],
                'picture': candidate['picture'],
                'skills': candidate['skills'],
            }
    return {'not_found': 'не найдено'}

def get_candidates_by_name(candidate_name: str):
    """
    Ищет ккандидатов по имени и возврвщвет список со словарями найденых кандидатов
    через списковое включение
    """
    return [candidate for candidate in __data if candidate_name.lower() in candidate['name'].lower()]


def get_candidates_by_skill(skill_name: str):
    candidates = []
    for candidate in __data:
        skills = candidate['skills'].lower().split(', ')
        if skill_name.lower() in skills:
            candidates.append(candidate)
    return candidates