import flet as ft
import datetime
import os

def main(page: ft.Page):
    page.title = "智慧主力籌碼看板系統"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0

    stock_pool = [
        {"id": "2330", "name": "台積電", "trend": "主力持續買超，控盤強勢", "predict": "看多 🚀", "post_close": "收盤驗證：拉尾盤符合預期，外資大買2萬張。"},
        {"id": "2317", "name": "鴻海", "trend": "主力高檔洗盤，籌碼略為分散", "predict": "震盪 ⚖️", "post_close": "收盤驗證：開高走低，投信小賣，維持區間震盪。"},
        {"id": "2454", "name": "聯發科", "trend": "外資反手賣超，自營商力挺", "predict": "偏空 📉", "post_close": "收盤驗證：中場跌破均線，主力避險情緒重。"},
    ]

    content_area = ft.Container(expand=True, padding=15)

    def show_stock_detail(stock):
        content_area.content = ft.Column([
            ft.Row([
                ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda _: show_pool_page()),
                ft.Text(f"{stock['name']} ({stock['id']})", size=22, weight=ft.FontWeight.BOLD)
            ]),
            ft.Divider(),
            ft.Card(content=ft.Container(padding=15, content=ft.Column([ft.Text("📊 籌碼動向", size=14, color=ft.Colors.BLUE_200), ft.Text(stock['trend'], size=16, weight=ft.FontWeight.BOLD)]))),
            ft.Card(content=ft.Container(padding=15, content=ft.Column([ft.Text("🔮 預測", size=14, color=ft.Colors.ORANGE_200), ft.Text(stock['predict'], size=18, weight=ft.FontWeight.BOLD)]))),
        ], scroll=ft.ScrollMode.AUTO)
        page.update()

    def show_pool_page():
        stock_list = ft.Column(scroll=ft.ScrollMode.AUTO, spacing=10)
        for stock in stock_pool:
            stock_list.controls.append(
                ft.Container(
                    content=ft.Row([
                        ft.Column([ft.Text(stock['name'], size=16, weight=ft.FontWeight.BOLD), ft.Text(stock['id'], size=12, color=ft.Colors.GREY_400)], expand=True),
                        # 這裡修正了語法：使用 ft.padding.symmetric
                        ft.Container(content=ft.Text(stock['predict'], size=12, weight=ft.FontWeight.BOLD), bgcolor=ft.Colors.GREY_800, padding=ft.padding.symmetric(horizontal=10, vertical=5), border_radius=5),
                        ft.IconButton(ft.Icons.CHEVRON_RIGHT, on_click=lambda e, s=stock: show_stock_detail(s))
                    ]),
                    padding=10, border=ft.border.all(1, ft.Colors.GREY_800), border_radius=8
                )
            )
        content_area.content = ft.Column([
            ft.Text("核心監測股池", size=20, weight=ft.FontWeight.BOLD),
            ft.Container(content=stock_list, expand=True)
        ])
        page.update()

    page.add(content_area)
    show_pool_page()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    # 使用 run() 是最新版的建議方式
    ft.app(target=main, host="0.0.0.0", port=port)
