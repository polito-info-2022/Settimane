def cube_volume(side_length):
    """
    Calcola il volume di un cubo

    :param side_length: lato del cubo
    :return: volume calcolato
    """
    volume = side_length ** 3
    return volume


lato = 3
vol = cube_volume(lato)
print(f'Il volume di un cubo di lato {lato} è pari a {vol}')
vol2 = cube_volume(lato*2)
print(vol2)

