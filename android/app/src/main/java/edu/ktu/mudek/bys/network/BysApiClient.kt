package edu.ktu.mudek.bys.network

import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

object BysApiClient {

    val mainUrl = "http://127.0.0.1:8000/api/"
    val apiKey = ""

    private var myRetrofit: Retrofit? = null

    fun getMyRetrofit(mainUrl: String): Retrofit? {

        if (myRetrofit == null) {

            myRetrofit = Retrofit.Builder()
                    .baseUrl(mainUrl)
                    .addConverterFactory(GsonConverterFactory.create())
                    .build()

        }
        return myRetrofit
    }
}