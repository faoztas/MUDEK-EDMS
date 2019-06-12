package edu.ktu.mudek.bys.network

import okhttp3.OkHttpClient
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

object BysApiClient {

    private const val mainUrl = "http://127.0.0.1:8000/api/"
    private const val apiKey = ""
    private const val apiAuth = ""

    private val okHttpClient = OkHttpClient.Builder()
            .addInterceptor {chain ->
                val original = chain.request()

                val requestBuilder = original.newBuilder()
                        .addHeader("Auth", apiAuth)
                        .method(original.method(),original.body())

                val request = requestBuilder.build()
                chain.proceed(request)
            }.build()

    val instance: BysApiInterface by lazy {
        val retrofit = Retrofit.Builder()
                .baseUrl(mainUrl)
                .addConverterFactory(GsonConverterFactory.create())
                .build()

        retrofit.create(BysApiInterface::class.java)
    }
}