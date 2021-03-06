def test_get_classes_full(class_info):
    (classes_full, err) = class_info.get_classes_full()

    crns = []
    for row in classes_full:
        for section in row['sections']:
            if section and section['crn']:
                crns.append(section['crn'])

    assert len(crns) == len(set(crns))
