#Dependencies - Python 3, pandas
import matplotlib.pyplot as plt
import pandas as pd 

#READ CSV
#file_new= r'payday_forecast_new.csv'
#file_old = r'payday_forecast_old.csv'
df = pd.read_csv('payday_forecast_new.csv')
df2 = pd.read_csv('payday_forecast_old.csv')

########################## CLEAN DATA ###################################
clean_data = pd.DataFrame(df, columns={"Issue Type","Custom field (Story Points)","Component/s","Fix Version/s","Sprint"})
#Looks for NaN values in Story points, updates with 7 if NaN=True
clean_data[['Custom field (Story Points)']] = clean_data[['Custom field (Story Points)']].fillna(value = 7)
no_martell_clean = clean_data.loc[(clean_data['Component/s']!= "Martell")]
total_sum = no_martell_clean['Custom field (Story Points)'].sum()

martell_data = clean_data.loc[(clean_data['Component/s'] == "Martell")]
total_martell = martell_data['Custom field (Story Points)'].sum()
########################## NEW TEAM CLEAN DATA ###################################
spine_total_df = no_martell_clean.loc[no_martell_clean['Fix Version/s'] == "Spine"]
martell_spine_total_df = martell_data.loc[martell_data['Fix Version/s'] == "Spine"]

tmc_total_df = no_martell_clean.loc[(no_martell_clean['Fix Version/s'] == "Trauma") | (no_martell_clean['Fix Version/s'] == "CMF")|(no_martell_clean['Fix Version/s'] == "MIT")]  
recon_total_df = no_martell_clean.loc[(no_martell_clean['Fix Version/s'] == "Recon - Direct ") | (no_martell_clean['Fix Version/s'] == "Recon - Distributer")]  
ecl_total_df = no_martell_clean.loc[(no_martell_clean['Fix Version/s'] == "ETH") | (no_martell_clean['Fix Version/s'] == "CSS")| (no_martell_clean['Fix Version/s'] == "LastBu")]  

        

########################## Total Team Average Story Points ####################
#av_total = clean_data['Custom field (Story Points)'].mean()
#print("Total Team Average: ",av_total)
###################### Stark Team Average Story Points ###################
#clean_data_stark = clean_data.loc[clean_data['Component/s'] == "Stark"]
#av_total_stark = clean_data_stark['Custom field (Story Points)'].mean()
#print("Total Stark Team Average: ", av_total_stark)
###################### Stark Team Average Story Points ###################
#av_total_spine = spine_total_df['Custom field (Story Points)'].mean()
#print("Total Stark Team Average: ", av_total_spine)

########################### PERCENT CHANGE ##############################
 
#compare with previous data for %change = ((y2 - y1) / y1)*100
percent_change = pd.DataFrame(df2, columns={"Issue Type","Custom field (Story Points)","Component/s","Fix Version/s","Sprint"})

#Looks for NaN values in Story points, updates with 7 if NaN=True
percent_change[['Custom field (Story Points)']] = percent_change[['Custom field (Story Points)']].fillna(value = 7)
no_martell_pc = percent_change.loc[(percent_change['Component/s']!= "Martell")]
total_sum_2 = no_martell_pc['Custom field (Story Points)'].sum()
total_diff = total_sum-total_sum_2
percent_change_total = ((total_diff/total_sum)*100)

########################## SPINE ########################################
#READ DATA, SPINE ONLY, ALL TEAMS
total_spine = spine_total_df['Custom field (Story Points)'].sum()
martell_total_spine = martell_spine_total_df['Custom field (Story Points)'].sum()




#SPINE PERCENT CHANGE
spine_total_df2 = no_martell_pc.loc[no_martell_pc['Fix Version/s'] == "Spine"]
total_spine_old = spine_total_df2['Custom field (Story Points)'].sum()
spine_diff = total_spine-total_spine_old
spine_percent_change = ((spine_diff/total_spine)*100)


