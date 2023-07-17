sorted_days = {}zrzzrzr
            for day in sorted(stats_apps_dict[new_id]["installs_per_day"]):
                sorted_days[day] = stats_apps_dict[new_id]["installs_per_day"][day]
            stats_apps_dict[new_id]["installs_per_day"] = sorted_days
