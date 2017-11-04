$(document).ready(function(){
    queue()
        .defer(d3.json, "/app/get_all_faults/")
        .await(makeGraphs);

    function makeGraphs(error, recordsJson) {
        //Clean data
        var records = recordsJson;
        //"2014-12-24T00:00:00Z"
        var dateFormat = d3.time.format("%Y-%m-%dT%H:%M:%SZ");

        records.forEach(function(d) {
            console.log(d);
            d["date_submitted"] = dateFormat.parse(d["date_submitted"]);
            d["date_created"] = new Date(d["date_created"]);
            d["date_submitted"].setMinutes(0);
            d["date_submitted"].setSeconds(0);
            d["category"] = d["category"];
            d["defect"] = d["defect"];
            d["location"] = d["location"];
            //d["reporters"] = d["reporters"];
        });

        //Create a Crossfilter instance
        var ndx = crossfilter(records);

        //Define Dimensions
        var submittedDim = ndx.dimension(function(d) { return d["date_submitted"]; });
        var createdDim = ndx.dimension(function(d) { return d["date_created"]; });
        var categoryDim = ndx.dimension(function(d) { return d["category"]; });
        var defectDim = ndx.dimension(function(d) { return d["defect"]; });
        var locationDim = ndx.dimension(function(d) { return d["location"]; });
        var allDim = ndx.dimension(function(d) {return d;});

        //Group Data
        var submittedGroup = submittedDim.group();
        var createdGroup = createdDim.group();
        var categoryGroup = categoryDim.group();
        var defectGroup = defectDim.group();
        var locationGroup = locationDim.group();
        var all = ndx.groupAll();

        //Charts
        var numberRecordsND = dc.numberDisplay("#number-records-nd");
        var submittedChart = dc.barChart("#submitted-chart");
        //var createdChart = dc.barChart("#created-chart");
        var categoryChart = dc.pieChart("#category-chart");
        var defectChart = dc.rowChart("#defect-chart");
        var locationChart = dc.rowChart("#location-chart");

        var minDate = submittedDim.bottom(1)[0]["date_submitted"];
        var maxDate = submittedDim.top(1)[0]["date_submitted"];
        
        numberRecordsND
            .formatNumber(d3.format("d"))
            .valueAccessor(function(d){return d; })
            .group(all);

        submittedChart
            .width(1500)
            .height(395)
            .margins({top: 10, right: 50, bottom: 40, left: 40})
            .dimension(submittedDim)
            .group(submittedGroup)
            .xUnits(d3.time.days)
            .controlsUseVisibility(true)
            .transitionDuration(500)
            .x(d3.time.scale().domain([minDate, maxDate]))
            .round(d3.time.month.round)
            .elasticX(true)
            //.xAxis().tickFormat(d3.time.format('%b %y'))
            .elasticY(true)
            .xAxisLabel("Date Submitted")
            .yAxisLabel("Number of faults");
            //.yAxis().ticks(4);

        categoryChart
            .width(350)
            .height(390)
            .dimension(categoryDim)
            .group(categoryGroup)
            .legend(dc.legend().x(380).y(20))
            .innerRadius(20);

        locationChart
            .data(function(group) { return group.top(10); })
            .width(300)
            .height(390)
            .dimension(locationDim)
            .group(locationGroup)
            .ordering(function(d) { return -d.value })
            //.colors(['#6baed6'])
            .elasticX(true)
            .xAxis().ticks(4);

        defectChart
            .data(function(group) { return group.top(10); })
            .width(300)
            .height(390)
            .dimension(defectDim)
            .group(defectGroup)
            .ordering(function(d) { return -d.value })
            //.colors(['#6baed6'])
            .elasticX(true)
            .xAxis().ticks(4);

        dc.renderAll();
    }
});
