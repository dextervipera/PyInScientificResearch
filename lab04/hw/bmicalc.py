import argparse
import colorama

colorama.init()

translator = {'name':'imię', 
              'mass':'waga',
              'height':'wysokość'}    

def parseargs():
    parser = argparse.ArgumentParser(description='BMI calc parser')
    parser.add_argument('mass', type=float, help='body mass in kg')
    parser.add_argument('height', type=float, help='body height in meters')
    parser.add_argument('-n', '--name', type=str, default='template', help='client name')
    parser.add_argument('-d','--display', type=str, help='display mode')
    parser.add_argument('-debug', type=int, help='display debug info')
    return parser.parse_args()

def textcolor(text, style=colorama.Style.RESET_ALL):
    print(f"{style} {text} {colorama.Style.RESET_ALL}")

def argdisplay (args, argn, spec=False):
    if argn in translator.keys():
        _argn = translator[argn]
    else:
        _argn = argn
        
    if not spec:
        print(f"{colorama.Fore.CYAN} {_argn:>10} \
        {colorama.Style.RESET_ALL}: {colorama.Style.BRIGHT} \
        {args[argn]:} \
        {colorama.Style.RESET_ALL}" )
    else:
        print(f"{colorama.Fore.CYAN} {argn:>10} \
        {colorama.Style.RESET_ALL}: {colorama.Style.BRIGHT} \
        {args[argn]:.2f} {colorama.Style.RESET_ALL}" )    

def display(base, mode=None):
    textcolor('------------ New record ------------', colorama.Style.BRIGHT)
    argdisplay(base,'name')
    argdisplay(base,'BMI',True)
    if mode=='full':
        argdisplay(base,'height')
        argdisplay(base,'mass')      

args=parseargs()
if vars(args)['debug']:
    print('new record, debug started...')
    textcolor(colorama.Fore.RED+'Debug info:', colorama.Style.BRIGHT)
    print(vars(args))

results = {'BMI': vars(args)['mass']/vars(args)['height']}
results.update(vars(args))

display(results, mode=vars(args)['display'])