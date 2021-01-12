import sys
from datetime import datetime
from jd_spider_requests import JdSeckill
from jd_logger import logger
from util import send_wechat


if __name__ == '__main__':
    a = """

       oooo oooooooooo.            .oooooo..o                     oooo         o8o  oooo  oooo  
       `888 `888'   `Y8b          d8P'    `Y8                     `888         `"'  `888  `888  
        888  888      888         Y88bo.       .ooooo.   .ooooo.   888  oooo  oooo   888   888  
        888  888      888          `"Y8888o.  d88' `88b d88' `"Y8  888 .8P'   `888   888   888  
        888  888      888 8888888      `"Y88b 888ooo888 888        888888.     888   888   888  
        888  888     d88'         oo     .d8P 888    .o 888   .o8  888 `88b.   888   888   888  
    .o. 88P o888bood8P'           8""88888P'  `Y8bod8P' `Y8bod8P' o888o o888o o888o o888o o888o 
    `Y888P                                                                                                                                                  
                                               
功能列表：                                                                                
 1. 预约商品
 2. 秒杀抢购商品
 3. login
 4. print item name and link
 5. send wechat message
    """
    print(a)

    jd_seckill = JdSeckill()
    choice_function = input('请选择:')
    if choice_function == '1':
        jd_seckill.reserve()
    elif choice_function == '2':
        jd_seckill.seckill_by_proc_pool()
    elif choice_function == '3':
        jd_seckill.login_by_qrcode()
    elif choice_function == '4':
        logger.info('Iteam.name: {}'.format(jd_seckill.get_sku_title()))
        link = jd_seckill.get_seckill_url()
        logger.info('Item.link: %s', link)
    elif choice_function == '5':
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.info('Sending message to wechat')
        send_wechat('A test message send from script %s' % now)
    else:
        print('没有此功能')
        sys.exit(1)