#STARK TOTALS
spine_stark = spine_total_df.loc[spine_total_df['Component/s']=="Stark"]
total_spine_stark = spine_stark['Custom field (Story Points)'].sum()
#STARK PREVIOUS TOTALS
spine_stark_old = spine_total_df2.loc[spine_total_df2['Component/s']=="Stark"]
total_spine_stark_old = spine_stark_old['Custom field (Story Points)'].sum()
change_spine_stark = total_spine_stark - total_spine_stark_old

#LANNISTER TOTALS
spine_lannister = spine_total_df.loc[spine_total_df['Component/s']=="Lannister"]
total_spine_lannister = spine_lannister['Custom field (Story Points)'].sum()
#LANNISTER PREVIOUS TOTALS
spine_lannister_old = spine_total_df2.loc[spine_total_df2['Component/s']=="Lannister"]
total_spine_lannister_old = spine_lannister_old['Custom field (Story Points)'].sum()
change_spine_lannister = total_spine_lannister - total_spine_lannister_old

#TARGARYEN TOTALS
spine_targaryen = spine_total_df.loc[spine_total_df['Component/s']=="Targaryen"]
total_spine_targaryen = spine_targaryen['Custom field (Story Points)'].sum()
#TARGARYEN PREVIOUS TOTALS
spine_targaryen_old = spine_total_df2.loc[spine_total_df2['Component/s']=="Targaryen"]
total_spine_targaryen_old = spine_targaryen_old['Custom field (Story Points)'].sum()
change_spine_targaryen = total_spine_targaryen - total_spine_targaryen_old

#MORMONT TOTALS
spine_mormont = spine_total_df.loc[spine_total_df['Component/s']=="Mormont"]
total_spine_mormont = spine_mormont['Custom field (Story Points)'].sum()
#MORMONT PREVIOUS TOTALS
spine_mormont_old = spine_total_df2.loc[spine_total_df2['Component/s']=="Mormont"]
total_spine_mormont_old = spine_mormont_old['Custom field (Story Points)'].sum()
change_spine_mormont = total_spine_mormont - total_spine_mormont_old
#FINAL DATAFRAME - SPINE
all_spine_df = pd.DataFrame(columns = ['Stark',
                                       'Lannister', 
                                       'Targaryen',
                                       'Mormont',
                                       'All Spine'], data= [[total_spine_stark, total_spine_lannister, total_spine_targaryen, total_spine_mormont, total_spine]], index=['Data'])


########################## MIT/TRAUMA/CMF #####################################

#READ DATA, FILTER CRITERIA FOR RELEASE
tmc_total = tmc_total_df['Custom field (Story Points)'].sum()

#PERCENT CHANGE 
tmc_total_df2 = no_martell_pc.loc[(no_martell_pc['Fix Version/s'] == "Trauma") | (no_martell_pc['Fix Version/s'] == "CMF")|(no_martell_pc['Fix Version/s'] == "MIT")] 
tmc_total_old = tmc_total_df['Custom field (Story Points)'].sum()
print(tmc_total_old)
tmc_diff = tmc_total - tmc_total_old
print("tar diff debug: ", tmc_diff)
tmc_percent_change = ((tmc_diff/tmc_total)*100)
print("targaryen Debug %: ", tmc_percent_change)

#STARK TOTALS
tmc_stark = tmc_total_df.loc[tmc_total_df['Component/s']=="Stark"]
total_tmc_stark = tmc_stark['Custom field (Story Points)'].sum()
#STARK PREVIOUS TOTALS
tmc_stark_old = tmc_total_df2.loc[tmc_total_df2['Component/s']=="Stark"]
total_tmc_stark_old = tmc_stark_old['Custom field (Story Points)'].sum()
change_tmc_stark = total_tmc_stark - total_tmc_stark_old

#LANNISTER TOTALS - Debug
tmc_lannister = tmc_total_df.loc[tmc_total_df['Component/s']=="Lannister"]
total_tmc_lannister = tmc_lannister['Custom field (Story Points)'].sum()
print(total_tmc_lannister)
#LANNISTER PREVIOUS TOTALS
tmc_lannister_old = tmc_total_df2.loc[tmc_total_df2['Component/s']=="Lannister"]
total_tmc_lannister_old = tmc_lannister_old['Custom field (Story Points)'].sum()
print(total_tmc_lannister_old)
change_tmc_lannister = total_tmc_lannister - total_tmc_lannister_old

