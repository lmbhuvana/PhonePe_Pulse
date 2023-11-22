import streamlit as st
import plotly.express as px
import mysql.connector
import pandas as pd

st.set_page_config(page_title='PhonePe Pulse', page_icon=':bar_chart:', layout="wide")
st.header(":blue[Phonepe Pulse Data Visualization and Exploration]")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="phonepe"
)

mycursor = mydb.cursor()



# st.image(r"C:\Users\Bhuvana Vignesh\OneDrive\Desktop\GUVI_Projects\Image_streamlit\Untitled.png", use_column_width=True)



st.write("Displays data's from 2018 to 2023")
st.subheader('Key Dimensions:')
st.write('- State - All States in India')
st.write('- Year -  2018 to 2023')
st.write('- Quarter - Q1 (Jan to Mar), Q2 (Apr to June), Q3 (July to Sep), Q4 (Oct to Dec)')

st.subheader('Aggregated Transaction:')
st.write('Transaction data agggregated by type of payments at state level.')

option = st.selectbox('Click the below & check the payment types.....',( '- Recharge & bill payments', '- Peer-to-peer payments','- Merchant payments', '- Financial Services',
                      '- Others'))
st.write(option)
# st.write('- Recharge & bill payments')
# st.write('- Peer-to-peer payments')
# st.write('- Merchant payments')
# st.write('- Financial Services')
# st.write('- Others')

st.subheader('Aggregated User:')
st.write('Users data aggregated by devices at state level.')
st.write('Click the below & check the devices.....')
col1,col2,col3,col4, col5, col6 = st.columns(6)
with col1:
    st.write(':small_blue_diamond: Apple')
    st.write(':small_blue_diamond: Asus')
    st.write(':small_blue_diamond: Coolpad')
    st.write(':small_blue_diamond: Gionee')
    st.write(':small_blue_diamond: HMD Global')
with col2:
    st.write(':small_blue_diamond: Huawei')
    st.write(':small_blue_diamond: Infinix')
    st.write(':small_blue_diamond: Lava')
    st.write(':small_blue_diamond: Lenovo')
    st.write(':small_blue_diamond: Lyf')
with col3:
    st.write(':small_blue_diamond: Micromax')
    st.write(':small_blue_diamond: Motorola')
    st.write(':small_blue_diamond: OnePlus')
    st.write(':small_blue_diamond: Oppo')
    st.write(':small_blue_diamond: Realme')
with col4:
    st.write(':small_blue_diamond: Samsung')
    st.write(':small_blue_diamond: Tecno')
    st.write(':small_blue_diamond: Vivo')
    st.write(':small_blue_diamond: Xiaomi')
    st.write(':small_blue_diamond: Others')

tab1,tab2= st.tabs(["Transaction","Users"])

quarter=['Q1','Q2','Q3','Q4']
types= ["Peer-to-peer payments","Merchant payments", "Financial Services","Recharge & bill payments", "Others"]
year= [2018, 2019, 2020, 2021, 2022,2023]
state= ['andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu',
        'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh', 
        'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland','odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
        'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal']
