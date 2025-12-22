import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from data.tg_bot.requests import DBC

matplotlib.use('Agg')
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
        times_ = (await req.get_info(tg_id, 'user_info'))[:, 1]
        times_s_ = await req.get_time(tg_id, 'user_info')
        # indices = np.argsort(times_)

        plt.title('Top 10 most used apps')
        plt.bar(range(len(times_)), times_,
                align='center', width=0.5)
        plt.xticks(range(len(apps_)), apps_, rotation=90)
        plt.yticks(range(len(times_)), times_s_)
        plt.ylabel('Used time')
        plt.tight_layout()
        plt.savefig('t10.png')

    async def total(self, tg_id):
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

        plt.plot(range(len(days_)),
                 (await req.get_info(tg_id, 'total_info')))
        plt.xticks(range(len(days_)), days_, rotation=90)
        plt.ylabel('Total time')
        plt.tight_layout()
        plt.savefig('total_s_p.png')
