package edu.ktu.mudek.bys.models


import com.google.gson.annotations.SerializedName

data class Users(
        @SerializedName("email")
        val email: String?, // ulutas@ktu.edu.tr
        @SerializedName("first_name")
        val firstName: String?, // Mustafa
        @SerializedName("id")
        val id: Int?, // 2
        @SerializedName("last_name")
        val lastName: String? // Ulutaş
)