$(function() {

  var linkCheckForm  = $('.linkcheck_form'),
      linkCheckField = $('.text_field'),
      linkCheckBtn   = $('.button'),
      errorList      = $('.error-list');

  linkCheckBtn.click(function(event) {

    event.preventDefault();
    errorList.empty();

    if (!linkCheckField.val()){
      linkCheckField.addClass('error_field');
      errorList.addClass('active');
      errorList.append('<li>Please enter a URL</li>');
      return false
    } else if (linkCheckField.val().indexOf("https://") <= -1) {
      errorList.addClass('active');
      errorList.append('<li>URLs must begin http:// or https://</li>');
      return false
    } else {
      linkCheckForm.submit();
    }
  });

});
