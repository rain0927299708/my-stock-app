import flet as ft

def main(page: ft.Page):
    # 設置頁面標題
    page.title = "Flet App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # 正確的 Padding 寫法：使用 ft.padding.symmetric
    # 這裡示範一個 Container，它使用了正確的 padding 屬性
    container = ft.Container(
        content=ft.Text("應用程式已成功啟動！", size=20),
        padding=ft.padding.symmetric(vertical=20, horizontal=20),
        bgcolor=ft.colors.BLUE_100,
        border_radius=10,
    )

    page.add(container)

# 確保在 Render 上運行的正確入口點
if __name__ == "__main__":
    ft.app(target=main)
