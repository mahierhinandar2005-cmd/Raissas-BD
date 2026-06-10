import streamlit as st

# 1. Judul halaman di browser & tema dasar bergaya love
st.set_page_config(page_title="Happy Birthday Sayang!", page_icon="❤️", layout="centered")

# --- MODIFIKASI TEMA LOVE (BACKGROUND PINK & EFEK HATI) ---
st.markdown("""
    <style>
    /* Mengubah latar belakang aplikasi menjadi pink muda lembut */
    .stApp {
        background-color: #FFF0F5;
    }
    /* Mengubah warna teks judul menjadi merah hati */
    h1, h2, h3 {
        color: #D81B60 !important;
        text-align: center;
    }
    /* Mengubah gaya tulisan teks biasa */
    .stText, p {
        color: #4A1525 !important;
        font-size: 18px !important;
        text-align: center;
    }
    /* Mengubah gaya tombol agar bernuansa pink/merah hati */
    div.stButton > button {
        background-color: #FF69B4 !important;
        color: white !important;
        border-radius: 20px !important;
        border: 2px solid #D81B60 !important;
        font-weight: bold !important;
        width: 100%;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    }
    div.stButton > button:hover {
        background-color: #D81B60 !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Pemutar Musik ditaruh di paling atas (Biar terus menyala tanpa putus)
try:
    audio_file = open("mirrors.mp3", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3", autoplay=True)
except FileNotFoundError:
    st.warning("Lagu mirrors.mp3 belum diupload ke GitHub!")

st.markdown("<p style='text-align:center; color:#D81B60;'>💖✨💖✨💖✨💖✨💖✨💖✨💖</p>", unsafe_allow_html=True)

# 3. Mengatur sistem halaman (Session State)
if "halaman" not in st.session_state:
    st.session_state.halaman = 1

# --- SLIDE 1: INTRO ---
if st.session_state.halaman == 1:
    st.title("🎂 Selamat Datang, Sayang! 🎂")
    st.write("Ada pesan kecil penuh cinta yang mau aku sampein ke kamu... 💕")
    st.write("Pastikan suara volumemu sudah aktif untuk dengerin lagu kesukaan kita (Mirrors - Justin Timberlake) ✨")
    
    st.write("") 
    if st.button("Buka Surat Cintanya Di Sini ❤️"):
        st.session_state.halaman = 2
        st.rerun()

# --- SLIDE 2: SURAT & PESAN ASLI DARI KAMU ---
elif st.session_state.halaman == 2:
    st.title("💌 Sepucuk Surat Buat Kamu...")
    
    # Kotak pesan dengan bingkai cinta yang cantik
    st.markdown("""
    <div style="background-color: #FFE4E1; padding: 20px; border-radius: 15px; border: 3px dashed #FF1493; margin-bottom: 20px;">
        <h3 style="margin-top:0; color: #D81B60;">SELAMAT ULANG TAHUN YANG KE 20 AYANGSSS 🎉🎊🎉🎊</h3>
        <p style="color: #4A1525;">Anjayy udah kepala 2 nih yee menyusull lakinyee 😁😁.</p>
        <p style="color: #4A1525;">Saran dari aku yang udah berada di kepala 2 <i>almost 1 year</i> adalah perbanyak olahraga, makan yg sehat biar ga gampang masuk angin dan sakit pinggang (penyakit orang berumur) 🫠.</p>
        <p style="color: #4A1525;">Doa nyaa semoga di umur yang ke 20 ini semoga menjadi pribadi yang lebih baik dari yang sebelumnyaa dan semoga banyak cita cita kamu yang sebelumnya mungkin masih tertunda sekarang bisa tercapai di usia yang ke 20 tahun ini 🤲🏻.</p>
        <p style="color: #4A1525;">Semoga berkah selalu yapss ayangss <b>i lovee youuuuuuuu so muchhhh</b> 😘😘😘😘</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Lanjut ke Kejutan Terakhir 🥰 👉"):
        st.session_state.halaman = 3
        st.rerun()

# --- SLIDE 3: FOTO & BALON ---
elif st.session_state.halaman == 3:
    st.title("📸 My Favorite View!")
    
    # Menampilkan Foto Pacar
    try:
        st.image("foto_pacar.jpg", caption="Kamu adalah prioritasku, cerminan terbaikku 🥰", use_container_width=True)
    except Exception:
        st.warning("Gagal memuat gambar. Pastikan file foto_pacar.jpg sudah ada di GitHub!")
        
    st.write("") 
    st.write("Sekali lagi, Selamat Ulang Tahun Sayang! 🎉 Semoga harimu penuh kebahagiaan!")
    
    # Tombol interaktif untuk merayakan
    if st.button("Rayakan Dengan Balon Cinta! 🎈❤️"):
        st.balloons()
        st.success("I Love You Mooreee! 💋✨")
        
    if st.button("🔄 Baca Ulang Dari Awal"):
        st.session_state.halaman = 1
        st.rerun()

st.markdown("<p style='text-align:center; color:#D81B60;'>💖✨💖✨💖✨💖✨💖✨💖✨💖</p>", unsafe_allow_html=True)