dist=  ['kurnool', 'guntur', 'krishna', 'spsr nellore', 'vizianagaram', 'ysr', 'west godavari', 'chittoor', 'lower subansiri', 'tirap', 'papum pare', 'anjaw', 'lower siang', 
        'dibang valley', 'west kameng', 'shi yomi', 'east kameng', 'lohit', 'lepa rada', 'lower dibang valley', 'longding', 'west siang', 'kamle', 'upper siang', 'kurung kumey',
        'siang', 'kra daadi', 'changlang', 'pakke kessang', 'east siang', 'upper subansiri', 'tawang', 'namsai', 'tinsukia', 'lakhimpur', 'kamrup', 'kokrajhar', 'karbi anglong',
        'sivasagar', 'dibrugarh', 'south salmara mancachar', 'nagaon', 'dhubri', 'golaghat', 'udalguri', 'majuli', 'sonitpur', 'hojai', 'marigaon', 'chirang', 'cachar', 
        'nalbari', 'west karbi anglong', 'dhemaji','karimganj', 'bongaigaon', 'dima hasao', 'baksa', 'charaideo', 'darrang', 'kamrup metropolitan', 'hailakandi', 'barpeta', 'goalpara',
        'biswanath', 'jorhat', 'madhepura', 'purnia', 'nalanda', 'buxar', 'darbhanga', 'nawada', 'jamui', 'sheikhpura', 'siwan', 'muzaffarpur', 'patna', 'jehanabad', 
        'rohtas', 'begusarai', 'supaul', 'sitamarhi', 'saran', 'arwal', 'vaishali', 'pashchim champaran', 'gopalganj', 'lakhisarai', 'aurangabad', 'kaimur bhabua', 'araria', 
        'munger', 'katihar', 'khagaria', 'saharsa', 'bhagalpur', 'madhubani', 'kishanganj', 'gaya', 'samastipur', 'banka', 'purbi champaran', 'sheohar', 'bhojpur',
        'chandigarh', 'dhamtari', 'korba', 'surajpur', 'baloda bazar', 'sukma', 'raigarh', 'janjgir champa', 'jashpur', 'balod', 'kabirdham', 'surguja', 'dantewada', 
        'gariyaband', 'durg', 'rajnandgaon', 'raipur', 'narayanpur', 'kanker', 'korea', 'mungeli', 'bilaspur', 'balrampur', 'bijapur', 'bemetara', 'bastar', 'kondagaon',
        'mahasamund', 'diu', 'daman', 'dadra and nagar haveli', 'south', 'central', 'new delhi', 'west', 'south west', 'south east delhi', 'shahdara', 'north east', 
        'east', 'north west', 'north', 'north goa', 'south goa', 'anand', 'jamnagar', 'devbhumi dwarka', 'rajkot', 'aravallis', 'chhotaudepur', 'botad', 'bharuch',
        'bhavnagar', 'junagadh', 'mahesana', 'the dangs', 'kheda', 'surat', 'porbandar', 'gandhinagar', 'panch mahals', 'narmada', 'gir somnath', 'valsad', 
        'mahisagar', 'sabar kantha', 'tapi', 'vadodara', 'banas kantha', 'amreli', 'ahmadabad', 'dohad', 'navsari', 'patan', 'kachchh', 'surendranagar', 'morbi', 
        'yamunanagar', 'sonipat', 'jind', 'rohtak', 'faridabad', 'mahendragarh', 'hisar', 'karnal', 'fatehabad', 'palwal', 'charkhi dadri', 'ambala', 'rewari', 
        'panchkula', 'bhiwani', 'sirsa', 'mewat', 'panipat', 'gurugram', 'kaithal', 'kurukshetra', 'jhajjar', 'solan', 'sirmaur', 'shimla', 'hamirpur', 'una', 'kangra', 
        'kullu', 'mandi', 'lahul and spiti', 'chamba', 'kinnaur', 'muzaffarabad', 'doda', 'samba', 'mirpur', 'srinagar', 'baramulla', 'jammu', 'ganderbal', 'udhampur', 
        'bandipore', 'reasi', 'shopian', 'poonch', 'kathua', 'kishtwar', 'pulwama', 'ramban', 'rajouri', 'kulgam', 'budgam', 'anantnag', 'kupwara', 'ramgarh', 'ranchi', 
        'east singhbhum', 'jamtara', 'dumka', 'koderma', 'hazaribagh', 'simdega', 'garhwa', 'saraikela kharsawan', 'gumla', 'chatra', 'khunti', 'dhanbad', 'godda', 'deoghar', 
        'palamu', 'latehar', 'west singhbhum', 'pakur', 'lohardaga', 'sahebganj', 'giridih', 'bokaro', 'mysuru', 'chitradurga', 'kalaburagi', 'ramanagara', 'mandya', 'kodagu',
        'chikkamagaluru', 'haveri', 'ballari', 'belagavi', 'kolar', 'uttara kannada', 'tumakuru', 'yadgir', 'bengaluru urban', 'chikkaballapura', 'davanagere', 'bagalkote', 
        'vijayapura', 'koppal', 'bidar', 'bengaluru rural', 'raichur', 'chamarajanagara', 'dakshina kannada', 'hassan', 'dharwad', 'shivamogga', 'udupi', 'gadag', 
        'thiruvananthapuram','kasaragod', 'malappuram', 'pathanamthitta', 'wayanad', 'alappuzha', 'kozhikode', 'kollam', 'thrissur', 'palakkad', 'kannur', 'kottayam', 
        'ernakulam', 'idukki', 'kargil', 'leh ladakh', 'lakshadweep', 'morena', 'alirajpur', 'sehore', 'rajgarh', 'khargone', 'satna', 'narsinghpur', 'jabalpur', 
        'hoshangabad', 'vidisha', 'balaghat', 'singrauli', 'betul', 'sidhi', 'datia', 'dewas', 'sheopur', 'neemuch', 'raisen', 'mandsaur', 'barwani', 'katni', 'dindori', 
        'shivpuri', 'gwalior', 'anuppur', 'agar malwa', 'ashoknagar', 'sagar', 'niwari', 'rewa', 'shajapur', 'ujjain', 'bhind', 'tikamgarh', 'seoni', 'harda', 'burhanpur', 
        'damoh', 'bhopal', 'jhabua', 'dhar', 'guna', 'east nimar', 'chhindwara', 'umaria', 'mandla', 'indore', 'shahdol', 'ratlam', 'panna', 'chhatarpur', 'jalgaon', 'latur',
        'thane', 'bhandara', 'nandurbar', 'chandrapur', 'kolhapur', 'solapur', 'mumbai', 'sindhudurg', 'dhule', 'wardha', 'parbhani', 'mumbai suburban', 'hingoli', 
        'ratnagiri', 'nanded', 'osmanabad', 'nagpur', 'buldhana', 'nashik', 'akola', 'yavatmal', 'amravati', 'washim', 'sangli', 'gadchiroli', 'raigad', 'palghar', 
        'jalna', 'gondia', 'ahmednagar','pune', 'beed', 'satara', 'kangpokpi', 'noney', 'imphal east', 'thoubal', 'kakching', 'jiribam', 'ukhrul', 'tamenglong', 'kamjong', 
        'chandel', 'bishnupur', 'senapati', 'pherzawl', 'churachandpur', 'tengnoupal', 'imphal west', 'north garo hills', 'south west khasi hills', 'west garo hills', 
        'south garo hills', 'east jaintia hills', 'south west garo hills', 'east khasi hills', 'east garo hills', 'ribhoi', 'west jaintia hills', 'west khasi hills', 
        'serchhip', 'aizawl', 'lunglei', 'mamit', 'lawngtlai', 'kolasib', 'champhai', 'saiha', 'mon', 'phek', 'longleng', 'mokokchung', 'kiphire', 'kohima', 'tuensang',
        'peren', 'dimapur', 'zunheboto', 'wokha', 'rayagada', 'koraput', 'malkangiri', 'sambalpur', 'kalahandi', 'anugul', 'ganjam', 'jajapur', 'bargarh', 'dhenkanal', 
        'bhadrak', 'nuapada', 'kendujhar', 'mayurbhanj', 'jharsuguda', 'kandhamal', 'deogarh', 'sundargarh', 'jagatsinghapur', 'balangir', 'baleshwar', 'puri', 'sonepur',
        'khordha', 'boudh', 'gajapati', 'nayagarh', 'nabarangpur', 'kendrapara', 'cuttack', 'karaikal', 'puducherry', 'yanam', 'mahe', 'shahid bhagat singh nagar', 
        'fazilka', 'barnala', 'mansa', 'ludhiana', 'sri muktsar sahib', 'patiala', 'pathankot', 'fatehgarh sahib', 'rupnagar', 'tarn taran', 'sas nagar', 'sangrur', 
        'jalandhar', 'bathinda', 'kapurthala', 'firozepur', 'gurdaspur', 'amritsar', 'faridkot', 'hoshiarpur', 'moga', 'pali', 'ganganagar', 'churu', 'jaipur', 'baran',
        'bhilwara', 'banswara', 'dungarpur', 'tonk', 'jodhpur', 'karauli', 'udaipur', 'dausa', 'nagaur', 'bharatpur', 'barmer', 'ajmer', 'chittorgarh', 'hanumangarh', 
        'pratapgarh', 'sawai madhopur', 'jalore', 'bikaner', 'sikar', 'dholpur', 'sirohi', 'rajsamand', 'jaisalmer', 'bundi', 'jhalawar', 'alwar', 'kota', 'jhunjhunu', 
        'tiruchirappalli', 'ramanathapuram', 'krishnagiri', 'cuddalore', 'kancheepuram', 'tiruppur', 'dharmapuri', 'thoothukkudi', 'thanjavur', 'madurai',
        'tiruvannamalai', 'salem', 'nagapattinam', 'tirupathur', 'ariyalur', 'chennai', 'the nilgiris', 'erode', 'karur', 'kallakkurichi', 'viluppuram', 
        'pudukkottai', 'perambalur', 'coimbatore', 'virudhunagar', 'dindigul', 'sivaganga', 'tenkasi', 'chengalpattu', 'kanniyakumari', 'tirunelveli', 'thiruvallur',
        'theni', 'ranipet', 'namakkal', 'vellore', 'thiruvarur']

