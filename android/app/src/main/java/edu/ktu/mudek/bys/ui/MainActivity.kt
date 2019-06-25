package edu.ktu.mudek.bys.ui

import android.app.Application
import android.content.Intent
import android.os.Bundle
import android.provider.AlarmClock
import android.support.design.widget.NavigationView
import android.support.v4.view.GravityCompat
import android.support.v7.app.ActionBarDrawerToggle
import android.support.v7.app.AppCompatActivity
import android.util.Log
import android.view.Menu
import android.view.MenuItem
import android.widget.Toast
import edu.ktu.mudek.R
import edu.ktu.mudek.bys.fragment.HomeFragment
import edu.ktu.mudek.bys.fragment.SettingsFragment
import edu.ktu.mudek.bys.fragment.DocFragment
import edu.ktu.mudek.bys.models.Users
import edu.ktu.mudek.bys.network.BysApiClient
import edu.ktu.mudek.scanner.scan.ScanActivity
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.android.synthetic.main.app_bar_main.*
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import android.view.View
import android.widget.TextView

class MainActivity : AppCompatActivity(), NavigationView.OnNavigationItemSelectedListener {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        setSupportActionBar(toolbar)

        supportFragmentManager.beginTransaction().replace(R.id.relativelayout, HomeFragment()).commit()

        val toggle = ActionBarDrawerToggle(
                this, drawer_layout, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close)
        drawer_layout.addDrawerListener(toggle)
        toggle.syncState()

        nav_view.setNavigationItemSelectedListener(this)
        val navigationView = findViewById<View>(R.id.nav_view) as NavigationView
        val headerView = navigationView.getHeaderView(0)
        val navUsername = headerView.findViewById(R.id.nav_username) as TextView
        val navMail = headerView.findViewById(R.id.nav_email) as TextView

        BysApiClient.instance.getUsers().enqueue(object: Callback<ArrayList<Users>> {

            override fun onResponse(call: Call<ArrayList<Users>>, response: Response<ArrayList<Users>>) {
                if (response.isSuccessful) {
                    Toast.makeText(this@MainActivity, "Login is successful!", Toast.LENGTH_SHORT).show()
                    Log.i("Response",response.body().toString())
                    Log.i("Call",call.toString())
                    Log.i("Call",call.request().headers().toString())
                    Log.i("Call",call.request().body().toString())



                    navMail.text = response.body()?.get(0)?.email.toString()
                    navUsername.text = response.body()?.get(0)?.firstName.toString()+" "+response.body()?.get(0)?.lastName.toString()

                }
                else {
                    Toast.makeText(this@MainActivity, "Login is bad :(", Toast.LENGTH_SHORT).show()
                    Log.i("Response",response.body().toString())
                    Log.i("Call",call.toString())
                    Log.i("Call",call.request().headers().toString())
                    Log.i("Call",call.request().body().toString())
                }
            }

            override fun onFailure(call: Call<ArrayList<Users>>, t: Throwable) {
                Toast.makeText(this@MainActivity,t.message, Toast.LENGTH_LONG).show()
                Log.i("Response","onFailure",t)
                Log.i("Call",call.toString())
                Log.i("Call",call.request().headers().toString())
                Log.i("Call",call.request().body().toString())
            }

        } )

        displayScreen(-1)
    }

    override fun onBackPressed() {
        if (drawer_layout.isDrawerOpen(GravityCompat.START)) {
            drawer_layout.closeDrawer(GravityCompat.START)
        } else {
            super.onBackPressed()
        }
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        menuInflater.inflate(R.menu.main, menu)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        when (item.itemId) {
            R.id.action_logout -> {
                val intent = Intent(this, LoginActivity::class.java)
                intent.putExtra(AlarmClock.EXTRA_MESSAGE, "Login Activity Open")
                startActivity(intent)
                return true
            }
            else -> {
                return super.onOptionsItemSelected(item)
            }
        }
    }

    fun displayScreen(id: Int){

        // val fragment =  when (id){

        when (id){
            R.id.nav_home -> {
                supportFragmentManager.beginTransaction().replace(R.id.relativelayout, HomeFragment()).commit()
            }

            R.id.nav_doc -> {
                supportFragmentManager.beginTransaction().replace(R.id.relativelayout, DocFragment()).commit()
            }

            R.id.nav_scanCrop -> {
                val intent = Intent(this, ScanActivity::class.java)
                intent.putExtra(AlarmClock.EXTRA_MESSAGE, "Scan Activity Open")
                startActivity(intent)
            }

            R.id.nav_notifications -> {
                Toast.makeText(this, "Clicked Notifications", Toast.LENGTH_SHORT).show()
            }

            R.id.nav_settings -> {
                supportFragmentManager.beginTransaction().replace(R.id.relativelayout, SettingsFragment()).commit()
            }

            R.id.nav_aboutUs -> {
                Toast.makeText(this, "Clicked About Us", Toast.LENGTH_SHORT).show()
            }

            R.id.nav_privacyPolicy -> {
                Toast.makeText(this, "Clicked Privacy Policy", Toast.LENGTH_SHORT).show()
            }
        }
    }

    override fun onNavigationItemSelected(item: MenuItem): Boolean {
        // Handle navigation view item clicks here.

        displayScreen(item.itemId)

        drawer_layout.closeDrawer(GravityCompat.START)
        return true
    }


}
