package edu.ktu.mudek.bys.network

import edu.ktu.mudek.bys.models.*
import retrofit2.Call
import retrofit2.http.GET
import retrofit2.http.Path

interface BysApiInterface {
    @GET("users/")
    fun getUsers(): Call<Users>

    @GET("users/{id}/")
    fun getUserDetails(@Path(
            "id") id: Int): Call<UserDetails>

    @GET("lessons/")
    fun getLessons(): Call<Lessons>

    @GET("lessons/{id}/")
    fun getLessonDetails(@Path(
            "id") id: Int): Call<LessonDetails>

    @GET("exams/")
    fun getExams(): Call<Exams>

    @GET("exams/{id}/")
    fun getExamDetails(@Path(
            "id") id: Int): Call<ExamDetails>

    @GET("other-documents/")
    fun getOtherDocuments(): Call<OtherDocuments>

    @GET("other-documents/{id}/")
    fun getOtherDocumentDetails(@Path(
            "id") id: Int): Call<OtherDocumentDetails>

    @GET("request-documents/")
    fun getRequestDocuments(): Call<RequestDocuments>

    @GET("request-documents/{id}/")
    fun getRequestDocumentDetails(@Path(
            "id") id: Int): Call<RequestDocumentDetails>
}