import matplotlib.pyplot as plt

generation_number = 10

initial_population = 100

reproduction_tax = 1.5

antibiotic_resistance = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

bacteria_population = [initial_population]

for i in range(1, generation_number):
    bacteria_population.append(bacteria_population[i-1] * reproduction_tax)

# ploting
plt.plot(range(generation_number), bacteria_population, label="População de Bactérias")
plt.plot(range(generation_number), antibiotic_resistance, label="Resistência ao Antibiótico")
plt.xlabel('Gerações')
plt.ylabel("Quantidade/Resistência")
plt.title("Evolução de uma Bactéria")
plt.legend()
plt.show()