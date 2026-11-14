def maximum(a, b):
    if a >= b:
        return a
    return b


def est_pair(n):
    
    return n % 2 == 0


def moyenne(notes):
    
    if not notes:
        return None
    return sum(notes) / len(notes)


if __name__ == "__main__":
    assert maximum(4, 7) == 7
    assert maximum(9, 2) == 9
    assert maximum(5, 5) == 5

    assert est_pair(8) is True
    assert est_pair(7) is False
    assert est_pair(-4) is True

    assert moyenne([10, 15, 20]) == 15
    assert moyenne([]) is None

    print("Tous les tests sont réussis.")
