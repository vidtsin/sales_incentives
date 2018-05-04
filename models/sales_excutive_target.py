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

class SalesExecutiveTarget(models.Model):
	_name = 'sales.excutive.target'
	_description = 'Sales Executive Target'
	_inherit = ['mail.thread']

	sales_executive =  fields.Many2one('res.users','Sales Executive', copy=False, required=True, track_visibility='onchange')
	currency_id = fields.Many2one('res.currency', string='Currency', required=True , default=lambda self: self.env.user.company_id.currency_id, copy=False)
	breakeaven_target = fields.Monetary('Breakeaven Target', copy=False, track_visibility='onchange')
	breakeaven_incentive = fields.Float("BT Incentive %", copy=False, track_visibility='onchange')
	minimum_target = fields.Monetary('Minimum Target', copy=False, track_visibility='onchange')
	minimum_incentive = fields.Float('MT Incentive %', copy=False, track_visibility='onchange')
	total_target = fields.Monetary('Total Target', copy=False, track_visibility='onchange')
	total_incentive = fields.Float('TT Incentive %', copy=False, track_visibility='onchange')
	exceeding_incentive = fields.Float('Exceeding Target Incentive %', copy=False, track_visibility='onchange')
	salesteam_target_id = fields.Many2one('salesteam.manager.target','Salesteam Target')
	target_splitup = fields.One2many('sales.target.splitup','sales_executive_target_id')