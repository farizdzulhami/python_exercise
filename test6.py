TAHUN = 365
BULAN = 30
hari = int(input('Hari :'))
tahun = int(hari/TAHUN)
hari = hari % TAHUN
bulan = int(hari/BULAN)
hari = hari % BULAN

print('Adalah',tahun,'Tahun',bulan,'Bulan','dan',hari,'Hari')