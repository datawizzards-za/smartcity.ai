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
        for (var $dataTable = $(".data-table"),
            $table = $dataTable.find("table"),
            datas = [{ engine: "Gecko", browser: "Firefox 3.0", platform: "Win 98+/OSX.2+" },
            { engine: "Presto", browser: "Opera 8.0", platform: "Win 95+/OS.2+" },
            { engine: "Trident", browser: "IE 6", platform: "Win 98+" },
            { engine: "Webkit", browser: "iPod Touch / iPhone", platform: "OSX.4+" }],
            prelength = datas.length, i = prelength; 10 > i; i++) { var rand = Math.floor(Math.random() * prelength); datas.push(datas[rand]) }

        var table = $table.DataTable({
            data: datas, columns: [{ data: "engine" }, { data: "browser" }, { data: "platform" }],
            searching: !0, dom: "rtip", pageLength: 5
        });

        $dataTable.find(".searchInput").on("keyup", function () {
            table.search(this.value).draw()
        }), $dataTable.find(".lengthSelect").on("change",
            function () { table.page.len(this.value).draw() }),
            $dataTable.find(".dataTables_info").css({ "margin-left": "20px", "font-size": "12px" })
    } function _init() { toggleBasicTableFns(), initDataTable() } _init()
});