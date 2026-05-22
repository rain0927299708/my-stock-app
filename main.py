import flet as ft
import os

def main(page: ft.Page):
    page.title = "智慧主力籌碼看板系統"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0

    # 監測股池數據
    stock_pool = [
        {"id": "2330", "name": "台積電", "trend": "主力買超", "predict": "看多 🚀"},
        {"id": "2317", "name": "鴻海", "trend": "主力洗盤", "predict": "震盪 ⚖️"},
        {"id": "2454", "name": "聯發科", "trend": "主力賣超", "predict": "偏空 📉"},
    ]

    content_area = ft.Container(expand=True, padding=15)

    def show_stock_detail(stock):
        content_area.content = ft.Column([
            ft.Row([
                ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda _: show_pool_page()),
                ft.Text(f"{stock['name']} ({stock['id']})", size=22, weight=ft.FontWeight.BOLD)
            ]),
            ft.Divider(),
            ft.Card(content=ft.Container(padding=15, content=ft.Column([ft.Text("📊 籌碼動向", size=14), ft.Text(stock['trend'], size=16)]))),
            ft.Card(content=ft.Container(padding=15, content=ft.Column([ft.Text("🔮 預測", size=14), ft.Text(stock['predict'], size=18)]))),
        ])
        page.update()

    def show_pool_page():
        stock_list = ft.Column(scroll=ft.ScrollMode.AUTO, spacing=10)
        for stock in stock_pool:
            stock_list.controls.append(
                ft.Container(
                    content=ft.Row([
                        ft.Column([ft.Text(stock['name'], size=16), ft.Text(stock['id'], size=12)], expand=True),
                        # 修正關鍵：使用 ft.padding.symmetric，避免舊語法錯誤
                        ft.Container(content=ft.Text(stock['predict'], size=12), bgcolor=ft.Colors.GREY_800, padding=ft.padding.symmetric(horizontal=10, vertical=5), border_radius=5),
                        ft.IconButton(ft.Icons.CHEVRON_RIGHT, on_click=lambda e, s=stock: show_stock_detail(s))
                    ]),
                    padding=10, border=ft.border.all(1, ft.Colors.GREY_800), border_radius=8
                )
            )
        content_area.content = ft.Column([ft.Text("核心監測股池", size=20, weight=ft.FontWeight.BOLD), ft.Container(content=stock_list, expand=True)])
        page.update()

    page.add(content_area)
    show_pool_page()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    # 使用正確的入口函式
    ft.app(target=main, host="0.0.0.0", port=port)
