class Show:
    def __init__(self, name, start_time, end_time):
        if start_time >= end_time:
            raise ValueError("End time must be after start time")
        self.name = name
        self.start_time = start_time
        self.end_time = end_time

def calculate_stages(show_list):
    show_list.sort(key=lambda p: (p.start_time, p.end_time))
    ongoing_shows = []
    stage_mapping = {}
    stage_count = 0

    for show in show_list:
        ongoing_shows = [p for p in ongoing_shows if p[0] > show.start_time]

        if len(ongoing_shows) < stage_count:
            assigned_stage = len(ongoing_shows) + 1
        else:
            stage_count += 1
            assigned_stage = stage_count

        stage_mapping[show.name] = assigned_stage
        ongoing_shows.append((show.end_time, assigned_stage))

    return stage_count, stage_mapping

def main():
    shows = [
        Show('show_1', 36, 39),
        Show('show_2', 30, 33),
        Show('show_3', 29, 36),
        Show('show_4', 26, 30),
        Show('show_5', 15, 20),
        Show('show_6', 8, 15),
        Show('show_7', 2, 9),
        Show('show_8', 30, 34),
        Show('show_9', 1, 9),
        Show('show_10', 20, 28),
        Show('show_11', 1, 4),
        Show('show_12', 2, 11),
        Show('show_13', 26, 29),
        Show('show_14', 5, 10),
        Show('show_15', 37, 44),
        Show('show_16', 27, 35),
        Show('show_17', 37, 39),
        Show('show_18', 4, 10),
        Show('show_19', 35, 44),
        Show('show_20', 22, 30),
        Show('show_21', 15, 20),
        Show('show_22', 42, 46),
        Show('show_23', 6, 9),
        Show('show_24', 19, 23),
        Show('show_25', 31, 38),
        Show('show_26', 37, 41),
        Show('show_27', 30, 36),
        Show('show_28', 14, 21),
        Show('show_29', 5, 13),
        Show('show_30', 33, 36)
    ]

    total_stages, stage_mapping = calculate_stages(shows)

    print(f"Total stages needed: {total_stages}")
    print("Show Schedule:")
    for show_name, stage in stage_mapping.items():
        print(f"{show_name} -> Stage {stage}")

if __name__ == "__main__":
    main()
