package edu.ktu.mudek.bys.adapters

import android.support.v7.widget.RecyclerView
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import edu.ktu.mudek.R
import edu.ktu.mudek.bys.models.Exams
import kotlinx.android.synthetic.main.exams_item_adapter.*

class ExamsAdapter(val examsList: ArrayList<Exams>) : RecyclerView.Adapter<ExamsAdapter.ViewHolder>() {

    override fun onCreateViewHolder(p0: ViewGroup, p1: Int): ViewHolder {
        val v = LayoutInflater.from(p0?.context).inflate(R.layout.exams_item_adapter, p0, false)
        return ViewHolder(v)
    }

    override fun getItemCount(): Int {
        return examsList.size
    }

    override fun onBindViewHolder(p0: ViewHolder, p1: Int) {

        p0.examId?.text = examsList[p1].id.toString()
        p0.examLessonName?.text = examsList[p1].id.toString()
        p0.examType?.text = examsList[p1].examFile.toString()
        p0.examInformation?.text = examsList[p1].examInformation.toString()
        p0.examFile?.text = "Exam File Path:" + examsList[p1].examFile.toString()
        p0.examAnswerFile?.text = "Answer File Path: " + examsList[p1].examAnswerFile.toString()
    }

    inner class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {

        val examId = itemView.findViewById<TextView>(R.id.examId)
        val examLessonName = itemView.findViewById<TextView>(R.id.examLessonName)
        val examType = itemView.findViewById<TextView>(R.id.examType)
        val examInformation = itemView.findViewById<TextView>(R.id.examInformation)
        val examFile = itemView.findViewById<TextView>(R.id.examFile)
        val examAnswerFile = itemView.findViewById<TextView>(R.id.examAnswerFile)

    }
}