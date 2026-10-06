# константы состояний больного
TEMP_MIN_NORMAL = 36
TEMP_MAX_NORMAL = 37
TEMP_MIN_SICK = 35
TEMP_MAX_SICK = 38

PRESSURE_MIN_NORMAL = 110
PRESSURE_MAX_NORMAL = 130
PRESSURE_MIN_SICK = 105
PRESSURE_MAX_SICK = 140

PULSE_MIN_NORMAL = 60
PULSE_MAX_NORMAL = 100
PULSE_MIN_SICK = 55
PULSE_MAX_SICK = 110

temperature = float(input("Температура (°C): "))
pressure = int(input("Давление (верхнее): "))
pulse = int(input("Пульс (уд/мин): "))

if temperature <= 0 or pressure <= 0 or pulse <= 0:
    print("Данные неверны!")
else:
    print(f"Температура: {temperature}°C, давление: {pressure}, пульс: {pulse}")
    if (temperature < TEMP_MIN_SICK or temperature > TEMP_MAX_SICK
            or pressure < PRESSURE_MIN_SICK or pressure > PRESSURE_MAX_SICK
            or pulse < PULSE_MIN_SICK or pulse > PULSE_MAX_SICK):
        print("Пациент болен и ему требуется врач! СКОРУЮ!!!")
    elif (TEMP_MIN_NORMAL <= temperature <= TEMP_MAX_NORMAL
            and PRESSURE_MIN_NORMAL <= pressure <= PRESSURE_MAX_NORMAL
            and PULSE_MIN_NORMAL <= pulse <= PULSE_MAX_NORMAL):
        print(f"Пациент в норме")
    else:
        print(f"Пациент испытывает недоMOGGание")