import asyncio
from data.user_activity import UserActivity


async def s_track():
    user_activity = UserActivity()
    monitor_window = asyncio.create_task(user_activity.monitor_window())
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        monitor_window.cancel()
        print('interrupted')
    except Exception as e:
        print(f'EXCEPTION {e}')
try:
    asyncio.run(s_track())
except KeyboardInterrupt:
    print('leave')