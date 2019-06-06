package edu.ktu.mudek.bys.models

import com.google.gson.annotations.Expose
import com.google.gson.annotations.SerializedName

class Lessons {

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
    var lessonContentFile: String? = null
    @SerializedName("lesson_notes")
    @Expose
    var lessonNotes: String? = null
    @SerializedName("lesson_notes_file")
    @Expose
    var lessonNotesFile: Any? = null

    fun withId(id: Int?): Lessons {
        this.id = id
        return this
    }

    fun withUser(user: Int?): Lessons {
        this.user = user
        return this
    }

    fun withLessonName(lessonName: String): Lessons {
        this.lessonName = lessonName
        return this
    }

    fun withLessonContent(lessonContent: String): Lessons {
        this.lessonContent = lessonContent
        return this
    }

    fun withLessonContentFile(lessonContentFile: String): Lessons {
        this.lessonContentFile = lessonContentFile
        return this
    }

    fun withLessonNotes(lessonNotes: String): Lessons {
        this.lessonNotes = lessonNotes
        return this
    }

    fun withLessonNotesFile(lessonNotesFile: Any): Lessons {
        this.lessonNotesFile = lessonNotesFile
        return this
    }

}