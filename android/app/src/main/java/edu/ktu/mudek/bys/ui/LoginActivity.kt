package edu.ktu.mudek.bys.ui

import android.content.Intent
import android.content.pm.PackageManager
import android.os.Bundle
import android.provider.AlarmClock.EXTRA_MESSAGE
import android.support.v4.app.ActivityCompat
import android.support.v4.content.ContextCompat
import android.support.v7.app.AppCompatActivity
import android.util.Log
import android.view.View
import android.widget.EditText
import android.widget.TextView
import android.widget.Toast
import edu.ktu.mudek.R
import edu.ktu.mudek.bys.adapters.LessonsAdapter
import edu.ktu.mudek.bys.models.AuthLogin
import edu.ktu.mudek.bys.models.Lessons
import edu.ktu.mudek.bys.network.BysApiClient
import kotlinx.android.synthetic.main.activity_login.*
import kotlinx.android.synthetic.main.fragment_home.*
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response


open class LoginActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)
    }

    private val REQUEST_INTERNET_PERMISSION = 0

    fun login(view: View) {

        val eUserName = findViewById<EditText>(R.id.editUsername)
        val ePassword = findViewById<EditText>(R.id.editPassword)
        val intent = Intent(this, MainActivity::class.java)


        if (ContextCompat.checkSelfPermission(this, android.Manifest.permission.INTERNET) != PackageManager.PERMISSION_GRANTED &&
                ContextCompat.checkSelfPermission(this, android.Manifest.permission.ACCESS_NETWORK_STATE) != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(this, arrayOf(android.Manifest.permission.INTERNET, android.Manifest.permission.ACCESS_NETWORK_STATE), REQUEST_INTERNET_PERMISSION)
        } else if (ContextCompat.checkSelfPermission(this, android.Manifest.permission.INTERNET) != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(this, arrayOf(android.Manifest.permission.INTERNET), REQUEST_INTERNET_PERMISSION)
        } else if (ContextCompat.checkSelfPermission(this, android.Manifest.permission.ACCESS_NETWORK_STATE) != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(this, arrayOf(android.Manifest.permission.ACCESS_NETWORK_STATE), REQUEST_INTERNET_PERMISSION)
        }

        Log.i("Password",ePassword.text.toString())
        Log.i("Username",eUserName.text.toString()+"@ktu.edu.tr")

        BysApiClient.login.AuthLogin(ePassword.text.toString(), eUserName.text.toString()+"@ktu.edu.tr").enqueue(object: Callback<AuthLogin> {

            override fun onResponse(call: Call<AuthLogin>, response: Response<AuthLogin>) {
                if (response.isSuccessful) {
                    Toast.makeText(this@LoginActivity, "Login is successful!", Toast.LENGTH_SHORT).show()
                    Log.i("Response",response.body().toString())
                    Log.i("Call",call.toString())
                    Log.i("Call",call.request().headers().toString())
                    Log.i("Call",call.request().body().toString())

                    BysApiClient.userToken = response.body()?.authToken.toString()

                    val mesaj = eUserName.text.toString()
                    intent.putExtra(EXTRA_MESSAGE, mesaj)
                    startActivity(intent)
                }
                else {
                    Toast.makeText(this@LoginActivity, "Login is bad :(", Toast.LENGTH_SHORT).show()
                    Log.i("Response",response.body().toString())
                    Log.i("Call",call.toString())
                    Log.i("Call",call.request().headers().toString())
                    Log.i("Call",call.request().body().toString())
                }
            }

            override fun onFailure(call: Call<AuthLogin>, t: Throwable) {
                Toast.makeText(this@LoginActivity,t.message, Toast.LENGTH_LONG).show()
                Log.i("Response","onFailure",t)
                Log.i("Call",call.toString())
                Log.i("Call",call.request().headers().toString())
                Log.i("Call",call.request().body().toString())
            }

        } )
    }
    fun missPassword(view: View) {

        val intent = Intent(this, MissPassActivity::class.java)
        val textView = findViewById<TextView>(R.id.textMissPassword)
        val mesaj = textView.text.toString()
        intent.putExtra(EXTRA_MESSAGE, mesaj)
        startActivity(intent)


    }

}