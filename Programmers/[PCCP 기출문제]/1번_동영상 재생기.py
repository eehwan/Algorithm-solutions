def solution(video_len, pos, op_start, op_end, commands):
    def _time_to_sec(time_str):
        """Convert time in 'MM:SS' format to seconds."""
        minutes, seconds = map(int, time_str.split(":"))
        return minutes * 60 + seconds

    def _sec_to_time(seconds):
        """Convert seconds to 'MM:SS' format."""
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"

    # Convert all times to seconds
    video_len = _time_to_sec(video_len)
    current_pos = _time_to_sec(pos)
    op_start = _time_to_sec(op_start)
    op_end = _time_to_sec(op_end)

    def _adjust_position(position):
        """Adjust position based on video length and oppening range."""
        # Ensure the position is within the video length
        position = max(0, min(position, video_len))
        # Apply the oppening skip (if within range, move to op_end)
        if op_start <= position <= op_end:
            position = op_end
        return position

    def _move_position(position, delta):
        """Move the position by a delta (positive or negative)."""
        return _adjust_position(position + delta)

    # Apply the initial position adjustment based on the oppening range
    current_pos = _adjust_position(current_pos)

    # Process each command ('prev' -> -10 seconds, 'next' -> +10 seconds)
    for command in commands:
        if command == 'prev':
            current_pos = _move_position(current_pos, -10)
        elif command == 'next':
            current_pos = _move_position(current_pos, 10)

    # Return the final position in 'MM:SS' format
    return _sec_to_time(current_pos)
