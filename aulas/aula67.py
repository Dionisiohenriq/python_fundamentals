def soma(x, y, z=None):
    """_summary_

    Args:
        x (_type_): _description_
        y (_type_): _description_
        z (int, optional): _description_. Defaults to 0.
    """
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)
        

soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)