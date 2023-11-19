
def get_now_weather():
    import untangle


    url1 = "https://xml.smg.gov.mo/c_actual_brief.xml"
    da1 = untangle.parse(url1)

    for f1 in da1.ActualWeatherBrief.Custom:
        try:
            nowtemp = f1.Temperature[0].Value.cdata
            nowtemp_unit = f1.Temperature[0].MeasureUnit.cdata
        except:
            nowtemp = f1.Temperature.Value.cdata
            nowtemp_unit = f1.Temperature.MeasureUnit.cdata

        nowhumid = f1.Humidity.Value.cdata
        humid_unit = f1.Humidity.MeasureUnit.cdata
        nowwindspeed = f1.WindSpeed.Value.cdata
        windspeed_unit = f1.WindSpeed.MeasureUnit.cdata
        pic = f1.Icon.IconURL.cdata
        if hasattr(f1, 'Rainfall'):    
            nowrainfall = f1.Rainfall.Value.cdata
            rainfall_unit = f1.Rainfall.MeasureUnit.cdata
        else:
            nowrainfall = 0
            rainfall_unit = "mm"

        return (nowtemp, nowtemp_unit, nowhumid, humid_unit, nowwindspeed, windspeed_unit, nowrainfall, rainfall_unit, pic)
    

print(get_now_weather())