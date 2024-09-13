HARI_DETIK = 60*60*24
JAM_DETIK = 60*60
detik = int(input('Detik : '))
hari = int(detik / HARI_DETIK)
sisa_detik = detik % HARI_DETIK
jam = int(sisa_detik / JAM_DETIK)
detik = detik % JAM_DETIK
menit = int(detik / 60)
detik = detik % 60
print('adalah',hari,'Hari',jam,'Jam',menit,'Menit',detik,'Detik')
# ... hari ... jam ... menit ... detik
#sisa bagi
