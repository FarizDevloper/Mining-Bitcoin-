<p align="center">

![welllll](https://github.com/user-attachments/assets/7eef222d-045a-4d88-a111-1804e441d1b8)
           
</p>

<h1 align="center">💰 Bitcoin Mining Simulator + Solana Wallet Tracker</h1>

<p align="center">
  <b>Simulasi mining Bitcoin berbasis Python dengan tampilan visual dan cek saldo dompet Solana secara real-time!</b><br>
  SHA256 Hash Simulation | Nonce Cracking | Solscan API Integration | Real-time Balance Display
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python">
  <img src="https://img.shields.io/badge/Solana-API-green?logo=solana">
  <img src="https://img.shields.io/badge/Mining-Simulation-orange?logo=bitcoin">
  <img src="https://img.shields.io/badge/License-MIT-lightgrey">
</p>

---

## 🚀 Fitur Utama

- 🔐 Simulasi proses *Bitcoin mining* menggunakan SHA-256 dan *nonce cracking*
- 🔄 Cek saldo dompet Solana secara langsung menggunakan [Solscan API](https://public-api.solscan.io)
- 🌈 Tampilan CLI berwarna dengan `rich` dan `colorama`
- 🔁 Loop otomatis dengan jeda antar blok
- 💡 Cocok untuk edukasi, demo proyek, dan visualisasi kriptografi dasar

---

## 🧠 Cara Kerja

Skrip ini melakukan:
1. Simulasi mining dengan mencari hash SHA-256 yang diawali dengan `0000`
2. Menampilkan hash valid jika ditemukan (seolah berhasil menambang satu blok)
3. Mengakses Solscan API untuk mengambil saldo dompet Solana
4. Menampilkan saldo di terminal secara interaktif

---

## 🛠️ Instalasi

```bash
git clone https://github.com/yourusername/bitcoin-sim-solana-checker
cd bitcoin-sim-solana-checker
pip install -r requirements.txt
python miner.py

