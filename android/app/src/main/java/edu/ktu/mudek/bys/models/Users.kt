package edu.ktu.mudek.bys.models

import com.google.gson.annotations.Expose
import com.google.gson.annotations.SerializedName

class Users {

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

    fun withId(id: Int?): Users {
        this.id = id
        return this
    }

    fun withEmail(email: String): Users {
        this.email = email
        return this
    }

    fun withFirstName(firstName: String): Users {
        this.firstName = firstName
        return this
    }

    fun withLastName(lastName: String): Users {
        this.lastName = lastName
        return this
    }

}