package edu.ktu.mudek.bys.models


import com.google.gson.annotations.SerializedName

data class UserDetails(
        @SerializedName("email")
        val email: String?, // ulutas@ktu.edu.tr
        @SerializedName("first_name")
        val firstName: String?, // Mustafa
        @SerializedName("id")
        val id: Int?, // 2
        @SerializedName("is_academician")
        val isAcademician: Boolean?, // true
        @SerializedName("is_active")
        val isActive: Boolean?, // true
        @SerializedName("is_assistant_department_manager")
        val isAssistantDepartmentManager: Boolean?, // false
        @SerializedName("is_dean_manager")
        val isDeanManager: Boolean?, // false
        @SerializedName("is_department_manager")
        val isDepartmentManager: Boolean?, // true
        @SerializedName("is_verified")
        val isVerified: Boolean?, // true
        @SerializedName("last_name")
        val lastName: String? // Ulutaş
)