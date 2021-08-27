
"""
Spyder Editor

This is a temporary script file.
"""

import os
import csv
filename = []
filedname = []
wrongidnum = []
wrongbirth =[]
wrongcentre = []
wrongidenty = []
wrongvcat = []


class chk:
#初始化
	def __init__(self):
	   pass
#grab filename in dir , and check filenames include .csv or not
	def csvname(self): 
		a = os.listdir()
		for j in a:
			if os.path.splitext(j)[1]  == '.csv':
				filename.append(j)
	def runchk(self,fname):
		#try:
		with open(fname, newline='',encoding = 'ANSI',
                 errors='ignore') as csvfile:
			#load csv file
			rows = csv.DictReader(csvfile)
			print(fname+'已讀入')
			for row in rows:
				if row['性別'] !='性別' and ord(row['身分證號'][0]) != 26:
					self.chkidnum(row)
					self.chkbirth(row)
					self.chkcentre(row)
					self.chkidenty(row)
					self.chkvcat(row)
		#except:
			#print('讀取'+fname+'錯誤，請確認該csv是否不合格式')
	def chkidnum(self,row):
		#身分證檢查長度與字首檢查
		F = ord(row['身分證號'][0]) - 55
		if row['身分證號'] ==None:
			print('身分證為空')
			wrongidnum.append(row)
			return
		if len(row['身分證號'])>10 :
			print(row['身分證號']+'該身分證超過10個字')
			wrongidnum.append(row)
		elif F > 35 or F < 10 :
			print(row['身分證號']+'第一個字不是大寫英文')
			wrongidnum.append(row)
		#將第一個英文字處理成數字()
		else:
			if row['身分證號'][0] == 'A':
				F = 10
			elif row['身分證號'][0] == 'B':
				F = 11
			elif row['身分證號'][0] == 'C':
				F = 12
			elif row['身分證號'][0] == 'D':
				F = 13
			elif row['身分證號'][0] == 'E':
				F = 14
			elif row['身分證號'][0] == 'F':
				F = 15
			elif row['身分證號'][0] == 'G':
				F = 16
			elif row['身分證號'][0] == 'H':
				F = 17
			elif row['身分證號'][0] == 'I':
				F = 34
			elif row['身分證號'][0] == 'J':
				F = 18
			elif row['身分證號'][0] == 'K':
				F = 19
			elif row['身分證號'][0] == 'L':
				F = 20
			elif row['身分證號'][0] == 'M':
				F = 21
			elif row['身分證號'][0] == 'N':
				F = 22
			elif row['身分證號'][0] == 'O':
				F = 35
			elif row['身分證號'][0] == 'P':
				F = 23
			elif row['身分證號'][0] == 'Q':
				F = 24
			elif row['身分證號'][0] == 'R':
				F = 25
			elif row['身分證號'][0] == 'S':
				F = 26
			elif row['身分證號'][0] == 'T':
				F = 27
			elif row['身分證號'][0] == 'U':
				F = 28
			elif row['身分證號'][0] == 'V':
				F = 29
			elif row['身分證號'][0] == 'X':
				F = 30
			elif row['身分證號'][0] == 'Y':
				F = 31
			else :
				F = 32
			#將第二個英文字處理成數字()
			if row['身分證號'][1] == 'A':
				S = 10
			elif row['身分證號'][1] == 'B':
				S = 11
			elif row['身分證號'][1] == 'C':
				S = 12
			elif row['身分證號'][1] == 'D':
				S = 13
			elif row['身分證號'][1] == 'E':
				S = 14
			elif row['身分證號'][1] == 'F':
				S = 15
			elif row['身分證號'][1] == 'G':
				S = 16
			elif row['身分證號'][1] == 'H':
				S = 17
			elif row['身分證號'][1] == 'I':
				S = 34
			elif row['身分證號'][1] == 'J':
				S = 18
			elif row['身分證號'][1] == 'K':
				S = 19
			elif row['身分證號'][1] == 'L':
				S = 20
			elif row['身分證號'][1] == 'M':
				S = 21
			elif row['身分證號'][1] == 'N':
				S = 22
			elif row['身分證號'][1] == 'O':
				S = 35
			elif row['身分證號'][1] == 'P':
				S = 23
			elif row['身分證號'][1] == 'Q':
				S = 24
			elif row['身分證號'][1] == 'R':
				S = 25
			elif row['身分證號'][1] == 'S':
				S = 26
			elif row['身分證號'][1] == 'T':
				S = 27
			elif row['身分證號'][1] == 'U':
				S = 28
			elif row['身分證號'][1] == 'V':
				S = 29
			elif row['身分證號'][1] == 'X':
				S = 30
			elif row['身分證號'][1] == 'Y':
				S = 31
			elif row['身分證號'][1] == 'Z':
				S = 32
			else :
				S = int(row['身分證號'][1])
	
			#開始驗證
			try:
				Total = (F)//10+(F%10)*9+S*8+int(row['身分證號'][2])*7+int(row['身分證號'][3])*6+int(row['身分證號'][4])*5+int(row['身分證號'][5])*4+int(row['身分證號'][6])*3+int(row['身分證號'][7])*2+int(row['身分證號'][8])*1+int(row['身分證號'][9])*1
				if Total % 10 != 0 :
					wrongidnum.append(row)
					print('身分證:'+row['身分證號']+'身分證驗證不合法')
			except:
				print('身分證:'+row['身分證號']+'身分證驗證不合法')
				wrongidnum.append(row)
	def chkbirth(self,row):
	#找出不合法的生日
		if (row['出生日期']) == None:
			print('身分證: '+row['身分證號']+','+' 生日日期為空')
			wrongbirth.append(row)
		elif len(row['出生日期']) < 7 :
			print('身分證: '+row['身分證號']+','+row['出生日期']+' 生日日期長度錯誤')
			wrongbirth.append(row)
		elif int(row['出生日期'])>1100101 :
			print('身分證: '+row['身分證號']+','+row['出生日期']+' 生日日期錯誤')
			wrongbirth.append(row)
	def chkcentre(self,row):
	#找出不合法的接種機構
		if (row['接種機構']) == None:
			print('身分證: '+row['身分證號']+','+'接踵機構為空')
			wrongcentre.append(row)
		elif len(row['接種機構'])<10:
			print('身分證:'+row['身分證號']+','+row['接種機構']+'接種機構錯誤')
			wrongcentre.append(row)
	def chkidenty(self,row):
	#找出不合法的身分別
		if row['身分別']== None:
			print('身分證:'+row['身分證號']+','+'身分別為空')
			wrongidenty.append(row)
	def chkvcat(self,row):
	#找出不合法的疫苗種類
		if (row['疫苗種類']) == None:
			print('身分證: '+row['身分證號']+','+'疫苗種類為空')
			wrongcentre.append(row)
		elif row['疫苗種類'] !='CoV_MediGen' and row['疫苗種類'] !='CoV_AZ' and row['疫苗種類'] !='CoV_Moderna' : 
			print('身分證:'+row['身分證號']+','+row['疫苗種類']+'疫苗種類錯誤')
			wrongvcat.append(row)

