#-*- coding: utf-8 -*-

{
    'name': 'Hotel Management',
    'version' : '1.0',
    'description': 'A comprehensive hotel management system that allows management of hotel rooms and guests',
    'category':'Industry/Hotel Management',
    'summary': 'Hotel Management',
    'installable': True,
    'application': True,
    'license': 'OEEL-1',
    'depends': ['base'],
    'data':[
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/hotel_service_model_view.xml',
        'views/hotel_management_menus.xml',
        'views/hotel_hotel_model_view.xml',
        'views/hotel_reservation_model_view.xml',
        'views/hotel_rooms_model_view.xml'],
}


#lisence