import tkinter as tk
import customtkinter

from data.classes.analyse_data.solution import Solution
import data.classes.analyse_data.image as img

class SolutionContent(Solution):
    def __init__(self):
        super().__init__()
        self.id = 1
        self.name = "Tape & Reel Handling Protocol"
        self.objects = [
            "* Damaged component tapes and reels can negatively affect overall system performance.\n\n"
            "* Damaged tapes can prevent smooth movement off the reel and through the feeder. For best performance, ensure that component tapes are flat: not bent, warped or twisted.\n\n"
            "* Damaged reels can prevent smooth release of tape from the reel and prevent the reel from rotating smoothly. For best performance, ensure that all reels inside and outside surfaces are smooth: not burred, bent, dented, or twisted. Ensure that corrugated paper reels are not torn or delaminated.\n\n"
            "* always use undamaged component tapes and reels to ensure the best performance of ion Feeders, Feeder Baskets, Basket Dividers, Reel Dividers, and Reel Holders.\n",
            "\img|feeder/01-image.png"
        ]
    