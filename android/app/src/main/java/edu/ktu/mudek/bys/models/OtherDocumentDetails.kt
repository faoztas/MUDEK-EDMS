package edu.ktu.mudek.bys.models

import com.google.gson.annotations.Expose
import com.google.gson.annotations.SerializedName

class OtherDocumentDetails {

    @SerializedName("id")
    @Expose
    var id: Int? = null
    @SerializedName("lesson")
    @Expose
    var lesson: Int? = null
    @SerializedName("course_evaluation_form")
    @Expose
    var courseEvaluationForm: String? = null
    @SerializedName("course_survey")
    @Expose
    var courseSurvey: String? = null
    @SerializedName("exam_note_list_midterm")
    @Expose
    var examNoteListMidterm: Any? = null
    @SerializedName("exam_note_list_end_of_term")
    @Expose
    var examNoteListEndOfTerm: Any? = null
    @SerializedName("exam_note_list_Integrated")
    @Expose
    var examNoteListIntegrated: Any? = null

    fun withId(id: Int?): OtherDocumentDetails {
        this.id = id
        return this
    }

    fun withLesson(lesson: Int?): OtherDocumentDetails {
        this.lesson = lesson
        return this
    }

    fun withCourseEvaluationForm(courseEvaluationForm: String): OtherDocumentDetails {
        this.courseEvaluationForm = courseEvaluationForm
        return this
    }

    fun withCourseSurvey(courseSurvey: String): OtherDocumentDetails {
        this.courseSurvey = courseSurvey
        return this
    }

    fun withExamNoteListMidterm(examNoteListMidterm: Any): OtherDocumentDetails {
        this.examNoteListMidterm = examNoteListMidterm
        return this
    }

    fun withExamNoteListEndOfTerm(examNoteListEndOfTerm: Any): OtherDocumentDetails {
        this.examNoteListEndOfTerm = examNoteListEndOfTerm
        return this
    }

    fun withExamNoteListIntegrated(examNoteListIntegrated: Any): OtherDocumentDetails {
        this.examNoteListIntegrated = examNoteListIntegrated
        return this
    }

}