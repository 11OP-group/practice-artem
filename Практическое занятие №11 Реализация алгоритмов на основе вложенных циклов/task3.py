print(f"У вас 100р\nПри стоимость Быка в 10, коровы в 5 и телёнка в 0,5\nВы можете купить максимум:\n")

for bull in range(0, 11):
    for cow in range(0, 21):
        for baby in range(0, 201):
            if 10 * bull + 5 * cow + 0.5 * baby == 100:
                if bull + cow + baby >= 1:
                    print(f"Быков: {bull}, Коров: {cow}, Телят: {baby}")