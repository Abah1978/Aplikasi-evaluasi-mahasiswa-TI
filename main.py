import joblib
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# Judul aplikasi
st.title('Aplikasi Evaluasi Pembelajaran Mahasiswa TI UNTIRTA')

# Masukkin gambar
st.subheader('Keterangan Nilai Bobot Mata Kuliah')
img = Image.open('Nilai Bobot Mata Kuliah.jpg')
st.image(img, use_column_width = True)

# Masukkan Nama
Nama_Lengkap = st.text_input("Nama Lengkap: ")

# Masukkan NIM
NIM = st.number_input("NIM:", min_value=0, max_value=3333999999, value=0)

# Set st.session_state setelah pengguna memasukkan Nama dan NIM
if Nama_Lengkap:
    st.session_state.name = Nama_Lengkap

if NIM:
    st.session_state.age = NIM

SEMESTER_1 = joblib.load('MODEL_SEMESTER1_RF.pkl')
SEMESTER_2 = joblib.load('MODEL_SEMESTER2_RF.pkl')
SEMESTER_3 = joblib.load('MODEL_SEMESTER3_RF.pkl')
SEMESTER_4 = joblib.load('MODEL_SEMESTER4_RF.pkl')
SEMESTER_5 = joblib.load('MODEL_SEMESTER5_RF.pkl')
SEMESTER_6 = joblib.load('MODEL_SEMESTER6_RF.pkl')
SEMESTER_7 = joblib.load('MODEL_SEMESTER7_RF.pkl')


# Sidebar for navigation

with st.sidebar:
    selected = option_menu('Pilihan Semester',
                           ['SEMESTER 1', 'SEMESTER 2', 'SEMESTER 3', 'SEMESTER 4',
                            'SEMESTER 5', 'SEMESTER 6', 'SEMESTER 7'],
                           default_index=0)

