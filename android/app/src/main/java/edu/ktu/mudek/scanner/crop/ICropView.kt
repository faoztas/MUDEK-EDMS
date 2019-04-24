package edu.ktu.mudek.scanner.crop

import android.widget.ImageView
import edu.ktu.mudek.scanner.view.PaperRectangle



class ICropView {
    interface Proxy {
        fun getPaper(): ImageView
        fun getPaperRect(): PaperRectangle
        fun getCroppedPaper(): ImageView
    }
}