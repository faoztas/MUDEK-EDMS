package edu.ktu.mudek.bys.models


import com.google.gson.annotations.SerializedName

data class RequestDocumentDetails(
        @SerializedName("d_bool")
        val dBool: Boolean?, // false
        @SerializedName("d_name")
        val dName: String?, // Ders İçeriği
        @SerializedName("id")
        val id: Int?, // 1
        @SerializedName("lesson")
        val lesson: Int? // 1
)