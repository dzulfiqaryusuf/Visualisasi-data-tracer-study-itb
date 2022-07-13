data = [
    {
        'Degree': 'Teknik Informatika',
        'Salary': 16000000,
        'Bonus': 25500000,
    },
    {
        'Degree': 'Teknik Perminyakan',
        'Salary': 12000000,
        'Bonus': 39000000,
    },
    {
        'Degree': 'Sistem dan Teknologi Informasi',
        'Salary': 8250000,
        'Bonus': 17000000,
    },
    {
        'Degree': 'Teknik Kimia',
        'Salary': 9150000,
        'Bonus': 20000000,
    },
    {
        'Degree': 'Teknik Pertambangan',
        'Salary': 10000000,
        'Bonus': 29000000,
    },
    {
        'Degree': 'Teknik Mesin',
        'Salary': 10000000,
        'Bonus': 35000000,
    },
    {
        'Degree': 'Teknik Elektro',
        'Salary': 8500000,
        'Bonus': 22500000,
    },
    {
        'Degree': 'Teknik Industri',
        'Salary': 9000000,
        'Bonus': 20500000,
    },
    {
        'Degree': 'Matematika',
        'Salary': 7700000,
        'Bonus': 13000000,
    },
    {
        'Degree': 'Teknik Tenaga Listrik',
        'Salary': 7550000,
        'Bonus': 45000000,
    },
    {
        'Degree': 'Teknik Telekomunikasi',
        'Salary': 7000000,
        'Bonus': 14000000,
    },
    {
        'Degree': 'Teknik Metalurgi',
        'Salary': 7800000,
        'Bonus': 15570000,
    },
    {
        'Degree': 'Manajemen Rekayasa Industri',
        'Salary': 10600000,
        'Bonus': 25000000,
    },
    {
        'Degree': 'Manajemen',
        'Salary': 9500000,
        'Bonus': 30000000,
    },
    {
        'Degree': 'Teknik Geologi',
        'Salary': 7500000,
        'Bonus': 14500000,
    },
    {
        'Degree': 'Teknik Geofisika',
        'Salary': 8500000,
        'Bonus': 30000000,
    },
    {
        'Degree': 'Teknik Material',
        'Salary': 6810000,
        'Bonus': 15000000,
    },
    {
        'Degree': 'Teknik Sipil',
        'Salary': 7175000,
        'Bonus': 20000000,
    },
    {
        'Degree': 'Teknik Fisika',
        'Salary': 6400000,
        'Bonus': 15000000,
    },
    {
        'Degree': 'Aeronautika dan Astronautika',
        'Salary': 7000000,
        'Bonus': 12000000,
    },
    {
        'Degree': 'Teknik Lingkungan',
        'Salary': 6650000,
        'Bonus': 17500000,
    },
    {
        'Degree': 'Teknik Geodesi dan Geomatika',
        'Salary': 7000000,
        'Bonus': 20000000,
    },
    {
        'Degree': 'Teknik Kelautan',
        'Salary': 8687500,
        'Bonus': 8500000,
    },
    {
        'Degree': 'Seni Rupa',
        'Salary': 3500000,
        'Bonus': 10000000,
    },
    {
        'Degree': 'Mikrobiologi',
        'Salary': 5950000,
        'Bonus': 14500000,
    },
    {
        'Degree': 'Desain Produk',
        'Salary': 5000000,
        'Bonus': 7000000,
    },
    {
        'Degree': 'Desain Komunikasi Visual',
        'Salary': 6500000,
        'Bonus': 5650000,
    },
    {
        'Degree': 'Arsitektur',
        'Salary': 6125000,
        'Bonus': 9000000,
    },
    {
        'Degree': 'Kimia',
        'Salary': 5525000,
        'Bonus': 10000000,
    },
    {
        'Degree': 'Fisika',
        'Salary': 7450000,
        'Bonus': 13000000,
    },
    {
        'Degree': 'Astronomi',
        'Salary': 6900000,
        'Bonus': 6000000,
    },
    {
        'Degree': 'Perencanaan Wilayah dan Kota',
        'Salary': 6353700,
        'Bonus': 10000000,
    },
    {
        'Degree': 'Rekayasa Pertanian',
        'Salary': 6000000,
        'Bonus': 6000000,
    },
    {
        'Degree': 'Rekayasa Hayati',
        'Salary': 5500000,
        'Bonus': 10000000,
    },
    {
        'Degree': 'Rekayasa Kehutanan',
        'Salary': 5000000,
        'Bonus': 7000000,
    },
    {
        'Degree': 'Sains dan Teknologi Farmasi',
        'Salary': 6050000,
        'Bonus': 10000000,
    },
    {
        'Degree': 'Meteorologi',
        'Salary': 5000000,
        'Bonus': 7875000,
    },
    {
        'Degree': 'Desain Interior',
        'Salary': 6000000,
        'Bonus': 5400000,
    },
    {
        'Degree': 'Biologi',
        'Salary': 5000000,
        'Bonus': 8500000,
    },
    {
        'Degree': 'Kewirausahaan',
        'Salary': 7200000,
        'Bonus': 22500000,
    },
    {
        'Degree': 'Rekayasa Infrastruktur Lingkungan',
        'Salary': 5000000,
        'Bonus': 15000000,
    },
    {
        'Degree': 'Teknik Pengelolaan Sumber Daya Air',
        'Salary': 5000000,
        'Bonus': 10000000,
    },
    {
        'Degree': 'Farmasi Klinik dan Komunitas',
        'Salary': 4757350,
        'Bonus': 7000000,
    },
    {
        'Degree': 'Kriya',
        'Salary': 4500000,
        'Bonus': 7250000,
    },
    {
        'Degree': 'Oseanografi',
        'Salary': 5000000,
        'Bonus': 11000000,
    },
]

for i in data:
    salary = i['Salary']
    bonus = i['Bonus']
    degree = i['Degree']
    salary *= 12
    bonus *= 2
    i['Total'] = salary + bonus
    i['Per Month'] = i['Salary'] + bonus
    # print(i['Total'])
