import webbrowser as wb

backing_tracks = {
    'track1': 'https://www.youtube.com/watch?v=BW73rDPVAU0&list=RDMMBW73rDPVAU0&index=1',
    'track2': 'https://www.youtube.com/watch?v=VyhUrgIRn7g&list=RDMMBW73rDPVAU0&index=2',
    'track3': 'https://www.youtube.com/watch?v=-HraMOLxPyE&list=RDMMBW73rDPVAU0&index=9',
    'track4': 'https://www.youtube.com/watch?v=I7LmHILR9AQ',
    'track5': 'https://www.youtube.com/watch?v=EHnuopwhgB0',
    'track6': 'https://www.youtube.com/watch?v=6Rf_7SVJJNM'
}

for key in backing_tracks:
    wb.open(backing_tracks[key])
