import flet as ft

current_theme_mode = ft.ThemeMode.LIGHT
version = "0.0.1"
maincolor = "#233dff"
page_color = "#2F2F2F"
text_color = "#F0F8FF"
tertiary_color = "#cae8ff"
ACCENT_COLOR = "#6A5ACD"
APP_NAME = "Vectras Desktop"
APP_COLOR = "#050a30"
ROUTE_LOGIN = "/login"
ROUTE_SIGNUP = "/signup"
ROUTE_WELCOME = "/welcome"
ROUTE_HOME = "/home"
ROUTE_ROMS = "/roms"
ROUTE_SETTINGS = "/settings"
ROUTE_HELP = "/help"
ROUTE_CUSTOMROMS = "/customroms"
ROUTE_ADD = "/addroms"
ROUTE_TEAM = "/team"
Mainheading = ft.Text(
    "Welcome to Vectras Desktop", size=24, weight=ft.FontWeight.BOLD, color=maincolor
)
logo = ft.Image(src="assets/logo.png", width=75, height=75)

def toggle_theme_mode(page):
    global current_theme_mode
    current_theme_mode = (
        ft.ThemeMode.DARK
        if current_theme_mode == ft.ThemeMode.LIGHT
        else ft.ThemeMode.LIGHT
    )
    page.theme_mode = current_theme_mode
    page.update()



