// NOTICE!! DO NOT USE ANY OF THIS JAVASCRIPT
// IT'S ALL JUST JUNK FOR OUR DOCS!
// ++++++++++++++++++++++++++++++++++++++++++

!function ($) {
  $(function(){

    $('.tooltip-demo').tooltip({
      selector: "[data-toggle=tooltip]",
      container: "body"
    });

	$("input[type='number']").stepper();

	$(".selecter_1").selecter();

	$(".selecter_2").selecter();

	$(".selecter_3").selecter();

	$(".selecter_4").selecter();

	$(".selecter_5").selecter();

	$(".selecter_6").selecter();

    $('.checkbox input').iCheck({
        checkboxClass: 'icheckbox_flat',
        increaseArea: '20%'
    });

    $('.radio input').iCheck({
        radioClass: 'iradio_flat',
        increaseArea: '20%'
    });
    $('#accordion1').collapse();
    $('#accordion2').collapse();
  })
}(window.jQuery)
