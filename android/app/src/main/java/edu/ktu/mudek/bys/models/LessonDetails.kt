package edu.ktu.mudek.bys.models

import com.google.gson.annotations.Expose
import com.google.gson.annotations.SerializedName

class LessonDetails {

    @SerializedName("id")
    @Expose
    var id: Int? = null
    @SerializedName("user")
    @Expose
    var user: Int? = null
    @SerializedName("lesson_name")
    @Expose
    var lessonName: String? = null
    @SerializedName("lesson_content")
    @Expose
    var lessonContent: String? = null
    @SerializedName("lesson_content_file")
    @Expose
    var lessonContentFile: Any? = null
    @SerializedName("lesson_notes")
    @Expose
    var lessonNotes: String? = null
    @SerializedName("lesson_notes_file")
    @Expose
    var lessonNotesFile: Any? = null

    fun withId(id: Int?): LessonDetails {
        this.id = id
        return this
    }

    fun withUser(user: Int?): LessonDetails {
        this.user = user
        return this
    }

    fun withLessonName(lessonName: String): LessonDetails {
        this.lessonName = lessonName
        return this
    }

    fun withLessonContent(lessonContent: String): LessonDetails {
        this.lessonContent = lessonContent
        return this
    }

    fun withLessonContentFile(lessonContentFile: Any): LessonDetails {
        this.lessonContentFile = lessonContentFile
        return this
    }

    fun withLessonNotes(lessonNotes: String): LessonDetails {
        this.lessonNotes = lessonNotes
        return this
    }

    fun withLessonNotesFile(lessonNotesFile: Any): LessonDetails {
        this.lessonNotesFile = lessonNotesFile
        return this
    }

}