#-*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Hotel Management',
    'version' : '1.0',
    'description': 'A comprehensive hotel management system that allows management of hotel rooms and guests',
    'category':'Industry/Hotel Management',
    'summary': 'Hotel Management',
    'installable': True,
    'application': True,
    'license': 'OEEL-1',
    'depends': ['base', 'website'],
    'data':[
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/hotel_reservation_model_view.xml',
        'views/hotel_hotel_model_view.xml',
        'views/hotel_service_model_view.xml',
        'views/hotel_rooms_model_view.xml',
        'views/hotel_category_model_view.xml',
        'views/hotel_management_menus.xml',
        'data/website_menu.xml',
        'views/website_template.xml',
        ],
}
