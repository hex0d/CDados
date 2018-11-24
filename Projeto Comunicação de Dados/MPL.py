import matplotlib.pyplot as plt

def plot_graph(input_amp):
    input_amp.insert(0,input_amp[0])
    input_amp.append(input_amp[-1])
    plt.axhline(y=0,color='gray',linestyle='--')
    plt.plot(input_amp, color='black', drawstyle='steps-pre')
    plt.grid()
    ax = plt.gca()
    ax.set_ylim(-1.25, 1.25)
    ax.set_xlim(-0.25, 5)
    plt.show()