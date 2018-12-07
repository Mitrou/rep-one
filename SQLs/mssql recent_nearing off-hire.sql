--for recently off hired email
--to have an email some data must be present in this query results
--if its empty some data must be updated through UPDATE statement below
--customer MICHILIS PTY LTD
--RECENT
select	t2.[Plant_Number] 
		,t2.[Ordered_Quantity] 
		,t2.[Item_Description]  
		,t1.[hire_no]						/*hire schedule*/
		,t1.[OrderedBy_PersonName]  
		,t1.[Customer_PoNo]			 
		,t2.Offhire_Date			 
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
		and Offhire_date > (GETDATE()-7)
		and Offhire_Date < (GETDATE())
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
		--monday>>sunday implenetation
		--and expectedOffhire_date >= DATEADD(wk, DATEDIFF(wk,0,GETDATE()), 0)
		--and expectedOffhire_date < DATEADD(wk, DATEDIFF(wk,0,GETDATE()), 0)+8
		--on demand run implementation
		and expectedOffhire_date >= (GETDATE())
		and expectedOffhire_date <= (GETDATE()+7)
		and MasterAccount_Name = 'MICHILIS PTY LTD'
		and Offhire_Date is null
		and OffHire_Reference is null
		--and ([Plant_Number] not in ('DAMAGE', 'FUEL') or [Plant_Number] is null)
order by 8 desc

--current date, Monday of current week, end date for nearing for debugging
select (GETDATE())
select (GETDATE()+7)
SELECT DATEADD(wk, DATEDIFF(wk,0,GETDATE()), 0)
SELECT DATEADD(wk, DATEDIFF(wk,0,GETDATE()), 0)+8


--update of top 30 rows of data to have those in email on on frontend side
/*
RECENT:
update top (30) [CPDB72].[dbo].[OrderLines]
	set offhire_date = '2018-04-01'
	where [Order_Id] in (select [Order_Id] from [CPDB72].[dbo].[Orders] where MasterAccount_id = '218786') and [OrderLines].[OffHire_Reference] is not null;

NEARING:
update top (2) [CPDB72].[dbo].[OrderLines]
	set expectedOffhire_date = '2018-04-03'
	where [Order_Id] in (select [Order_Id] from [CPDB72].[dbo].[Orders] where MasterAccount_id = '218786') and [OrderLines].[OffHire_Reference] is null;

*/

