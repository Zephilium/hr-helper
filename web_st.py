import os
import streamlit as st
import fungsi
import nltk
nltk.download('stopwords')


# Create a page dropdown
st.header('HR Helper')

page = st.selectbox("Pilih Menu", ["Seleksi CV", "Speech To Text"])

if page == "Seleksi CV":

    fungsi.ekstrak()
    p_posisi = ['UI / UX', 'Back-end developer',


                'Front-end developer', 'Cloud Computing', 'Data analytics', 'Network Engineer', 'Mobile Developer']

    pil_posisi = st.selectbox('Pilih Posisi', p_posisi)

    but = st.button('Proses')

    if but:

        mypath = 'CV/'
        allfiles = [f for f in os.listdir(
            mypath) if os.path.isfile(os.path.join(mypath, f))]
        st.write(allfiles)

        list_orang = []
        for filename in allfiles:
            list_orang.append(fungsi.seleksi(filename, pil_posisi, p_posisi))
            # list_orang.append(seleksi(filename))

        list_indeks = []
        for i in list_orang:
            indeks = list_orang.index(i)
            sekor = i['skor']
            list_indeks.append([indeks, sekor])
        list_indeks.sort(key=lambda x: x[1], reverse=True)

        list_ranked = []
        for j in list_indeks:
            for i in list_orang:
                if j[0] == list_orang.index(i):
                    list_ranked.append(i)

        ind = 1
        for j in list_ranked:
            a = ''
            st.subheader(f'{ind}. {j["nama"]}')
            # st.write(j['skil'])
            a = ', '.join(j['skil'])
            st.write('Skill :', a)
            ind += 1

        # dir = 'path/to/dir'
        for f in os.listdir(mypath):
            os.remove(os.path.join(mypath, f))


elif page == "Speech To Text":
    fungsi.stt()


if len(os.listdir('CV/')) == 0:
    pass
else:
    for f in os.listdir('CV/'):
        os.remove(os.path.join('CV/', f))

if len(os.listdir('output/example/')) == 0:
    pass
else:
    for f in os.listdir('output/example/'):
        os.remove(os.path.join('output/example/', f))

if len(os.listdir('output/sound/')) == 0:
    pass
else:
    for f in os.listdir('output/sound/'):
        os.remove(os.path.join('output/sound/', f))

if len(os.listdir('output/text/')) == 0:
    pass
else:
    for f in os.listdir('output/text/'):
        os.remove(os.path.join('output/text/', f))
