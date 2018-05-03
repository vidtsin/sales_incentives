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

{
	'name': 'Commission and Incentive Management for Ace',
	'version': '1.0',
	'author': 'VID Techno Solutions',
	'website':'http://vidts.in/',
	'category': 'Sales',
	'depends': [
		'sale',
		'sales_team',
		'product_master',
		'crm',
	],
	'description': """
		All management related with commisions and incentive for Ace
	""",
	# define data files (always loaded at installation)
	'data': [
		'views/sales_commission_menu.xml',
		'views/financial_year_sale_target_view.xml',
	],#END data file defenition
	# data files containing optionally loaded demonstration data
	'demo': [
	
	],
	'qweb': [

	],
}
