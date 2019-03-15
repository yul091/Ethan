#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sys
import os
sns.set(style="darkgrid")


# In[3]:


addmission_csv  = 'Admission_Predict_Ver1.1.csv'


# In[4]:


addmission = pd.read_csv(addmission_csv)


# In[5]:


addmission = addmission.drop('Serial No.', axis=1,inplace = False)
def modiffy(row):
    if row['Chance of Admit '] >0.7 :
        return 1
    else :
        return 0

addmission['Admit'] = addmission.apply(modiffy,axis=1)


# In[5]:


addmission.head()


# In[8]:


addmission_des = addmission.describe()
for i in addmission_des:
    addmission_des[i] = addmission_des[i].map(lambda x:('%.2f')%x)
    addmission_des[i][0] = int(float(addmission_des[i][0]))
addmission_des


# In[10]:


GRE = list(addmission['GRE Score'])
TOEFL = list(addmission['TOEFL Score'])
UR = list(addmission['University Rating'])
SOP = list(addmission['SOP'])
GPA = list(addmission['CGPA'])
Research = list(addmission['Research'])
LOR = list(addmission['LOR '])
Label = list(addmission['Chance of Admit '])


# In[8]:


addmission_CGPA = addmission['CGPA']


# In[11]:


score_list = []
frequency_list = np.zeros((1,10))
for i in GRE:
    if i not in score_list:
        score_list.append(i)
