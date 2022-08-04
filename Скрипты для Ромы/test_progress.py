class progress_bar_ilin():
    from time import sleep
    def Progress(it, pr):
        a = (pr / it) * 100
        if a >= 0 and a < 10:
            print(f"Progress: |                    |{int(a)}%", end='\r')
        if a >= 10 and a < 20:
            print(f"Progress: |██                  |{int(a)}%", end='\r')
        if a >= 20 and a < 30:
            print(f"Progress: |████                |{int(a)}%", end='\r')
        if a >= 30 and a < 40:
            print(f"Progress: |██████              |{int(a)}%", end='\r')
        if a >= 40 and a < 50:
            print(f"Progress: |████████            |{int(a)}%", end='\r')
        if a >= 50 and a < 60:
            print(f"Progress: |██████████          |{int(a)}%", end='\r')
        if a >= 60 and a < 70:
            print(f"Progress: |████████████        |{int(a)}%", end='\r')
        if a >= 70 and a < 80:
            print(f"Progress: |██████████████      |{int(a)}%", end='\r')
        if a >= 80 and a < 90:
            print(f"Progress: |████████████████    |{int(a)}%", end='\r')
        if a >= 90 and a < 100:
            print(f"Progress: |██████████████████  |{int(a)}%", end='\r')
        if a == 100:
            print(f"Progress: |████████████████████|{int(a)}%", end='\r')
