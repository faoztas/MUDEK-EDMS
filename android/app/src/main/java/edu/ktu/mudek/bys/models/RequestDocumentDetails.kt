package edu.ktu.mudek.bys.models

import com.google.gson.annotations.Expose
import com.google.gson.annotations.SerializedName

class RequestDocumentDetails {

    @SerializedName("id")
    @Expose
    var id: Int? = null
    @SerializedName("lesson")
    @Expose
    var lesson: Int? = null
    @SerializedName("d_name")
    @Expose
    var dName: String? = null
    @SerializedName("d_bool")
    @Expose
    var dBool: Boolean? = null

    fun withId(id: Int?): RequestDocumentDetails {
        this.id = id
        return this
    }

    fun withLesson(lesson: Int?): RequestDocumentDetails {
        this.lesson = lesson
        return this
    }

    fun withDName(dName: String): RequestDocumentDetails {
        this.dName = dName
        return this
    }

    fun withDBool(dBool: Boolean?): RequestDocumentDetails {
        this.dBool = dBool
        return this
    }

}