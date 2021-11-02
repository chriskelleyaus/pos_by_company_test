odoo.define('pos_product_restriction.DB', function (require) {
"use strict";

var DB = require('point_of_sale.DB');
var models = require('point_of_sale.models');


models.load_fields('product.product', ['available_in_pos_company', 'qty_available'])


DB.include({
    add_products: function( products ){
        if(!products instanceof Array){
            products = [products];
        }

        var target_products = [];
        for( var i=0; i < products.length; i++ ){
            var product = products[i];
            console.log(product.available_in_pos_company, product.qty_available)
            if( product.available_in_pos_company && product.qty_available ){
                target_products.push(product);
            }
        }

        this._super(target_products);
    },
});

})
