package edu.ktu.mudek.scanner.scan

import android.view.Display
import android.view.SurfaceView
import edu.ktu.mudek.scanner.view.PaperRectangle

interface IScanView {
    interface Proxy {
        fun exit()
        fun getDisplay(): Display
        fun getSurfaceView(): SurfaceView
        fun getPaperRect(): PaperRectangle
    }
}