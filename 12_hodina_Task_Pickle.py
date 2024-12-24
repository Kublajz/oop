import pickle


class Airplane:
    def __init__(self, model, year, id):
        self.model = model
        self.year = year
        self.id = id

    def save_to_json(self, name):
        data = {
            'model': self.model,
            'year': self.year,
            'id': self.id
        }

        with open(f'{name}.json', 'w') as outfile:
            json.dump(data, outfile)

    @staticmethod
    def from_json(file_name):
        with open(file_name) as json_file:
            data = json.load(json_file)

        return Airplane(data['model'], data['year'], data['id'])

    def __str__(self):
        return f'{self.model} {self.year} {self.id}'

    def start(self):
        print("I am starting.")

airplane = [
        Airplane("Mustang", "X1", 1944),
        Airplane("bf", "115", 1874),
        Airplane("Skoda", "octavia", 2020)
]

with open('airplanes.pkl', 'wb') as handle:
    pickle.dump(airplane, handle)

with open('airplanes.pkl', 'rb') as handle:
    loaded_airplanes = pickle.load(handle)

data = pickle.dumps(Airplane)
print(data)
new_data = pickle.loads(data)
print(new_data)

for plane in loaded_airplanes:
    print(plane)
