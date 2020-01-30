import winsound
import math

note_names = ['la', 'la_sh', 'si', 'do', 'do_sh', 're', 're_sh', 'mi', 'fa', 'fa_sh', 'sol', 'sol_sh', 'la_1', 'la_sh_1', 'si_1', 'do_1', 'do_sh_1', 're_1', 're_sh_1', 'mi_1', 'fa_1', 'fa_sh_1', 'sol_1', 'sol_sh_1', 'la_2']

n = dict(zip(note_names, [440*math.pow(2, i/12) for i in range(len(note_names))]))

def play(fig):
    for i in fig:
        winsound.Beep(i, 230)

melody = ['do', 'mi', 'sol', 'do_1', 'mi_1', 'sol', 'do_1', 'mi_1',
          'do', 'mi', 'sol', 'do_1', 'mi_1', 'sol', 'do_1', 'mi_1',
          'do', 're', 'la_1', 're_1', 'fa_1', 'la_1', 're_1', 'fa_1',
          'do', 're', 'la_1', 're_1', 'fa_1', 'la_1', 're_1', 'fa_1',
          'si', 're', 'sol', 're_1', 'fa_1', 'sol', 're_1', 'fa_1',
          'si', 're', 'sol', 're_1', 'fa_1', 'sol', 're_1', 'fa_1',
          'do', 'mi', 'sol', 'do_1', 'mi_1', 'sol', 'do_1', 'mi_1',
          'do', 'mi', 'sol', 'do_1', 'mi_1', 'sol', 'do_1', 'mi_1',
          'do', 'mi', 'la_1', 'mi_1', 'la_2', 'la_1', 'mi_1', 'la_2',
          'do', 'mi', 'la_1', 'mi_1', 'la_2', 'la_1', 'mi_1', 'la_2',
          'do', 're', 'fa_sh', 'la_1', 're_1', 'fa_sh', 'la_1', 're_1',
          'do', 're', 'fa_sh', 'la_1', 're_1', 'fa_sh', 'la_1', 're_1',
          ]

c = [int(n[i]) for i in melody]

play(c)


