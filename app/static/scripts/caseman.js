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

    $('#parent_case ul#case_nav').on('click', 'li', function () {
        $('#pending_case_view').hide();
        $('#messaging_view').hide();
        $('#inprogress_case_view').hide();
        $('#closed_case_view').hide();
        $('#rejected_case_view').hide();
        $('#all_case_view').hide();
        $('#new_case_view').show();

        $('#parent_case ul#case_list').empty();

        for (i = 0; i < mycases.length; i++) {
            if (mycases[i].status == 'open') {
                $('#parent_case ul#case_list').append(addLi);
            }
        }
    });

    function addLi() {
        return '<li class="active"> <a href="javascript:;">' +
            '<div class="group clearfix small">' +
            '<span class="sender-name left text-bold">kempton park</span>' +
            '<span class="email-date right xsmall mt1 text-pink">2 hours ago</span>' +
            '</div >' +
            '<p class="subject">big sinkhole in mid road</p>' +
            '<p class="summary small text-muted">TEXT HERE</p>' +
            '<div class="group clearfix">' +
            '<span class="ion ion-trash-a left remove-email"></span>' +
            '<span class="ion right ion-paperclip"></span>' +
            '</div>' +
            '</a> </li>';
    }

    //console.log(mycases)

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