eol_rebase = {
    "app.one.2": ["app.one.1"],
    "app.one.3": ["app.one.2"],
    "app.one.4": ["app.one.3"],
    "app.one.5": ["app.one.4"],
    "app.two.2": ["app.two.1"],
    "app.two.3": ["app.two.2"]
}


while True:
    found = False
    remove_list = []
    for app_id, old_id_list in eol_rebase.items():
        for new_app_id, check_id_list in eol_rebase.items():
            if app_id in check_id_list:
                eol_rebase[new_app_id] += old_id_list
                remove_list.append(app_id)
                found = True
    for i in remove_list:
        del eol_rebase[i]
    if not found:
        break


print(eol_rebase)
