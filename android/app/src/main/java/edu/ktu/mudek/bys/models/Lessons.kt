package edu.ktu.mudek.bys.models


import com.google.gson.annotations.SerializedName

data class Lessons(
        @SerializedName("id")
        val id: Int?, // 3
        @SerializedName("lesson_content")
        val lessonContent: String?,
        @SerializedName("lesson_content_file")
        val lessonContentFile: String?, // http://127.0.0.1:8000/media/user_2/BMD_Sistem_Modelleri.doc
        @SerializedName("lesson_name")
        val lessonName: String?, // Bilgisayar Organizasyon Lab
        @SerializedName("lesson_notes")
        val lessonNotes: String?,
        @SerializedName("lesson_notes_file")
        val lessonNotesFile: Any?, // null
        @SerializedName("user")
        val user: Int? // 2
)