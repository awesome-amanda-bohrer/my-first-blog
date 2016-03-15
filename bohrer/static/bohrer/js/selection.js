$(function(){
	$('div.product-chooser').find('div.product-chooser-item').not('.disabled').on('click', function(){
		$(this).parent().parent().find('div.product-chooser-item').removeClass('selected');
		$(this).addClass('selected');
		$(this).find('input[type="radio"]').prop("checked", true);
		
	});
});