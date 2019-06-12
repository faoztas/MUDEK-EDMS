package edu.ktu.mudek.bys.models


import com.google.gson.annotations.SerializedName

data class OtherDocumentDetails(
        @SerializedName("course_evaluation_form")
        val courseEvaluationForm: String?, // http://127.0.0.1:8000/media/BMD_Sistem_Modelleri.doc
        @SerializedName("course_survey")
        val courseSurvey: String?, // http://127.0.0.1:8000/media/BMD_Sistem_Modelleri_4ZpUgzE.doc
        @SerializedName("exam_note_list_end_of_term")
        val examNoteListEndOfTerm: Any?, // null
        @SerializedName("exam_note_list_Integrated")
        val examNoteListIntegrated: Any?, // null
        @SerializedName("exam_note_list_midterm")
        val examNoteListMidterm: Any?, // null
        @SerializedName("id")
        val id: Int?, // 1
        @SerializedName("lesson")
        val lesson: Int? // 1
)