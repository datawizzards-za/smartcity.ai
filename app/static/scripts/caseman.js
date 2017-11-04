$(document).ready(function () {
    var caseman_url = document.location.origin + '/app/api/casemanager/';
    var mycases = null;
    $.ajax({
        url: caseman_url,
        type: 'GET',
        async: false,
        success: function (data) {
            mycases = data;
        }
    });

    console.log(mycases.length)

    /*
        $('#pending_case_view').hide();
        $('#messaging_view').hide();
        $('#inprogress_case_view').hide();
        $('#closed_case_view').hide();
        $('#rejected_case_view').hide();
    
        $('#case_nav').on('click', 'li', function () {
            $('#case_nav li').each(function () {
                $(this).removeClass('active');
            });
            $(this).addClass('active');
        }); */
});