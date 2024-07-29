import flet as ft
from flet import colors
from flet import icons

def __n(e):
    ... 

def app(page: ft.Page):

    def escurecer(e):
        if e.control.content.color == colors.BLACK26:
            e.control.content.color = colors.BLACK
            page.update()
        else:
            e.control.content.color = colors.BLACK26
            page.update()


    page.title = 'Login User'
    page.scroll = True
    page.window.width = 500
    page.window.height = 850
    page.window.resizable = False
    page.fonts = {
        'LeagueSpartan': 'fonts/LeagueSpartan/LeagueSpartan-Bold.ttf',
        'LeagueSpartan2': 'fonts/LeagueSpartan/LeagueSpartan.ttf'
    }
    _sett = ft.Row(
        [
            ft.Container(
                content = ft.Icon(icons.SETTINGS, color=colors.BLACK),
                bgcolor=colors.WHITE,
                width=64,
                height=64,
                border_radius=100,
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=10,
                    offset=ft.Offset(0, 0),
                    color= ft.colors.BLUE_GREY_300,
                    blur_style=ft.ShadowBlurStyle.OUTER
                ),
                alignment=ft.Alignment(x=-0.25, y=0.2),
                on_click= lambda e: __n(e),
                on_hover = lambda e: escurecer(e),
                
            ),

        ],
        alignment='end'
    )

    title = ft.Row(
        [
            ft.Text(
                value='Hello.',
                size=50,
                color=colors.BLACK,
                font_family='LeagueSpartan',
            ),
            
        ],
        alignment='center'
    )
    
    sub_title = ft.Row(
        [
            ft.Text(
                value='Welcome to our app.',
                size=25,
                color=colors.BLACK,
                font_family='LeagueSpartan2',
            ),
            
        ],
        alignment='center'
    )
    
    image = ft.Image(src='images/img_logo.png', width=150, height=106)

    entries = ft.Row(
        [
            ft.Container(
                content = ft.Column(
                    [  
                        ft.Row(
                            [
                                
                            ]
                        ), 
                        ft.Row(
                            [image],
                            alignment='center',
                            spacing=20
                        ),
                        ft.Row(
                            [
                                ft.TextField(
                                    label='Your e-mail',
                                    width=300,
                                    border_radius=20,
                                    border_color= colors.BLUE_GREY_100,
                                    color=colors.BLACK,
                                )
                            ],
                            alignment='center',
                            
                        ),
                        
                        ft.Row(
                            [
                                ft.TextField(
                                    label='Your password',
                                    width=300,
                                    border_radius=20,
                                    border_color= colors.BLUE_GREY_100,
                                    password=True,
                                    can_reveal_password=True,
                                    color=colors.BLACK
                                )
                            ],
                            alignment='center'
                        )
                        ,

                        ft.Row(
                            [   ft.Text('         '),
                                ft.Checkbox(
                                    label='Remenber account',
                                    check_color='#e6faf0',
                                    active_color='#00de6f',
                                    hover_color= colors.BLUE_GREY_100,
                                    focus_color='#00de6f'
                                )
                            ],
                            alignment=ft.MainAxisAlignment.START
                        ),

                        ft.Row(
                            [
                                ft.ElevatedButton(
                                    text='Create an account',
                                    bgcolor='#00de6f',
                                    color = '#e6faf0',
                                    height=50,
                                    width=150,

                                ),

                                ft.ElevatedButton(
                                    text='Login',
                                    bgcolor='#1fadff',
                                    color = '#e6faf0',
                                    height=50,
                                    width=150,

                                )
                            ],
                            alignment='center'
                        ),

                        ft.Row(
                            [
                                ft.Text(
                                    value='© Copyright 2024-2024 | LOGIN PAGE',
                                    color='#7e807e'
                                )
                            ],
                            alignment='center'
                        )

                    ],
                        spacing=30
                ),
                bgcolor=colors.WHITE,
                width=400,
                height=600,
                border_radius=40,
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=10,
                    offset=ft.Offset(0, 0),
                    color= ft.colors.BLUE_GREY_300,
                    blur_style=ft.ShadowBlurStyle.OUTER
                ),
                
            )
        ],
        alignment='center'
    )
    
    _main_col = ft.Column()
    
    _main_col.controls.append(_sett)
    _main_col.controls.append(title)
    _main_col.controls.append(sub_title)
    _main_col.controls.append(entries)

    bg = ft.Container(
        height=850,
        margin=-30,
        gradient=ft.LinearGradient(
            begin=ft.alignment.bottom_right,
            end=ft.alignment.top_left,
            colors=['#05fc81', '#e6faf0']
        ),
        content=_main_col
    )

    page.add(
        bg
    )

if __name__ == '__main__':
    ft.app(target=app, assets_dir='assets')