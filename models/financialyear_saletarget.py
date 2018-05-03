# -*- coding: utf-8 -*-

##############################################################################
#
#    VID Techno Solutions.
#    Copyright (C) 2017-TODAY VID Techno Solutions(<https://www.ligs.in>).
#    Author: VID Techno Solutions(<http://vidts.in/>)
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <https://www.gnu.org/licenses/>.
#
##############################################################################
import re
import datetime

import logging
_logger = logging.getLogger(__name__)

from odoo import api, models, fields, _

class FinancialYearSaleTarget(models.Model):
	_name = 'financialyear.saletarget'
	_description = 'Financial Year Sale Target'
	_inherit = ['mail.thread']

	name = fields.Char("Financial Year", copy=False, track_visibility='onchange', required=True)
	date_start = fields.Date('Start Date', required=True,  copy=False, track_visibility='onchange')
	date_stop = fields.Date('End Date', required=True,  copy=False, track_visibility='onchange')
	currency_id = fields.Many2one('res.currency', string='Currency', required=True , default=lambda self: self.env.user.company_id.currency_id, copy=False)
	yearly_target = fields.Monetary('Target Amount',  copy=False, track_visibility='onchange', required=True)
	company_id = fields.Many2one('res.company', string='Company', readonly=True, default=lambda self: self.env.user.company_id, required=True, copy=False)
	# weekly_target = fields.Monetary('Weekly Target',  copy=False, compute="compute_weekly_target", store=True)
	# sales_manager = fields.Many2one('res.users',"Sales Manager", default=lambda self: self.env.user, required=True)

	_sql_constraints = [('name_uniq', 'unique (name)', 'This Financial Year Target already exists'),]

	# @api.depends('yearly_target')
	# def compute_weekly_target(self):
	# 	self.weekly_target = self.yearly_target/52

	def _check_duration(self):
		if self.date_stop < self.date_start:
			return False
		return True

	def _check_name(self):
		r = re.compile('[0-9]{4}-[0-9]{4}')
		if r.match(self.name):
			date_form,date_to = self.name.split("-")
			if int(date_form) >= int(date_to):
				return False
			return True
		return False

	_constraints = [
		(_check_duration, 'Error!\nThe start date of a fiscal year must precede its end date.', ['date_start','date_stop']),
		(_check_name, 'Error!\nFiscal year format must must be yyyy-yyyy', ['name'])
	]

	@api.onchange('date_start')
	def change_date_start(self):
		if self.date_start:
			date_start_year = datetime.datetime.strptime(self.date_start, '%Y-%m-%d').date().year
			self.name = str(date_start_year)+'-'+str(date_start_year+1)
