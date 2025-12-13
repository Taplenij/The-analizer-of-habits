import matplotlib.pyplot as plt
import matplotlib

from data.classification.data_clf import categories
from data.tg_bot.requests import DBC

matplotlib.use('Agg')
req = DBC()

class Statistic:
    async def general(self, tg_id, categories):
        plt.title('General statistic')
        plt.bar(range(len(categories)), (await req.category_time(tg_id)), align='center')
        plt.xticks(range(len(categories)), categories, rotation=90)
        plt.ylabel('Used time')
        plt.tight_layout()
        plt.savefig('general_stats.png')

    async def top10(self, tg_id, apps):
        plt.title('Top 10 most used apps')
        plt.bar(range(len(apps)), (await req.get_info(tg_id))[:, 1], align='center')
        plt.xticks(range(len(apps)), apps, rotation=90)
        plt.ylabel('Used time')
        plt.tight_layout()
        plt.savefig('top10.png')

    async def total(self):
        pass