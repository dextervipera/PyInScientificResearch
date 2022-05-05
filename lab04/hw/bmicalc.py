import argparse
import colorama

colorama.init()

translation = {'name':'imię', 
              'mass':'waga',
              'height':'wysokość'}    

def parseargs():
    parser = argparse.ArgumentParser(description='BMI calc parser')
    parser.add_argument('mass', type=float, help='body mass in kg')
    parser.add_argument('height', type=float, help='body height in meters')
    parser.add_argument('-n', '--name', type=str, default='template', help='client name')
    parser.add_argument('-d','--display', type=str, help='display mode')
    return parser.parse_args()

def textcolor(text, style=colorama.Style.RESET_ALL):
    print(f"{style} {text} {colorama.Style.RESET_ALL}")

def argdisplay (args, argn):
    _argn = lambda arg_caption, dictionary: dictionary[arg_caption] if arg_caption in dictionary else arg_caption
    any2str = lambda any: f"{any:.2f}" if isinstance(any, (float,)) else any
    print(f" |{colorama.Fore.CYAN} {_argn(argn,translation):>10}{colorama.Style.RESET_ALL}: {colorama.Style.BRIGHT}{any2str(args[argn])} {colorama.Style.RESET_ALL}" )   

def display(base, mode=None):
    textcolor('+------- New record --------', colorama.Style.BRIGHT)
    argdisplay(base,'name')
    argdisplay(base,'BMI')
    if mode in ('full','debug'):
        argdisplay(base,'height')
        argdisplay(base,'mass')      

args=parseargs()
if vars(args)['display'] == "debug":
    print('new record, debug started...')
    textcolor(colorama.Fore.RED+'Debug info:', colorama.Style.BRIGHT)
    print(vars(args))

results = {'BMI': vars(args)['mass']/vars(args)['height']}
results.update(vars(args))

display(results, mode=vars(args)['display'])