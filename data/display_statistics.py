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
        indices = np.argsort(times_)[::-1]

        fig, ax = plt.subplots()

        bars = ax.bar(apps_[indices], times_[indices])

        ax.yaxis.set_major_formatter(ticker.FuncFormatter(time_formatter))

        plt.ylim(bottom=0)
        if max(times_, default=0) > 0:
            plt.ylim(top=max(times_) * 1.2)

        plt.title('Топ 10 используемых приложений')
        plt.ylabel('Затраченное время')
        plt.tight_layout()
        plt.savefig('t10.png')
        plt.close()

    async def week_d(self, tg_id):
        await req.create_pool()
        day_ = date.today()
        day_l_, day_d = week_days(day_)
        times_ = await req.get_info(tg_id, 'total_info', day_)

        fig = plt.figure(figsize=(10, 6))

        plt.plot(range(len(day_d)), times_, marker='o', color='blue')
        plt.fill_between(range(len(day_d)), times_, color='blue', alpha=0.3)

        plt.xticks(range(len(day_d)), day_l_, rotation=90)

        ax = plt.gca()
        ax.yaxis.set_major_formatter(ticker.FuncFormatter(time_formatter))
        plt.ylim(bottom=0)
        if max(times_, default=0) > 0:
            plt.ylim(top=max(times_) * 1.2)

        plt.ylabel('Затраченное время')
        plt.title('Статистика за неделю')
        plt.grid(True, linestyle='--', alpha=0.6)

        plt.tight_layout()
        plt.savefig('week_d.png')
        plt.close()


    async def week_c(self, tg_id):
        await req.create_pool()
        times_ = await req.get_time_catgrs(tg_id, 'total_info')
        catgrs_ = np.unique(await req.categories(tg_id, 'total_info'))

        fig = plt.figure(figsize=(10, 6))

        plt.bar(range(len(catgrs_)), times_)
        plt.xticks(range(len(catgrs_)), catgrs_)

        ax = plt.gca()
        ax.yaxis.set_major_formatter(ticker.FuncFormatter(time_formatter))
        plt.ylim(bottom=0)
        if max(times_, default=0) > 0:
            plt.ylim(top=max(times_) * 1.2)

        plt.title('Статистика по категориям')
        plt.xlabel('Категории')
        plt.ylabel('Затраченное время')

        plt.tight_layout()
        plt.savefig('week_c.png')
        plt.close()
