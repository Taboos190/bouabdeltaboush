#!/data/data/com.termux/files/usr/bin/bash

# تعريف المتغيرات
INPUT="input.mp4"
OUTPUT="output_bouabdel.mp4"
FONT="/system/fonts/Roboto-Regular.ttf"

# إضافة نص في البداية
ffmpeg -i $INPUT -vf "drawtext=fontfile=$FONT:text='بوعبدل طبوش يشكر كل من يريد تعلم البرمجة والتطوير والاختراق الأخلاقي':fontcolor=white:fontsize=40:box=1:boxcolor=black@0.7:boxborderw=10:x=(w-text_w)/2:y=50" -codec:a copy intro_$OUTPUT

# إضافة نص النهاية
ffmpeg -i intro_$OUTPUT -vf "drawtext=fontfile=$FONT:text='تابعنا: فيسبوك | واتساب | تليجرام':fontcolor=white:fontsize=30:x=(w-text_w)/2:y=h-th-50:enable='between(t,5,15)'" -codec:a copy $OUTPUT

# حذف الملف المؤقت
rm intro_$OUTPUT

echo "تم إنشاء الفيديو: $OUTPUT"
