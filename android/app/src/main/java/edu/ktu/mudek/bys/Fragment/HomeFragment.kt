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
import edu.ktu.mudek.bys.adapters.LessonsAdapter
import edu.ktu.mudek.bys.models.Lessons
import edu.ktu.mudek.bys.network.BysApiClient
import edu.ktu.mudek.bys.network.BysApiInterface
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.create


// TODO: Rename parameter arguments, choose names that match
// the fragment initialization parameters, e.g. ARG_ITEM_NUMBER
private const val ARG_PARAM1 = "param1"
private const val ARG_PARAM2 = "param2"

/**
 * A simple [Fragment] subclass.
 * Activities that contain this fragment must implement the
 * [HomeFragment.OnFragmentInteractionListener] interface
 * to handle interaction events.
 * Use the [HomeFragment.newInstance] factory method to
 * create an instance of this fragment.
 *
 */
class HomeFragment : Fragment() {

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?,
                              savedInstanceState: Bundle?): View? {
        val rootView = inflater.inflate(R.layout.fragment_home, container, false)

        val recyclerView = rootView.findViewById<RecyclerView>(R.id.recyclerView)
//        Initializing the type of layout, here I have used LinearLayoutManager you can try GridLayoutManager
//        Based on your requirement to allow vertical or horizontal scroll , you can change it in  LinearLayout.VERTICAL
        recyclerView.layoutManager = LinearLayoutManager(activity?.baseContext, LinearLayout.VERTICAL, false)
//        Create an arraylist
        val lessonList = ArrayList<Lessons>()

        Log.i("Response","ClientBefore")
        BysApiClient.instance.getLessons().enqueue(object: Callback<Lessons>{

            override fun onResponse(call: Call<Lessons>, response: Response<Lessons>) {
                if (response.isSuccessful) {
                    Toast.makeText(activity?.baseContext, "... which is successful!", Toast.LENGTH_SHORT).show()
                    Log.i("Response",response.body().toString())
                }
                else {
                    Toast.makeText(activity?.baseContext, "... which is bad :(", Toast.LENGTH_SHORT).show()
                    Log.i("Response",response.body().toString())
                }
            }

            override fun onFailure(call: Call<Lessons>, t: Throwable) {
                Toast.makeText(activity?.baseContext,t.message,Toast.LENGTH_LONG).show()
                Log.i("Response","onFailure",t)
            }

        } )
        Log.i("Response","ClientAfter")

        lessonList.add(Lessons(1,"Sayısal sistemlerin üstünlükleri Bilgilerin sayısal gösterimi, Sayı sistemleri, tam ve kesirli sayıların gösterimi, Boole cebiri, Boole fonksiyonların cebirsel ve Karnough diyagramlarıyla indirgenmesi. Lojik kapılar. Sabit-noktalı aritmetik: Toplama, ileri- eldeli toplama, çıkarma, çarpma. Booth çarpma algoritması. Restoring ve nonrestoring bölme. Onlu aritmetik. Kayan- noktalı biçim, kutuplu üs, normalizasyon, taşma, kayan-noktalı sayıların dört işlemi. Bilgisayarın genel yapısı. İşletim sistemleri hakkında genel bilgiler. Assembly dili.",null,"BİLGİSAYARIN TEMELLERİ",null,null,2))
        lessonList.add(Lessons(2,null,null,"MİKROİŞLEMCİLER",null,null,2))
        lessonList.add(Lessons(3,null,"http://127.0.0.1:8000/media/user_2/BMD_Sistem_Modelleri.doc","BİLGİSAYAR ORGANİZASYON LAB",null,null,2))
//        pass the values to LessonsAdapter
        val lessonsAdapter = LessonsAdapter(lessonList)
//        set the recyclerView to the adapter
        recyclerView.adapter = lessonsAdapter

        // Inflate the layout for this fragment
        return rootView
    }
}
