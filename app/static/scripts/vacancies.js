// $(document).ready(function () {

//     var vancies_url = document.location.origin + '/app/api/get_vacancies/';
//     var vacancies = null;
//     $.ajax({
//         url: vancies_url,
//         type: 'GET',
//         async: false,
//         success: function (data) {
//             vacancies = data;
//             var tbody = $('#meeting-1 tbody')[0];
//             $.each(data, function (i, element) {
//                     var tr = document.createElement('tr');
//                     var fn = document.createElement('td');
//                     fn.innerHTML = element.full_names;
//                     var jt = document.createElement('td');
//                     jt.innerHTML = new Date();
//                     var id = document.createElement('td');
//                     id.innerHTML = element.emp_id;
//                     tr.appendChild(id)
//                     tr.appendChild(fn)
//                     tr.appendChild(jt)

//                     tbody.appendChild(tr);
//         }
//     });


// }