chec = chk()
if __name__ == '__main__':
	print('本程式對應ANSI版本，資料夾內的csv文件必須要為ANSI編碼')
	chec.csvname()
	for fname in filename:
		chec.runchk(fname)
		with open('錯誤列表'+'_'+fname,'w',encoding = 'ANSI',
                 errors='ignore') as output:
			headers =['身分證號','姓名','性別','出生日期','同胎次序','通訊地址','電話','父或母身分證號','接種機構','接種日期','疫苗種類','劑次','疫苗批號','疫苗廠商','疫苗型別','曾接種流感','身分別','接種站識別碼','期別','時段','醫師','接種位址','接種站名稱']
			writer = csv.DictWriter(output,fieldnames=headers)
			writer.writeheader()
			writer.writerow({'身分證號':'身分證錯誤'})
			for data in wrongidnum:
				writer.writerow(data)
			writer.writerow({'身分證號':'出生日期錯誤'})
			for data in wrongbirth:
				writer.writerow(data)
			writer.writerow({'身分證號':'接種機構錯誤'})
			for data in wrongcentre:
				writer.writerow(data)
			writer.writerow({'身分證號':'身分別空白'})
			for data in wrongidenty:
				writer.writerow(data)
			writer.writerow({'身分證號':'疫苗種類錯誤'})
			for data in wrongvcat:
				writer.writerow(data)
		wrongidnum.clear()
		wrongbirth.clear()
		wrongcentre.clear()
		wrongidenty.clear()
		wrongvcat.clear()
os.system("pause")