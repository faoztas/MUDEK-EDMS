package edu.ktu.mudek.bys.models

import com.google.gson.annotations.Expose
import com.google.gson.annotations.SerializedName

class Exams {

    @SerializedName("id")
    @Expose
    var id: Int? = null
    @SerializedName("lesson")
    @Expose
    var lesson: Int? = null
    @SerializedName("exam_type")
    @Expose
    var examType: String? = null
    @SerializedName("exam_information")
    @Expose
    var examInformation: String? = null
    @SerializedName("exam_file")
    @Expose
    var examFile: Any? = null
    @SerializedName("exam_answer_file")
    @Expose
    var examAnswerFile: Any? = null

    fun withId(id: Int?): Exams {
        this.id = id
        return this
    }

    fun withLesson(lesson: Int?): Exams {
        this.lesson = lesson
        return this
    }

    fun withExamType(examType: String): Exams {
        this.examType = examType
        return this
    }

    fun withExamInformation(examInformation: String): Exams {
        this.examInformation = examInformation
        return this
    }

    fun withExamFile(examFile: Any): Exams {
        this.examFile = examFile
        return this
    }

    fun withExamAnswerFile(examAnswerFile: Any): Exams {
        this.examAnswerFile = examAnswerFile
        return this
    }

}