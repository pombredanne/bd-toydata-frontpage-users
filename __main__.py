import bitdeli
from bitdeli.widgets import Users, Text, set_theme, get_themes

print '\n'.join(get_themes())

set_theme('lime')

HASHES = ['205e460b479e2e5b48aec07710c08d50',
          '25c7c18223fb42a4c6ae1c8db6f50f9b',
          'x',
          'f0a7bfdc9c509e8ea02b3ad25ba768b6',
          'b42c651650ec8d3d95829c75e318af2d',
          'd0ae789ef12347de8ec30b3765dd5d89',
          'x',
          '476d8afffbfa06fa852e677848c2388d']

for profile in bitdeli.profiles():
    pass

Text(size=(12, 2),
     head='All systems UP!')
Text(label='Conversions',
     size=(4, 2),
     head='8.13%',
     color=3)
Text(label='Revenue',
     size=(4, 2),
     head='$6,412',
     color=2)
Text(label='Avg. Latency',
     size=(4, 2),
     head='320ms')
Text(size=(3, 2),
     head='8 new users:',
     color=1)
Users(size=(9, 2),
      large=True,
      data=[{'gravatar_hash': h} for h in HASHES])