import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from data.tg_bot.requests import DBC
from data.classification.help_functions import time_formatter, week_days
import numpy as np
from datetime import date, timedelta


req = DBC()

class Statistic:
    async def general(self, tg_id):
        await req.create_pool()
        categories_ = (await req.categories(tg_id, 'user_info'))

        plt.title('General statistic')
        plt.bar(range(len(categories_)), categories_,
                align='center')
        plt.xticks(range(len(categories_)), categories_, rotation=90)
        plt.ylabel('Used time')
        plt.tight_layout()
        plt.savefig('general_s.png')

    async def top10(self, tg_id):
        await req.create_pool()
        apps_ = (await req.get_info(tg_id, 'user_info'))[:, 0]
        times_ = np.array([int(t) for t in (await req.get_info(tg_id, 'user_info'))[:, 1]])
        times_s_ = await req.get_time(tg_id, 'user_info')
        indices = np.argsort(times_)[::-1]

        fig, ax = plt.subplots()

        bars = ax.bar(apps_[indices], times_[indices])

        ax.yaxis.set_major_formatter(ticker.FuncFormatter(time_formatter))

        plt.title('Топ 10 используемых приложений')
        plt.ylabel('Затраченное время')
        plt.tight_layout()
        plt.savefig('t10.png')
        plt.close()

    async def week_d(self, tg_id):
        day_ = date.today()
        day_l_, day_d = week_days(day_)
        times_ = await req.get_info(tg_id, day_)
        times_l_ = np.array([str(timedelta(seconds=t)) for t in times_])

        plt.plot(range(len(day_d)), times_)
        plt.fill_between(range(len(day_d)), times_, color='blue', alpha=0.3)
        plt.yticks(range(len(times_l_)), times_l_)
        plt.ylabel('Затраченное время')
        plt.xlabel('Дата')
        plt.title('Статистика по дням')
        plt.tight_layout()
        plt.savefig('week_d.png')
        plt.close()


    async def week_c(self, tg_id):
        await req.create_pool()
        categories_ = (await req.categories(tg_id, 'total_info'))
        days_ = (await req.get_days(tg_id))

        plt.title('Total statistic')
        plt.bar(range(len(categories_)),
                categories_, align='center')
        plt.xticks(range(len(categories_)), categories_, rotation=90)
        plt.ylabel('Used time')
        plt.tight_layout()
        plt.savefig('total_s_b.png')
        plt.close()

        plt.plot(range(len(days_)),
                 (await req.get_info(tg_id, 'total_info')))
        plt.xticks(range(len(days_)), days_, rotation=90)
        plt.ylabel('Total time')
        plt.tight_layout()
        plt.savefig('total_s_p.png')
        plt.close()
