package edu.ktu.mudek.bys.models

import com.google.gson.annotations.Expose
import com.google.gson.annotations.SerializedName

class UserDetails {

    @SerializedName("id")
    @Expose
    var id: Int? = null
    @SerializedName("email")
    @Expose
    var email: String? = null
    @SerializedName("first_name")
    @Expose
    var firstName: String? = null
    @SerializedName("last_name")
    @Expose
    var lastName: String? = null
    @SerializedName("is_active")
    @Expose
    var isActive: Boolean? = null
    @SerializedName("is_verified")
    @Expose
    var isVerified: Boolean? = null
    @SerializedName("is_academician")
    @Expose
    var isAcademician: Boolean? = null
    @SerializedName("is_department_manager")
    @Expose
    var isDepartmentManager: Boolean? = null
    @SerializedName("is_assistant_department_manager")
    @Expose
    var isAssistantDepartmentManager: Boolean? = null
    @SerializedName("is_dean_manager")
    @Expose
    var isDeanManager: Boolean? = null

    fun withId(id: Int?): UserDetails {
        this.id = id
        return this
    }

    fun withEmail(email: String): UserDetails {
        this.email = email
        return this
    }

    fun withFirstName(firstName: String): UserDetails {
        this.firstName = firstName
        return this
    }

    fun withLastName(lastName: String): UserDetails {
        this.lastName = lastName
        return this
    }

    fun withIsActive(isActive: Boolean?): UserDetails {
        this.isActive = isActive
        return this
    }

    fun withIsVerified(isVerified: Boolean?): UserDetails {
        this.isVerified = isVerified
        return this
    }

    fun withIsAcademician(isAcademician: Boolean?): UserDetails {
        this.isAcademician = isAcademician
        return this
    }

    fun withIsDepartmentManager(isDepartmentManager: Boolean?): UserDetails {
        this.isDepartmentManager = isDepartmentManager
        return this
    }

    fun withIsAssistantDepartmentManager(isAssistantDepartmentManager: Boolean?): UserDetails {
        this.isAssistantDepartmentManager = isAssistantDepartmentManager
        return this
    }

    fun withIsDeanManager(isDeanManager: Boolean?): UserDetails {
        this.isDeanManager = isDeanManager
        return this
    }

}