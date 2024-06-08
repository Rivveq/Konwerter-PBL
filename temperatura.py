def conv_celsjusz(output, quantity: float):
    match output:
        case 'fahrenheit': return (quantity * 9/5) + 32
        case 'kelvin': return quantity + 273.15
        case 'newton': return quantity * 33/100
        case 'renkine': return (quantity + 273.15) * 9/5,
        case 'romer': return quantity * 21/40 + 7.5,
        case 'temperatura plancka': return (quantity + 273.15) / 1.416808e32,

def conv_fahrenheit(output, quantity: float):
    match output:
        case 'calsjusz': return (quantity - 32) * 5/9
        case 'kelvin': return (quantity - 32) * 5/9 + 273.15
        case 'newton': return (quantity - 32) * 11/60
        case 'renkine': return quantity + 459.67
        case 'romer': return (quantity - 32) * 7/24 + 7.5
        case 'temperatura plancka': return ((quantity - 32) * 5/9 + 273.15) / 1.416808e32

def conv_kelvin(output, quantity: float):
    match output:
        case 'celsjusz': return quantity - 273.15
        case 'fahrenheit': return (quantity - 273.15) * 9/5 + 32
        case 'newton': return (quantity - 273.15) * 33/100
        case 'renkine': return quantity * 9/5
        case 'romer': return (quantity - 273.15) * 21/40 + 7.5
        case 'temperatura plancka': return quantity / 1.416808e32

def conv_newton(output, quantity: float):
    match output:
        case 'celsjusz': return quantity * 100/33
        case 'fahrenheit': return quantity * 60/11 + 32
        case 'kelvin': return quantity * 100/33 + 273.15
        case 'renkine': return (quantity * 100/33 + 273.15) * 9/5
        case 'romer': return quantity * 35/22 + 7.5
        case 'temperatura plancka': return (quantity * 100/33 + 273.15) / 1.416808e32

def conv_rankine(output, quantity: float):
    match output:
        case 'celsjusz': return (quantity - 491.67) * 5/9
        case 'fahrenheit': return quantity - 459.67
        case 'kelvin': return quantity * 5/9
        case 'newton': return (quantity - 491.67) * 11/60
        case 'romer': return (quantity - 491.67) * 7/24 + 7.5
        case 'temperatura plancka': return (quantity * 5/9) / 1.416808e32

def conv_romer(output, quantity: float):
    match output:
        case 'celsjusz': return (quantity - 7.5) * 40/21
        case 'fahrenheit': return (quantity - 7.5) * 24/7 + 32
        case 'kelvin': return (quantity - 7.5) * 40/21 + 273.15
        case 'newton': return (quantity - 7.5) * 22/35
        case 'rankine': return ((quantity - 7.5) * 40/21 + 273.15) * 9/5
        case 'temperatura plancka': return ((quantity - 7.5) * 40/21 + 273.15) / 1.416808e32

def conv_planck(output, quantity: float):
    match output:
        case 'fahrenheit': return (quantity * 1.416808e32 - 273.15) * 9/5 + 32
        case 'kelvin': return quantity * 1.416808e32
        case 'newton': return (quantity * 1.416808e32 - 273.15) * 33/100
        case 'renkine': return quantity * 1.416808e32 * 9/5
        case 'romer': return (quantity * 1.416808e32 - 273.15) * 21/40 + 7.5
        case 'celsjusz': return quantity * 1.416808e32 - 273.15

def convert_temperature(input, output, quantity: float):
    match input:
        case 'celsjusz': return conv_celsjusz(output, quantity)
        case 'fahrenheit': return conv_fahrenheit(output, quantity)
        case 'kelvin': return conv_kelvin(output, quantity)
        case 'newton': return conv_newton(output, quantity)
        case 'renkine': return conv_rankine(output, quantity)
        case 'romer': return conv_romer(output, quantity)
        case 'temperatura plancka': return conv_planck(output, quantity)