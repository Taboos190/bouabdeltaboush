import os
import sys
import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

console = Console()

PAGES_DIR = "pages"
FACEBOOK_PAGE = os.path.join(PAGES_DIR, "facebook.html")
INSTAGRAM_PAGE = os.path.join(PAGES_DIR, "instagram.html")

def banner():
    console.print(Panel("[bold red]بوعبدل طبوش - Hacker Lab[/bold red]\n[green]By Taboush[/green]", expand=False))

def menu():
    console.print("""
[bold cyan]1.[/bold cyan] توليد صفحة تسجيل وهمية (فيسبوك / انستغرام)
[bold cyan]2.[/bold cyan] هجوم تخمين تعليمي (Brute Force)
[bold cyan]3.[/bold cyan] فحص توفر أسماء مستخدم
[bold cyan]4.[/bold cyan] سحب بيانات عامة من بروفايل انستغرام
[bold cyan]5.[/bold cyan] تشغيل واجهة مزيفة وهمية للتدريب
[bold cyan]0.[/bold cyan] خروج
""")

def generate_fake_page():
    console.print("\n[bold yellow]توليد صفحة وهمية...[/bold yellow]")
    os.makedirs(PAGES_DIR, exist_ok=True)

    fb_html = """
<html><body><h2>Facebook Login</h2>
<form>
<input placeholder='Email'><br>
<input placeholder='Password' type='password'><br>
<button>Login</button>
</form></body></html>
"""

    insta_html = """
<html><body><h2>Instagram Login</h2>
<form>
<input placeholder='Username'><br>
<input placeholder='Password' type='password'><br>
<button>Login</button>
</form></body></html>
"""

    with open(FACEBOOK_PAGE, "w") as f:
        f.write(fb_html)
    with open(INSTAGRAM_PAGE, "w") as f:
        f.write(insta_html)
    
    console.print("[green]✔ تم إنشاء الصفحات داخل مجلد 'pages'[/green]")

def brute_force_demo():
    console.print("\n[bold yellow]تشغيل هجوم تخمين وهمي (تجريبي)...[/bold yellow]")
    user = Prompt.ask("أدخل اسم المستخدم")
    passwords = ["123456", "password", "admin123", "letmein"]
    for pwd in passwords:
        console.print(f"[cyan]*[/cyan] محاولة: [bold]{pwd}[/bold] ...")
    console.print("[green]انتهى التخمين (تجريبي فقط)[/green]")

def check_username():
    username = Prompt.ask("أدخل اسم المستخدم للتحقق")
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)
    if response.status_code == 404:
        console.print("[green]الاسم متاح[/green]")
    else:
        console.print("[red]الاسم مستخدم[/red]")

def fetch_instagram_info():
    username = Prompt.ask("أدخل اسم المستخدم (انستغرام)")
    url = f"https://www.instagram.com/{username}/"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        console.print("[red]فشل في الوصول إلى الحساب[/red]")
        return
    soup = BeautifulSoup(res.text, "html.parser")
    title = soup.find("title").text
    console.print(f"[green]اسم الحساب:[/green] {title}")

def training_interface():
    console.print("\n[bold yellow]واجهة وهمية للتدريب[/bold yellow]")
    console.print(Panel("""
[ LOGIN SYSTEM ]
Username: _______
Password: _______
[ Submit ]
""", title="Simulation"))

def main():
    while True:
        banner()
        menu()
        choice = Prompt.ask("اختر خيارك", choices=["1", "2", "3", "4", "5", "0"])
        if choice == "1":
            generate_fake_page()
        elif choice == "2":
            brute_force_demo()
        elif choice == "3":
            check_username()
        elif choice == "4":
            fetch_instagram_info()
        elif choice == "5":
            training_interface()
        elif choice == "0":
            console.print("[bold red]خروج...[/bold red]")
            sys.exit()

if __name__ == "__main__":
    main()




