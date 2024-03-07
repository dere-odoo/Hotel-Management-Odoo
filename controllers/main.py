#-*- coding: utf-8 -*-

from odoo import http

number_of_record_per_page = 10
class hotelManagementCOntroller(http.Controller):
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

    @http.route('/index/service', auth='public', website=True)
    def service(self, **kwargs):
        service_id = kwargs['service_id']
        service = [val for val in http.request.env['hotel.service'].browse(int(service_id))]
        return http.request.render('Hotel-Management-Odoo.service', {
            'service': service
        })