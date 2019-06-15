package edu.ktu.mudek.bys.ui

import android.content.Intent
import android.os.Bundle
import android.provider.AlarmClock
import android.support.v7.app.AppCompatActivity
import android.view.View
import edu.ktu.mudek.R
import edu.ktu.mudek.scanner.scan.ScanActivity


open class MissPassActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_misspass)
    }

    fun scan(view: View) {

        val intent = Intent(this, ScanActivity::class.java)
        intent.putExtra(AlarmClock.EXTRA_MESSAGE, "Scan Activity Open")
        startActivity(intent)
    }
}