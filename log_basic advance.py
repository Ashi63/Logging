import logging
import employee

logger=logging.getLogger(__name__)
logger.setLevel('DEBUG')

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('log_basic.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)




#logging.basicConfig(filename='log_basic.log',level='DEBUG',format='%(asctime)s:%(levelname)s:%(message)s')


def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

num_1 = 10
num_2 = 5

add_result = add(num_1,num_2)
logger.info("Addition: {} + {} = {}".format(num_1,num_2,add_result))

sub_result = sub(num_1,num_2)
logger.info("Subtract: {} - {} = {}".format(num_1,num_2,sub_result))

mul_result = mul(num_1,num_2)
logger.info("Multiply : {} * {} = {}".format(num_1,num_2,mul_result))

div_result = div(num_1,num_2)
logger.info("Division : {} / {} = {}".format(num_1,num_2,div_result))


