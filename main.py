import flet as ft
# from flet import alignment
from time import sleep

def main(page: ft.Page):
    page.vertical_alignment = 'end'
    page.window_width = 300


    c = ft.Container(alignment=ft.alignment.center, width=300, height=1, bgcolor="green",
        # animate=ft.animation.Animation(5000, ft.AnimationCurve.EASE_IN_TO_LINEAR)
                        )
    a = ft.Column([c],alignment= 'center')
    a= ft.Row([c],alignment='center')

    def animate_container(e):
        # c.width = 100 if c.width == 150 else 150
        c.height = 50 if c.height == 150 else 150
        c.bgcolor = "blue" if c.bgcolor == "red" else "red"
        c.update()
    # page.add(c, ft.ElevatedButton("Animate container", on_click=animate_container))
    # while True:
    VALOR_MAXIMO = 650
    def Inspirar():
        page.add(a)
        inc = -1
        while c.height <= VALOR_MAXIMO:
            inc = inc+1
            sleep(0.02)  
            if inc == 0:  
                c.bgcolor = 'green'
                c.height = 0  
            c.height += 20
            c.update()            
            page.update()


    def Expirar():
        page.add(a)
        inc = -1
        while c.height >0:
            inc = inc+1
            sleep(0.07)  
            if inc == 0:  
                c.bgcolor = 'yellow'
                c.height = VALOR_MAXIMO  
            c.height -= 5
            c.update()            
            page.update()           
    
    while True:
        Inspirar()
        Expirar()
    # page.add(c)





ft.app(target=main, view=ft.AppView.WEB_BROWSER)
