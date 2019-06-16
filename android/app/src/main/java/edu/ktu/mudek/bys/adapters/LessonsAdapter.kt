package edu.ktu.mudek.bys.adapters

import android.support.v7.widget.RecyclerView
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import edu.ktu.mudek.R
import edu.ktu.mudek.bys.models.Lessons

class LessonsAdapter(val lessonList: ArrayList<Lessons>) : RecyclerView.Adapter<LessonsAdapter.ViewHolder>() {
    override fun onCreateViewHolder(p0: ViewGroup, p1: Int): ViewHolder {
        val v = LayoutInflater.from(p0?.context).inflate(R.layout.lessons_item_adapter, p0, false)
        return ViewHolder(v)
    }
    override fun getItemCount(): Int {
        return lessonList.size
    }
    override fun onBindViewHolder(p0: ViewHolder, p1: Int) {

        p0.lessonId?.text = lessonList[p1].id.toString()
        p0.userId?.text = lessonList[p1].user.toString()
        p0.lessonName?.text = lessonList[p1].lessonName.toString()
        p0.lessonContent?.text = lessonList[p1].lessonContent.toString()
        p0.lessonContentFile?.text = lessonList[p1].lessonContentFile.toString()
        p0.lessonNotes?.text = lessonList[p1].lessonNotes.toString()
        p0.lessonNotesFile?.text = lessonList[p1].lessonNotesFile.toString()
    }
    class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val lessonId = itemView.findViewById<TextView>(R.id.lessonId)
        val userId = itemView.findViewById<TextView>(R.id.userId)
        val lessonName = itemView.findViewById<TextView>(R.id.lessonName)
        val lessonContent = itemView.findViewById<TextView>(R.id.lessonContent)
        val lessonContentFile = itemView.findViewById<TextView>(R.id.lessonContentFile)
        val lessonNotes = itemView.findViewById<TextView>(R.id.lessonNotes)
        val lessonNotesFile = itemView.findViewById<TextView>(R.id.lessonNotesFile)

    }
}