#TARGARYEN TOTALS - Debug
tmc_targaryen = tmc_total_df.loc[tmc_total_df['Component/s']=="Targaryen"]
total_tmc_targaryen = tmc_targaryen['Custom field (Story Points)'].sum()
print("Debug Targaryen: ", total_tmc_targaryen)
#TARGARYEN PREVIOUS TOTALS
tmc_targaryen_old = tmc_total_df2.loc[tmc_total_df2['Component/s']=="Targaryen"]
total_tmc_targaryen_old = tmc_targaryen_old['Custom field (Story Points)'].sum()
print("Debug Targaryen: " , total_tmc_targaryen_old)

change_tmc_targaryen = total_tmc_targaryen - total_tmc_targaryen_old
print("Debug Targaryen: ", change_tmc_targaryen)

#MORMONT TOTALS
tmc_mormont = tmc_total_df.loc[tmc_total_df['Component/s']=="Mormont"]
total_tmc_mormont = tmc_mormont['Custom field (Story Points)'].sum()
#MORMONT PREVIOUS TOTALS
tmc_mormont_old = tmc_total_df2.loc[tmc_total_df2['Component/s']=="Mormont"]
total_tmc_mormont_old = tmc_mormont_old['Custom field (Story Points)'].sum()
change_tmc_mormont = total_tmc_mormont - total_tmc_mormont_old

#FINAL DATAFRAME
all_tmc_df = pd.DataFrame(columns = ['Stark',
                                       'Lannister', 
                                       'Targaryen',
                                       'Mormont',
                                       'All MIT/Trauma/CMF'], data= [[total_tmc_stark, total_tmc_lannister, total_tmc_targaryen, total_tmc_mormont, tmc_total]], index=['Data'])
########################## RECON #####################################

#READ DATA, FILTER CRITERIA
recon_total = recon_total_df['Custom field (Story Points)'].sum()

#PERCENT CHANGE
recon_total_df2 = no_martell_pc.loc[(no_martell_pc['Fix Version/s'] == "Recon - Direct ") | (no_martell_pc['Fix Version/s'] == "Recon - Distributer")]  
recon_total_old = recon_total_df2['Custom field (Story Points)'].sum()
recon_diff = recon_total-recon_total_old 
recon_percent_change = ((recon_diff/recon_total)*100)

#STARK
recon_stark = recon_total_df.loc[recon_total_df['Component/s']=="Stark"]
total_recon_stark = recon_stark['Custom field (Story Points)'].sum()
#STARK PREVIOUS TOTALS
recon_stark_old = recon_total_df2.loc[recon_total_df2['Component/s']=="Stark"]
total_recon_stark_old = recon_stark_old['Custom field (Story Points)'].sum()
change_recon_stark = total_recon_stark - total_recon_stark_old

#LANNISTER
recon_lannister = recon_total_df.loc[recon_total_df['Component/s']=="Lannister"]
total_recon_lannister = recon_lannister['Custom field (Story Points)'].sum()
#LANNISTER PREVIOUS TOTALS
recon_lannister_old = recon_total_df2.loc[recon_total_df2['Component/s']=="Lannister"]
total_recon_lannister_old = recon_lannister_old['Custom field (Story Points)'].sum()
change_recon_lannister = total_recon_lannister - total_recon_lannister_old

#TARGARYEN
recon_targaryen = recon_total_df.loc[recon_total_df['Component/s']=="Targaryen"]
total_recon_targaryen = recon_targaryen['Custom field (Story Points)'].sum()
#TARGARYEN PREVIOUS TOTALS
recon_targaryen_old = recon_total_df2.loc[recon_total_df2['Component/s']=="Targaryen"]
total_recon_targaryen_old = recon_targaryen_old['Custom field (Story Points)'].sum()
change_recon_targaryen = total_recon_targaryen - total_recon_targaryen_old

