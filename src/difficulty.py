def difficulty_level(language):

    if language == 'Japanese':
        jlpt_levels = ['N5', 'N4', 'N3', 'N2', 'N1']
        print('Select the JLPT difficulty level you want to practice:')
        for idx, level in enumerate(jlpt_levels, 1):
            print(f'{idx}. {level}')
        while True:
            jlpt_choice = input('Enter the number corresponding to the JLPT level: ')
            if jlpt_choice.isdigit() and 1 <= int(jlpt_choice) <= len(jlpt_levels):
                difficulty = jlpt_levels[int(jlpt_choice) - 1]
                break
            else:
                print('Invalid option. Please try again.')
    else:
        print('No specific difficulty level selected.')
        exit()

    return difficulty