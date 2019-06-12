package edu.ktu.mudek.bys.models


import com.google.gson.annotations.SerializedName

data class LessonDetails(
        @SerializedName("id")
        val id: Int?, // 1
        @SerializedName("lesson_content")
        val lessonContent: String?, // Sayısal sistemlerin üstünlükleri Bilgilerin sayısal gösterimi, Sayı sistemleri, tam ve kesirli sayıların gösterimi, Boole cebiri, Boole fonksiyonların cebirsel ve Karnough diyagramlarıyla indirgenmesi. Lojik kapılar. Sabit-noktalı aritmetik: Toplama, ileri- eldeli toplama, çıkarma, çarpma. Booth çarpma algoritması. Restoring ve nonrestoring bölme. Onlu aritmetik. Kayan- noktalı biçim, kutuplu üs, normalizasyon, taşma, kayan-noktalı sayıların dört işlemi. Bilgisayarın genel yapısı. İşletim sistemleri hakkında genel bilgiler. Assembly dili.
        @SerializedName("lesson_content_file")
        val lessonContentFile: Any?, // null
        @SerializedName("lesson_name")
        val lessonName: String?, // BİLGİSAYARIN TEMELLERİ
        @SerializedName("lesson_notes")
        val lessonNotes: String?,
        @SerializedName("lesson_notes_file")
        val lessonNotesFile: Any?, // null
        @SerializedName("user")
        val user: Int? // 2
)