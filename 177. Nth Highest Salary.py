# Time complexity = O(n)
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    result = []
    for i in range(len(employee)):
        salary = employee['salary'][i]
        if salary not in result:
            result.append(salary)
    result.sort(reverse=True)
    if N > len(result) or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})' : [None]})
    return pd.DataFrame({f'getNthHighestSalary({N})' : [result[N-1]]})

#Using set DS Time complexity- O(1)
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    resultSet = set()
    for i in range(len(employee)):
        salary = employee['salary'][i]
        resultSet.add(salary)
    result = []
    for element in resultSet:
        result.append(element)
    result.sort(reverse=True)
    if N > len(result) or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})' : [None]})
    return pd.DataFrame({f'getNthHighestSalary({N})' : [result[N-1]]})
 
#Using pandas
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee[['salary']].drop_duplicates()
    if N > len(df) or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})' : [None]})
    df = df.sort_values(by='salary',ascending=False,inplace=False)
    return df.head(N).tail(1)[['salary']].rename(columns={'salary':f'getNthHighestSalary({N})'})

	
