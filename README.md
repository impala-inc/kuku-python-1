# kuku-python-1

見よう見まねで学ぶプログラミング

## 準備

### パソコンにソフトをインストールしない場合

ブラウザ上でPythonを実行できる
https://replit.com
または
https://colab.research.google.com を使用します（Googleアカウントなどでのログインが必要です）。

### パソコンにソフトをインストールする場合

#### Python

- 本講座で使用するプログラミング言語

Windowsの場合: https://www.python.jp/install/windows/index.html

Macの場合: https://www.python.jp/install/macos/index.html

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

課題は算数の九九のように1から9の段にそれぞれ9問づつあります
1の段（x_1_1〜）から9の段（〜x_9_9）まで段ごとに正解を見ずに解けるまで繰り返します
正解は `answers` フォルダーの中の同名のファイルにあります

それぞれの問題ごとに以下のことを繰り返します

- まず問題文を実行してみる
- 何が起きているのかを観察する
- 何が起きているのかを推測する
- 課題にしたがってコードを追加や修正する
- さらに自分なりにアレンジしてみる

## 各段の内容

### 1 の段

「文字列（str）」というデータの型とデータの入れ物となる「変数」について学習します

### 2 の段

「数値（int,float）」というデータの型とさまざまな計算について学習します

### 3 の段

正しいか正しくないかを扱う「真偽値（boolean）」というデータの型とそれを利用した「条件文」について学習します

### 4 の段

「真偽値」を利用した「繰り返し」について学習します

### 5 の段

「リスト（list）」というデータの型とそれを利用した「繰り返し」について学習します

### 6 の段

「リスト」の中に「リスト」が存在するデータとそれを利用した「多重ループ」について学習します

### 7 の段

「辞書（dict）」というデータの型とそれを利用したチャットボットを作ってみます

### 8 の段

データを「時間」や「ランダムな値」から取得することでプログラミングの活用範囲を広げます

### 9 の段

データを「ファイル」から読み込んだり、書き込むことでプログラミングの活用範囲を広げます

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
