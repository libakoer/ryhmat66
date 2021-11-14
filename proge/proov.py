import PySimpleGUI as sg
import time
import create_event
import playsound
import pygame
sg.theme('Dark Green 4')  
paigutus = [[sg.Text('Isikuandmed:', text_color='white', font=('Helvetica', 15))],
            
            [sg.Text('Sisestage oma nimi: ', text_color='white', font=("Helvetica", 12))],
          [sg.Input(key='sisestatud_nimi', size=(80,1))],
             
             [sg.Text('Meeldetuletuse kuupäev ja aeg', text_color='white', font=('Helvetica', 15))],
             
             [sg.Text('Sisestage aasta : ', text_color='white', font=("Helvetica", 12))],
          [sg.Input(key='sisestatud_aasta', size=(80,1))],
             
             [sg.Text('Sisestage kuu (number): ', text_color='white', font=("Helvetica", 12))],
          [sg.Input(key='sisestatud_kuu', size=(80,1))],
             
             [sg.Text('Sisestage päev (number): ', text_color='white', font=("Helvetica", 12))],
          [sg.Input(key='sisestatud_päev', size=(80,1))],
             
             [sg.Text('Sisestage mitmendal tunnil: ', text_color='white', font=("Helvetica", 12))],
          [sg.Input(key='sisestatud_tunnid', size=(80,1))],
            
            [sg.Text('Sisestage mitmendal minutil: ', text_color='white', font=("Helvetica", 12))],
          [sg.Input(key='sisestatud_minutid', size=(80,1))],
            
          [sg.Submit('Edasi'), sg.Cancel('Välju')]]

aken = sg.Window('K-Äratus', paigutus, size=(500,500))

while True:  
    syndmus, v22rtused = aken.read()
    
    if syndmus == sg.WIN_CLOSED or syndmus == 'Välju':
        break
    
    if syndmus == 'Edasi':
        aken.close()
        
        nimi = v22rtused['sisestatud_nimi']
        aasta = v22rtused['sisestatud_aasta']
        kuu = v22rtused['sisestatud_kuu']
        päev = v22rtused['sisestatud_päev']
        tunnid = v22rtused['sisestatud_tunnid']
        minutid = v22rtused['sisestatud_minutid']
        
        paigutus2 = [[sg.Text('Meeldetuletus: ', text_color='white', font=('Helvetica', 15))],
                  [sg.Text('Sisestage meeldetuletus: ', size=(20, 1)), sg.InputText(key='sisestatud_meeldetuletus', size=(50,50))],
                  [sg.Submit('Salvesta'), sg.Cancel('Välju')]]
        
        aken = sg.Window('Meeldetuletus', paigutus2, size=(500,100))
        
        syndmus2, v22rtused2 = aken.read()
        
        tekst = str(v22rtused2['sisestatud_meeldetuletus'])
        tahetud_aeg=(aasta,kuu, päev, tunnid, minutid)
        Filter=0
        
        if syndmus2 == sg.WIN_CLOSED or syndmus == 'Välju':
            break
        
        elif syndmus2 == 'Salvesta':
            sg.Popup(str(nimi)+ ', ' + 'Teile on seatud meeldetuletus:' + ' ' + str(tekst) , str(päev) + '.' + str(kuu) + '.' + str(aasta)+ ' ' + 'kell ' + str(tunnid) + ':' + str(minutid))    
            time.sleep(2)
            create_event.main(aasta,kuu,päev,tunnid,minutid,tekst)
            break
aken.close()
if syndmus!="VÄLJU" or syndmus2 == sg.WIN_CLOSED :
    while Filter!=5:
        Filter=0
        aeg=time.localtime()
        for i in tahetud_aeg:
            if str(aeg[Filter])==tahetud_aeg[Filter]:
                Filter+=1
        time.sleep(15)
        if Filter==5:
            print(tekst)
            pygame.mixer.init()
            pygame.mixer.music.load('sample.mp3')
            pygame.mixer.music.play()
            while True:
                aken = sg.Window('k-Äratus', paigutus2, size=(500,100))
                time.sleep(5)
                break
                

            

    


