package edu.ktu.mudek.bys.network

import okhttp3.OkHttpClient
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

object BysApiClient {

    const val mainUrl = "http://mhproje.ktu.edu.tr:8000/api/"
    var userToken = ""

    private val okHttpClient = OkHttpClient.Builder()
            .addInterceptor {chain ->
                val original = chain.request()

                val requestBuilder = original.newBuilder()
                        .addHeader("Authorization", "Token "+userToken)
                        .method(original.method(),original.body())

                val request = requestBuilder.build()
                chain.proceed(request)
            }.build()

    val instance: BysApiInterface by lazy {
        val retrofit = Retrofit.Builder()
                .baseUrl(mainUrl)
                .addConverterFactory(GsonConverterFactory.create())
                .client(okHttpClient)
                .build()

        retrofit.create(BysApiInterface::class.java)
    }
    val login: BysApiInterface by lazy {
        val retrofit = Retrofit.Builder()
                .baseUrl(mainUrl)
                .addConverterFactory(GsonConverterFactory.create())
                .build()

        retrofit.create(BysApiInterface::class.java)
    }
}