n0 = 290
gap = 5
for i in score_list:
    
    if i != 340:
        frequency_list[0,(i-n0)//gap] += GRE.count(i)
    else:
        frequency_list[0,-1] += GRE.count(i)
score_rangelist = list(np.linspace(290,335,10))
plt.figure(edgecolor='black')
# GRE
def draw_hist(score_list,frequency_list):
    fig1 = plt.subplot2grid((1,1),(0,0))
    #fig1 = plt.figure(0)
    rects = plt.bar(x=tuple(score_rangelist),height=tuple(frequency_list[0]),width=4.8,bottom=0,color=sns.cubehelix_palette(10, start=0.5, rot=0.3, dark=0.2, light=.8, reverse=True),align='edge')
    plt.xlabel('Score')
    plt.xlim(290,340)
    plt.ylabel('Frequency')
    plt.ylim(0,95)
    plt.title('GRE')
    plt.show()

draw_hist(score_rangelist,frequency_list)

score_list = []
frequency_list = np.zeros((1,10))
for i in TOEFL:
    if i not in score_list:
        score_list.append(i)
n0 = 90
gap = 3
for i in score_list:
    if i != 120:
        frequency_list[0,(i-n0)//gap] += TOEFL.count(i)
    else:
        frequency_list[0,-1] += TOEFL.count(i)
score_rangelist = list(np.linspace(90,117,10))

# TOEFL
def draw_hist(score_list,frequency_list):
    #plt.subplot2grid((4,2),(0,1))
    fig1 = plt.subplot2grid((1,1),(0,0))
    rects = plt.bar(x=tuple(score_rangelist),height=tuple(frequency_list[0]),width=2.8,bottom=0,color=sns.cubehelix_palette(10, start=6, rot=0.3, dark=0.2, light=.8, reverse=True),align='edge')
    plt.xlabel('Score')
    plt.xlim(90,120)
    plt.ylabel('Frequency')
    plt.ylim(0,100)
    plt.title('TOEFL')
    plt.show()
draw_hist(score_rangelist,frequency_list)

score_list = []
frequency_list = np.zeros((1,10))
for i in GPA:
    if i not in score_list:
        score_list.append(i)
n0 = 6
gap = 0.4
for i in score_list:
    if i != 10:
        frequency_list[0,int((i-n0)//gap)] += GPA.count(i)
    else:
        frequency_list[0,-1] += GPA.count(i)
score_rangelist = list(np.linspace(6,9.6,10))

# CGPA
def draw_hist(score_list,frequency_list):
    #plt.subplot2grid((4,2),(1,0))
    fig1 = plt.figure(2)
    rects = plt.bar(x=tuple(score_rangelist),height=tuple(frequency_list[0]),width=0.38,bottom=0,color=sns.cubehelix_palette(10, start=2, rot=0.3, dark=0.2, light=.8, reverse=True),align='edge')
    plt.xlabel('Score')
    plt.xlim(6,10)
    plt.ylabel('Frequency')
    plt.ylim(0,140)
    plt.title('CGPA')
    plt.show()

draw_hist(score_rangelist,frequency_list)

score_list = []
frequency_list = np.zeros((1,10))
for i in LOR:
    if i not in score_list:
        score_list.append(i)
n0 = 1
gap = 0.4
for i in score_list:
    if i != 5:
        frequency_list[0,int((i-n0)//gap)] += LOR.count(i)
    else:
        frequency_list[0,-1] +=LOR.count(i)
score_rangelist = list(np.linspace(1,4.6,10))

# LOR
def draw_hist(score_list,frequency_list):
    #plt.subplot2grid((4,2),(1,1))
    fig1 = plt.figure(2)
    rects = plt.bar(x=tuple(score_rangelist),height=tuple(frequency_list[0]),width=0.38,bottom=0,color=sns.light_palette("red",10,reverse=True),align='edge')
    plt.xlabel('Score')
    plt.xlim(1,5)
    plt.ylabel('Frequency')
    plt.ylim(0,110)
    plt.title('LOR')
    plt.show()

draw_hist(score_rangelist,frequency_list)

score_list = []
frequency_list = np.zeros((1,10))
for i in SOP:
    if i not in score_list:
        score_list.append(i)
n0 = 1
gap = 0.4
for i in score_list:
    if i != 5:
        frequency_list[0,int((i-n0)//gap)] += SOP.count(i)
    else:
        frequency_list[0,-1] +=SOP.count(i)
score_rangelist = list(np.linspace(1,4.6,10))

# SOP
def draw_hist(score_list,frequency_list):
    #plt.subplot2grid((4,2),(2,0))
    fig1 = plt.figure(2)
    rects = plt.bar(x=tuple(score_rangelist),height=tuple(frequency_list[0]),width=0.38,bottom=0,color=sns.light_palette("yellow",10,reverse=True),align='edge')
    plt.xlabel('Score')
    plt.xlim(1,5)
    plt.ylabel('Frequency')
    plt.ylim(0,95)
    plt.title('SOP')
    plt.show()

draw_hist(score_rangelist,frequency_list)

score_list = []
frequency_list = np.zeros((1,10))
for i in Research:
    if i not in score_list:
        score_list.append(i)
n0 = 0
gap = 0.1
for i in score_list:
    if i != 1:
        frequency_list[0,int((i-n0)//gap)] += Research.count(i)
    else:
        frequency_list[0,-1] += Research.count(i)
score_rangelist = list(np.linspace(0,0.9,10))

# RESEARCH
def draw_hist(score_list,frequency_list):
    #plt.subplot2grid((4,2),(2,1))
    fig1 = plt.figure(2)
    rects = plt.bar(x=tuple(score_rangelist),height=tuple(frequency_list[0]),width=0.1,bottom=0,color=sns.color_palette("Greys_r",3),align='edge')
    plt.xlabel('Score')
    plt.xlim(0,1)
    plt.ylabel('Frequency')
    plt.ylim(0,300)
    plt.title('Research')
    plt.show()

draw_hist(score_rangelist,frequency_list)

score_list = []
frequency_list = np.zeros((1,10))
for i in UR:
    if i not in score_list:
        score_list.append(i)
n0 = 1
gap = 0.4
for i in score_list:
    if i != 5:
        frequency_list[0,int((i-n0)//gap)] += UR.count(i)
    else:
        frequency_list[0,-1] +=UR.count(i)
score_rangelist = list(np.linspace(1,4.6,10))

# UR
def draw_hist(score_list,frequency_list):
    #plt.subplot2grid((4,2),(3,0))
    fig1 = plt.figure(2)
    rects = plt.bar(x=tuple(score_rangelist),height=tuple(frequency_list[0]),width=0.4,bottom=0,color=sns.color_palette("Blues_r",10),align='edge')
    plt.xlabel('Score')
    plt.xlim(1,5)
    plt.ylabel('Frequency')
    plt.ylim(0,175)
    plt.title('University Rating')
    plt.show()

draw_hist(score_rangelist,frequency_list)

score_list = []
frequency_list = np.zeros((1,10))
for i in Label:
    if i not in score_list:
        score_list.append(i)
n0 = 0
gap = 0.1
for i in score_list:
    if i != 1:
        frequency_list[0,int((i-n0)//gap)] += Label.count(i)
    else:
        frequency_list[0,-1] += Label.count(i)
score_rangelist = list(np.linspace(0,0.9,10))

# CHANCE
def draw_hist(score_list,frequency_list):
    #plt.subplot2grid((4,2),(3,1))
    fig1 = plt.figure(2)
    rects = plt.bar(x=tuple(score_rangelist),height=tuple(frequency_list[0]),width=0.09,bottom=0,color=sns.color_palette("Oranges_r",10),align='edge')
    plt.xlabel('Score')
    plt.xlim(0,1)
    plt.ylabel('Frequency')
    plt.ylim(0,140)
    plt.title('Chance of Admit')
    plt.show()

draw_hist(score_rangelist,frequency_list)


# In[13]:


fig=plt.gcf()
fig.set_size_inches(10,10)
fig=sns.heatmap(addmission.corr(),annot=True,cmap="Blues")


# #### With a high CGPA, you are more likely be addmitted

# In[498]:


plt.figure(figsize=(8,6))
sns.scatterplot(x = addmission['CGPA'], y = addmission['Chance of Admit '],hue=addmission['Chance of Admit '], palette = "inferno_r")
#sns.pointplot(x = addmission['CGPA'], y = addmission['Chance of Admit '],alpha=1,ci=None,markers='',color='k')
plt.title('Chance of admission in CGPA wise', fontsize = 16)


# Students with high GPA usually have a high probability of addmission and have some research experience.
# 
# However, from the figure we can see that student whoes GPA in the range between 8.5 to 9.5 usually have some research experience, but their probability of addmission is lower than 85%. Some students with a high CGPA are more likely be addimited even if they have no research experience. Compared with research experience, CGPA is more important for graduation addmission.
# 
# Reasearch experience won't effect the chance of addmission a lot, just like the regression figure shows.

# In[133]:


plt.figure(figsize = (8,8))
sns.violinplot(x = addmission['Research'],y = addmission['CGPA'],hue=addmission['Admit'], data=addmission,split=True,palette = "Reds",grid = True)


# In[57]:


plt.figure(figsize=(8,6))
sns.scatterplot(x = addmission['CGPA'], y = addmission['Chance of Admit '],hue=addmission['Research'],palette = "Reds")


# In[135]:


plt.figure(figsize=(8,6))
sns.lmplot(data= addmission, x='CGPA',y='Chance of Admit ',hue = 'Research',palette = "Reds")
plt.title("Chance of Admit for CGPA")
plt.xlabel("CGPA")
plt.ylabel("Chance of Admit")
plt.show()


# #### correlation between features  (GRE & CGPA

# In[128]:


plt.figure(figsize=(8,6))
sns.scatterplot(y = addmission['CGPA'], x = addmission['GRE Score'],hue=addmission['Chance of Admit '])
plt.legend(loc='best')
plt.xlabel('GRE Score')
plt.ylabel('CGPA')
plt.title('CGPA for GRE')


# In[130]:


plt.figure(figsize=(12,8))
sns.lmplot(data= addmission, x='GRE Score',y='CGPA',hue = 'Admit',palette = "Blues")
plt.title("CGPA for GRE Score")
plt.xlabel("GRE Score")
plt.ylabel("CGPA")


# #### correlation between features (TOEFL & CGPA)

# In[54]:


plt.figure(figsize=(8,6))
sns.scatterplot(x = addmission['TOEFL Score'], y = addmission['CGPA'], hue=addmission['Chance of Admit '],palette = 'inferno_r')
plt.legend(loc='best')
plt.xlabel('TOEFL Score')
plt.ylabel('CGPA')
plt.title('CGPA for TOEFL Score')


# In[59]:


plt.figure(figsize=(8,8))
sns.jointplot( x = 'GRE Score', y='CGPA', data= addmission,kind="reg", color='r', height=6)


# In[179]:


plt.figure(figsize=(8,8))
sns.jointplot( x = 'TOEFL Score', y='CGPA', data= addmission,kind="reg", color='M', height=7)


# In[119]:


plt.figure(figsize=(8,6))
sns.lmplot(data= addmission, x='TOEFL Score',y='CGPA',hue = 'Admit',palette = "Blues")
plt.title("CGPA for TOEFL Score")
plt.xlabel("TOEFL Score")
plt.ylabel("CGPA")


# With figures shows above, students with high GRE&TOEFL score are more likely have a outstanding CGPA. 
# But, students who do not have such a outstanding CGPA can still do very well in GRE or TOEFL exam

# #### Obviously, students in a high rating university are typically have a high GPA 

# In[116]:


plt.figure(figsize=(8,6))
plt.scatter(addmission["University Rating"],addmission['CGPA'])
plt.title("CGPA Scores for University Ratings")
plt.xlabel("University Rating")
plt.ylabel("CGPA")
plt.show()


# In[194]:



plt.figure(figsize=(8,6))
sns.boxplot(addmission["University Rating"],y=addmission["Chance of Admit "])
plt.title("Chance of admit for University Ratings")

plt.figure(figsize=(8,6))
sns.boxplot(addmission["University Rating"],y=addmission["CGPA"])
plt.title("CGPA for University Ratings")

plt.figure(figsize=(8,6))
sns.boxplot(addmission["University Rating"],y=addmission["GRE Score"])
plt.title("GRE Score Scores for University Ratings")

plt.figure(figsize=(8,6))
sns.boxplot(addmission["University Rating"],y=addmission["TOEFL Score"])
plt.title("TOEFL Scores for University Ratings")

plt.figure(figsize=(8,6))
sns.boxplot(addmission["University Rating"],y=addmission["SOP"])
plt.title("SOP Scores for University Ratings")

plt.figure(figsize=(8,6))
sns.boxplot(addmission["University Rating"],y=addmission["LOR "])
plt.title("LOR Scores for University Ratings")

plt.show()


# In[48]:


plt.figure(figsize=(8,6))
sns.scatterplot(x = addmission['GRE Score'], y = addmission['Chance of Admit '],hue=addmission['Chance of Admit '], palette = "magma_r")
plt.title('Chance of admission in GRE wise', fontsize = 16)


# In[44]:


plt.figure(figsize=(8,8))
sns.jointplot( x = 'TOEFL Score', y='GRE Score', data= addmission,kind="reg", color='orange', height=7)


# In[17]:


plt.figure(figsize=(8,8))
sns.jointplot( x = 'CGPA', y='GRE Score', data= addmission,kind="reg", color='M', height=7)


# In[505]:


plt.figure(figsize=(8,8))
sns.jointplot( x= 'SOP', y='GRE Score', data= addmission,kind="reg", color='M', height=7)


# In[519]:


plt.figure(figsize=(8,8))
sns.jointplot( x= 'SOP', y='TOEFL Score', data= addmission,kind="reg", color ="orange", height=7)


# In[520]:


plt.figure(figsize=(8,8))
sns.jointplot( x= 'SOP', y='CGPA', data= addmission,kind="reg", color='orange', height=7)


# In[18]:


plt.figure(figsize=(8,6))
sns.lmplot(data= addmission, x='GRE Score',y='Chance of Admit ',hue = 'Research',palette = "Oranges")
plt.title("Chance of Admit for GRE")
plt.xlabel("GRE Score")
plt.ylabel("Chance of Admit")
plt.show()


# In[19]:


plt.figure(figsize = (8,8))
sns.violinplot(x = addmission['Research'],y = addmission['GRE Score'],hue=addmission['Admit'], data=addmission,split=True,palette = "Oranges",grid = True)


# In[545]:


plt.figure(figsize=(8,6))
sns.scatterplot(x = addmission['TOEFL Score'], y = addmission['Chance of Admit '],hue=addmission['Chance of Admit '],palette = 'magma_r')
#sns.pointplot(x = addmission['TOEFL Score'], y = addmission['Chance of Admit '],alpha=1,ci=None,markers='',color='g')
#
plt.title('Chance of admission in TOEFL wise', fontsize = 16)
plt.show()


# In[42]:


plt.figure(figsize=(8,8))
sns.jointplot( x = 'GRE Score', y='TOEFL Score', data= addmission,kind="reg", color='purple', height=7)


# In[41]:


plt.figure(figsize=(8,8))
sns.jointplot( x = 'CGPA', y='TOEFL Score', data= addmission,kind="reg", color='purple', height=7)


# In[31]:


plt.figure(figsize=(8,6))
sns.lmplot(data= addmission, x='TOEFL Score',y='Chance of Admit ',hue = 'Research',palette = "magma")
plt.title("Chance of Admit for TOEFL")
plt.xlabel("TOEFL Score")
plt.ylabel("Chance of Admit")
plt.show()


# In[32]:


plt.figure(figsize = (8,8))
sns.violinplot(x = addmission['Research'],y = addmission['TOEFL Score'],hue=addmission['Admit'], data=addmission,split=True,palette = "magma",grid = True)


# In[62]:


plt.figure(figsize=(8,6))
sns.scatterplot(x = addmission['LOR '], y = addmission['Chance of Admit '],hue=addmission['Chance of Admit '], palette = "magma_r")
plt.title('Chance of admission in LOR wise', fontsize = 16)


# In[63]:


plt.figure(figsize=(8,6))
sns.scatterplot(x = addmission['SOP'], y = addmission['Chance of Admit '],hue=addmission['Chance of Admit '], palette = "magma_r")
plt.title('Chance of admission in SOP wise', fontsize = 16)


# In[64]:


plt.figure(figsize=(8,6))
sns.scatterplot(x = addmission['University Rating'], y = addmission['Chance of Admit '],hue=addmission['Chance of Admit '], palette = "magma_r")
plt.title('Chance of admission in University Rating wise', fontsize = 16)


# In[65]:


plt.figure(figsize=(8,6))
sns.scatterplot(x = addmission['Research'], y = addmission['Chance of Admit '],hue=addmission['Chance of Admit '], palette = "magma_r")
plt.title('Chance of admission in Research wise', fontsize = 16)


# In[364]:



plt.figure(figsize=(12,8))
x = addmission[addmission['Chance of Admit ' ] > 0.5].mean()
y = addmission[addmission['Chance of Admit ' ] < 0.5].mean()
grades = ['GRE','TOEFL','University Rating','SOP','LOR','CGPA','Research']
print(x)
max_list = [340,120,5,5,5,10,1]
a = []
b = []
for i in range(len(x)-2):
    a.append(x[i]/max_list[i])
    b.append(y[i]/max_list[i])
a = np.array(a)
b = np.array(b)
plt.bar(grades, a, color = sns.color_palette('hot',1),edgecolor = sns.color_palette('hot',1),width = 0.5,label = 'Chance of Admit > 0.5')
plt.bar(grades, -b, color = sns.color_palette("rainbow",1),edgecolor = sns.color_palette('rainbow',1),width = 0.5,label = 'Chance of Admit < 0.5')
plt.title('Grades/Maximum with respect of Admit probability', fontsize = 16)
plt.legend(loc = 'upper right')
plt.show()


# In[227]:


addmission.head()


# In[346]:


x = addmission[addmission['Chance of Admit ' ] > 0.5].mean()
y = addmission[addmission['Chance of Admit ' ] < 0.5].mean()
grades = ['GRE','TOEFL','University Rating','SOP','LOR','CGPA','Research']
print(x)
max_list = [340,120,5,5,5,10,1]
a = []
b = []
for i in range(len(x)-2):
    a.append(x[i]/max_list[i])
    b.append(y[i]/max_list[i])
a = np.array(a)
b = np.array(b)
#grades = ['GRE','TOEFL','University Rating','SOP','LOR','CGPA','Research']
#print(x)
#max_list = [340,120,5,5,5,10,1]
#a = []
#b = []
#for i in range(len(x)-2):
#    a.append(x[i]/max_list[i])
#    b.append(y[i]/max_list[i])
#a = np.array(a)
#b = np.array(b)


# In[356]:


chance_degree = []
chance_list = [0.4,0.5,0.6,0.7,0.8,0.9,1]
for i in range(len(chance_list)):
    if i == 0:
        num = addmission[addmission['Chance of Admit ' ] <chance_list[0]].count()
        chance_degree.append(num[0])
    else:
        num1 = addmission[addmission['Chance of Admit ' ] <chance_list[i]].count()
        num2 = addmission[addmission['Chance of Admit ' ] <chance_list[i-1]].count()
        chance_degree.append(num1[0]-num2[0])
print(chance_degree)


# In[483]:


# Data to plot
chance_degree = []
chance_list = [0.4,0.5,0.6,0.7,0.8,0.9,1]
for i in range(len(chance_list)):
    if i == 0:
        num = addmission[addmission['Chance of Admit ' ] <chance_list[0]].count()
        chance_degree.append(num[0])
    else:
        num1 = addmission[addmission['Chance of Admit ' ] <chance_list[i]].count()
        num2 = addmission[addmission['Chance of Admit ' ] <chance_list[i-1]].count()
        chance_degree.append(num1[0]-num2[0])
labels = ['0.3~0.4','0.4~0.5','0.5~0.6','0.6~0.7','0.7~0.8','0.8~0.9','0.9~1']
sizes = chance_degree
#colors = ['red','orange','gold', 'yellowgreen', 'cyan','lightskyblue','violet']
colors=sns.color_palette("rainbow",7)
patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
plt.close()
#explode = (0.1, 0, 0, 0, 0, 0, 0)  # explode 1st slice
 
# Plot
f,ax=plt.subplots(1,2,figsize=(18,8))
#plt.bar(x=tuple(labels),height=tuple(sizes),width=0.09,bottom=0,color=sns.color_palette("Oranges_r",10),align='edge')
sns.barplot(x = labels, y = sizes, palette = "rainbow",edgecolor = sns.color_palette('rainbow',7),ax=ax[0])
wedges, texts, autotexts = plt.pie(sizes, colors=sns.color_palette("rainbow",7),autopct='%1.1f%%',shadow=False,wedgeprops={'linewidth': 0}) 
plt.setp(autotexts,size=16)
plt.legend(patches, labels, loc="upper left",title = 'Admit Chance')
plt.axis('equal')
plt.tight_layout()
ax[0].set_title('Number of students distribution with respect to chance of admit',fontsize = 16)
ax[1].set_title('Number of students distribution with respect to chance of admit',fontsize = 16)
ax[0].set_ylabel('Student Count',fontsize = 16)
ax[0].set_xlabel('Chance of Admit',fontsize = 16)
plt.show()


# In[539]:


do_research = addmission[addmission['Research'] == 1].count()
num1 = do_research[0]
no_research = addmission[addmission['Research'] == 0].count()
num2 = no_research[0]

patches, texts = plt.pie(sizes,shadow=True, startangle=90)
plt.close()
#explode = (0.1, 0, 0, 0, 0, 0, 0)  # explode 1st slice
labels = ['do research','no research'] 
sizes = [num1,num2]
# Plot
f,ax=plt.subplots(1,2,figsize=(18,8))
#plt.bar(x=tuple(labels),height=tuple(sizes),width=0.09,bottom=0,color=sns.color_palette("Oranges_r",10),align='edge')
sns.barplot(x = labels, y = sizes,ax=ax[0])
wedges, texts, autotexts = plt.pie(sizes,autopct='%1.1f%%',shadow=False,wedgeprops={'linewidth': 0}) 
plt.setp(autotexts,size=20)
plt.legend(patches, labels, loc="upper left",title = 'Admit Chance')
plt.axis('equal')
plt.tight_layout()
ax[0].set_title('Number of students distribution with respect to chance of admit',fontsize = 16)
ax[1].set_title('Number of students distribution with respect to chance of admit',fontsize = 16)
ax[0].set_ylabel('Student Count',fontsize = 16)
ax[0].set_xlabel('Chance of Admit',fontsize = 16)
plt.show()


# In[15]:


admt_sort=addmission.sort_values(by=addmission.columns[-1],ascending=False)
m = admt_sort[admt_sort['Chance of Admit '] > 0.5].mean().reset_index()
m.rename(columns = {'index':'Grades',0:'Score'},inplace = True)
n = admt_sort[admt_sort['Chance of Admit '] < 0.6].mean().reset_index()
n.rename(columns = {'index':'Grades',0:'Score'},inplace = True)
q = admt_sort[admt_sort['Chance of Admit '] > 0.96].mean().reset_index()
q.rename(columns = {'index':'Grades',0:'Score'},inplace = True)
m


# In[16]:


n


# In[17]:


q


# In[581]:


GPAS=[]
for i in GPA:
    GPAS.append(round(i*10)/10)
plt.figure(figsize=(12,8))
sns.pointplot(TOEFL,Label,alpha=1,ci=None,markers='',color='y')
plt.ylabel('chance', fontsize=15)
plt.xlabel('TOEFL', fontsize=15)
plt.xticks(rotation='horizontal')
sns.set_style('darkgrid')
plt.title('TOEFL for Chance of admit',fontsize=20)
plt.show()

plt.figure(figsize=(12,8))
sns.pointplot(GPAS,Label,alpha=1,ci=None,markers='',color='k')
plt.ylabel('chance', fontsize=15)
plt.xlabel('CGPA', fontsize=15)
plt.xticks(rotation='horizontal')
sns.set_style('darkgrid')
plt.title('CGPA for Chance of admit',fontsize=20)
plt.show()

plt.figure(figsize=(18,13))
sns.pointplot(GRE,Label,alpha=1,ci=None,markers='',color='r')
plt.ylabel('chance', fontsize=20)
plt.xlabel('GRE', fontsize=20)
plt.xticks(rotation='horizontal')
sns.set_style('darkgrid')
plt.title('GRE for Chance of admit',fontsize=30)
plt.show()

plt.figure(figsize=(12,6))
sns.pointplot(LOR,Label,alpha=1,ci=None,markers='',color='b',label = 'LOR')
plt.ylabel('chance', fontsize=15)
plt.xlabel('LOR', fontsize=15)
plt.xticks(rotation='horizontal')
sns.set_style('darkgrid')
plt.title('LOR for Chance of admit',fontsize=20)
plt.show()
plt.figure(figsize=(12,6))
sns.pointplot(SOP,Label,alpha=1,ci=None,markers='',color='g',label = 'SOP')
plt.ylabel('chance', fontsize=15)
plt.xlabel('SOP', fontsize=15)
plt.xticks(rotation='horizontal')
sns.set_style('darkgrid')
plt.title('SOP for Chance of admit',fontsize=20)
#plt.show()
plt.figure(figsize=(12,6))
sns.pointplot(UR,Label,alpha=1,ci=None,markers='',color='r')
plt.ylabel('chance', fontsize=15)
plt.xlabel('UR', fontsize=15)
plt.xticks(rotation='horizontal')
sns.set_style('darkgrid')
plt.title('Universities rating for Chance of admit',fontsize=20)
plt.show()
plt.figure(figsize=(12,6))
sns.pointplot(Research,Label,alpha=1,ci=None,markers='',color = 'orange')
plt.ylabel('chance', fontsize=15)
plt.xlabel('Research', fontsize=15)
plt.xticks(rotation='horizontal')
sns.set_style('darkgrid')
plt.title('Research for Chance of admit',fontsize=20)
plt.show()


# In[14]:


from sklearn.ensemble import RandomForestRegressor
import numpy as np
from numpy.random import normal
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.pylab import subplots
import pandas as pd
import sys
import os
import seaborn as sns
from sklearn.model_selection import train_test_split 
admission_csv = 'Admission_Predict_Ver1.1.csv'
admission = pd.read_csv(admission_csv)
admission = admission.drop('Serial No.', axis =1, inplace = False)
rf_model = RandomForestRegressor(n_estimators = 1000,random_state = 123)
X = admission.drop('Chance of Admit ',axis = 1)
y = admission['Chance of Admit ']
X_train,X_val,y_train,y_val = train_test_split(X,y,test_size = .25,random_state = 123)
rf_model = RandomForestRegressor(n_estimators = 1000,random_state = 123)
rf_model.fit(X_train,y_train)
feature_importance = pd.DataFrame(sorted(zip(rf_model.feature_importances_, X.columns)), columns=['Value','Feature'])
sns.set(style="darkgrid")
plt.figure(figsize=(15, 7))
sns.barplot(x="Value", y="Feature", data=feature_importance.sort_values(by="Value", ascending=False))
plt.xlabel('Importance Value',fontsize=20)
plt.ylabel('Grade type',fontsize=20)
plt.title('All Grades Importance',fontsize=20)
plt.ioff()
#plt.tight_layout()


# In[ ]:




