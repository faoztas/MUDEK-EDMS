package edu.ktu.mudek.bys.fragment

import android.os.Bundle
import android.support.v4.app.Fragment
import android.support.v7.widget.LinearLayoutManager
import android.support.v7.widget.RecyclerView
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.LinearLayout
import android.widget.Toast
import edu.ktu.mudek.R
import edu.ktu.mudek.bys.adapters.ExamsAdapter
import edu.ktu.mudek.bys.adapters.LessonsAdapter
import edu.ktu.mudek.bys.models.Exams
import edu.ktu.mudek.bys.models.Lessons
import edu.ktu.mudek.bys.network.BysApiClient
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class DocFragment : Fragment() {

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?,
                              savedInstanceState: Bundle?): View? {
        val rootView = inflater.inflate(R.layout.fragment_doc, container, false)
        val recyclerView = rootView.findViewById<RecyclerView>(R.id.recyclerView)

        recyclerView.layoutManager = LinearLayoutManager(activity?.baseContext, LinearLayout.VERTICAL, false)
        BysApiClient.instance.getExams().enqueue(object: Callback<ArrayList<Exams>>{

            override fun onResponse(call: Call<ArrayList<Exams>>, response: Response<ArrayList<Exams>>) {
                if (response.isSuccessful) {
                    Toast.makeText(activity?.baseContext, "... which is successful!", Toast.LENGTH_SHORT).show()
                    Log.i("Response",response.body().toString())
                    Log.i("Call",call.toString())
                    Log.i("Call",call.request().headers().toString())
                    Log.i("Call",call.request().body().toString())

                    val examsAdapter = ExamsAdapter(response.body()!!)
                    recyclerView.adapter = examsAdapter

                }
                else {
                    Toast.makeText(activity?.baseContext, "... which is bad :(", Toast.LENGTH_SHORT).show()
                    Log.i("Response",response.body().toString())
                    Log.i("Call",call.toString())
                    Log.i("Call",call.request().headers().toString())
                    Log.i("Call",call.request().body().toString())
                }
            }

            override fun onFailure(call: Call<ArrayList<Exams>>, t: Throwable) {
                Toast.makeText(activity?.baseContext,t.message,Toast.LENGTH_LONG).show()
                Log.i("Response","onFailure",t)
                Log.i("Call",call.toString())
                Log.i("Call",call.request().headers().toString())
                Log.i("Call",call.request().body().toString())

            }

        } )

        return rootView
    }
}
