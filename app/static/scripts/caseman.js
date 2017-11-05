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

    $('#parent_case ul#case_nav').on('click', 'li#all_cases', function () {
        $('#new_case_view').hide();
        $('#messaging_view').hide();
        $('#inprogress_case_view').hide();
        $('#closed_case_view').hide();
        $('#rejected_case_view').hide();
        $('#pending_case_view').hide();
        
        $('#parent_case div#all_case_view').attr("class", "email-content animated rotateInDownRight");
        $('#all_case_view').show();

        $('#parent_case ul#case_list').empty();
        for (i = 0; i < mycases.length; i++) {
            $('#parent_case ul#case_list').append(addLi(mycases[i].fault));
        }
    });

    $('#parent_case ul#case_nav').on('click', 'li#new_case', function () {
        $('#pending_case_view').hide();
        $('#messaging_view').hide();
        $('#inprogress_case_view').hide();
        $('#closed_case_view').hide();
        $('#rejected_case_view').hide();
        $('#all_case_view').hide();
        
        $('#parent_case div#new_case_view').attr("class", "email-content animated rotateInDownRight");
        $('#new_case_view').show();

        $('#parent_case ul#case_list').empty();
        for (i = 0; i < mycases.length; i++) {
            if (mycases[i].status == 'open') {
                $('#parent_case ul#case_list').append(addLi(mycases[i].fault));
                //console.log(mycases[i])
                //console.log(mycases[i].fault)
            }
        }
    });

    $('#parent_case ul#case_nav').on('click', 'li#pending_case', function () {
        $('#new_case_view').hide();
        $('#messaging_view').hide();
        $('#inprogress_case_view').hide();
        $('#closed_case_view').hide();
        $('#rejected_case_view').hide();
        $('#all_case_view').hide();
        
        $('#parent_case div#pending_case_view').attr("class", "email-content animated rotateInDownRight");
        $('#pending_case_view').show();

        $('#parent_case ul#case_list').empty();
        for (i = 0; i < mycases.length; i++) {
            if (mycases[i].status == 'pending') {
                $('#parent_case ul#case_list').append(addLi(mycases[i].fault));
                //console.log(mycases[i])
                //console.log(mycases[i].fault)
            }
        }
    });

    $('#parent_case ul#case_nav').on('click', 'li#closed_case', function () {
        $('#pending_case_view').hide();
        $('#inprogress_case_view').hide();
        $('#new_case_view').hide();
        $('#messaging_view').hide();
        $('#rejected_case_view').hide();
        $('#all_case_view').hide();
        
        
        $('#parent_case div#closed_case_view').attr("class", "email-content animated rotateInDownRight");
        $('#closed_case_view').show();

        $('#parent_case ul#case_list').empty();
        for (i = 0; i < mycases.length; i++) {
            if (mycases[i].status == 'closed') {
                $('#parent_case ul#case_list').append(addLi(mycases[i].fault));
                //console.log(mycases[i])
                //console.log(mycases[i].fault)
            }
        }
    });

    function addLi(fault) {
        return '<li class="active"> <a href="javascript:;">' +
            '<div class="group clearfix small">' +
            '<span class="sender-name left text-bold">' + fault.category + '</span>' +
            '<span class="email-date right xsmall mt1 text-pink">' + fault.date_submitted.slice(0, 10)
            + '</span>' +
            '</div >' +
            '<p class="subject">'+ fault.defect +'</p>' +
            '<p class="summary small text-muted">' + fault.location+ '</p>' +
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