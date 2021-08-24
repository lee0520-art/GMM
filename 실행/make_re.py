from make_ import make_re

for x in range(1,101):
    if(x<10):
        filename="SW201105ETRNI4F07852PKJ000"+str(x)
    elif(x>=10 and x<100):
        filename="SW201105ETRNI4F07852PKJ00"+str(x)
    else:
        filename="SW201105ETRNI4F07852PKJ0"+str(x)
    make_re("C:\\Users\\user\\SpeakerRecognition_tutorial_\\feat_logfbank_nfilt40\\train","I4F0785",filename)