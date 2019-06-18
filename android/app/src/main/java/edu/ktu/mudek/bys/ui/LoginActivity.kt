package edu.ktu.mudek.bys.ui

import android.content.Intent
import android.content.pm.PackageManager
import android.os.Bundle
import android.provider.AlarmClock.EXTRA_MESSAGE
import android.support.v4.app.ActivityCompat
import android.support.v4.content.ContextCompat
import android.support.v7.app.AppCompatActivity
import android.view.View
import android.widget.EditText
import android.widget.TextView
import edu.ktu.mudek.R



open class LoginActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)
    }

    private val REQUEST_INTERNET_PERMISSION = 0

    fun login(view: View) {

        if (ContextCompat.checkSelfPermission(this, android.Manifest.permission.INTERNET) != PackageManager.PERMISSION_GRANTED &&
                ContextCompat.checkSelfPermission(this, android.Manifest.permission.ACCESS_NETWORK_STATE) != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(this, arrayOf(android.Manifest.permission.INTERNET, android.Manifest.permission.ACCESS_NETWORK_STATE), REQUEST_INTERNET_PERMISSION)
        } else if (ContextCompat.checkSelfPermission(this, android.Manifest.permission.INTERNET) != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(this, arrayOf(android.Manifest.permission.INTERNET), REQUEST_INTERNET_PERMISSION)
        } else if (ContextCompat.checkSelfPermission(this, android.Manifest.permission.ACCESS_NETWORK_STATE) != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(this, arrayOf(android.Manifest.permission.ACCESS_NETWORK_STATE), REQUEST_INTERNET_PERMISSION)
        }

        val intent = Intent(this, MainActivity::class.java)
        val editText = findViewById<EditText>(R.id.editUsername)
        val mesaj = editText.text.toString()
        intent.putExtra(EXTRA_MESSAGE, mesaj)
        startActivity(intent)

    }
    fun missPassword(view: View) {

        val intent = Intent(this, MissPassActivity::class.java)
        val textView = findViewById<TextView>(R.id.textMissPassword)
        val mesaj = textView.text.toString()
        intent.putExtra(EXTRA_MESSAGE, mesaj)
        startActivity(intent)


    }

}