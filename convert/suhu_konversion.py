suhumula=int(input("""
Pilih suhu Awal :

1. Celcius
2. Fahrenheit
3. Reamur
4. Rankine
5. Kelvin
	"""))
valsuhu=float(input("Input besar suhu: "))

if suhumula==1:
	c2f=9/5*valsuhu+32
	c2k=valsuhu+273.15
	c2r=4/5*valsuhu
	c2ra=(valsuhu+273.15)*9/5
	print(f"""
{valsuhu} derajat Celcius sama dengan {c2f} derajat Fahrenheit
{valsuhu} derajat Celcius sama dengan {c2k} Kelvin
{valsuhu} derajat Celcius sama dengan {c2r} derajat Reamur
{valsuhu} derajat Celcius sama dengan {c2ra} derajat Rankie

		""")
elif suhumula==2:
	f2c=(valsuhu-32)*5/9
	f2k=valsuhu+459.67*5/9
	f2r=4/9*(valsuhu-32)
	f2ra=valsuhu+459.67
	print(f"""
{valsuhu} derajat Fahrenheit sama dengan {f2c} derajat Celcius
{valsuhu} derajat Fahrenheit sama dengan {f2k} Kelvin
{valsuhu} derajat Fahrenheit sama dengan {f2r} derajat Reamur
{valsuhu} derajat Fahrenheit sama dengan {f2ra} derajat Rankie

		""")
elif suhumula==3:
	r2c=valsuhu*0.8
	r2f=(valsuhu*2.25)+32
	r2k=(valsuhu/0.8)+273.15
	r2ra=(valsuhu*2.25)+491.67
	print(f"""
{valsuhu} derajat Reamur sama dengan {r2c} derajat Celcius
{valsuhu} derajat Reamur sama dengan {r2f} derajat Fahreinheit
{valsuhu} derajat Reamur sama dengan {r2k} Kelvin
{valsuhu} derajat Reamur sama dengan {r2ra} derajat Rankie

		""")
elif suhumula==4:
	ra2c=(valsuhu-491.67)*5/9
	ra2f=valsuhu-459.67
	ra2k=valsuhu*5/9
	ra2r=(valsuhu/1.8+273.15)*0.8
	print(f"""
{valsuhu} derajat Rankie sama dengan {ra2c} derajat Celcius
{valsuhu} derajat Rankie sama dengan {ra2f} derajat Fahreinheit
{valsuhu} derajat Rankie sama dengan {ra2k} Kelvin
{valsuhu} derajat Rankie sama dengan {ra2r} derajat Reaamur

		""")
elif suhumula==5:
	k2c=valsuhu-273.15
	k2f=(valsuhu*9/5)-459.67
	k2r=4/5(valsuhu-273)
	k2ra=valsuhu*9/5
	print(f"""
{valsuhu} Kelvin sama dengan {k2c} derajat Celcius
{valsuhu} Kelvin sama dengan {k2f} derajat Fahreinheit
{valsuhu} Kelvin sama dengan {k2r} derajat Reaamur
{valsuhu} Kelvin sama dengan {k2ra} derajat Rankie

		""")
else:
	print("Pilihan yang anda masukkan tidak valid")

#20.83.0572_Raihan Rinto Andiansyah
