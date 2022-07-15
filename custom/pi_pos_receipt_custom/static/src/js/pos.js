odoo.define('pi_pos_receipt_custom.pos', function (require) {
	"use strict";

	var chrome = require('point_of_sale.chrome');
	var screens = require('point_of_sale.screens');
	var models = require('point_of_sale.models');
	var gui = require('point_of_sale.gui');
	var PopupWidget = require('point_of_sale.popups');
	var core = require('web.core');
	var _t = core._t;

	var _super_order = models.Order.prototype;
	models.Order = models.Order.extend({

		initialize: function() {
			_super_order.initialize.apply(this,arguments);
			this.total_items = this.total_items || 0;
		},
		
		get_total_product_items : function () {
			var self = this;
			var tot_qty = 0;
			var orderlines = this.orderlines.models;
			for (var i = 0; i < orderlines.length; i++) {
				tot_qty += orderlines[i].quantity;
			}	
			this.total_items = tot_qty;
			return tot_qty;			
		},
	});

});