#MORMONT
recon_mormont = recon_total_df.loc[recon_total_df['Component/s']=="Mormont"]
total_recon_mormont = recon_mormont['Custom field (Story Points)'].sum()
#MORMONT PREVIOUS TOTALS
recon_mormont_old = recon_total_df2.loc[recon_total_df2['Component/s']=="Mormont"]
total_recon_mormont_old = recon_mormont_old['Custom field (Story Points)'].sum()
change_recon_mormont = total_recon_mormont - total_recon_mormont_old

#FINAL DATAFRAME
all_recon_df = pd.DataFrame(columns = ['Stark',
                                       'Lannister', 
                                       'Targaryen',
                                       'Mormont',
                                       'All Recon'], data= [[total_recon_stark, total_recon_lannister, total_recon_targaryen, total_recon_mormont, recon_total]],index=['Data'])
########################## ETH/CSS/LASTBU #####################################

#READ DATA, FILTER CRITERIA 
ecl_total = ecl_total_df['Custom field (Story Points)'].sum()

#PERCENT CHANGE
ecl_total_df2 = no_martell_pc.loc[(no_martell_pc['Fix Version/s'] == "ETH") | (no_martell_pc['Fix Version/s'] == "CSS")| (no_martell_pc['Fix Version/s'] == "LastBu")]  
ecl_total_old = ecl_total_df2['Custom field (Story Points)'].sum()
ecl_diff = ecl_total-ecl_total_old
ecl_percent_change = ((ecl_diff/ecl_total)*100)

#STARK TOTALS
ecl_stark = ecl_total_df.loc[ecl_total_df['Component/s']=="Stark"]
total_ecl_stark = ecl_stark['Custom field (Story Points)'].sum()
#STARK PREVIOUS TOTALS
ecl_stark_old = ecl_total_df2.loc[ecl_total_df2['Component/s']=="Stark"]
total_ecl_stark_old = ecl_stark_old['Custom field (Story Points)'].sum()
change_ecl_stark = total_ecl_stark - total_ecl_stark_old

#LANNISTER TOTALS
ecl_lannister = ecl_total_df.loc[ecl_total_df['Component/s']=="Lannister"]
total_ecl_lannister = ecl_lannister['Custom field (Story Points)'].sum()
#LANNISTER PREVIOUS TOTALS
ecl_lannister_old = ecl_total_df2.loc[ecl_total_df2['Component/s']=="Lannister"]
total_ecl_lannister_old = ecl_lannister_old['Custom field (Story Points)'].sum()
change_ecl_lannister = total_ecl_lannister - total_ecl_lannister_old

#TARGARYEN TOTALS
ecl_targaryen = ecl_total_df.loc[ecl_total_df['Component/s']=="Targaryen"]
total_ecl_targaryen = ecl_targaryen['Custom field (Story Points)'].sum()
#TARGARYEN PREVIOUS TOTALS
ecl_targaryen_old = ecl_total_df2.loc[ecl_total_df2['Component/s']=="Targaryen"]
total_ecl_targaryen_old = ecl_targaryen_old['Custom field (Story Points)'].sum()
change_ecl_targaryen = total_ecl_targaryen - total_ecl_targaryen_old


#MORMONT TOTALS
ecl_mormont = ecl_total_df.loc[ecl_total_df['Component/s']=="Mormont"]
total_ecl_mormont = ecl_mormont['Custom field (Story Points)'].sum()
#MORMONT PREVIOUS TOTALS
ecl_mormont_old = ecl_total_df2.loc[ecl_total_df2['Component/s']=="Mormont"]
total_ecl_mormont_old = ecl_mormont_old['Custom field (Story Points)'].sum()
change_ecl_mormont = total_ecl_mormont - total_ecl_mormont_old

#FINAL DATAFRAME
all_ecl_df = pd.DataFrame(columns = ['Stark',
                                       'Lannister', 
                                       'Targaryen',
                                       'Mormont',
                                       'All ETH/CSS/LastBu'], data= [[total_ecl_stark, total_ecl_lannister, total_ecl_targaryen, total_ecl_mormont, ecl_total]], index=['Data'])
