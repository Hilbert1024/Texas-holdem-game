import numpy as np
import pandas as pd

path = 'train_data.csv'
train = pd.read_csv(path)
def DF_pct(train):
	train1 = train[['Pick1','Result']]
	train2 = train[['Pick2','Result']]
	train3 = train[['Pick3','Result']]

	#Train1
	train1_1 = train1[train1.Pick1<200]
	train1_1_win = train1_1[train1_1.Result==1].shape[0]/train1_1.shape[0]
	train1_1_draw = train1_1[train1_1.Result==0].shape[0]/train1_1.shape[0]
	train1_1_lose = train1_1[train1_1.Result==-1].shape[0]/train1_1.shape[0]

	train1_2 = train1[train1.Pick1>200]
	train1_2 = train1_2[train1_2.Pick1<300]
	train1_2_win = train1_2[train1_2.Result==1].shape[0]/train1_2.shape[0]
	train1_2_draw = train1_2[train1_2.Result==0].shape[0]/train1_2.shape[0]
	train1_2_lose = train1_2[train1_2.Result==-1].shape[0]/train1_2.shape[0]

	train1_3 = train1[train1.Pick1>300]
	train1_3 = train1_3[train1_3.Pick1<400]
	train1_3_win = train1_3[train1_3.Result==1].shape[0]/train1_3.shape[0]
	train1_3_draw = train1_3[train1_3.Result==0].shape[0]/train1_3.shape[0]
	train1_3_lose = train1_3[train1_3.Result==-1].shape[0]/train1_3.shape[0]

	train1_4 = train1[train1.Pick1>400]
	train1_4 = train1_4[train1_4.Pick1<500]
	train1_4_win = train1_4[train1_4.Result==1].shape[0]/train1_4.shape[0]
	train1_4_draw = train1_4[train1_4.Result==0].shape[0]/train1_4.shape[0]
	train1_4_lose = train1_4[train1_4.Result==-1].shape[0]/train1_4.shape[0]


	#Train2
	train2_1 = train2[train2.Pick2<200]
	train2_1_win = train2_1[train2_1.Result==1].shape[0]/train2_1.shape[0]
	train2_1_draw = train2_1[train2_1.Result==0].shape[0]/train2_1.shape[0]
	train2_1_lose = train2_1[train2_1.Result==-1].shape[0]/train2_1.shape[0]

	train2_2 = train2[train2.Pick2>200]
	train2_2 = train2_2[train2_2.Pick2<300]
	train2_2_win = train2_2[train2_2.Result==1].shape[0]/train2_2.shape[0]
	train2_2_draw = train2_2[train2_2.Result==0].shape[0]/train2_2.shape[0]
	train2_2_lose = train2_2[train2_2.Result==-1].shape[0]/train2_2.shape[0]

	train2_3 = train2[train2.Pick2>300]
	train2_3 = train2_3[train2_3.Pick2<400]
	train2_3_win = train2_3[train2_3.Result==1].shape[0]/train2_3.shape[0]
	train2_3_draw = train2_3[train2_3.Result==0].shape[0]/train2_3.shape[0]
	train2_3_lose = train2_3[train2_3.Result==-1].shape[0]/train2_3.shape[0]

	train2_4 = train2[train2.Pick2>400]
	train2_4 = train2_4[train2_4.Pick2<500]
	train2_4_win = train2_4[train2_4.Result==1].shape[0]/train2_4.shape[0]
	train2_4_draw = train2_4[train2_4.Result==0].shape[0]/train2_4.shape[0]
	train2_4_lose = train2_4[train2_4.Result==-1].shape[0]/train2_4.shape[0]

	train2_5 = train2[train2.Pick2>500]
	train2_5 = train2_5[train2_5.Pick2<600]
	train2_5_win = train2_5[train2_5.Result==1].shape[0]/train2_5.shape[0]
	train2_5_draw = train2_5[train2_5.Result==0].shape[0]/train2_5.shape[0]
	train2_5_lose = train2_5[train2_5.Result==-1].shape[0]/train2_5.shape[0]

	train2_6 = train2[train2.Pick2>600]
	train2_6 = train2_6[train2_6.Pick2<700]
	train2_6_win = train2_6[train2_6.Result==1].shape[0]/train2_6.shape[0]
	train2_6_draw = train2_6[train2_6.Result==0].shape[0]/train2_6.shape[0]
	train2_6_lose = train2_6[train2_6.Result==-1].shape[0]/train2_6.shape[0]

	train2_7 = train2[train2.Pick2>700]
	train2_7 = train2_7[train2_7.Pick2<800]
	train2_7_win = train2_7[train2_7.Result==1].shape[0]/train2_7.shape[0]
	train2_7_draw = train2_7[train2_7.Result==0].shape[0]/train2_7.shape[0]
	train2_7_lose = train2_7[train2_7.Result==-1].shape[0]/train2_7.shape[0]


	#Train3

	train3_1 = train3[train3.Pick3<200]
	train3_1_win = train3_1[train3_1.Result==1].shape[0]/train3_1.shape[0]
	train3_1_draw = train3_1[train3_1.Result==0].shape[0]/train3_1.shape[0]
	train3_1_lose = train3_1[train3_1.Result==-1].shape[0]/train3_1.shape[0]

	train3_2 = train3[train3.Pick3>200]
	train3_2 = train3_2[train3_2.Pick3<300]
	train3_2_win = train3_2[train3_2.Result==1].shape[0]/train3_2.shape[0]
	train3_2_draw = train3_2[train3_2.Result==0].shape[0]/train3_2.shape[0]
	train3_2_lose = train3_2[train3_2.Result==-1].shape[0]/train3_2.shape[0]

	train3_3 = train3[train3.Pick3>300]
	train3_3 = train3_3[train3_3.Pick3<400]
	train3_3_win = train3_3[train3_3.Result==1].shape[0]/train3_3.shape[0]
	train3_3_draw = train3_3[train3_3.Result==0].shape[0]/train3_3.shape[0]
	train3_3_lose = train3_3[train3_3.Result==-1].shape[0]/train3_3.shape[0]

	train3_4 = train3[train3.Pick3>400]
	train3_4 = train3_4[train3_4.Pick3<500]
	train3_4_win = train3_4[train3_4.Result==1].shape[0]/train3_4.shape[0]
	train3_4_draw = train3_4[train3_4.Result==0].shape[0]/train3_4.shape[0]
	train3_4_lose = train3_4[train3_4.Result==-1].shape[0]/train3_4.shape[0]

	train3_5 = train3[train3.Pick3>500]
	train3_5 = train3_5[train3_5.Pick3<600]
	train3_5_win = train3_5[train3_5.Result==1].shape[0]/train3_5.shape[0]
	train3_5_draw = train3_5[train3_5.Result==0].shape[0]/train3_5.shape[0]
	train3_5_lose = train3_5[train3_5.Result==-1].shape[0]/train3_5.shape[0]

	train3_6 = train3[train3.Pick3>600]
	train3_6 = train3_6[train3_6.Pick3<700]
	train3_6_win = train3_6[train3_6.Result==1].shape[0]/train3_6.shape[0]
	train3_6_draw = train3_6[train3_6.Result==0].shape[0]/train3_6.shape[0]
	train3_6_lose = train3_6[train3_6.Result==-1].shape[0]/train3_6.shape[0]

	train3_7 = train3[train3.Pick3>700]
	train3_7 = train3_7[train3_7.Pick3<800]
	train3_7_win = train3_7[train3_7.Result==1].shape[0]/train3_7.shape[0]
	train3_7_draw = train3_7[train3_7.Result==0].shape[0]/train3_7.shape[0]
	train3_7_lose = train3_7[train3_7.Result==-1].shape[0]/train3_7.shape[0]

	# train3_8 = train3[train3.Pick3>800][train3.Pick3<900]
	# train3_8_win = train3_8[train3.Result==1].shape[0]/train3_8.shape[0]
	# train3_8_draw = train3_8[train3.Result==0].shape[0]/train3_8.shape[0]
	# train3_8_lose = train3_8[train3.Result==-1].shape[0]/train3_8.shape[0]
	temp1=temp2=temp3=win=draw=lose=WDL_df1=WDL_df2=WDL_df3=[]
	names=locals()
	for i in range(1,4):
		win=[]
		draw=[]
		lose=[]
		for j in range(1,8):
			try:
				temp1=names['train%d_%d_win'%(i,j)]
				temp2=names['train%d_%d_draw'%(i,j)]
				temp3=names['train%d_%d_lose'%(i,j)]
			except KeyError:
				temp1=np.nan
				temp2=np.nan
				temp3=np.nan
			win.append(temp1)
			draw.append(temp2)
			lose.append(temp3)
		names['WDL_df%d'%i]=pd.DataFrame({'Win':win,'Draw':draw,'Lose':lose})
	WDL_df1=names['WDL_df1']
	WDL_df2=names['WDL_df2']
	WDL_df3=names['WDL_df3']
	return WDL_df1,WDL_df2,WDL_df3


df1,df2,df3=DF_pct(train)
