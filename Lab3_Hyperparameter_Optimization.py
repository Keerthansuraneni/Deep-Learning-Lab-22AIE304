learning_rates=[0.001,0.01]
hidden_units=[32,64]
dropouts=[0.2,0.3]
for lr in learning_rates:
    for hu in hidden_units:
        for d in dropouts:
            print(f"Trial -> LR={lr}, Hidden={hu}, Dropout={d}")
