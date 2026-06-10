import streamlit as st

# 1. Judul halaman di browser
st.set_page_config(page_title="Happy Birthday Sayang!", page_icon="❤️")

# 2. Mengatur sistem halaman (Session State)
if "halaman" not in st.session_state:
    st.session_state.halaman = 1

# --- SLIDE 1: INTRO & MUSIK ---
if st.session_state.halaman == 1:
    st.title("🎂 Selamat Datang, Sayang! 🎂")
    st.write("Sebelum kita mulai, yuk hidupkan dulu musiknya biar lebih romantis...")
    
    # Pemutar Musik
    try:
        audio_file = open("mirrors.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3", autoplay=True)
    except FileNotFoundError:
        st.warning("Lagu mirrors.mp3 belum diupload ke GitHub!")
        
    st.write("") # Jarak kosong
    st.write("Kalau musiknya sudah nyala, klik tombol di bawah ya! 👇")
    
    if st.button("Lanjut ke Kejutan ✨"):
        st.session_state.halaman = 2
        st.rerun()

# --- SLIDE 2: SURAT & PESAN ASLI DARI KAMU ---
elif st.session_state.halaman == 2:
    st.title("💌 Sepucuk Surat Buat Kamu...")
    
    # Ini pesan asli darimu yang sudah dimasukkan ke dalam aplikasi
    st.write("""
    ### SELAMAT ULANG TAHUN YANG KE 20 AYANGSSS 🎉🎊🎉🎊
    
    Anjayy udah kepala 2 nih yee menyusull lakinyee 😁😁. 
    
    Saran dari aku yang udah berada di kepala 2 *almost 1 year* adalah perbanyak olahraga, makan yg sehat biar ga gampang masuk angin dan sakit pinggang (penyakit orang berumur) 🫠. 
    
    Doa nyaa semoga di umur yang ke 20 ini semoga menjadi pribadi yang lebih baik dari yang sebelumnyaa dan semoga banyak cita cita kamu yang sebelumnya mungkin masih tertunda sekarang bisa tercapai di usia yang ke 20 tahun ini 🤲🏻. 
    
    Semoga berkah selalu yapss ayangss *i lovee youuuuuuuu so muchhhh* 😘😘😘😘
    """)
    
    st.write("") # Jarak kosong
    st.write("Aku punya satu hal lagi buat kamu... 👇")
    
    if st.button("Lihat Kejutan Selanjutnya 📸"):
        st.session_state.halaman = 3
        st.rerun()

# --- SLIDE 3: FOTO & BALON ---
elif st.session_state.halaman == 3:
    st.title("📸 My Favorite View!")
    
    # Menampilkan Foto
    try:
        st.image("foto_pacar.jpg", caption="Kamu adalah prioritasku 🥰", use_container_width=True)
    except Exception:
        st.warning("Gagal memuat gambar. Pastikan file foto_pacar.jpg sudah ada di GitHub!")
        
    st.write("") # Jarak kosong
    st.write("Sekali lagi, Selamat Ulang Tahun Sayang! 🎉")
    
    # Tombol untuk memunculkan efek balon lagi jika mau
    if st.button("Rayakan! 🎈"):
        st.balloons()
        st.success("Semoga semua permohonanmu dikabulkan ya! 🕯️✨")
        
    # Tombol untuk mengulang dari awal slide jika pacarmu mau baca lagi
    if st.button("Ulangi dari Awal 🔄"):
        st.session_state.halaman = 1
        st.rerun()
