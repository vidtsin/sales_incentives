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

class SalesTeamManagerTarget(models.Model):
	_name = 'salesteam.manager.target'
	_description = 'Sales Team Manager Target'
	_inherit = ['mail.thread']

	sales_team = fields.Many2one('crm.team', "Sales Team", copy=False, required=True, track_visibility='onchange')
	sales_manager = fields.Many2one('res.users', track_visibility='onchange', required=True)
	currency_id = fields.Many2one('res.currency', string='Currency', required=True , default=lambda self: self.env.user.company_id.currency_id, copy=False)
	total_target = fields.Monetary('Yearly Target Amount', copy=False, track_visibility='onchange', required=True)
	sae_target = fields.Monetary('Sales Executives Target', copy=False, track_visibility='onchange', required=True)
	self_direct_target = fields.Monetary('Self Direct Target', copy=False, track_visibility='onchange', required=True)
	self_direct_incentive = fields.Float('Incentive %', copy=False, track_visibility='onchange', required=True)
	below_msp_credit = fields.Float('Below MSP Credit for SaE', copy=False, track_visibility='onchange')
	below_msp_dedit = fields.Float('Below MSP Debit for SM', copy=False, track_visibility='onchange')

	