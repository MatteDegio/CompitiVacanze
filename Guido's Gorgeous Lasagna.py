# Definire il tempo di cottura previsto in minuti
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

# 
def bake_time_remaining(elapsed_bake_time: int) -> int:
    """
    Calcola il tempo di cottura rimanente in minuti
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """
    Calcola il tempo di preparazione in minuti
    """ 
    return PREPARATION_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """
    Calcolare il tempo di cottura totale trascorso (preparazione + cottura) in minuti
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
