<<<<<<< HEAD
--validate do we have data for a particular customer
select top(10)
		t2.[Plant_Number] 
=======
--for recently off hired email
--to have an email some data must be present in this query results
--if its empty some data must be updated through UPDATE statement above
--RECENT
select	t2.[Plant_Number] 
>>>>>>> 01d1d21f785263c20a4aaadc39828b65e70d352e
		,t2.[Ordered_Quantity] 
		,t2.[Item_Description]  
		,t1.[hire_no]						/*hire schedule*/
		,t1.[OrderedBy_PersonName]  
		,t1.[Customer_PoNo]			 
		,t2.Offhire_Date			 
		,t2.[OffHire_Reference]
		,t3.[MasterAccount_Name]			/*for MA grouping/filtering*/
		,t4.[SiteAccount_Name]				/*for SA groupin/filtering*/
<<<<<<< HEAD
		,t2.OrderLine_Id				    /*for debugging and further updates*/
		,t1.MasterAccount_Id				/*for debugging and further updates*/
	FROM [CPDB].[dbo].[Orders] as t1
		left join [CPDB].[dbo].[OrderLines] as t2 on (t1.[Order_Id] = t2.[Order_Id])
		left join [CPDB].[dbo].[MasterAccounts] t3  on (t1.[MasterAccount_id] = t3.[MasterAccount_id])
		left join [CPDB].[dbo].[SiteAccounts] t4  on (t1.[SiteAccount_id] = t4.[SiteAccount_id])
=======
		,t2.OrderLine_Id				    /*for debugging*/
		,t1.MasterAccount_Id
	FROM [CPDB72].[dbo].[Orders] as t1
		left join [CPDB72].[dbo].[OrderLines] as t2 on (t1.[Order_Id] = t2.[Order_Id])
		left join [CPDB72].[dbo].[MasterAccounts] t3  on (t1.[MasterAccount_id] = t3.[MasterAccount_id])
		left join [CPDB72].[dbo].[SiteAccounts] t4  on (t1.[SiteAccount_id] = t4.[SiteAccount_id])
>>>>>>> 01d1d21f785263c20a4aaadc39828b65e70d352e
	WHERE
		1=1
		and Offhire_date > (GETDATE()-7)
		and Offhire_Date < (GETDATE())
<<<<<<< HEAD
		and MasterAccount_Name like '%ACCIONA%'
order by 8 desc

--current date Australia
=======
		and MasterAccount_Name = 'MICHILIS PTY LTD'
		and ([Plant_Number] not in ('DAMAGE', 'FUEL') or [Plant_Number] is null)
order by 8 desc
--NEARING
select	t2.[Plant_Number] 
		,t2.[Ordered_Quantity] 
		,t2.[Item_Description]  
		,t1.[hire_no]						/*hire schedule*/
		,t1.[OrderedBy_PersonName]  
		,t1.[Customer_PoNo]			 
		,t2.Offhire_Date
		,t2.ExpectedOffhire_Date			 
		,t2.[OffHire_Reference]
		,t3.[MasterAccount_Name]			/*for MA grouping/filtering*/
		,t4.[SiteAccount_Name]				/*for SA groupin/filtering*/
		,t2.OrderLine_Id				    /*for debugging*/
		,t1.MasterAccount_Id
	FROM [CPDB72].[dbo].[Orders] as t1
		left join [CPDB72].[dbo].[OrderLines] as t2 on (t1.[Order_Id] = t2.[Order_Id])
		left join [CPDB72].[dbo].[MasterAccounts] t3  on (t1.[MasterAccount_id] = t3.[MasterAccount_id])
		left join [CPDB72].[dbo].[SiteAccounts] t4  on (t1.[SiteAccount_id] = t4.[SiteAccount_id])
	WHERE
		1=1
		and expectedOffhire_date >= DATEADD(wk, DATEDIFF(wk,0,GETDATE()), 0)
		and expectedOffhire_date < DATEADD(wk, DATEDIFF(wk,0,GETDATE()), 0)+8
		and MasterAccount_Name = 'MICHILIS PTY LTD'
		and Offhire_Date is null
		and OffHire_Reference is null
		and ([Plant_Number] not in ('DAMAGE', 'FUEL') or [Plant_Number] is null)
order by 8 desc

--current date, Monday of current week, end date for nearing for debugging
>>>>>>> 01d1d21f785263c20a4aaadc39828b65e70d352e
select (GETDATE())
SELECT DATEADD(wk, DATEDIFF(wk,0,GETDATE()), 0)
SELECT DATEADD(wk, DATEDIFF(wk,0,GETDATE()), 0)+8

<<<<<<< HEAD
--getting particular row for the further update (if needed)
select * 
	from [CPDB].[dbo].[OrderLines]
	where 1=1
	--and plant_number = '9110104'
	--and OrderLine_Id = '143726851'
	and [Order_Id] in (select [Order_Id] from [CPDB].[dbo].[Orders] where MasterAccount_id = '218786')
	and OffHire_date = '2018-02-20'
	and OffHire_Reference is null;
;
=======

--update of top 30 rows of data to have those in email on on frontend side
/*
RECENT:
update top (30) [CPDB72].[dbo].[OrderLines]
	set offhire_date = '2018-03-19'
	where [Order_Id] in (select [Order_Id] from [CPDB72].[dbo].[Orders] where MasterAccount_id = '218786') and [OrderLines].[OffHire_Reference] is not null;
>>>>>>> 01d1d21f785263c20a4aaadc39828b65e70d352e

NEARING:
update top (10) [CPDB72].[dbo].[OrderLines]
	set expectedOffhire_date = '2018-03-23'
	where [Order_Id] in (select [Order_Id] from [CPDB72].[dbo].[Orders] where MasterAccount_id = '218786') and [OrderLines].[OffHire_Reference] is null;

<<<<<<< HEAD
/*
update top (50) [CPDB].[dbo].[OrderLines]		--<<<<<<<<<updating 50 rows of data
	set offhire_date = '2018-03-01'   			--<<<<<<<<<set the correct data here
=======
select * from [CPDB72].[dbo].[OrderLines]
=======
update top (2) [CPDB].[dbo].[OrderLines]
	set offhire_date = '2018-03-01'
>>>>>>> 01d1d21f785263c20a4aaadc39828b65e70d352e
	where [Order_Id] in (select [Order_Id] from [CPDB].[dbo].[Orders] where MasterAccount_id = '218786') and OffHire_Reference is not null;
delete [CPDB].[dbo].[OrderLines] where [Order_Id] in (select [Order_Id] from [CPDB].[dbo].[Orders] where MasterAccount_id = '218786') 
		and OffHire_Reference is not null and OrderLine_id in ('139484360', '139484407')
*/

