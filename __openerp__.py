# -*- encoding: utf-8 -*-

#
# Este modulo tiene reportes personalizados para Guatemala.
    
#
# Status 2.0 - tested on Open ERP 7.00
#

{
    'name' : 'Deducible en Proveedores / Fiscal Clientes',
    'version' : '1.0',
    'category': 'Custom',
    'description': """Este modulo agrega Deducible SI o NO a las Facturas de proveedor y SI NO a Facturas de Ventas""",
    'author': 'Miguel Chuga',
    'website': 'http://openerpgt.wordpress.com',
    'depends' : ['base','sale'],
    'init_xml' : [ ],
    'demo_xml' : [ ],
    'update_xml' : ['invoice_view.xml'],
    'installable': True,
    'certificate': '',
}
#,'catalogos_view.xml'
