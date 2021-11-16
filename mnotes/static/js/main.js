
(function ($) {
    "use strict";
        $('.input3-debt').slideUp(300);
        $('.input3-size').slideUp(300);
        $('.input3-season').slideUp(300);
        $('.input3-color').slideUp(300);
        $('.input3-photo').slideUp(300);
        $('.input3-debt-part').slideUp(300);
    /*==================================================================
    [ Focus Contact2 ]*/
    $('.input3').each(function(){
        $(this).on('blur', function(){
            if($(this).val().trim() != "") {
                $(this).addClass('has-val');
            }
            else {
                $(this).removeClass('has-val');
            }
        })    
    })
            

    /*==================================================================
    [ Chose Radio ]*/
    $("#radio1").on('change', function(){
        if ($(this).is(":checked")) {
            $('.input3-select').slideUp(300);
        }
    });

    $("#radio2").on('change', function(){
        if ($(this).is(":checked")) {
            $('.input3-select').slideDown(300);
        }
    });

    $("#isdebt").on('change', function(){
        if ($(this).is(":checked")) {
            $('.input3-debt').slideDown(300);
            console.log('Checked');
        } else {
            console.log('Not Checked');
            $('.input3-debt').slideUp(300);
        }
    });   

    $("#hascolor").on('change', function(){
        if ($(this).is(":checked")) {
            $('.input3-color').slideDown(300);
            console.log('Checked');
        } else {
            console.log('Not Checked');
            $('.input3-color').slideUp(300);
        }
    }); 

    $("#hasseason").on('change', function(){
        if ($(this).is(":checked")) {
            $('.input3-season').slideDown(300);
            console.log('Checked');
        } else {
            console.log('Not Checked');
            $('.input3-season').slideUp(300);
        }
    }); 

    $("#hassize").on('change', function(){
        if ($(this).is(":checked")) {
            $('.input3-size').slideDown(300);
            console.log('Checked');
        } else {
            console.log('Not Checked');
            $('.input3-size').slideUp(300);
        }
    }); 

    $("#hasphoto").on('change', function(){
        if ($(this).is(":checked")) {
            $('.input3-photo').slideDown(300);
            console.log('Checked');
        } else {
            console.log('Not Checked');
            $('.input3-photo').slideUp(300);
        }
    });

    $("#ispartlypaid").on('change', function(){
        if ($(this).is(":checked")) {
            $('.input3-debt-part').slideDown(300);
            console.log('Checked');
        } else {
            console.log('Not Checked');
            $('.input3-debt-part').slideUp(300);
        }
    });

})(jQuery);