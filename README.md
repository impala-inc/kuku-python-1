# kuku

見よう見まねで学ぶプログラミング

## 準備

### パソコンにソフトをインストールしない場合

ブラウザ上で Python を実行できる
https://replit.com
または
https://colab.research.google.com を使用します(Google アカウント などでのログインが必要です)。

### パソコンにソフトをインストールする場合

#### Python

- 本講座で使用するプログラミング言語

Windows の場合: https://www.python.jp/install/windows/index.html

Mac の場合: https://www.python.jp/install/macos/index.html

#### Visual Studio Code

- プログラミングを書くことに適したソフトウエア
- Microsoft が開発している

https://azure.microsoft.com/ja-jp/products/visual-studio-code/

##### Visual Studio Code の便利な拡張機能

- Japanese Language Pack for Visual Studio Code
- Python
- Code Spell Checker
- indent-rainbow

#### Git

- ファイルの変更履歴を記録でき、他人数でのソフトウエア開発を可能にする分散型バージョン管理システム
- 本講座では最新の問題の取得や一度回答した問題を回答前に戻すためなどに利用

https://git-scm.com

## 課題の進め方

課題は算数の九九のように 1 から 9 の段にそれぞれ 9 問づつあります
1 の段(x_1_1〜)から 9 の段(〜x_9_9)まで段ごとに正解を見ずに解けるまで繰り返します
正解は `answers` フォルダの中の同名のファイルにあります

それぞれの問題ごとに以下のことを繰り返します

- まず問題文を実行してみる
- 何が起きているのかを観察する
- 何が起きているのかを推測する
- 課題に従ってコードを追加や修正する
- さらに自分なりにアレンジしてみる

## ModuleNotFoundError と表示された場合

```
ModuleNotFoundError: No module named 'requests'
```

などのように表示された場合、必要なパッケージがインストールされていません。
以下を参考に `pip` でインストールしましょう

### Windows の場合

https://www.python.jp/install/windows/pip.html

### Mac の場合

https://www.python.jp/install/macos/pip.html
