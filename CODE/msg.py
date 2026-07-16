codes = [143, 505, 911]

txt = {
    143: "I Love You",
    505: "Come Outside",
    911: "Emergency",
}



def lookup(cd):
    return txt.get(cd, "Unknown")


