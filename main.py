from reptile import Reptile
import matplotlib.pyplot as plt

if __name__ == '__main__':
    target_url = "https://data.stats.gov.cn/easyquery.htm?cn=A01"

    reptile = Reptile()
    reptile.crawling(target_url, '//*[@id="treeZhiBiao_2_span"]', '//*[@id="treeZhiBiao_18_span"]',
                     '//*[@id="treeZhiBiao_32_span"]')

    fig, ax = plt.subplots(figsize=(16, 8))
    for i in range(0, len(reptile.name_list)):
        ax.plot(reptile.head_list, reptile.data_list[i], label=reptile.name_list[i])
    ax.legend()

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来显示中文
    plt.title('消费价格指数')
    plt.savefig('fig.png')
    plt.show()
