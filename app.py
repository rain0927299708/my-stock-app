import flet as ft

def main(page: ft.Page):
    # 設定頁面標題
    page.title = "我的 Flet 應用程式"
    
    # 設置頁面基礎佈局
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # 這裡使用了正確的 ft.padding.symmetric
    # 這就是解決你錯誤訊息的關鍵點
    container = ft.Container(
        content=ft.Text("應用程式運行正常！", size=24, color=ft.colors.WHITE),
        padding=ft.padding.symmetric(vertical=20, horizontal=20),
        bgcolor=ft.colors.BLUE_700,
        border_radius=15,
        alignment=ft.alignment.center
    )

    page.add(container)

# 這是 Render 部署時必須的正確入口
if __name__ == "__main__":
    ft.app(target=main, port=8080)
