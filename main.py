import flet as ft
import datetime
import os

def main(page: ft.Page):
    page.title = "智慧主力籌碼看板系統"
    page.window_width = 390
    page.window_height = 844
    page.padding = 0
    page.theme_mode = ft.ThemeMode.DARK

    stock_pool = [
        {"id": "2330", "name": "台積電", "trend": "主力持續買超，控盤強勢", "predict": "看多 🚀", "post_close": "收盤驗證：拉尾盤符合預期，外資大買2萬張。"},
        {"id": "2317", "name": "鴻海", "trend": "主力高檔洗盤，籌碼略為分散", "predict": "震盪 ⚖️", "post_close": "收盤驗證：開高走低，投信小賣，維持區間震盪。"},
        {"id": "2454", "name": "聯發科", "trend": "外資反手賣超，自營商力挺", "predict": "偏空 📉", "post_close": "收盤驗證：中場跌破均線，主力避險情緒重。"},
        {"id": "2308", "name": "台達電", "trend": "關鍵券商急買，低檔現進貨訊號", "predict": "看多 🚀", "post_close": "收盤驗證：拉出長下影線，底部支撐強勁。"},
        {"id": "2382", "name": "廣達", "trend": "AI主力大戶獲利了結，賣壓沉重", "predict": "偏空 📉", "post_close": "收盤驗證：開盤即遭灌壓，尾盤量縮續跌。"},
        {"id": "3008", "name": "大立光", "trend": "主力連三日量縮築底", "predict": "震盪 ⚖️", "post_close": "收盤驗證：終場平盤打轉，等待法人明確表態。"},
        {"id": "2603", "name": "長榮", "trend": "航運主力點火，散戶融資大退", "predict": "看多 🚀", "post_close": "收盤驗證：突破波段高點，主力鎖碼完畢。"},
        {"id": "2881", "name": "富邦金", "trend": "官股券商護盤，籌碼相對穩健", "predict": "震盪 🚀", "post_close": "收盤驗證：金融撐盤，外資小幅調節不影響趨勢。"},
        {"id": "2324", "name": "仁寶", "trend": "隔日沖大戶進駐，防範假突破", "predict": "震盪 ⚖️", "post_close": "收盤驗證：早盤暴量衝高後急殺，標準隔日沖洗盤。"},
        {"id": "6415", "name": "矽力-KY", "trend": "主力與法人同步站在賣方", "predict": "偏空 📉", "post_close": "收盤驗證：弱勢續跌，短線籌碼尚未止穩。"},
    ]

    content_area = ft.Container(expand=True, padding=15)

    def show_stock_detail(stock):
        content_area.content = ft.Column([
            ft.Row([
                ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda _: show_pool_page()),
                ft.Text(f"{stock['name']} ({stock['id']})", size=22, weight=ft.FontWeight.BOLD)
            ]),
            ft.Divider(),
            ft.Card(content=ft.Container(padding=15, content=ft.Column([ft.Text("📊 開盤持續監測 (籌碼動向)", size=14, color=ft.Colors.BLUE_200), ft.Text(stock['trend'], size=16, weight=ft.FontWeight.BOLD)]))),
            ft.Card(content=ft.Container(padding=15, content=ft.Column([ft.Text("🔮 預測明日動向", size=14, color=ft.Colors.ORANGE_200), ft.Text(stock['predict'], size=18, weight=ft.FontWeight.BOLD)]))),
            ft.Card(content=ft.Container(padding=15, content=ft.Column([ft.Text("📝 收盤後修正與詳細數據", size=14, color=ft.Colors.GREEN_200), ft.Text(stock['post_close'], size=15, italic=True)]))),
        ], scroll=ft.ScrollMode.AUTO)
        page.update()

    def show_pool_page():
        stock_list = ft.Column(scroll=ft.ScrollMode.AUTO, spacing=10)
        for stock in stock_pool:
            badge_color = ft.Colors.RED_ACCENT if "看多" in stock['predict'] else (ft.Colors.GREEN_ACCENT if "偏空" in stock['predict'] else ft.Colors.GREY_400)
            stock_list.controls.append(
                ft.Container(
                    content=ft.Row([
                        ft.Column([ft.Text(stock['name'], size=16, weight=ft.FontWeight.BOLD), ft.Text(stock['id'], size=12, color=ft.Colors.GREY_400)], expand=True),
                        ft.Container(content=ft.Text(stock['predict'], size=12, color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD), bgcolor=badge_color, padding=ft.padding.symmetric(horizontal=8, vertical=4), border_radius=5),
                        ft.IconButton(ft.Icons.CHEVRON_RIGHT, on_click=lambda e, s=stock: show_stock_detail(s))
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    padding=12, border=ft.border.all(1, ft.Colors.GREY_800), border_radius=8, bgcolor=ft.Colors.SURFACE_VARIANT,
                )
            )
        content_area.content = ft.Column([
            ft.Row([ft.Text("我的核心監測股池", size=20, weight=ft.FontWeight.BOLD), ft.Text(f"({len(stock_pool)}/10 檔)", size=14, color=ft.Colors.GREY_400)], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Text(f"更新時間: {datetime.datetime.now().strftime('%Y-%m-%d')} 開盤持續監測中", size=12, color=ft.Colors.BLUE_300),
            ft.Divider(),
            ft.Container(content=stock_list, expand=True)
        ])
        page.update()

    page.add(content_area)
    show_pool_page()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, host="0.0.0.0", port=port)
