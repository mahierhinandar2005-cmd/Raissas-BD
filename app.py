import streamlit as st

# 1. Mengatur judul halaman di browser
st.set_page_config(page_title="Happy Birthday Sayang!", page_icon="❤️")

# 2. Judul Utama
st.title("🎂 Happy Birthday, Sayang! 🎂")

# 3. Bagian Pemutar Musik
st.write("🎵 Hidupkan musiknya dulu ya... (Mirrors - Justin Timberlake)")
try:
    audio_file = open("mirrors.mp3", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3", autoplay=True)
except FileNotFoundError:
    st.warning("Lagu mirrors.mp3 belum diupload ke GitHub!")

# 4. Bagian Foto (Menggunakan file lokal dari GitHub)
try:
    # Membaca file foto yang sudah kamu upload ke GitHub kamu
    foto_pacar = open("foto_pacar.jpg", "rb")
    st.image(foto_pacar, caption="Kamu adalah prioritasku 🥰", use_container_width=True)
except FileNotFoundError:
    st.warning("Foto foto_pacar.jpg belum diupload ke GitHub atau salah nama file!")

# 5. Surat Ucapan Ulang Tahun
st.subheader("Surat Spesial Buat Kamu:")
st.write("""
SELAMAT ULANG TAHUN YANG KE 20 AYANGSSS🎊🎉🎊🎉. 
Anjayy udah kepala 2 nih yee menyusull lakinyee😁😁.
Saran dari aku yang udah berada di kepala 2 almost 1 year
adalah perbanyak olahraga makan yg sehat biar ga gampang masuk
angin dan sakit pinggan(penyakit orang berumur)🫠. 
Doa nyaa semoga di umur yang ke 20 ini semoga menjadi pribadi yang 
lebih baik dari yang sebelumnyaa dan semoga banyak cita cita kamu 
yang sebelumnya mungkin masih tertunda sekarang bisa tercapai di usia
yang ke 20 tahun ini🤲🏻. Semoga berkah selalu yapss ayangss i lovee youuuuuuuu so muchhhh 😘😘😘😘
""")

# 6. Tombol Kejutan Interaktif
if st.button("Klik di sini untuk kejutan! ✨"):
    st.balloons()
    st.success("Selamat Ulang Tahun! Tiup lilinnya dan buat permohonan! 🕯️✨")
