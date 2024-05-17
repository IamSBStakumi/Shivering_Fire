import sys
import pygame

def main():
    # pygame初期化
    pygame.init()
    # メイン画面の初期化
    main_surface = pygame.display.set_mode((980, 600))
    # メイン画面のタイトル
    pygame.display.set_caption("シヴァリング・ファイア  Shivering_Fire")
    # フォントオブジェクト生成
    # フォント名をNoneにすると既定のフォント
    font = pygame.font.Font(None, 30)

    # テキストのSerfaceオブジェクトを生成(テキスト内容, antialias, RGB)
    text_serface = font.render("Hello, World", True, (0,0,255))
    # メイン画面の色
    main_surface.fill((220, 220, 220))
    # メイン画面にテキストを配置(配置するserface, 座標)
    main_surface.blit(text_serface, (100, 100))
    # メイン画面の更新
    pygame.display.update()
    # Clockオブジェクトの生成
    clock = pygame.time.Clock()

    # ループを続けるためのフラグ
    is_roop = True
    # 終了イベントまでループを回す
    while is_roop:
        # イベントを取得
        for event in pygame.event.get():
            # 終了イベント（×クリック）でループを抜ける
            if event.type == pygame.QUIT:
                is_roop = False
        
        # フレームレートの設定
        clock.tick(10)

    # 終了処理
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()