#Dependencies - Python 3, pandas
import matplotlib.pyplot as plt
import pandas as pd 
from flask import Flask, request, redirect, jsonify, render_template

app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
	
		

	return render_template("index.html")

@app.route('/results', methods=['GET','POST'])
def load_results():
	df = pd.read_csv('payday_forecast_new.csv')
	df2 = pd.read_csv('payday_forecast_old.csv')



	#Data Prep
	#latest dataset
	clean_data = pd.DataFrame(df, columns={"Issue Type","Custom field (Story Points)","Component/s",
											"Fix Version/s","Sprint","Labels","Status","Resolution"})
	# #older dataset
	# clean_data_2 = pd.DataFrame(df2, columns={"Issue Type","Custom field (Story Points)","Component/s",
	# 										"Fix Version/s","Sprint","Labels","Status","Resolution"})
	#Fill NaN Story Point values with Average = 7
	clean_data[['Custom field (Story Points)']] = clean_data[['Custom field (Story Points)']].fillna(value = 7)
	# clean_data_2[['Custom field (Story Points)']] = clean_data_2[['Custom field (Story Points)']].fillna(value = 7)

	#average story point
	average_sp = clean_data['Custom field (Story Points)'].mean()
	####---- lists to store values from loop ---####
	sp_list = []
	sp_done_list = []
	perc_completed_list = []

	#get unique releases
	unique_release = clean_data['Fix Version/s'].unique()
	# unique_release_2 = clean_data_2['Fix Version/s'].unique()

	### INFO - This loop grabs the TOTAL sum for each unique Version and appends it to lists-- line 35
	for x in unique_release:
		release_total_df = clean_data.loc[clean_data['Fix Version/s'] == x]
		# release_completed_df = (release_total_df) & (clean_data.loc[clean_data['Resolution']=='Done'])
		release_completed_df_2 = release_total_df.loc[release_total_df['Resolution']=='Done']
		total_done_sp = release_completed_df_2['Custom field (Story Points)'].sum()
		sp_done_list.append(total_done_sp)
		
		#sum of total story points in backlog per release
		total_story_point = release_total_df['Custom field (Story Points)'].sum()

		sp_list.append(total_story_point)

		#percent of compeltion per release
		perc_completed=(total_done_sp/total_story_point)*100
		perc_completed_list.append(perc_completed)

	#dataframe to merge data into one view
	total_done_sp_release = pd.DataFrame(columns = unique_release, data=[sp_list,sp_done_list,perc_completed_list], index=['total sp', 'total sp done','%completed'])



	#(G) Velocity Attainment - investigation story points of start of sprint/total completed 


	#---New/Existing - Keep or throw out

	#average Story Point/Team/Program? 
	##Change in Average? 

	#Burnup Chart Numbers/team/release
	#Fix Version - MVP/R1/R2/R3
	#label - SPN, MIT
	#fix = SPN, MIT
	#label = MVP 

	#Team       R1.   R2.  R3. 
	#Lannister. 200
	#Targaryen. 200
	#Stark.     200
	#total.     600


	#Scope Change Analysis (PI or Release? Split by team?)
	#Release %    Story points
	#R1.     4%.  20
	#R2.     6%.  30   

	#Scope Change per Team & Release? 
	#Targaryen 
	##Release. %.  Story Points

	#Lannister 
	##Release. %.  Story Points
	# return render_template("results.html", tables=[total_done_sp_release.to_html(classes='table')],titles=['test'])
	return render_template('results.html', data_frame=total_done_sp_release.to_html(classes='table'), data2= clean_data.head(10).to_html(classes='table'))
if __name__ == "__main__":
	app.run()	










