from sqlalchemy import inspect
from src.models import Bill, BillDetail
import datetime

day_of_week = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}


def product_amount_sell_day(product):
    datetime_now = datetime.datetime.now()
    """ Statistic of today"""
    list_row = BillDetail.query.filter(BillDetail.ProductId == product['ProductId'])
    list_bill_detail = [object_as_dict(x) for x in list_row]
    for x in list_bill_detail:
        list_row = Bill.query.filter(Bill.BillId == x['BillId'])
        list_bill = [object_as_dict(y) for y in list_row]
        if len(list_bill) != 0:
            x['Datetime'] = list_bill[0]['Datetime']
            x['Type'] = list_bill[0]['Type']
        else:
            x['Datetime'] = datetime_now
            x['Type'] = 3

    i = 0
    while i < len(list_bill_detail):
        if (list_bill_detail[i]['Datetime'].date() - datetime_now.date()).days != 0:
            list_bill_detail.pop(i)
        else:
            i += 1

    amount_buy_day = 0
    amount_sell_day = 0
    for x in list_bill_detail:
        if x['Type'] == 0:
            amount_buy_day += x['Amount']
        elif x['Type'] == 1:
            amount_sell_day += x['Amount']

    """Statistic of week"""
    amount_buy_week = 0
    amount_sell_week = 0
    week_day = datetime_now.weekday()


    list_row = BillDetail.query.filter(BillDetail.ProductId == product['ProductId'])
    list_bill_detail = [object_as_dict(x) for x in list_row]
    for x in list_bill_detail:
        list_row = Bill.query.filter(Bill.BillId == x['BillId'])
        list_bill = [object_as_dict(y) for y in list_row]
        if len(list_bill) != 0:
            x['Datetime'] = datetime_now
            x['Type'] = list_bill[0]['Type']
        else:
            x['Datetime'] = datetime_now
            x['Type'] = 3
    i = 0
    while i < len(list_bill_detail):
        if (datetime_now.date() - list_bill_detail[i]['Datetime'].date()).days < 0 or \
                (datetime_now.date() - list_bill_detail[i]['Datetime'].date()).days > week_day:
            list_bill_detail.pop(i)
        else:
            i += 1
    amount_buy_week = 0
    amount_sell_week = 0
    for x in list_bill_detail:
        if x['Type'] == 0:
            amount_buy_week += x['Amount']
        elif x['Type'] == 1:
            amount_sell_week += x['Amount']


    return {
        'amount_buy_day': amount_buy_day,
        'amount_sell_day': amount_sell_day,
        'amount_buy_week': amount_buy_week,
        'amount_sell_week': amount_sell_week
    }

def product_statistic_one_week(product):
    datetime_now = datetime.datetime.now()
    list_result = []
    for i in range(7):
        list_result.append(
            {
                'Datetime': datetime_now,
                'WeekDay': "Thứ 2",
                'Weather': "Nắng",
                'Temperature': "29",
                'NumberPurchased': 0,
                'NumberSold': 0
            }
        )
    for i in range(7):
        date = datetime_now - datetime.timedelta(i)
        list_result[i]['Datetime'] = date
        list_result[i]['WeekDay'] = date.weekday()

    """ Statistic of today"""
    list_row = BillDetail.query.filter(BillDetail.ProductId == product['ProductId'])
    list_bill_detail = [object_as_dict(x) for x in list_row]
    for x in list_bill_detail:
        list_row = Bill.query.filter(Bill.BillId == x['BillId'])
        list_bill = [object_as_dict(y) for y in list_row]
        if len(list_bill) != 0:
            x['Datetime'] = list_bill[0]['Datetime']
            x['Type'] = list_bill[0]['Type']
        else:
            x['Datetime'] = datetime_now
            x['Type'] = 3


    for x in list_result:
        for y in list_bill_detail:
            if (y['Datetime'].date() == x['Datetime'].date()):
                if (y['Type'] == 0):
                    x['NumberPurchased'] += y['Amount']
                elif (y['Type'] == 1):
                    x['NumberSold'] += y['Amount']
    return list_result

def get_success(data):
    return {
        "status": True,
        "msg": "Lấy thành công",
        "data": data
    }


def get_fail():
    return {
        "status": False,
        "msg": "Lấy thất bại"
    }


def create_success():
    return {
        "status": True,
        "msg": "Thêm mới thành công",
    }


def create_fail():
    return {
        "status": False,
        "msg": "Thêm mới thất bại"
    }

def update_success():
    return {
        "status": True,
        "msg": "Sửa thành công",
    }


def update_fail():
    return {
        "status": False,
        "msg": "Sửa thất bại"
    }

def delete_success():
    return {
        "status": True,
        "msg": "Xóa thành công",
    }


def delete_fail():
    return {
        "status": False,
        "msg": "Xóa thất bại"
    }