if (selected == 'SEMESTER 1'):

    # Page title
    st.title('Evaluasi Pembelajaran Mahasiswa Semester 1 Teknik Industri UNTIRTA')

    Fisika_Dasar_1 = st.selectbox('Fisika Dasar 1', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kalkulus_1 = st.selectbox('Kalkulus 1', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kimia_Dasar = st.selectbox('Kimia Dasar', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Material_Teknik = st.selectbox('Material Teknik', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Pengantar_Teknik_Industri = st.selectbox('Pengantar Teknik Industri', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Menggambar_Teknik = st.selectbox('Menggambar Teknik', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Menggambar_Teknik = st.selectbox('Praktikum Menggambar Teknik', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Logika_Pemrograman = st.selectbox('Logika Pemrograman', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))

    # Code for prediction
    SEMESTER_1_PREDICTION = ''

    # Creating a button for prediction

    if st.button('EVALUASI'):
        if 'name' in st.session_state:
            st.write(f"Halo {st.session_state.name}!")

        if 'age' in st.session_state:
            st.write(f"NIM {st.session_state.age}.")

        Fisika_Dasar_1 = float(Fisika_Dasar_1)
        Kalkulus_1 = float(Kalkulus_1)
        Kimia_Dasar = float(Kimia_Dasar)
        Material_Teknik = float(Material_Teknik)
        Pengantar_Teknik_Industri = float(Pengantar_Teknik_Industri)
        Menggambar_Teknik = float(Menggambar_Teknik)
        Praktikum_Menggambar_Teknik = float(Praktikum_Menggambar_Teknik)
        Logika_Pemrograman = float(Logika_Pemrograman)

        SEMESTER_1_prediction = SEMESTER_1.predict([[Fisika_Dasar_1, Kalkulus_1, Kimia_Dasar, Material_Teknik, Pengantar_Teknik_Industri, Menggambar_Teknik, Praktikum_Menggambar_Teknik, Logika_Pemrograman]])
        
        if SEMESTER_1_prediction[0] == 0:
            SEMESTER_1_PREDICTION = 'MASIH BANYAK NILAI YANG HARUS DIPERBAIKI'
            MOTIVASI = (' '
                        ' Ada beberapa mata kuliah yang menjadi prasayarat dalam mata kuliah lain dan harus diperhatikan untuk menaikan nilai IPK.'
                        ' Berikut mata kuliah menjadi prasayarat dan setara saat di semester 2 : '
                        ' Nilai pada mata kuliah Menggambar Teknik menjadi prasyarat untuk  mata kuliah Mekanika Teknik. '
                        ' Mata kuliah Kalkulus 2 harus diambil bersamaan dengan mata kuliah aljabar linear. '
                        ' Nilai pada mata kuliah Material Teknik menjadi prasyarat pada mata kuliah Proses Manufaktur dan harus diambil berbarengan dengan mata kuliah Mekanika Teknik. '
                        ' Mata kuliah Praktikum Proses Manufaktur harus diambil bersamaan dengan mata kuliah Proses Manufaktur. ')
  
        else:
            SEMESTER_1_PREDICTION = 'NILAI MU SUDAH BAGUS DAN KAMU DAPAT MENGAMBIL LEBIH DARI 20 SKS UNTUK SEMESTER 2'
            MOTIVASI = (' '
                        ' Pertahankan dan tingkatkan kembali nilai-nilai di semester kedepan.'
                        ' Berikut mata kuliah menjadi prasyarat dan setara saat di semester 2 : '
                           ' Nilai pada mata kuliah Menggambar Teknik menjadi prasyarat untuk  mata kuliah Mekanika Teknik. '
                        ' Mata kuliah Kalkulus 2 harus diambil bersamaan dengan mata kuliah aljabar linear. '
                        ' Nilai pada mata kuliah Material Teknik menjadi prasyarat pada mata kuliah Proses Manufaktur dan harus diambil berbarengan dengan mata kuliah Mekanika Teknik. '
                        ' Mata kuliah Praktikum Proses Manufaktur harus diambil bersamaan dengan mata kuliah Proses Manufaktur. ')
            
        pesan_hasil = f'{SEMESTER_1_PREDICTION}, {MOTIVASI}'

        st.success(pesan_hasil)
        
        img3 = Image.open('SYARAT NILAI.jpg')
        st.image(img3, use_column_width=True) 
        
        img4 = Image.open('MKP_SEM2.jpg')
        st.image(img4, use_column_width=True)
        
if (selected == 'SEMESTER 2'):

    # Page title
    st.title('Evaluasi Pembelajaran Mahasiswa SEMESTER 2 Teknik Industri UNTIRTA')

    Fisika_Dasar_1 = st.selectbox('Fisika Dasar 1', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kalkulus_1 = st.selectbox('Kalkulus 1', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kimia_Dasar = st.selectbox('Kimia Dasar', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Material_Teknik = st.selectbox('Material Teknik', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Pengantar_Teknik_Industri = st.selectbox('Pengantar Teknik Industri', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Menggambar_Teknik = st.selectbox('Menggambar Teknik', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Menggambar_Teknik = st.selectbox('Praktikum Menggambar Teknik', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Logika_Pemrograman = st.selectbox('Logika Pemrograman', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Aljabar_Linear = st.selectbox('Aljabar Linear', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Fisika_Dasar_2 = st.selectbox('Fisika Dasar 2', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kalkulus_2 = st.selectbox('Kalkulus 2', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Mekanika_Teknik = st.selectbox('Mekanika Teknik', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Fisika_Dasar = st.selectbox('Praktikum Fisika Dasar', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Proses_Manufaktur = st.selectbox('Proses Manufaktur', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Ekologi_Industri = st.selectbox('Ekologi Industri', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Proses_Manufaktur = st.selectbox('Praktikum Proses Manufaktur', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))

    # Code for prediction
    SEMESTER_2_PREDICTION = ''

    # Creating a button for prediction

    if st.button('EVALUASI'):
        if 'name' in st.session_state:
            st.write(f"Halo {st.session_state.name}!")

        if 'age' in st.session_state:
            st.write(f"NIM {st.session_state.age}.")

        Fisika_Dasar_1 = float(Fisika_Dasar_1)
        Kalkulus_1 = float(Kalkulus_1)
        Kimia_Dasar = float(Kimia_Dasar)
        Material_Teknik = float(Material_Teknik)
        Pengantar_Teknik_Industri = float(Pengantar_Teknik_Industri)
        Menggambar_Teknik = float(Menggambar_Teknik)
        Praktikum_Menggambar_Teknik = float(Praktikum_Menggambar_Teknik)
        Logika_Pemrograman = float(Logika_Pemrograman)
        Aljabar_Linear = float(Aljabar_Linear)
        Fisika_Dasar_2 = float(Fisika_Dasar_2)
        Kalkulus_2 = float(Kalkulus_2)
        Mekanika_Teknik = float(Mekanika_Teknik)
        Praktikum_Fisika_Dasar = float(Praktikum_Fisika_Dasar)
        Proses_Manufaktur = float(Proses_Manufaktur)
        Ekologi_Industri = float(Ekologi_Industri)
        Praktikum_Proses_Manufaktur = float(Praktikum_Proses_Manufaktur)

        SEMESTER_2_prediction = SEMESTER_2.predict([[Fisika_Dasar_1, Kalkulus_1, Kimia_Dasar, Material_Teknik, Pengantar_Teknik_Industri,
                                                     Menggambar_Teknik, Praktikum_Menggambar_Teknik, Logika_Pemrograman,
                                                     Aljabar_Linear, Fisika_Dasar_2, Kalkulus_2, Mekanika_Teknik, Praktikum_Fisika_Dasar,
                                                     Proses_Manufaktur, Ekologi_Industri, Praktikum_Proses_Manufaktur]])

        if SEMESTER_2_prediction[0] == 1:
            SEMESTER_2_PREDICTION = 'MASIH BANYAK NILAI YANG HARUS DIPERBAIKI'
            MOTIVASI = (
                        ' Jangan patah semangat, terus perbaiki nilaimu.'
                        ' Jika kamu malas dan hanya membuang-buang waktu, kamu tak akan tahu bagaimana cara melihat peluang bahkan ketika peluang itu tepat berada di hadapan kamu. '
                        ' Bukan nasib yang menentukan hidupmu, tapi kamu sendirilah yang menentukan masa depanmu. '
                        ' Rasa malas akan menjadi penghalang rezeki dari yang Tuhan berikan.'
                        ' --- '
                        ' Berikut mata kuliah menjadi prasayarat dan setara saat di semester 3 :'
                        ' Nilai pada mata kuliah Kalkulus 2 menjadi prasyarat pada mata kuliah Kalkulus 3 dan Statistika 1. '
                        ' Nilai pada mata kuliah Kuliah Aljabar Linear menjadi prasayarat pada mata kuliah Penelitian Operasional 1 . '
                        ' Nilai pada mata kuliah Pengantar Teknik Industri menjadi prasyarat pada mata kuliah Ergonomi 1 dan harus diambali bersamaan dengan mata kuliah Statistika 1'
                        ' Nilai pada mata kuliah Proses manufaktur menjadi prasyarat pada mata kuliah Perencanaan dan Pengendalian Produksi dan harus diambil bersamaan dengan mata kuliah Ergonomi 1.'
                        ' Mata Kuliah Analisis Biaya dan atau Sistem Rantai Pasok harus diambil bersamaan dengan mata kulliah Perencanaan dan Pengendalian Produksi. ')

        else:
            SEMESTER_2_PREDICTION = 'NILAI MU SUDAH BAGUS DAN KAMU DAPAT MENGAMBIL LEBIH DARI 20 SKS UNTUK SEMESTER 3'
            MOTIVASI = (
                        ' Pertahankan dan tingkatkan kembali nilai-nilai di semester kedepan. '             
                        ' Menjadi mahasiswa tidaklah mudah, namun semua bisa dilalui oleh mereka yang semangatnya yang tak akan goyah.  '
                        ' --- '
                        ' Berikut mata kuliah menjadi prasayarat dan setara saat di semester 3 :'
                        ' Nilai pada mata kuliah Kalkulus 2 menjadi prasyarat pada mata kuliah Kalkulus 3 dan Statistika 1. '
                        ' Nilai pada mata kuliah Kuliah Aljabar Linear menjadi prasayarat pada mata kuliah Penelitian Operasional 1 . '
                        ' Nilai pada mata kuliah Pengantar Teknik Industri menjadi prasyarat pada mata kuliah Ergonomi 1 dan harus diambali bersamaan dengan mata kuliah Statistika 1'
                        ' Nilai pada mata kuliah Proses manufaktur menjadi prasyarat pada mata kuliah Perencanaan dan Pengendalian Produksi dan harus diambil bersamaan dengan mata kuliah Ergonomi 1.'
                        ' Mata Kuliah Analisis Biaya dan atau Sistem Rantai Pasok harus diambil bersamaan dengan mata kulliah Perencanaan dan Pengendalian Produksi. ')


        pesan_hasil = f'{SEMESTER_2_PREDICTION}, {MOTIVASI}'

        st.success(pesan_hasil)

        img3 = Image.open('SYARAT NILAI.jpg')
        st.image(img3, use_column_width=True) 
        
        img5 = Image.open('MKP_SEM3..jpg')
        st.image(img5, use_column_width=True)

if (selected == 'SEMESTER 3'):

    # Page title
    st.title('Evaluasi Pembelajaran Mahasiswa SEMESTER 3 Teknik Industri UNTIRTA')

    Fisika_Dasar_1 = st.selectbox('Fisika Dasar 1', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kalkulus_1 = st.selectbox('Kalkulus 1', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kimia_Dasar = st.selectbox('Kimia Dasar', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Material_Teknik = st.selectbox('Material Teknik', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Pengantar_Teknik_Industri = st.selectbox('Pengantar Teknik Industri', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Menggambar_Teknik = st.selectbox('Menggambar Teknik', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Menggambar_Teknik = st.selectbox('Praktikum Menggambar Teknik', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Logika_Pemrograman = st.selectbox('Logika Pemrograman', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Aljabar_Linear = st.selectbox('Aljabar Linear', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Fisika_Dasar_2 = st.selectbox('Fisika Dasar 2', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kalkulus_2 = st.selectbox('Kalkulus 2', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Mekanika_Teknik = st.selectbox('Mekanika Teknik', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Fisika_Dasar = st.selectbox('Praktikum Fisika Dasar', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Proses_Manufaktur = st.selectbox('Proses Manufaktur', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Ekologi_Industri = st.selectbox('Ekologi Industri', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Proses_Manufaktur = st.selectbox('Praktikum Proses Manufaktur', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Analisis_Biaya = st.selectbox('Analisis Biaya', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Penelitian_Operasional_1 = st.selectbox('Peneletian Operasional 1', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Perencanaan_dan_Pengendalian_Produksi = st.selectbox('Perencanaan dan Pengendalian Produksi', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Sistem_Rantai_Pasok = st.selectbox('Sistem Rantai Pasok', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Ergonomi_1 = st.selectbox('Ergonomi 1', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kalkulus_3 = st.selectbox('Kalkulus 3', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Statistika_1 = st.selectbox('Statistika 1', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))

    # Code for prediction
    SEMESTER_3_PREDICTION = ''

    # Creating a button for prediction

    if st.button('EVALUASI'):
        if 'name' in st.session_state:
            st.write(f"Halo {st.session_state.name}!")

        if 'age' in st.session_state:
            st.write(f"NIM {st.session_state.age}.")

        Fisika_Dasar_1 = float(Fisika_Dasar_1)
        Kalkulus_1 = float(Kalkulus_1)
        Kimia_Dasar = float(Kimia_Dasar)
        Material_Teknik = float(Material_Teknik)
        Pengantar_Teknik_Industri = float(Pengantar_Teknik_Industri)
        Menggambar_Teknik = float(Menggambar_Teknik)
        Praktikum_Menggambar_Teknik = float(Praktikum_Menggambar_Teknik)
        Logika_Pemrograman = float(Logika_Pemrograman)
        Aljabar_Linear = float(Aljabar_Linear)
        Fisika_Dasar_2 = float(Fisika_Dasar_2)
        Kalkulus_2 = float(Kalkulus_2)
        Mekanika_Teknik = float(Mekanika_Teknik)
        Praktikum_Fisika_Dasar = float(Praktikum_Fisika_Dasar)
        Proses_Manufaktur = float(Proses_Manufaktur)
        Ekologi_Industri = float(Ekologi_Industri)
        Praktikum_Proses_Manufaktur = float(Praktikum_Proses_Manufaktur)
        Analisis_Biaya = float(Analisis_Biaya)
        Penelitian_Operasional_1 = float(Penelitian_Operasional_1)
        Perencanaan_dan_Pengendalian_Produksi = float(Perencanaan_dan_Pengendalian_Produksi)
        Sistem_Rantai_Pasok = float(Sistem_Rantai_Pasok)
        Ergonomi_1 = float(Ergonomi_1)
        Kalkulus_3 = float(Kalkulus_3)
        Statistika_1 = float(Statistika_1)


        SEMESTER_3_prediction = SEMESTER_3.predict([[Fisika_Dasar_1, Kalkulus_1, Kimia_Dasar, Material_Teknik, Pengantar_Teknik_Industri,
                                                     Menggambar_Teknik, Praktikum_Menggambar_Teknik, Logika_Pemrograman,
                                                     Aljabar_Linear, Fisika_Dasar_2, Kalkulus_2, Mekanika_Teknik, Praktikum_Fisika_Dasar,
                                                     Proses_Manufaktur, Ekologi_Industri, Praktikum_Proses_Manufaktur, Analisis_Biaya,
                                                     Penelitian_Operasional_1, Perencanaan_dan_Pengendalian_Produksi, Sistem_Rantai_Pasok,
                                                     Ergonomi_1, Kalkulus_3, Statistika_1]])

        if SEMESTER_3_prediction[0] == 0:
            SEMESTER_3_PREDICTION = 'MASIH BANYAK NILAI YANG HARUS DIPERBAIKI  '
            MOTIVASI = (
                ' Jangan patah semangat, terus perbaiki nilaimu. '
                ' Jika tak ingin tertinggal dengan temanmu hilangkan rasa malas, '
                ' Jadilah orang yang dikagumi karena kesuksesanmu nantinya bukan orang yang direndahkan'
                ' --- '
                ' Berikut mata kuliah menjadi prasyarat dan setara saat di semester 4 : '
                ' Mata kuliah Pemodelan Sistem harus diambil setara dengan mata kuliah Penelitian Operasional dan Analitika Data. ' 
                ' Mata kuliah Penelitian Operasional 1 menjadi prasyarat untuk mata kuliah Penelitian Operasional 2. '
                ' Mata kuliah Statistika 1 menjadi prasayarat untuk mata kuliah Statistika 2.  '
                ' Mata kuliah Perencanaan dan Pengendalian Produksi menjadi prasayarat untuk mata kuliah Pengendalian dan Penjaminan Mutu dan harus diambil bersamaan dengan Statistika 2.  '
                ' Mata kuliah Ergonomi 1 menjadi prasyarat untuk mata kuliah Ergonomi 2. '
                ' Mata kuliah Statistika 1 dan Pemrograman Komputer menjadi prasyarat untuk mata kuliah Analitika Data. '
                ' Mata kuliah Pemroragaman Komputer menjadi prasyarat mata kuliah Analisis dan Perancangan Sistem Informasi dan harus diambil setara dengan mata kuliah Pemodelan Sistem. '
                ' Mata Kuliah Analisis dan Perancangan Sistem Informasi harus diambil setara dengan mata kuliah Praktikum Analisis dan Perancangan Sistem Informasi. ')
        else:
            SEMESTER_3_PREDICTION = 'NILAI MU SUDAH BAGUS DAN KAMU DAPAT MENGAMBIL LEBIH DARI 20 SKS UNTUK SEMESTER 4.   '
            MOTIVASI = (
                ' Kamu telah melalui lebih dari 20 sks dengan baik. Pertahankan dan tingkatkan kembali nilai-nilai di semester kedepan. '
                ' "Jika kita terus melakukan apa yang kita lakukan, kita juga terus akan mendapatkan apa yang kita dapatkan" '
                ' --- '
                ' Berikut mata kuliah menjadi prasyarat dan setara saat di semester 4 : '
                ' Mata kuliah Pemodelan Sistem harus diambil setara dengan mata kuliah Penelitian Operasional dan Analitika Data. ' 
                ' Mata kuliah Penelitian Operasional 1 menjadi prasyarat untuk mata kuliah Penelitian Operasional 2. '
                ' Mata kuliah Statistika 1 menjadi prasayarat untuk mata kuliah Statistika 2.  '
                ' Mata kuliah Perencanaan dan Pengendalian Produksi menjadi prasayarat untuk mata kuliah Pengendalian dan Penjaminan Mutu dan harus diambil bersamaan dengan Statistika 2.  '
                ' Mata kuliah Ergonomi 1 menjadi prasyarat untuk mata kuliah Ergonomi 2. '
                ' Mata kuliah Statistika 1 dan Pemrograman Komputer menjadi prasyarat untuk mata kuliah Analitika Data. '
                ' Mata kuliah Pemroragaman Komputer menjadi prasyarat mata kuliah Analisis dan Perancangan Sistem Informasi dan harus diambil setara dengan mata kuliah Pemodelan Sistem. '
                ' Mata Kuliah Analisis dan Perancangan Sistem Informasi harus diambil setara dengan mata kuliah Praktikum Analisis dan Perancangan Sistem Informasi. ')

        pesan_hasil = f'{SEMESTER_3_PREDICTION}, {MOTIVASI}'

        st.success(pesan_hasil)

        img3 = Image.open('SYARAT NILAI.jpg')
        st.image(img3, use_column_width=True) 

        img6 = Image.open('MKP_SEM4..jpg')
        st.image(img6, use_column_width=True)

if (selected == 'SEMESTER 4'):

    # Page title
    st.title('Klasifikasi Kelulusan Mahasiswa SEMESTER 4 Teknik Industri UNTIRTA')

    Fisika_Dasar_1 = st.selectbox('Fisika Dasar 1', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kalkulus_1 = st.selectbox('Kalkulus 1', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kimia_Dasar = st.selectbox('Kimia Dasar', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Material_Teknik = st.selectbox('Material Teknik', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Pengantar_Teknik_Industri = st.selectbox('Pengantar Teknik Industri', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Menggambar_Teknik = st.selectbox('Menggambar Teknik', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Menggambar_Teknik = st.selectbox('Praktikum Menggambar Teknik', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Logika_Pemrograman = st.selectbox('Logika Pemrograman', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Aljabar_Linear = st.selectbox('Aljabar Linear', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Fisika_Dasar_2 = st.selectbox('Fisika Dasar 2', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kalkulus_2 = st.selectbox('Kalkulus 2', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Mekanika_Teknik = st.selectbox('Mekanika Teknik', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Fisika_Dasar = st.selectbox('Praktikum Fisika Dasar', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Proses_Manufaktur = st.selectbox('Proses Manufaktur', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Ekologi_Industri = st.selectbox('Ekologi Industri', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Proses_Manufaktur = st.selectbox('Praktikum Proses Manufaktur', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Analisis_Biaya = st.selectbox('Analisis Biaya', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Penelitian_Operasional_1 = st.selectbox('Peneletian Operasional 1', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Perencanaan_dan_Pengendalian_Produksi = st.selectbox('Perencanaan dan Pengendalian Produksi', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Sistem_Rantai_Pasok = st.selectbox('Sistem Rantai Pasok', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Ergonomi_1 = st.selectbox('Ergonomi 1', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kalkulus_3 = st.selectbox('Kalkulus 3', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Statistika_1 = st.selectbox('Statistika 1', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Analisis_dan_Perancangan_Sistem_Informasi = st.selectbox('AnalisiS dan Perancangan Sistem Informasi', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Pemodelan_Sistem = st.selectbox('Pemodelan Sistem', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Penelitian_Operasional_2 = st.selectbox('Penelitian Operasional 2', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Pengendalian_dan_Penjaminan_Mutu = st.selectbox('Pengendalian dan Penjaminan Mutu', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Analitika_Data = st.selectbox('Analitika Data', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Ergonomi_2 = st.selectbox('Ergonomi 2', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Analisis_dan_Perancangan_Sistem_Informasi = st.selectbox('Praktikum Analisis dan Perancangan Sistem Informasi', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Statistika_2 = st.selectbox('Statistika 2', ('4.00','3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))

    # Code for prediction
    SEMESTER_4_PREDICTION = ''

    # Creating a button for prediction

    if st.button('KLASIFIKASI KELULUSAN'):
        if 'name' in st.session_state:
            st.write(f"Halo {st.session_state.name}!")

        if 'age' in st.session_state:
            st.write(f"NIM {st.session_state.age}.")

        Fisika_Dasar_1 = float(Fisika_Dasar_1)
        Kalkulus_1 = float(Kalkulus_1)
        Kimia_Dasar = float(Kimia_Dasar)
        Material_Teknik = float(Material_Teknik)
        Pengantar_Teknik_Industri = float(Pengantar_Teknik_Industri)
        Menggambar_Teknik = float(Menggambar_Teknik)
        Praktikum_Menggambar_Teknik = float(Praktikum_Menggambar_Teknik)
        Logika_Pemrograman = float(Logika_Pemrograman)
        Aljabar_Linear = float(Aljabar_Linear)
        Fisika_Dasar_2 = float(Fisika_Dasar_2)
        Kalkulus_2 = float(Kalkulus_2)
        Mekanika_Teknik = float(Mekanika_Teknik)
        Praktikum_Fisika_Dasar = float(Praktikum_Fisika_Dasar)
        Proses_Manufaktur = float(Proses_Manufaktur)
        Ekologi_Industri = float(Ekologi_Industri)
        Praktikum_Proses_Manufaktur = float(Praktikum_Proses_Manufaktur)
        Analisis_Biaya = float(Analisis_Biaya)
        Penelitian_Operasional_1 = float(Penelitian_Operasional_1)
        Perencanaan_dan_Pengendalian_Produksi = float(Perencanaan_dan_Pengendalian_Produksi)
        Sistem_Rantai_Pasok = float(Sistem_Rantai_Pasok)
        Ergonomi_1 = float(Ergonomi_1)
        Kalkulus_3 = float(Kalkulus_3)
        Statistika_1 = float(Statistika_1)
        Analisis_dan_Perancangan_Sistem_Informasi = float(Analisis_dan_Perancangan_Sistem_Informasi)
        Pemodelan_Sistem = float(Pemodelan_Sistem)
        Penelitian_Operasional_2 = float(Penelitian_Operasional_2)
        Pengendalian_dan_Penjaminan_Mutu = float(Pengendalian_dan_Penjaminan_Mutu)
        Analitika_Data = float(Analitika_Data)
        Ergonomi_2 = float(Ergonomi_2)
        Praktikum_Analisis_dan_Perancangan_Sistem_Informasi = float(Praktikum_Analisis_dan_Perancangan_Sistem_Informasi)
        Statistika_2 = float(Statistika_2)

        SEMESTER_4_prediction = SEMESTER_4.predict([[Fisika_Dasar_1, Kalkulus_1, Kimia_Dasar, Material_Teknik, Pengantar_Teknik_Industri,
                                                     Menggambar_Teknik, Praktikum_Menggambar_Teknik, Logika_Pemrograman,
                                                     Aljabar_Linear, Fisika_Dasar_2, Kalkulus_2, Mekanika_Teknik, Praktikum_Fisika_Dasar,
                                                     Proses_Manufaktur, Ekologi_Industri, Praktikum_Proses_Manufaktur, Analisis_Biaya,
                                                     Penelitian_Operasional_1, Perencanaan_dan_Pengendalian_Produksi, Sistem_Rantai_Pasok,
                                                     Ergonomi_1, Kalkulus_3, Statistika_1, Analisis_dan_Perancangan_Sistem_Informasi,
                                                     Pemodelan_Sistem, Penelitian_Operasional_2, Pengendalian_dan_Penjaminan_Mutu, Ergonomi_2,
                                                     Analitika_Data, Praktikum_Analisis_dan_Perancangan_Sistem_Informasi, Statistika_2]])

        if SEMESTER_4_prediction[0] == 0:
            SEMESTER_4_PREDICTION = 'KAMU DIPREDIKSI LULUS TIDAK TEPAT WAKTU!'
            MOTIVASI = (
                ' Jangan patah semangat, terus perbaiki nilaimu.')
            img3 = Image.open('SYARAT NILAI.jpg')
            st.image(img3, use_column_width=True) 

        else:
            SEMESTER_4_PREDICTION = 'SELAMAT KAMU DIPREDIKSI LULUS TEPAT WAKTU!'
            MOTIVASI = (
                ' Kamu telah melalui lebih dari 20 sks dengan baik. Pertahankan dan tingkatkan kembali nilai-nilai di semester kedepan. '
                'Kamu bisa mengambil lebih dari 20 sks untuk semester 5. '
                'Pilihlah mata kuliah pilihan sesuai dengan passion mu, jangan mengikuti teman!!')

        pesan_hasil = f'{SEMESTER_4_PREDICTION}, {MOTIVASI}'

        st.success(pesan_hasil)

if (selected == 'SEMESTER 5'):

    # Page title
    st.title('Klasifikasi Kelulusan Mahasiswa SEMESTER 5 Teknik Industri UNTIRTA')

    Fisika_Dasar_1 = st.selectbox('Fisika Dasar 1',
                                  ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kalkulus_1 = st.selectbox('Kalkulus 1', ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kimia_Dasar = st.selectbox('Kimia Dasar', ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Material_Teknik = st.selectbox('Material Teknik',
                                   ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Pengantar_Teknik_Industri = st.selectbox('Pengantar Teknik Industri',
                                             ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Menggambar_Teknik = st.selectbox('Menggambar Teknik',
                                     ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Menggambar_Teknik = st.selectbox('Praktikum Menggambar Teknik',
                                               ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Logika_Pemrograman = st.selectbox('Logika Pemrograman',
                                      ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Aljabar_Linear = st.selectbox('Aljabar Linear',
                                  ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Fisika_Dasar_2 = st.selectbox('Fisika Dasar 2',
                                  ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kalkulus_2 = st.selectbox('Kalkulus 2', ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Mekanika_Teknik = st.selectbox('Mekanika Teknik',
                                   ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Fisika_Dasar = st.selectbox('Praktikum Fisika Dasar',
                                          ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Proses_Manufaktur = st.selectbox('Proses Manufaktur',
                                     ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Ekologi_Industri = st.selectbox('Ekologi Industri',
                                    ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Proses_Manufaktur = st.selectbox('Praktikum Proses Manufaktur',
                                               ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Analisis_Biaya = st.selectbox('Analisis Biaya',
                                  ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Penelitian_Operasional_1 = st.selectbox('Peneletian Operasional 1',
                                            ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Perencanaan_dan_Pengendalian_Produksi = st.selectbox('Perencanaan dan Pengendalian Produksi', (
    '4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Sistem_Rantai_Pasok = st.selectbox('Sistem Rantai Pasok',
                                       ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Ergonomi_1 = st.selectbox('Ergonomi 1',
                                     ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kalkulus_3 = st.selectbox('Kalkulus 3', ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Statistika_1 = st.selectbox('Statistika 1',
                                ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Analisis_dan_Perancangan_Sistem_Informasi = st.selectbox('AnalisiS dan Perancangan Sistem Informasi', (
    '4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Pemodelan_Sistem = st.selectbox('Pemodelan Sistem',
                                    ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Penelitian_Operasional_2 = st.selectbox('Penelitian Operasional 2',
                                            ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Pengendalian_dan_Penjaminan_Mutu = st.selectbox('Pengendalian dan Penjaminan Mutu', (
    '4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Analitika_Data = st.selectbox('Analitika Data',
                                  ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Ergonomi_2 = st.selectbox('Ergonomi 2', ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Analisis_dan_Perancangan_Sistem_Informasi = st.selectbox(
        'Praktikum Analisis dan Perancangan Sistem Informasi',
        ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Statistika_2 = st.selectbox('Statistika 2',
                                ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Keselamatan_dan_Keamanan_Kerja = st.selectbox('Keselamatan dan Keamanan Kerja', (
    '4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Perancangan_dan_Pengembangan_Produk = st.selectbox('Perancangan dan Pengembangan Produk', (
    '4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Perancangan_Tata_Letak_Fasilitas = st.selectbox('Perancangan Tata Letak Fasilitas', (
    '4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kerja_Praktek = st.selectbox('Kerja Praktek', (
    '4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Ekonomika_dan_Ekonomi_Teknik = st.selectbox('Ekonomika dan Ekonomi Teknik', (
    '4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Perancangan_dan_Manajemen_Organisasi_Industri = st.selectbox('Perancangan dan Manajemen Organisasi Industri', (
    '4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Simulasi_Sistem = st.selectbox('Simulasi Sistem',
                                   ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Sistem_Produksi = st.selectbox('Sistem Produksi',
                                   ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Perilaku_Organisasi = st.selectbox('Perilaku Organisasi',
                                       ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Tata_Letak_Fasilitas = st.selectbox('Praktikum Tata Letak Fasilitas', (
    '4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Terintegarasi = st.selectbox('Praktikum Terintegrasi',
                                           ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))


    # Code for prediction
    SEMESTER_5_PREDICTION = ''

    # Creating a button for prediction

    if st.button('KLASIFIKASI KELULUSAN'):
        if 'name' in st.session_state:
            st.write(f"Halo {st.session_state.name}!")

        if 'age' in st.session_state:
            st.write(f"NIM {st.session_state.age}.")

        Fisika_Dasar_1 = float(Fisika_Dasar_1)
        Kalkulus_1 = float(Kalkulus_1)
        Kimia_Dasar = float(Kimia_Dasar)
        Material_Teknik = float(Material_Teknik)
        Pengantar_Teknik_Industri = float(Pengantar_Teknik_Industri)
        Menggambar_Teknik = float(Menggambar_Teknik)
        Praktikum_Menggambar_Teknik = float(Praktikum_Menggambar_Teknik)
        Logika_Pemrograman = float(Logika_Pemrograman)
        Aljabar_Linear = float(Aljabar_Linear)
        Fisika_Dasar_2 = float(Fisika_Dasar_2)
        Kalkulus_2 = float(Kalkulus_2)
        Mekanika_Teknik = float(Mekanika_Teknik)
        Praktikum_Fisika_Dasar = float(Praktikum_Fisika_Dasar)
        Proses_Manufaktur = float(Proses_Manufaktur)
        Ekologi_Industri = float(Ekologi_Industri)
        Praktikum_Proses_Manufaktur = float(Praktikum_Proses_Manufaktur)
        Analisis_Biaya = float(Analisis_Biaya)
        Penelitian_Operasional_1 = float(Penelitian_Operasional_1)
        Perencanaan_dan_Pengendalian_Produksi = float(Perencanaan_dan_Pengendalian_Produksi)
        Sistem_Rantai_Pasok = float(Sistem_Rantai_Pasok)
        Ergonomi_1 = float(Ergonomi_1)
        Kalkulus_3 = float(Kalkulus_3)
        Statistika_1 = float(Statistika_1)
        Analisis_dan_Perancangan_Sistem_Informasi = float(Analisis_dan_Perancangan_Sistem_Informasi)
        Pemodelan_Sistem = float(Pemodelan_Sistem)
        Penelitian_Operasional_2 = float(Penelitian_Operasional_2)
        Pengendalian_dan_Penjaminan_Mutu = float(Pengendalian_dan_Penjaminan_Mutu)
        Analitika_Data = float(Analitika_Data)
        Praktikum_Analisis_dan_Perancangan_Sistem_Informasi = float(Praktikum_Analisis_dan_Perancangan_Sistem_Informasi)
        Statistika_2 = float(Statistika_2)
        Ergonomi_2 = float(Ergonomi_2)
        Keselamatan_dan_Keamanan_Kerja = float(Keselamatan_dan_Keamanan_Kerja)
        Perancangan_dan_Pengembangan_Produk = float(Perancangan_dan_Pengembangan_Produk)
        Perancangan_Tata_Letak_Fasilitas = float(Praktikum_Tata_Letak_Fasilitas)
        Simulasi_Sistem = float(Simulasi_Sistem)
        Sistem_Produksi = float(Sistem_Produksi)
        Perilaku_Organisasi = float(Perilaku_Organisasi)
        Praktikum_Tata_Letak_Fasilitas = float(Perancangan_Tata_Letak_Fasilitas)
        Praktikum_Terintegarasi = float(Praktikum_Terintegarasi)
        Kerja_Praktek = float(Kerja_Praktek)
        Ekonomika_dan_Ekonomi_Teknik = float(Ekonomika_dan_Ekonomi_Teknik)
        Perancangan_dan_Manajemen_Organisasi_Industri = float(Perancangan_dan_Manajemen_Organisasi_Industri)

        SEMESTER_5_prediction = SEMESTER_5.predict(
            [[Fisika_Dasar_1, Kalkulus_1, Kimia_Dasar, Material_Teknik, Pengantar_Teknik_Industri,
              Menggambar_Teknik, Praktikum_Menggambar_Teknik, Logika_Pemrograman,
              Aljabar_Linear, Fisika_Dasar_2, Kalkulus_2, Mekanika_Teknik, Praktikum_Fisika_Dasar,
              Proses_Manufaktur, Ekologi_Industri, Praktikum_Proses_Manufaktur, Analisis_Biaya,
              Penelitian_Operasional_1, Perencanaan_dan_Pengendalian_Produksi, Sistem_Rantai_Pasok,
              Ergonomi_1, Kalkulus_3, Statistika_1, Analisis_dan_Perancangan_Sistem_Informasi,
              Pemodelan_Sistem, Penelitian_Operasional_2, Pengendalian_dan_Penjaminan_Mutu,
              Analitika_Data, Praktikum_Analisis_dan_Perancangan_Sistem_Informasi, Statistika_2,
              Keselamatan_dan_Keamanan_Kerja, Ergonomi_2,
              Perancangan_dan_Pengembangan_Produk, Perancangan_Tata_Letak_Fasilitas, Simulasi_Sistem,
              Sistem_Produksi, Perilaku_Organisasi, Praktikum_Tata_Letak_Fasilitas, Praktikum_Terintegarasi,
              Kerja_Praktek, Ekonomika_dan_Ekonomi_Teknik, Perancangan_dan_Manajemen_Organisasi_Industri]])


        if SEMESTER_5_prediction[0] == 0:
            SEMESTER_5_PREDICTION = 'KAMU DIPREDIKSI LULUS TIDAK TEPAT WAKTU!'
            MOTIVASI = (
                ' Sedikit lagi sudah berada di titik akhir, coba perbaiki nilaimu yang masih kurang. '
                'Mungkin akan sedikit terlambat, tapi pelan pelan kamu pasti bisa mencapai titik akhir')
            img3 = Image.open('SYARAT NILAI.jpg')
            st.image(img3, use_column_width=True) 
        else:
            SEMESTER_5_PREDICTION = 'SELAMAT KAMU DIPREDIKSI LULUS TEPAT WAKTU!'
            MOTIVASI = (
                ' Kamu telah melalui lebih dari 20 sks dengan baik. Pertahankan dan tingkatkan kembali nilai-nilai di semester kedepan. '
                'Kamu bisa mengambil lebih dari 20 sks untuk semester 6. '
                'Pilihlah mata kuliah pilihan sesuai dengan passion mu, jangan mengikuti teman!!')

        pesan_hasil = f'{SEMESTER_5_PREDICTION}, {MOTIVASI}'

        st.success(pesan_hasil)

if (selected == 'SEMESTER 6'):

    # Page title
    st.title('Klasifikasi Kelulusan Mahasiswa SEMESTER 6 Teknik Industri UNTIRTA')

    Fisika_Dasar_1 = st.selectbox('Fisika Dasar 1',
                                  ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kalkulus_1 = st.selectbox('Kalkulus 1', ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kimia_Dasar = st.selectbox('Kimia Dasar', ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Material_Teknik = st.selectbox('Material Teknik',
                                   ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Pengantar_Teknik_Industri = st.selectbox('Pengantar Teknik Industri',
                                             ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Menggambar_Teknik = st.selectbox('Menggambar Teknik',
                                     ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Menggambar_Teknik = st.selectbox('Praktikum Menggambar Teknik',
                                               ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Logika_Pemrograman = st.selectbox('Logika Pemrograman',
                                      ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Aljabar_Linear = st.selectbox('Aljabar Linear',
                                  ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Fisika_Dasar_2 = st.selectbox('Fisika Dasar 2',
                                  ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kalkulus_2 = st.selectbox('Kalkulus 2', ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Mekanika_Teknik = st.selectbox('Mekanika Teknik',
                                   ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Fisika_Dasar = st.selectbox('Praktikum Fisika Dasar',
                                          ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Proses_Manufaktur = st.selectbox('Proses Manufaktur',
                                     ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Ekologi_Industri = st.selectbox('Ekologi Industri',
                                    ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Proses_Manufaktur = st.selectbox('Praktikum Proses Manufaktur',
                                               ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Analisis_Biaya = st.selectbox('Analisis Biaya',
                                  ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Penelitian_Operasional_1 = st.selectbox('Peneletian Operasional 1',
                                            ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Perencanaan_dan_Pengendalian_Produksi = st.selectbox('Perencanaan dan Pengendalian Produksi', (
    '4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Sistem_Rantai_Pasok = st.selectbox('Sistem Rantai Pasok',
                                       ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Ergonomi_1 = st.selectbox('Ergonomi 1',
                                     ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kalkulus_3 = st.selectbox('Kalkulus 3', ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Statistika_1 = st.selectbox('Statistika 1',
                                ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Analisis_dan_Perancangan_Sistem_Informasi = st.selectbox('AnalisiS dan Perancangan Sistem Informasi', (
    '4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Pemodelan_Sistem = st.selectbox('Pemodelan Sistem',
                                    ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Penelitian_Operasional_2 = st.selectbox('Penelitian Operasional 2',
                                            ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Pengendalian_dan_Penjaminan_Mutu = st.selectbox('Pengendalian dan Penjaminan Mutu', (
    '4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Analitika_Data = st.selectbox('Analitika Data',
                                  ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Ergonomi_2 = st.selectbox('Ergonomi 2', ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Analisis_dan_Perancangan_Sistem_Informasi = st.selectbox(
        'Praktikum Analisis dan Perancangan Sistem Informasi',
        ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Statistika_2 = st.selectbox('Statistika 2',
                                ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Keselamatan_dan_Keamanan_Kerja = st.selectbox('Keselamatan dan Keamanan Kerja', (
    '4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Perancangan_dan_Pengembangan_Produk = st.selectbox('Perancangan dan Pengembangan Produk', (
    '4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Perancangan_Tata_Letak_Fasilitas = st.selectbox('Perancangan Tata Letak Fasilitas', (
    '4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Simulasi_Sistem = st.selectbox('Simulasi Sistem',
                                   ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Sistem_Produksi = st.selectbox('Sistem Produksi',
                                   ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Perilaku_Organisasi = st.selectbox('Perilaku Organisasi',
                                       ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Tata_Letak_Fasilitas = st.selectbox('Praktikum Tata Letak Fasilitas', (
    '4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Terintegarasi = st.selectbox('Praktikum Terintegrasi',
                                           ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kerja_Praktek = st.selectbox('Kerja Praktek', (
    '4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Ekonomika_dan_Ekonomi_Teknik = st.selectbox('Ekonomika dan Ekonomi Teknik', (
    '4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Perancangan_dan_Manajemen_Organisasi_Industri = st.selectbox('Perancangan dan Manajemen Organisasi Industri', (
    '4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))

    # Code for prediction
    SEMESTER_6_PREDICTION = ''

    # Creating a button for prediction

    if st.button('KLASIFIKASI KELULUSAN'):
        if 'name' in st.session_state:
            st.write(f"Halo {st.session_state.name}!")

        if 'age' in st.session_state:
            st.write(f"NIM {st.session_state.age}.")

        Fisika_Dasar_1 = float(Fisika_Dasar_1)
        Kalkulus_1 = float(Kalkulus_1)
        Kimia_Dasar = float(Kimia_Dasar)
        Material_Teknik = float(Material_Teknik)
        Pengantar_Teknik_Industri = float(Pengantar_Teknik_Industri)
        Menggambar_Teknik = float(Menggambar_Teknik)
        Praktikum_Menggambar_Teknik = float(Praktikum_Menggambar_Teknik)
        Logika_Pemrograman = float(Logika_Pemrograman)
        Aljabar_Linear = float(Aljabar_Linear)
        Fisika_Dasar_2 = float(Fisika_Dasar_2)
        Kalkulus_2 = float(Kalkulus_2)
        Mekanika_Teknik = float(Mekanika_Teknik)
        Praktikum_Fisika_Dasar = float(Praktikum_Fisika_Dasar)
        Proses_Manufaktur = float(Proses_Manufaktur)
        Ekologi_Industri = float(Ekologi_Industri)
        Praktikum_Proses_Manufaktur = float(Praktikum_Proses_Manufaktur)
        Analisis_Biaya = float(Analisis_Biaya)
        Penelitian_Operasional_1 = float(Penelitian_Operasional_1)
        Perencanaan_dan_Pengendalian_Produksi = float(Perencanaan_dan_Pengendalian_Produksi)
        Sistem_Rantai_Pasok = float(Sistem_Rantai_Pasok)
        Ergonomi_1 = float(Ergonomi_1)
        Kalkulus_3 = float(Kalkulus_3)
        Statistika_1 = float(Statistika_1)
        Analisis_dan_Perancangan_Sistem_Informasi = float(Analisis_dan_Perancangan_Sistem_Informasi)
        Pemodelan_Sistem = float(Pemodelan_Sistem)
        Penelitian_Operasional_2 = float(Penelitian_Operasional_2)
        Pengendalian_dan_Penjaminan_Mutu = float(Pengendalian_dan_Penjaminan_Mutu)
        Analitika_Data = float(Analitika_Data)
        Praktikum_Analisis_dan_Perancangan_Sistem_Informasi = float(Praktikum_Analisis_dan_Perancangan_Sistem_Informasi)
        Statistika_2 = float(Statistika_2)
        Ergonomi_2 = float(Ergonomi_2)
        Keselamatan_dan_Keamanan_Kerja = float(Keselamatan_dan_Keamanan_Kerja)
        Perancangan_dan_Pengembangan_Produk = float(Perancangan_dan_Pengembangan_Produk)
        Perancangan_Tata_Letak_Fasilitas = float(Praktikum_Tata_Letak_Fasilitas)
        Simulasi_Sistem = float(Simulasi_Sistem)
        Sistem_Produksi = float(Sistem_Produksi)
        Perilaku_Organisasi = float(Perilaku_Organisasi)
        Praktikum_Tata_Letak_Fasilitas = float(Perancangan_Tata_Letak_Fasilitas)
        Praktikum_Terintegarasi = float(Praktikum_Terintegarasi)
        Kerja_Praktek = float(Kerja_Praktek)
        Ekonomika_dan_Ekonomi_Teknik = float(Ekonomika_dan_Ekonomi_Teknik)
        Perancangan_dan_Manajemen_Organisasi_Industri = float(Perancangan_dan_Manajemen_Organisasi_Industri)

        SEMESTER_6_prediction = SEMESTER_6.predict(
            [[Fisika_Dasar_1, Kalkulus_1, Kimia_Dasar, Material_Teknik, Pengantar_Teknik_Industri,
              Menggambar_Teknik, Praktikum_Menggambar_Teknik, Logika_Pemrograman,
              Aljabar_Linear, Fisika_Dasar_2, Kalkulus_2, Mekanika_Teknik, Praktikum_Fisika_Dasar,
              Proses_Manufaktur, Ekologi_Industri, Praktikum_Proses_Manufaktur, Analisis_Biaya,
              Penelitian_Operasional_1, Perencanaan_dan_Pengendalian_Produksi, Sistem_Rantai_Pasok,
              Ergonomi_1, Kalkulus_3, Statistika_1, Analisis_dan_Perancangan_Sistem_Informasi,
              Pemodelan_Sistem, Penelitian_Operasional_2, Pengendalian_dan_Penjaminan_Mutu,
              Analitika_Data, Praktikum_Analisis_dan_Perancangan_Sistem_Informasi, Statistika_2,
              Keselamatan_dan_Keamanan_Kerja, Ergonomi_2,
              Perancangan_dan_Pengembangan_Produk, Perancangan_Tata_Letak_Fasilitas, Simulasi_Sistem,
              Sistem_Produksi, Perilaku_Organisasi, Praktikum_Tata_Letak_Fasilitas, Praktikum_Terintegarasi,
              Kerja_Praktek, Ekonomika_dan_Ekonomi_Teknik, Perancangan_dan_Manajemen_Organisasi_Industri]])

        if SEMESTER_6_prediction[0] == 0:
            SEMESTER_6_PREDICTION = 'KAMU DIPREDIKSI LULUS TIDAK TEPAT WAKTU!'
            MOTIVASI = (
                ' Sedikit lagi sudah berada di titik akhir, coba perbaiki nilaimu yang masih kurang. '
                'Mungkin akan sedikit terlambat, tapi pelan pelan kamu pasti bisa mencapai titik akhir. '
                '"Mau tidak mau kita harus segera menyelesaikan kuliah agar tidak memberatkan biaya"')
            img3 = Image.open('SYARAT NILAI.jpg')
            st.image(img3, use_column_width=True) 
            
        else:
            SEMESTER_6_PREDICTION = 'SELAMAT KAMU DIPREDIKSI LULUS TEPAT WAKTU!'
            MOTIVASI = (
                ' Kamu telah melalui lebih dari 20 sks dengan baik. Pertahankan dan tingkatkan kembali nilai-nilai di semester kedepan. '
                'Pikirkan dengan matang, apa topik yang akan kamu teliti di skripsi. '
                '"Jangan jadikan skripsi menjadi hantu di akhir semestermu."')

        pesan_hasil = f'{SEMESTER_6_PREDICTION}, {MOTIVASI}'

        st.success(pesan_hasil)

if (selected == 'SEMESTER 7'):

    # Page title
    st.title('Klasifikasi Kelulusan Mahasiswa SEMESTER 7 Teknik Industri UNTIRTA')

    Fisika_Dasar_1 = st.selectbox('Fisika Dasar 1',
                                  ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kalkulus_1 = st.selectbox('Kalkulus 1', ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kimia_Dasar = st.selectbox('Kimia Dasar', ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Material_Teknik = st.selectbox('Material Teknik',
                                   ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Pengantar_Teknik_Industri = st.selectbox('Pengantar Teknik Industri',
                                             ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Menggambar_Teknik = st.selectbox('Menggambar Teknik',
                                     ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Menggambar_Teknik = st.selectbox('Praktikum Menggambar Teknik',
                                               ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Logika_Pemrograman = st.selectbox('Logika Pemrograman',
                                      ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Aljabar_Linear = st.selectbox('Aljabar Linear',
                                  ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Fisika_Dasar_2 = st.selectbox('Fisika Dasar 2',
                                  ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kalkulus_2 = st.selectbox('Kalkulus 2', ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Mekanika_Teknik = st.selectbox('Mekanika Teknik',
                                   ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Fisika_Dasar = st.selectbox('Praktikum Fisika Dasar',
                                          ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Proses_Manufaktur = st.selectbox('Proses Manufaktur',
                                     ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Ekologi_Industri = st.selectbox('Ekologi Industri',
                                    ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Proses_Manufaktur = st.selectbox('Praktikum Proses Manufaktur',
                                               ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Analisis_Biaya = st.selectbox('Analisis Biaya',
                                  ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Penelitian_Operasional_1 = st.selectbox('Peneletian Operasional 1',
                                            ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Perencanaan_dan_Pengendalian_Produksi = st.selectbox('Perencanaan dan Pengendalian Produksi', (
    '4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Sistem_Rantai_Pasok = st.selectbox('Sistem Rantai Pasok',
                                       ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Ergonomi_1 = st.selectbox('Ergonomi 1',
                                     ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kalkulus_3 = st.selectbox('Kalkulus 3', ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Statistika_1 = st.selectbox('Statistika 1',
                                ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Analisis_dan_Perancangan_Sistem_Informasi = st.selectbox('AnalisiS dan Perancangan Sistem Informasi', (
    '4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Pemodelan_Sistem = st.selectbox('Pemodelan Sistem',
                                    ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Penelitian_Operasional_2 = st.selectbox('Penelitian Operasional 2',
                                            ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Pengendalian_dan_Penjaminan_Mutu = st.selectbox('Pengendalian dan Penjaminan Mutu', (
    '4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Analitika_Data = st.selectbox('Analitika Data',
                                  ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Ergonomi_2 = st.selectbox('Ergonomi 2', ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Analisis_dan_Perancangan_Sistem_Informasi = st.selectbox(
        'Praktikum Analisis dan Perancangan Sistem Informasi',
        ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Statistika_2 = st.selectbox('Statistika 2',
                                ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Keselamatan_dan_Keamanan_Kerja = st.selectbox('Keselamatan dan Keamanan Kerja', (
    '4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Perancangan_dan_Pengembangan_Produk = st.selectbox('Perancangan dan Pengembangan Produk', (
    '4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Perancangan_Tata_Letak_Fasilitas = st.selectbox('Perancangan Tata Letak Fasilitas', (
    '4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Simulasi_Sistem = st.selectbox('Simulasi Sistem',
                                   ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Sistem_Produksi = st.selectbox('Sistem Produksi',
                                   ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Perilaku_Organisasi = st.selectbox('Perilaku Organisasi',
                                       ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Tata_Letak_Fasilitas = st.selectbox('Praktikum Tata Letak Fasilitas', (
    '4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Praktikum_Terintegarasi = st.selectbox('Praktikum Terintegrasi',
                                           ('4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Kerja_Praktek = st.selectbox('Kerja Praktek', (
    '4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Ekonomika_dan_Ekonomi_Teknik = st.selectbox('Ekonomika dan Ekonomi Teknik', (
    '4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Perancangan_dan_Manajemen_Organisasi_Industri = st.selectbox('Perancangan dan Manajemen Organisasi Industri', (
    '4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Metodologi_Penelitian = st.selectbox('Metodologi Penelitian', (
    '4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))
    Perancangan_Sistem_Terpadu = st.selectbox('Perancangan Sistem Terpadu', (
    '4.00', '3.75', '3.50', '3.00', '2.75', '2.50', '2.00', '1.00', '0.00'))

    # Code for prediction
    SEMESTER_7_PREDICTION = ''

    # Creating a button for prediction

    if st.button('Klasifikasi KELULUSAN'):
        if 'name' in st.session_state:
            st.write(f"Halo {st.session_state.name}!")

        if 'age' in st.session_state:
            st.write(f"NIM {st.session_state.age}.")

        Fisika_Dasar_1 = float(Fisika_Dasar_1)
        Kalkulus_1 = float(Kalkulus_1)
        Kimia_Dasar = float(Kimia_Dasar)
        Material_Teknik = float(Material_Teknik)
        Pengantar_Teknik_Industri = float(Pengantar_Teknik_Industri)
        Menggambar_Teknik = float(Menggambar_Teknik)
        Praktikum_Menggambar_Teknik = float(Praktikum_Menggambar_Teknik)
        Logika_Pemrograman = float(Logika_Pemrograman)
        Aljabar_Linear = float(Aljabar_Linear)
        Fisika_Dasar_2 = float(Fisika_Dasar_2)
        Kalkulus_2 = float(Kalkulus_2)
        Mekanika_Teknik = float(Mekanika_Teknik)
        Praktikum_Fisika_Dasar = float(Praktikum_Fisika_Dasar)
        Proses_Manufaktur = float(Proses_Manufaktur)
        Ekologi_Industri = float(Ekologi_Industri)
        Praktikum_Proses_Manufaktur = float(Praktikum_Proses_Manufaktur)
        Analisis_Biaya = float(Analisis_Biaya)
        Penelitian_Operasional_1 = float(Penelitian_Operasional_1)
        Perencanaan_dan_Pengendalian_Produksi = float(Perencanaan_dan_Pengendalian_Produksi)
        Sistem_Rantai_Pasok = float(Sistem_Rantai_Pasok)
        Ergonomi_1 = float(Ergonomi_1)
        Kalkulus_3 = float(Kalkulus_3)
        Statistika_1 = float(Statistika_1)
        Analisis_dan_Perancangan_Sistem_Informasi = float(Analisis_dan_Perancangan_Sistem_Informasi)
        Pemodelan_Sistem = float(Pemodelan_Sistem)
        Penelitian_Operasional_2 = float(Penelitian_Operasional_2)
        Pengendalian_dan_Penjaminan_Mutu = float(Pengendalian_dan_Penjaminan_Mutu)
        Analitika_Data = float(Analitika_Data)
        Praktikum_Analisis_dan_Perancangan_Sistem_Informasi = float(Praktikum_Analisis_dan_Perancangan_Sistem_Informasi)
        Statistika_2 = float(Statistika_2)
        Ergonomi_2 = float(Ergonomi_2)
        Keselamatan_dan_Keamanan_Kerja = float(Keselamatan_dan_Keamanan_Kerja)
        Perancangan_dan_Pengembangan_Produk = float(Perancangan_dan_Pengembangan_Produk)
        Perancangan_Tata_Letak_Fasilitas = float(Praktikum_Tata_Letak_Fasilitas)
        Simulasi_Sistem = float(Simulasi_Sistem)
        Sistem_Produksi = float(Sistem_Produksi)
        Perilaku_Organisasi = float(Perilaku_Organisasi)
        Praktikum_Tata_Letak_Fasilitas = float(Perancangan_Tata_Letak_Fasilitas)
        Praktikum_Terintegarasi = float(Praktikum_Terintegarasi)
        Kerja_Praktek = float(Kerja_Praktek)
        Ekonomika_dan_Ekonomi_Teknik = float(Ekonomika_dan_Ekonomi_Teknik)
        Perancangan_dan_Manajemen_Organisasi_Industri = float(Perancangan_dan_Manajemen_Organisasi_Industri)
        Metodologi_Penelitian = float(Metodologi_Penelitian)
        Perancangan_Sistem_Terpadu = float(Perancangan_Sistem_Terpadu)

        SEMESTER_7_prediction = SEMESTER_7.predict(
            [[Fisika_Dasar_1, Kalkulus_1, Kimia_Dasar, Material_Teknik, Pengantar_Teknik_Industri,
              Menggambar_Teknik, Praktikum_Menggambar_Teknik, Logika_Pemrograman,
              Aljabar_Linear, Fisika_Dasar_2, Kalkulus_2, Mekanika_Teknik, Praktikum_Fisika_Dasar,
              Proses_Manufaktur, Ekologi_Industri, Praktikum_Proses_Manufaktur, Analisis_Biaya,
              Penelitian_Operasional_1, Perencanaan_dan_Pengendalian_Produksi, Sistem_Rantai_Pasok,
              Ergonomi_1, Kalkulus_3, Statistika_1, Analisis_dan_Perancangan_Sistem_Informasi,
              Pemodelan_Sistem, Penelitian_Operasional_2, Pengendalian_dan_Penjaminan_Mutu,
              Analitika_Data, Praktikum_Analisis_dan_Perancangan_Sistem_Informasi, Statistika_2, Ergonomi_2,
              Keselamatan_dan_Keamanan_Kerja, Perancangan_dan_Pengembangan_Produk, Perancangan_Tata_Letak_Fasilitas,
              Simulasi_Sistem, Sistem_Produksi, Perilaku_Organisasi, Praktikum_Tata_Letak_Fasilitas,
              Praktikum_Terintegarasi, Kerja_Praktek, Ekonomika_dan_Ekonomi_Teknik,
              Perancangan_dan_Manajemen_Organisasi_Industri, Metodologi_Penelitian, Perancangan_Sistem_Terpadu]])

        if SEMESTER_7_prediction[0] == 0:
            SEMESTER_7_PREDICTION = 'KAMU DIPREDIKSI LULUS TIDAK TEPAT WAKTU!'
            MOTIVASI = (
                ' Mungkin akan sedikit terlambat, tapi pelan pelan kamu pasti bisa mencapai titik akhir.'
                '"Mau tidak mau kita harus segera menyelesaikan kuliah agar tidak memberatkan biaya"')
            img3 = Image.open('SYARAT NILAI.jpg')
            st.image(img3, use_column_width=True) 

        else:
            SEMESTER_7_PREDICTION = 'SELAMAT KAMU DIPREDIKSI LULUS TEPAT WAKTU!'
            MOTIVASI = (
                ' Sudah hampir sedikit lagi selesai. Bukalah Laptop dan Kerjakan Skripsimu.'
                'Akhir yang indah dengan gelar di belakang nama, siap menantimu!!')

        pesan_hasil = f'{SEMESTER_7_PREDICTION}, {MOTIVASI}'
        st.success(pesan_hasil)
        
        img2 = Image.open('OPSI LULUS.jpg')
        st.image(img2, use_column_width=True)