############################# BURN-UP TOTALS ############################################
#FINAL VIEWS 
tmc_total_sum = total_spine + tmc_total
recon_total_sum = tmc_total_sum+recon_total
ecl_total_sum = recon_total_sum+ecl_total

df_index = [['All']]
df_col = [['Spine','Trauma/CMF/MIT','Recon', 'ETH/CSS/LastBu','Total']]
last_view = pd.DataFrame(columns=['Spine','Trauma/CMF/MIT','Recon', 'ETH/CSS/LastBu','Total'], index=['All'],data = [[total_spine, tmc_total_sum, recon_total_sum, ecl_total_sum, total_sum]])


########################### PRINT STATEMENTS ##############################################

print("========================================================================")
print("START OF REPORT")
print("========================================================================")

print("This report shows data used for Payday Analysis")

print("========================================================================")
print("Spine Analysis")
print("========================================================================")
print("Current Spine total: ", total_spine)
print("Old Spine total: ", total_spine_old)
print("Stark Total Change: ", change_spine_stark)
print("Martell Spine Total: ", martell_total_spine)
print("Lannister Total Change: ", change_spine_lannister)
print("Targaryen Total Change: ", change_spine_targaryen)
print("Mormont Total Change: ", change_spine_mormont)
print("Spine Release Change in Story Points: ", spine_diff)
print("Spine Percent Change: ", spine_percent_change, "%")
print("All Spine Data: ")
print(all_spine_df)
print("------------------------------------------------------------------------")

print("========================================================================")
print("Trauma/CMF/MIT Analysis")
print("========================================================================")
print("Current Trauma/CMF/MIT Total: ", tmc_total)
print("Old Trauma/CMF/MIT total: ", tmc_total_old)
print("Stark Total Change: ", change_tmc_stark)
print("Lannister Total Change: ", change_tmc_lannister)
print("Targaryen Total Change: ", change_tmc_targaryen)
print("Mormont Total Change: ", change_tmc_mormont)
print("Trauma/CMF/MIT Release change in Story Points: ", tmc_diff)
print("Trauma/CMF/MIT: ", tmc_percent_change, "%")
print("All Trauma/CMF/MIT Data: ")
print(all_tmc_df)
print("------------------------------------------------------------------------")

print("========================================================================")
print("Recon Analysis")
print("========================================================================")
print("Current Recon: ", recon_total)
print("Old Recon: ", recon_total_old)
print("Stark Total Change: ", change_recon_stark)
print("Lannister Total Change: ", change_recon_lannister)
print("Targaryen Total Change: ", change_recon_targaryen)
print("Mormont Total Change: ", change_recon_mormont)
print("Recon Release Change in Story Points: ", recon_diff)
print("Recon Percent Change: ", recon_percent_change,"%")
print("All Recon Data: ")
print(all_recon_df)
print("------------------------------------------------------------------------")

print("========================================================================")
print("ETH/CSS/LastBu Analysis")
print("========================================================================")
print("Current ETH/CSS/LastBu: ", ecl_total)
print("Old ETH/CSS/LastBu: ", ecl_total_old)
print("Stark Total Change: ", change_ecl_stark)
print("Lannister Total Change: ", change_ecl_lannister)
print("Targaryen Total Change: ", change_ecl_targaryen)
print("Mormont Total Change: ", change_ecl_mormont)
print("ETH/CSS/LastBu Release Change in Story Points: ", ecl_diff)
print("ETH/CSS/LastBu Percent Change: ", ecl_percent_change,"%")
print("All ETH/CSS/LastBu Data: ")
print(all_ecl_df)
print("------------------------------------------------------------------------")

print("========================================================================")
print("Total Backlog Analysis")
print("========================================================================")
print("Total Backlog Change in Story Points: ", total_diff)
print("Total Percent Change: ", percent_change_total, "%")
print("Final Burn Up data: ")
print(last_view)
print("========================================================================")
print("End of Report, Created by Zach Quasney")
print("========================================================================")

      