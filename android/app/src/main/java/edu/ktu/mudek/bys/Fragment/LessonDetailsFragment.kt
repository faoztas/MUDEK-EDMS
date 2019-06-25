package edu.ktu.mudek.bys.fragment

import android.content.Context
import android.os.Bundle
import android.support.v4.app.Fragment
import android.support.v7.widget.LinearLayoutManager
import android.support.v7.widget.RecyclerView
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.*
import edu.ktu.mudek.R
import edu.ktu.mudek.bys.models.LessonDetails
import edu.ktu.mudek.bys.network.BysApiClient
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class LessonDetailsFragment : Fragment() {

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?,
                              savedInstanceState: Bundle?): View? {

        val rootView = inflater.inflate(R.layout.fragment_lesson_details, container, false)

        val lessonId = rootView.findViewById<TextView>(R.id.lessonId)
        val userId = rootView.findViewById<TextView>(R.id.userId)
        val lessonName = rootView.findViewById<TextView>(R.id.lessonName)
        val lessonContent = rootView.findViewById<TextView>(R.id.lessonContent)
        val lessonContentFileButton = rootView.findViewById<Button>(R.id.lessonContentFileButton)
        val lessonContentFile = rootView.findViewById<TextView>(R.id.lessonContentFile)
        val lessonNotes = rootView.findViewById<TextView>(R.id.lessonNotes)
        val lessonNotesFileButton = rootView.findViewById<Button>(R.id.lessonNotesFileButton)
        val lessonNotesFile = rootView.findViewById<TextView>(R.id.lessonNotesFile)
        val uploadButton = rootView.findViewById<Button>(R.id.upload)

        BysApiClient.instance.getLessonDetails(1).enqueue(object: Callback<LessonDetails>{

            override fun onResponse(call: Call<LessonDetails>, response: Response<LessonDetails>) {
                if (response.isSuccessful) {
                    Toast.makeText(activity?.baseContext, "... which is successful!", Toast.LENGTH_SHORT).show()
                    Log.i("Response",response.body().toString())
                    Log.i("Call",call.toString())
                    Log.i("Call",call.request().headers().toString())
                    Log.i("Call",call.request().body().toString())

                    lessonId.text = response.body()?.id.toString()
                    userId.text = response.body()?.user.toString()
                    lessonName.text = response.body()?.lessonName.toString()
                    lessonContent.text = response.body()?.lessonContent.toString()
                    lessonContentFile.text = response.body()?.lessonContentFile.toString()
                    lessonNotes.text = response.body()?.lessonNotes.toString()
                    lessonNotesFile.text = response.body()?.lessonNotesFile.toString()

                }
                else {
                    Toast.makeText(activity?.baseContext, "... which is bad :(", Toast.LENGTH_SHORT).show()
                    Log.i("Response",response.body().toString())
                    Log.i("Call",call.toString())
                    Log.i("Call",call.request().headers().toString())
                    Log.i("Call",call.request().body().toString())
                }
            }

            override fun onFailure(call: Call<LessonDetails>, t: Throwable) {
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
