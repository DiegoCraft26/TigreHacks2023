import flet as ft
from flet import *
from src.views.LoginPageView import _view_ as LoginPage
from src.views.SingUpView import _view_ as SingUpPage
from src.views.IndexView import _view_ as IndexPage
from src.views.SettingsView import _view_ as SettingsPage
from src.views.VerificationView import _view_ as VerificationPage

# el precio del PET ronda entre los $4.50 y los $5
# id grupo cognito:   us-east-1_IsVAzmCPD
# arn:aws:cognito-idp:us-east-1:130278754658:userpool/us-east-1_IsVAzmCPD
def main(page:Page):
    page.theme_mode = "dark"
    page.scroll = True
    page.title = "EcoBalance"

    def route_change(route):
        page.views.clear()
        if page.route == '/login':
            page.views.append(LoginPage())
        if page.route == '/singup':
            page.views.append(SingUpPage())
        if page.route == '/index':
            page.views.append(IndexPage())
        if page.route == '/settings':
            page.views.append(SettingsPage())
        if page.route == '/verification':
            page.views.append(VerificationPage())
        page.update()
    
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    page.views.append(VerificationPage())
    page.views.append(SettingsPage())
    page.views.append(IndexPage())
    page.views.append(SingUpPage())
    page.views.append(LoginPage())
    
    page.update()
    
ft.app(target=main, assets_dir='assets')