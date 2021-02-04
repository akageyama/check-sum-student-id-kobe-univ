# 神戸大学の（学部学生）学籍番号チェックサム確認スクリプト

陰山 聡 (Akira Kageyama)

注意: 今のところ例外は見つかっていないが、このチェックサムアルゴリズムは私の推測である

- 学績番号は7桁の数字に一桁のアルファベットを加えたもの

- 左からi桁目の数字をNiとする

- N3がチェックディジット

- アルゴリズムは以下の通りらしい

```
   m = ( 4*N1+5*N2+6*N4+7*N5+8*N6+9*N7 ) % 11

   if (m==10)
     チェックディジット = 0
   else if (m==0)
     チェックディジット = 1
   else
     チェックディジット = m
```            
