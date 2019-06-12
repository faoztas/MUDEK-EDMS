package edu.ktu.mudek.bys.models


import com.google.gson.annotations.SerializedName

data class Exams(
        @SerializedName("exam_answer_file")
        val examAnswerFile: Any?, // null
        @SerializedName("exam_file")
        val examFile: Any?, // null
        @SerializedName("exam_type")
        val examType: String?, // Arasınav
        @SerializedName("exam_information")
        val examInformation: String?, // Bilgisayarların nasıl çalıştığıyla ilgili temel bilgileri öğrenciye kazandırmak ve bilgisayarın yazılım ve donanım öğelerininin kavramsal olarak anlaşılmasını sağlamak ve tanıtmaktır. Bilgisayar açıldığı zaman komut kabul edeceği düzeye gelinceye kadar yaptığı işleri ve işletim sisteminin çalışması anlatılacaktır.
        @SerializedName("id")
        val id: Int?, // 1
        @SerializedName("lesson")
        val lesson: Int? // 1
)