def fuse_events(api_events, video_events):

    all_events = api_events + video_events

    unique_events = []

    seen = set()

    for event in all_events:

        event_key = (
            event["match_id"],
            event["event_type"],
            event["minute"],
            event["description"]
        )

        if event_key not in seen:
            seen.add(event_key)
            unique_events.append(event)

    unique_events.sort(key=lambda event: event["minute"])

    return unique_events