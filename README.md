# raspi-awsiot
## 概要
Raspberry PiからAWS IoTを利用するサンプルプログラムです。
## ファイル説明
* tmp36.py
    * raspiberry piから温度センサーTMP36を使用するライブラリです。
* sendTemp.py
    * AWS IoTにTMP36で取得した温度データを送信するプログラムです。
* ContorolValve.py
    * AWS IoTにTMP36で取得した温度データを送信し、電磁弁の開閉指示を受け取るプログラムです。
