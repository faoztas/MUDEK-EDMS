package edu.ktu.mudek.bys.ui

import android.content.Intent
import android.os.Bundle
import android.provider.AlarmClock.EXTRA_MESSAGE
import android.support.v7.app.AppCompatActivity
import android.view.View
import android.widget.EditText
import android.widget.TextView
import edu.ktu.mudek.scanner.R



open class LoginActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)
    }

    fun login(view: View) {

        val intent = Intent(this, FileActivity::class.java)
        val editText = findViewById(R.id.editUsername) as EditText
        val mesaj = editText.text.toString()
        intent.putExtra(EXTRA_MESSAGE, mesaj)
        startActivity(intent)

    }
    fun missPassword(view: View) {

        val intent = Intent(this, MisspassActivity::class.java)
        val textView = findViewById(R.id.textMissPassword) as TextView
        val mesaj = textView.text.toString()
        intent.putExtra(EXTRA_MESSAGE, mesaj)
        startActivity(intent)

    }

}