def convert_units(value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    conversion_factors = {
        ('kilometers', 'miles'): 0.621371,
        ('miles', 'kilometers'): 1.60934,
        ('meters', 'feet'): 3.28084,
        ('feet', 'meters'): 0.3048,
        ('celsius', 'fahrenheit'): lambda c: (c * 9/5) + 32,
        ('fahrenheit', 'celsius'): lambda f: (f - 32) * 5/9,
    }

    key = (from_unit, to_unit)
    
    if key in conversion_factors:
        factor = conversion_factors[key]
        return factor(value) if callable(factor) else value * factor
    else:
        return "Conversion not supported"
