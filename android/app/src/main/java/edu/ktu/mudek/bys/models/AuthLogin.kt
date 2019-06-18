package edu.ktu.mudek.bys.models


import com.google.gson.annotations.SerializedName

data class AuthLogin(
        @SerializedName("auth_token")
        val authToken: String? // 1cee95f3c058454853311c3b78c6cdf037e177c5
)