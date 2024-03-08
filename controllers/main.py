#-*- coding: utf-8 -*-

from odoo import http, Command, fields

number_of_record_per_page = 10
class hotelManagementController(http.Controller):
    @http.route(['/index', '/'], auth='public', website=True)
    def index(self, page=1, name=None, address=None, **kwargs):
        page=int(page)
        page = 1 if not page else page
        hotels = http.request.env['hotel.hotel'].search([])
        total_hotels = hotels.search_count([])
        num_pages = total_hotels/number_of_record_per_page
        num_pages = int(num_pages)+1 if num_pages > int(num_pages) else int(num_pages) 
        pager = http.request.website.pager(
            url="/hotel",
            total = total_hotels,
            page=page,
            step = number_of_record_per_page,
            scope = num_pages
        )
        domain = []
        if name:
            domain.append(('name', 'ilike', name))
        if address:
            domain.append(('address', 'ilike', address))

        return http.request.render('Hotel-Management-Odoo.index', {
            'hotels': hotels.search(domain,  limit=number_of_record_per_page, offset=(page-1)*number_of_record_per_page),
            'pager': pager
        })

    @http.route('/index/hotel', auth='public', website=True)
    def hotel(self, **kwargs):
        hotel_id = kwargs['hotel_id']
        hotel = http.request.env['hotel.hotel'].browse(int(hotel_id))
        return http.request.render('Hotel-Management-Odoo.hotel', {
            'hotel': hotel
        })

    @http.route('/index/room', auth='public', website=True)
    def room(self, **kwargs):
        room_id = kwargs['room_id']
        room = [val for val in http.request.env['hotel.rooms'].browse(int(room_id))]
        return http.request.render('Hotel-Management-Odoo.room', {
            'rooms': room
        })

    @http.route('/index/form', auth='public' , website=True)
    def form(self, id=None,**kwargs):
        hotel = http.request.env['hotel.hotel'].browse(int(id))
        return http.request.render('Hotel-Management-Odoo.form', {
            'hotel': hotel,
        })

    @http.route('/form/submit', auth='public' , website=True)
    def book(self,**kwargs):
        user = http.request.env.user
        date_from = kwargs.get('date_from')
        date_end = kwargs.get('date_to')
        hotel_id = kwargs.get('hotel')
        reservation_line = []
        for key,value in kwargs.items():
            if key.startswith('room'):
                reservation_line.append(Command.create({
                    "room_id" : int(value),
                }))
        val = {
            "res_name": f"website {user.id}",
            "hotel_id": hotel_id,
            "start_date" : date_from,
            "end_date" : date_end,
            "stay_for" : (fields.Datetime.to_datetime(date_end) - fields.Datetime.to_datetime(date_from)).days,
            "customer_id" : user.id,
            "reservation_line_ids" : reservation_line
        }
        http.request.env['hotel.reservation'].sudo().create(val)
        return http.request.render('Hotel-Management-Odoo.ThankYou')
        