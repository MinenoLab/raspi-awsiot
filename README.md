# raspi-awsiot
## 概要
Raspberry PiからAWS IoTを利用するサンプルプログラムです。
## ファイル説明
* sendTemp.py
    * AWS IoTにAM2302で取得した温度データを送信するプログラムです。
* ControlValve.py
    * AWS IoTにAM2302で取得した温度データを送信し、電磁弁の開閉指示を受け取るプログラムです。
* tmp36.py
    * raspiberry piから温度センサーTMP36を使用するライブラリです。
* sendTemp_tmp36.py
    * sendTemp.pyをTMP36で実装したものです。
* ControlValve_tmp36.py
    * ControlValve.pyをTMP36で実装したものです。
