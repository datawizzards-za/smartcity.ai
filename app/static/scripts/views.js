$(document).ready(function () {
    $('#pending_case_view').hide();
    $('#messaging_view').hide();
    $('#inprogress_case_view').hide();
    $('#closed_case_view').hide();
    $('#rejected_case_view').hide();
    $('#all_case_view').hide();

    $('#case_nav').on('click', 'li', function () {
        $('#case_nav li').each(function () {
            $(this).removeClass('active');
        });
        $(this).addClass('active');
    });

    $('#all_cases').click(function () {
        $('#new_case_view').hide();
        $('#messaging_view').hide();
        $('#inprogress_case_view').hide();
        $('#closed_case_view').hide();
        $('#rejected_case_view').hide();
        $('#pending_case_view').hide();
        $('#all_case_view').show();
    });

    $('#pending_case').click(function () {
        $('#new_case_view').hide();
        $('#messaging_view').hide();
        $('#inprogress_case_view').hide();
        $('#closed_case_view').hide();
        $('#rejected_case_view').hide();
        $('#all_case_view').hide();
        $('#pending_case_view').show();
    });

    $('#inprogress_case').click(function () {
        $('#pending_case_view').hide();
        $('#messaging_view').hide();
        $('#new_case_view').hide();
        $('#closed_case_view').hide();
        $('#rejected_case_view').hide();
        $('#all_case_view').hide();
        $('#inprogress_case_view').show();
    });

    $('#case_messages').click(function () {
        $('#pending_case_view').hide();
        $('#inprogress_case_view').hide();
        $('#new_case_view').hide();
        $('#closed_case_view').hide();
        $('#rejected_case_view').hide();
        $('#all_case_view').hide();
        $('#messaging_view').show();
    });

    $('#closed_case').click(function () {
        $('#pending_case_view').hide();
        $('#inprogress_case_view').hide();
        $('#new_case_view').hide();
        $('#messaging_view').hide();
        $('#rejected_case_view').hide();
        $('#all_case_view').hide();
        $('#closed_case_view').show();
    });

    $('#rejected_case').click(function () {
        $('#pending_case_view').hide();
        $('#inprogress_case_view').hide();
        $('#new_case_view').hide();
        $('#messaging_view').hide();
        $('#closed_case_view').hide();
        $('#all_case_view').hide();
        $('#rejected_case_view').show();
    });
});