import pickle
from flask import Flask,render_template,request
import pandas as pd

data = pd.read_csv('Training.csv')
X = data.iloc[:,:-1]
l1=X.columns
l2=[]
for i in range(0,len(l1)):
    l2.append(0)
    
model = pickle.load(open('model.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('log.html')

@app.route('/login',methods = ['POST','GET'])
def login():
    username = request.form['userid']
    password = request.form['pwd']
    if username=='demo' and password=='1234':
        return render_template('reg.html')
    else:
        return render_template('log.html',err_log='invalidcredentials')
    
@app.route('/evaluate',methods =['POST','GET'])
def evaluate():
    name = request.form['name']
    aadhaar = request.form['aadhaar']
    district = request.form['district']
    village = request.form['village']
    phone =request.form['phone']
    age = request.form['age']
    gender = request.form['gender']
    symptoms =request.form['symptoms']
    symptoms = symptoms.split('\r\n')
    for j in range(0,len(l1)):
        for k in symptoms:
            if k==l1[j]:
                l2[j]=1
    inputtest =[l2]
    out = model.predict(inputtest)
    h = out[0]
    if (h=='Fungal infection'): 
     medicines='Fluconazole tab ,  if chronic - voriconazole tab (Fungal Infection)' 
    elif(h=='Allergy'): 
      medicines='Cetrizine tab ,  Levocetrizine tab ,  Loratidine tab, ' 
    elif(h=='GERD'): 
      medicines='Raveprazole tab ,  Lansoprazole tab ,  Esomeprazole tab ,  Dexlansoprazole tab' 
    elif(h=='Chronic cholestasis'): 
     medicines='Piparcillin tazobactum injection' 
    elif(h=='Drug Reaction'): 
     medicines='Avil tab' 
    elif(h=='Peptic ulcer diseae'): 
      medicines='Raveprazole tab ,  Lansoprazole tab ,  Esomeprazole tab ,  Dexlansoprazole tab' 
    elif(h=='AIDS'): 
      medicines='Dolutegravir tab ,  Antiretroviral drug ,  Tenofovar tab ,  Lamivudine tab ,  Triomune tab ,  Darunavir tab' 
    elif(h=='Diabetes'): 
      medicines='Glimepride tab ,  Metformin tab ,  Gliclazide tab' 
    elif(h=='Gastroenteritis'): 
      medicines='Raveprazole tab \r,  Lansoprazole tab \r,  Esomeprazole tab \r,  Dexlansoprazole tab' 
    elif(h=='Bronchial Asthma'): 
      medicines='Doxiffillin tab ,  Levosolbutomol Bromexyne syrup ,  Asebrofithillin tab ,  Theophylline tab ,  Buducorte inhaler ,  Foracorte Forte inhaler' 
    elif(h=='Hypertension'): 
      medicines='Amlodipine tab ,  Ditiazem tab ,  Isravipine tab ,  Nicardipine tab ,  Verapimil tab' 
    elif(h=='Migraine'): 
      medicines='Paracetamol tab ,  Naproxen tab' 
    elif(h=='Cervical spondylosis'): 
      medicines='Indomethacin tab ,  Piroxicam tab ,  Naproxen tab ,  Methylpregnisolin tab ,  Ibuprofin tab ,  Baclofen tab ,  Cyclobenzaprine tab ,  Aceclophenac' 
    elif(h=='Paralysis (brain hemorrhage)'): 
      medicines='Anafranil tab ,  Clomipranime tab ,  methylphenidate tab' 
    elif(h=='Jaundice'): 
      medicines='Live52 tab' 
    elif(h=='Malaria'): 
      medicines='Ivermectin tab ,  Chloroquine Phosphate tab ,  Larinate 200mg tab ,  injections 60mg, ,  Mefloquine Artesunate tab' 
    elif(h=='Chicken pox'): 
      medicines='Immune System ,  Acyclovir tab 800mg ,  Valacyclovir tab' 
    elif(h=='Dengue'): 
      medicines='Paracetamol ,  Aspirin ,  Immune System' 
    elif(h=='Typhoid'): 
      medicines='Ciprofloxacin tab ,  Oflaxacin tab ,  Norflaxacin tab ,  Amoxycillin Clavu 625mg tab ,  Levofloxacin tab' 
    elif(h=='hepatitis A'): 
      medicines='Get Doctor Prescription' 
    elif(h=='Hepatitis B'): 
      medicines='Get Doctor Prescription' 
    elif(h=='Hepatitis C'): 
      medicines='Get Doctor Prescription' 
    elif(h=='Hepatitis D'): 
      medicines='Get Doctor Prescription' 
    elif(h=='Hepatitis E'): 
      medicines='Get Doctor Prescription' 
    elif(h=='Alcoholic hepatitis'): 
      medicines='Metadoxine tab' 
    elif(h=='Tuberculosis'): 
      medicines='Ethambutol tab ,  Pyrazinamide tab ,  Cycloserine tab ,  Ethionamide tab ,  Levofloxacin tab ,  Kanamycan tab' 
    elif(h=='Common Cold'): 
      medicines='Immune System ,  Phenylephrine Hydrochloride + Chlorpheniramine Malete tab ,  Levocetrizine tab ,  Cetrizine tab' 
    elif(h=='Pneumonia'): 
      medicines='Azithromycin tab ,  Linezolid tab ,  Delafloxacin tab Clindamycin tab ,  Doxycycline tab ,  Ertapenem tab ,  Lincosamide tab' 
    elif(h=='Dimorphic hemmorhoids(piles)'): 
      medicines='Pilex tab ,  Pilenil tab' 
    elif(h=='Heart attack'): 
      medicines='Sorbitrate tab' 
    elif(h=='Varicose veins'): 
      medicines='Polydocanal Injection ,  Sodium Tetradecyl Sulphate Injection ,  Ibuprofin tab ,  Paracetomal tab' 
    elif(h=='Hypothyroidism'): 
      medicines='Levothyroxine Soduim tab ,  Pyridoxin Hydrochloride sustained released tab ,  Tirosint capsules ,  Levoxyl tab ,  Synthroid tab ,  Unithroid tab' 
    elif(h=='Hyperthyroidism'): 
      medicines='Levothyroxine Soduim tab ,  Pyridoxin Hydrochloride sustained released tab ,  Tirosint capsules ,  Levoxyl tab ,  Synthroid tab ,  Unithroid tab' 
    elif(h=='Hypoglycemia'): 
      medicines='Glucose tab' 
    elif(h=='Osteoarthristis'): 
      medicines='Glucosamine Sulphate tab ,  Ibuprofin tab ,  Naproxen tab' 
    elif(h=='Arthritis'): 
      medicines='Glucosamine Sulphate tab ,  Ibuprofin tab ,  Naproxen tab' 
    elif(h=='(vertigo) Paroymsal  Positional Vertigo'): 
      medicines='Sinarzine tab ,  Flunarzine tab' 
    elif(h=='Acne'): 
      medicines='Clindamycin Phosphate & NicotinamdeGel ,  Adapalene Benzylperoxide Gel ' 
    elif(h=='Urinary tract infection'): 
      medicines='Oflaxacin tab ,  Norfloxacin tab ,  Siprofloxacin tab ,  Tinidazole tab' 
    elif(h=='Psoriasis'): 
      medicines='Aloe vera creams ,  White soft paraffin Gel  ,  Flucanazole tab (Optional if itchy) ,  Clobetasole Propionite and Salicylicacid Gel' 
    elif(h=='Impetigo'): 
      medicines='Mupirosin Ointment ,  Retamulin Ointment ,  Amoxycillin Potassium Clavunate'
    return (render_template('out.html',medicines=medicines,disease_details=h,fname=name,adhaar=aadhaar,district=district,village=village,phone=phone,age=age,gender=gender))

if __name__=="__main__":
    app.run('0.0.0.0',debug=True)