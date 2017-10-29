$(document).ready(function () {
    $('#pending_task_view').hide();
    $('#messaging_view').hide();
    $('#inprogress_task_view').hide();
    $('#closed_task_view').hide();
    $('#rejected_task_view').hide();

    $('#task_nav').on('click', 'li', function () {
        $('#task_nav li').each(function () {
            $(this).removeClass('active');
        });
        $(this).addClass('active');
    });

    $('#pending_task').click(function () {
        $('#new_task_view').hide();
        $('#messaging_view').hide();
        $('#inprogress_task_view').hide();
        $('#closed_task_view').hide();
        $('#rejected_task_view').hide();
        $('#pending_task_view').show();
    });

    $('#new_task').click(function () {
        $('#pending_task_view').hide();
        $('#messaging_view').hide();
        $('#inprogress_task_view').hide();
        $('#closed_task_view').hide();
        $('#rejected_task_view').hide();
        $('#new_task_view').show();
    });

    $('#inprogress_task').click(function () {
        $('#pending_task_view').hide();
        $('#messaging_view').hide();
        $('#new_task_view').hide();
        $('#closed_task_view').hide();
        $('#rejected_task_view').hide();
        $('#inprogress_task_view').show();
    });

    $('#task_messages').click(function () {
        $('#pending_task_view').hide();
        $('#inprogress_task_view').hide();
        $('#new_task_view').hide();
        $('#closed_task_view').hide();
        $('#rejected_task_view').hide();
        $('#messaging_view').show();
    });

    $('#closed_task').click(function () {
        $('#pending_task_view').hide();
        $('#inprogress_task_view').hide();
        $('#new_task_view').hide();
        $('#messaging_view').hide();
        $('#rejected_task_view').hide();
        $('#closed_task_view').show();
    });

    $('#rejected_task').click(function () {
        $('#pending_task_view').hide();
        $('#inprogress_task_view').hide();
        $('#new_task_view').hide();
        $('#messaging_view').hide();
        $('#closed_task_view').hide();
        $('#rejected_task_view').show();
    });
});