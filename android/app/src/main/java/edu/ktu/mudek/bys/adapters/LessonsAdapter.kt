package edu.ktu.mudek.bys.adapters

import android.support.v7.widget.RecyclerView
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import edu.ktu.mudek.R
import edu.ktu.mudek.bys.models.Lessons

class LessonsAdapter(val lessonList: ArrayList<Lessons>, var onItemClick: ((Lessons) -> Unit)? = null) : RecyclerView.Adapter<LessonsAdapter.ViewHolder>() {

    override fun onCreateViewHolder(p0: ViewGroup, p1: Int): ViewHolder {
        val v = LayoutInflater.from(p0?.context).inflate(R.layout.lessons_item_adapter, p0, false)
        return ViewHolder(v)
    }

    override fun getItemCount(): Int {
        return lessonList.size
    }

    override fun onBindViewHolder(p0: ViewHolder, p1: Int) {

        p0.lessonId?.text = lessonList[p1].id.toString()
        //p0.userId?.text = lessonList[p1].user.toString()
        p0.lessonName?.text = lessonList[p1].lessonName.toString()
        p0.lessonContent?.text = "Content: " + lessonList[p1].lessonContent.toString()
        if (!lessonList[p1].lessonContentFile.isNullOrEmpty()) {
            p0.lessonContentFile?.text = "Content File Path: " + lessonList[p1].lessonContentFile.toString()
        } else {
            p0.lessonContentFile?.text = "Content File not uploaded"
        }
        p0.lessonNotes?.text = "Notes: " + lessonList[p1].lessonNotes.toString()
        p0.lessonNotesFile?.text = "Notes File Path: " + lessonList[p1].lessonNotesFile.toString()
    }

    inner class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {

        val lessonId = itemView.findViewById<TextView>(R.id.lessonId)
        //val userId = itemView.findViewById<TextView>(R.id.userId)
        val lessonName = itemView.findViewById<TextView>(R.id.lessonName)
        val lessonContent = itemView.findViewById<TextView>(R.id.lessonContent)
        val lessonContentFile = itemView.findViewById<TextView>(R.id.lessonContentFile)
        val lessonNotes = itemView.findViewById<TextView>(R.id.lessonNotes)
        val lessonNotesFile = itemView.findViewById<TextView>(R.id.lessonNotesFile)

        init {
            itemView.setOnClickListener {
                onItemClick?.invoke(lessonList[adapterPosition])
            }
        }

    }
}