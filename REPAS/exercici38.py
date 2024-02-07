contactes = {'Roger':678232311, 'Oriol':566879326}

def elimina(contactes, user):
    try:
        del contactes[user]
        return contactes
    except:
        return contactes

print(elimina(contactes, 'Pablo'))

"""
L4. "del" da error porque no existe la key Pablo. se soluciona con un try except.
L5. el return no debe ser el valor eliminado, sino la lista modificada
(si quisieras eliminar el registro de Pablo pero printear el teléfono, el método seria pop() )

"""
