import hashlib
import time
import random
import requests
from colorama import init, Fore, Back, Style
from rich.console import Console
from rich.panel import Panel

init(autoreset=True)
console = Console()

# Ganti dengan alamat dompet Solana kamu
SOLANA_ADDRESS = "tm-c6ffe8ca-fd3a-4779-9ada-cb411fd95ec5"

def get_sol_balance(address):
    url = f"https://public-api.solscan.io/account/{address}"
    headers = {
        'accept': 'application/json'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()
        lamports = data.get('lamports', 0)
        sol_balance = lamports / 1_000_000_000
        return sol_balance
    except Exception as e:
        console.print(f"[red]❌ Gagal mengakses Solscan API: {e}[/red]")
        return None

def simulate_bitcoin_mining():
    prefix = "0000"
    nonce = 0
    target = prefix + ("f" * (64 - len(prefix)))
    
    console.print("[bold yellow]🚀 Memulai simulasi mining Bitcoin...[/bold yellow]")
    
    while True:
        nonce += 1
        text = f"block{time.time_ns()}{nonce}{random.random()}"
        hash_result = hashlib.sha256(text.encode()).hexdigest()
        
        if hash_result.startswith(prefix):
            console.print(Panel.fit(
                f"[green]💎 Block ditemukan![/green]\nNonce: {nonce}\nHash: {hash_result}",
                title="MINING SUCCESS", style="bold green"
            ))
            break
        
        if nonce % 50000 == 0:
            console.print(f"[cyan]⛏️ Masih menambang... Nonce: {nonce}[/cyan]")

def main():
    while True:
        simulate_bitcoin_mining()
        
        sol_balance = get_sol_balance(SOLANA_ADDRESS)
        if sol_balance is not None:
            console.print(Panel.fit(
                f"[bold blue]🏦 Saldo SOL Anda:[/bold blue] {sol_balance:.4f} SOL",
                title="SOLSCAN BALANCE", style="bold blue"
            ))
        else:
            console.print("[red]❌ Gagal mengambil saldo SOL.[/red]")

        time.sleep(10)  # jeda antar mining

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]⛔ Dihentikan oleh pengguna.[/red]")
