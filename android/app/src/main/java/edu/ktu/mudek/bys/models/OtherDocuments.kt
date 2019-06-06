package edu.ktu.mudek.bys.models

import com.google.gson.annotations.Expose
import com.google.gson.annotations.SerializedName

class OtherDocuments {

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

    fun withId(id: Int?): OtherDocuments {
        this.id = id
        return this
    }

    fun withLesson(lesson: Int?): OtherDocuments {
        this.lesson = lesson
        return this
    }

    fun withCourseEvaluationForm(courseEvaluationForm: String): OtherDocuments {
        this.courseEvaluationForm = courseEvaluationForm
        return this
    }

    fun withCourseSurvey(courseSurvey: String): OtherDocuments {
        this.courseSurvey = courseSurvey
        return this
    }

    fun withExamNoteListMidterm(examNoteListMidterm: Any): OtherDocuments {
        this.examNoteListMidterm = examNoteListMidterm
        return this
    }

    fun withExamNoteListEndOfTerm(examNoteListEndOfTerm: Any): OtherDocuments {
        this.examNoteListEndOfTerm = examNoteListEndOfTerm
        return this
    }

    fun withExamNoteListIntegrated(examNoteListIntegrated: Any): OtherDocuments {
        this.examNoteListIntegrated = examNoteListIntegrated
        return this
    }

}