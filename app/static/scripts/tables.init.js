jQuery(function () {
    "use strict";
    function toggleBasicTableFns() {
        var $btable = $(".basic-table"), btns = [".btable-bordered", ".btable-striped", ".btable-condensed", ".btable-hover"];
        btns.forEach(function (btn) {
            $btable.find(btn).on("click touchstart", function (e) {
                var tableClass = $(this).data("table-class");
                e.preventDefault(), $(this).toggleClass("active"), $btable.find("table").toggleClass(tableClass)
            })
        })
    }
    function initDataTable() {
        var vancies_url = document.location.origin + '/app/api/get_vacancies/';
        var vacancies = null;
        $.ajax({
            url: vancies_url,
            type: 'GET',
            async: false,
            success: function (data) {
                vacancies = data;
            }
        });
        for (var $dataTable = $(".data-table"), $table = $dataTable.find("table"), vacancies,
            prelength = vacancies.length, i = prelength; 10 > i; i++) {
            //vacancies;
            //console.log(vacancies);
        }

        var table = $table.DataTable({
            data: vacancies, columns: [{ data: "title" },
            { data: "qualifications" }, { data: "posting_date" },
            { data: "closing_date" }],
            searching: !0, dom: "rtip", pageLength: 10
        });
        //console.log(table);

        $dataTable.find(".searchInput").on("keyup", function () {
            table.search(this.value).draw()
        }), $dataTable.find(".lengthSelect").on("change",
            function () { table.page.len(this.value).draw() }),
            $dataTable.find(".dataTables_info").css({ "margin-left": "20px", "font-size": "12px" })
    } function _init() { toggleBasicTableFns(), initDataTable() } _init()
});