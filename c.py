def flood_attack():
    while True:
        for i in range(10000):
            for j in range(10000):
                for k in range(1, 10000):
                    s = i * j / k


if __name__ == '__main__':
    flood_attack()
