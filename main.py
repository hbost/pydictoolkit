from pydictoolkit import *

deck = Deck("deck.yaml")

dic_data = DIC_reader(deck.dic_path)

data_modes = DataMods(dic_data.dataframe, deck)
key = '"e1"'
plott = Plotter(
        key,
        dic_data, 
        deck, 
        data_modes,
        plot_grid = True, 
        plot_deltas = True,
        plot_heatmaps = True,
        create_gif= True
        )   