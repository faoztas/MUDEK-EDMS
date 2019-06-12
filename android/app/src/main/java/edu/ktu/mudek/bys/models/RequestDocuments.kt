package edu.ktu.mudek.bys.models


import com.google.gson.annotations.SerializedName

data class RequestDocuments(
        @SerializedName("d_bool")
        val dBool: Boolean?, // true
        @SerializedName("d_name")
        val dName: String?, // Final Sınav Kağıdı
        @SerializedName("id")
        val id: Int?, // 4
        @SerializedName("lesson")
        val lesson: Int? // 1
)