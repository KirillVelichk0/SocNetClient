
def LoadNextForm(next_instanse, cur_instanse):
    cur_instanse[0].DestroyMenu(cur_instanse)
    cur_instanse[0] = next_instanse
    cur_instanse[0].CreateMenu(cur_instanse)
    return None