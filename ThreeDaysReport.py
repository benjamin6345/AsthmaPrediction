

def get_three_days_temp():
    import untangle

    url1 = "https://xml.smg.gov.mo/c_4daysforecast.xml"
    da1 = untangle.parse(url1)

    data = dict()
    for f1 in da1.FourDaysForecast.Custom.WeatherForecast[:3]:
        date = f1.ValidFor.cdata

        mintemp = f1.Temperature[0].Value.cdata
        maxtemp = f1.Temperature[1].Value.cdata
        temp_unit = f1.Temperature[1].MeasureUnit.cdata

        max_hum = f1.Humidity[0].Value.cdata
        min_hum = f1.Humidity[1].Value.cdata
        hum_unit = f1.Humidity[1].MeasureUnit.cdata

        icon = f1.Icon.IconURL.cdata
        
        data[date] = (mintemp, maxtemp, temp_unit, min_hum, max_hum, hum_unit, icon)

    return data
print(get_three_days_temp())