brand_type= ['Apple', 'Asus', 'COOLPAD', 'Gionee', 'HMD Global', 'Huawei', 'Infinix', 'Lava', 'Lenovo','Lyf', 'Micromax', 
             'Motorola', 'OnePlus', 'Oppo', 'Others', 'Realme', 'Samsung', 'Tecno', 'Vivo', 'Xiaomi']


if SELECT == "Basic insights":
    st.title("BASIC INSIGHTS")
    #st.write("----")
    st.subheader("Let's know some basic insights about the data")
    options = ["--select--","Top 10 states based on year and amount of transaction","Least 10 states based on type and amount of transaction",
               "Top 10 mobile brands based on percentage of transaction","Top 10 Registered-users based on States and District(pincode)",
               "Top 10 Districts based on states and amount of transaction","Least 10 Districts based on states and amount of transaction",
               "Least 10 registered-users based on Districts and states","Top 10 transactions_type based on states and transaction_amount"]
    select = st.selectbox("Select the option",options)
    if select=="Top 10 states based on year and amount of transaction":
        mycursor.execute("SELECT DISTINCT State,Transaction_amount,Year,Quater FROM top_transaction GROUP BY State ORDER BY transaction_amount DESC LIMIT 10");
        df = pd.DataFrame(mycursor.fetchall(),columns=['State','Transaction_amount','Year','Quater'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 states based on type and amount of transaction")
            fig=px.bar(df,x="State",y="Transaction_amount")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)

with tab1:

    
    query1 = f"SELECT DISTINCT State, Quarter, Year, Transaction_type, Transaction_amount FROM aggregated_transaction WHERE Transaction_type IN {tuple(types)} ORDER BY State, Quarter, Year;"

    mycursor.execute(query1)
    df1 = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Quarter', 'Year', 'Transaction_type', 'Transaction_amount'])
    st.dataframe(df1)

    query2=f"SELECT DISTINCT State,Year,Quarter,Transaction_type,Transaction_amount FROM aggregated_transaction WHERE Year IN {tuple(year)} AND Transaction_type IN {tuple(types)} ORDER BY State,Quarter,Year;"
    mycursor.execute(query2)
    df2 = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Year',"Quarter", 'Transaction_type', 'Transaction_amount'])
    st.dataframe(df2)

    query3=f"SELECT DISTINCT State,Year,Quarter,Transaction_type,Transaction_amount FROM aggregated_transaction WHERE State IN {tuple(state)} AND Transaction_type IN {tuple(types)} And Year IN {tuple(year)} ORDER BY State,Quarter,Year;"
    mycursor.execute(query3)
    df3 = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Year',"Quarter", 'Transaction_type', 'Transaction_amount'])
    st.dataframe(df3)

    query4 =f"SELECT DISTINCT State,Year,Quarter,District,Transaction_amount FROM map_transaction WHERE State IN {tuple(state)} ORDER BY State,Year,Quarter,District;"
    mycursor.execute(query4)
    df4 = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Year',"Quarter", 'District', 'amount'])
    st.dataframe(df4)

    query5=f"SELECT DISTINCT State,Year,Quarter,District,Transaction_amount FROM map_transaction WHERE Year IN {tuple(year)} AND State IN {tuple(state)} ORDER BY State,Year,Quarter,District;"
    mycursor.execute(query5)
    df5 = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Year',"Quarter", 'District', 'amount'])
    st.dataframe(df5)

    query6=f"SELECT DISTINCT State,Year,Quarter,District,Transaction_amount FROM map_transaction WHERE District IN {tuple(dist)} AND State IN {tuple(state)} AND Year IN {tuple(year)} ORDER BY State,Year,Quarter,District;"
    mycursor.execute(query6)
    df6 = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Year',"Quarter", 'District', 'amount'])
    st.dataframe(df6)

    query10=f"SELECT State,Year,Quarter,District_pincode,Transaction_count,Transaction_amount FROM top_transaction WHERE State IN {tuple(state)} GROUP BY State,Year,Quarter;"
    mycursor.execute(query10)
    df10 = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Year',"Quarter", 'District', 'Transaction_count', 'Transaction_amount'])
    st.dataframe(df10)

    query11=f"SELECT State,Year,Quarter,District_pincode,Transaction_count,Transaction_amount FROM top_transaction WHERE Year IN {tuple(year)} AND State IN {tuple(state)} GROUP BY State,Year,Quarter;"
    mycursor.execute(query11)
    df11 = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Year',"Quarter", 'District', 'Transaction_count', 'Transaction_amount'])
    st.dataframe(df11)

    query12=f"SELECT State,Year,Quarter,District_pincode,Transaction_count,Transaction_amount FROM top_transaction WHERE Year IN {tuple(year)} AND Quarter IN {tuple(quarter)} AND State IN {tuple(state)} GROUP BY State,Year,Quarter;"
    mycursor.execute(query12)
    df12 = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Year','Quarter', 'District', 'Transaction_count', 'Transaction_amount'])
    st.dataframe(df12)

with tab2:
    query7=f"SELECT State,Year,Quarter,brands,Percentage FROM aggregated_user WHERE brands IN {tuple(brand_type)} ORDER BY State,Year,Quarter,brands,Percentage DESC;"
    mycursor.execute(query7)
    df7 = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Year',"Quarter", 'brands', 'Percentage'])
    st.dataframe(df7)

    query8=f"SELECT State,Year,Quarter,brands,Percentage FROM aggregated_user WHERE Year IN {tuple(year)} AND brands IN {tuple(brand_type)} ORDER BY State,Year,Quarter,brands,Percentage DESC;"
    mycursor.execute(query8)
    df8 = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Year',"Quarter", 'brands', 'Percentage'])
    st.dataframe(df8)

    query9=f"SELECT State,Year,Quarter,brands,Percentage FROM aggregated_user WHERE State IN {tuple(state)} AND brands IN {tuple(brand_type)} AND Year IN {tuple(year)} ORDER BY State,Year,Quarter,brands,Percentage DESC"
    mycursor.execute(query9)
    df9 = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Year',"Quarter", 'brands', 'Percentage'])
    st.dataframe(df9)

    query13=f"SELECT State,Year,Quarter,District,Registered_User FROM map_user WHERE State IN {tuple(state)} ORDER BY State,Year,Quarter,District"
    mycursor.execute(query13)
    df13 = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Year',"Quarter", 'District', 'RegisteredUser'])
    st.dataframe(df13)

    query14=f"SELECT State,Year,Quarter,District,Registered_User FROM map_user WHERE Year IN {tuple(year)} AND State IN {tuple(state)} ORDER BY State,Year,Quarter,District"
    mycursor.execute(query14)
    df14 = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Year',"Quarter", 'District', 'RegisteredUser'])
    st.dataframe(df14)

    query15=f"SELECT State,Year,Quarter,District,Registered_User FROM map_user WHERE Year IN {tuple(year)} AND State IN {tuple(state)} AND District = {tuple(dist)} ORDER BY State,Year,Quarter,District;"
    mycursor.execute(query15)
    df15 = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Year',"Quarter", 'District', 'RegisteredUser'])
    st.dataframe(df15)