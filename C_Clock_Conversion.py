t = int(input().strip())
for _ in range(t):
    raw_hours, raw_minutes = input().strip().split(':')
    pm = True
    if raw_hours[0] == '0' and raw_hours[1] == '0':
        hours  = 12
        pm = False
    elif raw_hours[0] == '0':
        hours = int(raw_hours[1])
    else:
        hours = int(raw_hours)
    
    
    if hours >= 12:
        if hours > 12:
            hours -= 12 
    else:
        pm = False 
    
    if pm:
        if hours < 10:
            print(f"0{hours}:{raw_minutes} PM")
        else:
            print(f"{hours}:{raw_minutes} PM")
    else:
        if hours < 10:
            print(f"0{hours}:{raw_minutes} AM")
        else:
            print(f"{hours}:{raw_minutes} AM")
        