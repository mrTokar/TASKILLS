from artificial_intelligence import NeuronNetwork

def main(event: list) -> str:
    """Главная функция логки программы.
    Возращает готовое описание Локаций"""
    neuron_network = NeuronNetwork(event)

    exposition = neuron_network.create_exposition()

    return exposition
