import tkinter as tk

# スライダーでRGB値を指定して返すGUI
class RGB_slider_GUI:
    def __init__(self, description):
        self.description = description # 「何の色を選択させているか（下地・柄の色1・柄の色2）」を受け取り、説明をウィンドウ内に表示する
    def main(self):
        def confirm_color():
            print("Button clicked!")

            slider_window.quit()

        # ウィンドウの作成
        slider_window = tk.Tk()
        slider_window.title('色選択')
        slider_window.geometry('256x270')
        slider_window.resizable(False, False)

        def update_color(r, g, b):
            color = f'#{r:02x}{g:02x}{b:02x}'
            canvas.config(bg=color)

        def on_scale_r(val):
            r = int(val)
            g = scale_g.get()
            b = scale_b.get()
            update_color(r, g, b)

        def on_scale_g(val):
            r = scale_r.get()
            g = int(val)
            b = scale_b.get()
            update_color(r, g, b)

        def on_scale_b(val):
            r = scale_r.get()
            g = scale_g.get()
            b = int(val)
            update_color(r, g, b)


        #
        description_text = tk.Label(slider_window, text = f'{self.description}の色を選択してください')
        description_text.place(x = 0, y = 10)

        # スライダーの作成
        scale_r = tk.Scale(slider_window, from_ = 255, to_ = 0, label='R', command=on_scale_r)
        scale_r.place(x = 0, y = 34)
        scale_g = tk.Scale(slider_window, from_ = 255, to_ = 0, label='G', command=on_scale_g)
        scale_g.place(x = 85, y = 34)
        scale_b = tk.Scale(slider_window, from_ = 255, to_ = 0, label='B', command=on_scale_b)
        scale_b.place(x = 170, y = 34)

        # キャンバスの作成
        label = tk.Label(slider_window, text = '色見本')
        label.place(x = 0, y = 144)
        canvas = tk.Canvas(slider_window, width=100, height=100, bg='#000000')
        canvas.place(x = 0, y = 164)

        # 決定ボタン
        confirm_button = tk.Button(slider_window, text='決定', command=confirm_color)
        confirm_button.place (x = 210, y = 234)

        # ウィンドウの表示
        slider_window.mainloop()

        # 終了時、ユーザーに指定されたRGB値を返す
        rgb = (scale_r.get(), scale_g.get(), scale_b.get())
        return rgb

# ui = RGB_slider_GUI
# print(ui.main())