import flet as ft
from utils import *
from romspage import roms_page
from settings import settings_page
from homepage import home_page
from helppage import help_page
from onboardingpage import *
from addroms import addroms
from teampage import team_page

def main(page: ft.Page):
    def route_change(route):
        page.views.clear()
        if page.route == ROUTE_WELCOME:
            welcome_view = ft.View(route, [welcome_page(page)])
            welcome_view.vertical_alignment = (
                ft.MainAxisAlignment.CENTER
            )
            welcome_view.horizontal_alignment = ft.CrossAxisAlignment.CENTER
            page.views.append(welcome_view)
        elif page.route == ROUTE_HELP:
            help_view = ft.View(route, [help_page(page)])
            help_view.vertical_alignment = ft.MainAxisAlignment.CENTER  
            help_view.horizontal_alignment = ft.CrossAxisAlignment.CENTER
            page.views.append(help_view)
        elif page.route == ROUTE_HOME:
            home_view = ft.View(
                route,
                [
                    ft.Container(
                        expand=True,
                        alignment=ft.alignment.center,
                        content=home_page(page),
                    )
                ],
            )
            home_view.vertical_alignment = ft.MainAxisAlignment.CENTER
            home_view.horizontal_alignment = ft.CrossAxisAlignment.CENTER
            page.views.append(home_view)
        elif page.route == ROUTE_TEAM:
            team_view = ft.View(route, [team_page(page)])
            team_view.vertical_alignment = ft.MainAxisAlignment.CENTER
            team_view.horizontal_alignment = ft.CrossAxisAlignment.CENTER
            page.views.append(team_view)
        elif page.route == ROUTE_ROMS:
            roms_view = ft.View(route, [roms_page(page)])
            roms_view.vertical_alignment = (
                ft.MainAxisAlignment.CENTER
            )  # Add this line
            roms_view.horizontal_alignment = ft.CrossAxisAlignment.CENTER
            page.views.append(roms_view)
        elif page.route == ROUTE_SETTINGS:
            settings_view = ft.View(route, [settings_page(page)])
            settings_view.vertical_alignment = (
                ft.MainAxisAlignment.CENTER
            )  # Add this line
            settings_view.horizontal_alignment = ft.CrossAxisAlignment.CENTER
            page.views.append(settings_view)
        elif page.route == ROUTE_ADD:
            customroms_view = ft.View(route, [addroms(page)])
            customroms_view.vertical_alignment = (
                ft.MainAxisAlignment.CENTER
            )  # Add this line
            customroms_view.horizontal_alignment = ft.CrossAxisAlignment.CENTER
            page.views.append(customroms_view)
        else:
            welcome_view = ft.View(route, [welcome_page(page)])
            welcome_view.vertical_alignment = (
                ft.MainAxisAlignment.CENTER
            )  # Add this line
            welcome_view.horizontal_alignment = ft.CrossAxisAlignment.CENTER
            page.views.append(welcome_view)
        page.update()

    page.title = APP_NAME
    page.window.always_on_top = True
    page.window.width = 1300
    page.window.height = 800
    theme = ft.Theme()
    theme.page_transitions.windows = ft.PageTransitionTheme.CUPERTINO
    theme.page_transitions.android = ft.PageTransitionTheme.CUPERTINO
    page.theme = theme
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.on_route_change = route_change
    page.go(ROUTE_WELCOME)


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
