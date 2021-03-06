# -*- coding: utf-8 -*-
##############################################################################
#
#    Sistemas de Datos, Open Source Management Solution
#    Copyright (C) 2016 Rodrigo Colombo - Sistemas de Datos (<http://www.sdatos.com>).
#    Migrated v10 2018 Rodrigo Colombo Vlaeminch (http://sdatos.com).
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0
#
##############################################################################

{
    'name' : 'SDatos Distribution Price Margin',
    'version' : '1.2',
    'author' : 'Sistemas de Datos',
    'maintainer': 'Sistemas de Datos',
    'category' : 'Purchases',
    'summary': 'Introduce margin in distribution cost to established sale price',
    'description' : """
Sale Price Margin in Distribution Cost
======================================

This module allows introduce benefits margin in distribution cost of purchases
------------------------------------------------------------------------------

The method used to calculate the sale price is as follows: Sale = Cost / (1 - %margin)\n
Reference: https://manueldelgado.com/como-calcular-el-precio-de-venta-coste-margen/

    """,
    'website': 'http://www.sdatos.com',
    # End General Data
    'depends' : ['sale',
                 'purchase_landed_cost'],
    'data': ['views/purchase_cost_distribution_view.xml'],
    'images':[],                
    'installable': True,
    'auto_install': False,        
    'application': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: