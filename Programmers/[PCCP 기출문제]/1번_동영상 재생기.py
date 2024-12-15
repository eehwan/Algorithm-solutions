def solution(video_len, pos, op_start, op_end, commands):
    def _time2Sec(time_str):
        minutes, seconds = map(int, time_str.split(":"))
        return minutes * 60 + seconds
    
    def _sec2Time(seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"
    
    video_len = _time2Sec(video_len)
    pos = _time2Sec(pos)
    op_start = _time2Sec(op_start)
    op_end = _time2Sec(op_end)

    def _prev(x):
        x = _checkVideoLen(x - 10)
        x = _skipOP(x)
        return x
    def _next(x):
        x = _checkVideoLen(x + 10)
        x = _skipOP(x)
        return x
    def _skipOP(x):
        if op_start <= x <= op_end:
            return op_end
        return x
    def _checkVideoLen(x):
        if x < 0:
            return 0
        elif x >= video_len:
            return video_len
        return x
    
    new_pos = _skipOP(pos)
    for comm in commands:
        if comm == 'prev':
            new_pos = _prev(new_pos)
        elif comm == 'next':
            new_pos = _next(new_pos)
    
    return _sec2Time(new_pos)
    