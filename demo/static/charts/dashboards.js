var chart_font = {
    family: "Arial",
    size: 30,
    color: "#FFFFFF"
};

var gTacometer = new JustGage(
    {
        id: "tacometer",
        value: 80,
        min: 0,
        max: 200,
        valueMinFontSize: 40,
        gaugeWidthScale: 1.0,
        donut: true,
        levelColors: ["#a9d70b", "#f9c802", "#ff0000"]
      }
);