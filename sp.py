import pandas as pd
import statistics
import csv
df = pd.read_csv("StudentsPerfomance.csv")
math score_list = df["math score"].to_list()
reeding score_list = df["reeding score"].to_list()
writting score_list = df["writing score"].to_list
#Mean for math score and reedingscore
math score_mean = statistics.mean(math score_list)
reeding score_mean = statistics.mean(reeding score_list)
writting score_mean=statistics.mean(writting score_list)
#Median for math score and reedingscore
math score_median = statistics.median(math score_list)
reedingscore_median = statistics.median(reedingscore_list)
writting score_mean=statistics.median(writting score_list)
#Mode for math score and reedingscore
math score_mode = statistics.mode(math score_list)
reedingscore_mode = statistics.mode(reedingscore_list)
writting score_mean=statistics.mode(writting score_list)
#Printing mean, median and mode to validate
print("Mean, Median and Mode of math score is {}, {} and {} respectively".format(math score_mean, math score_median, math score_mode))
print("Mean, Median and Mode of reedingscore is {}, {} and {} respectively".format(reedingscore_mean, reedingscore_median, reedingscore_mode))
print("Mean, Median and Mode of reedingscore is {}, {} and {} respectively".format(writting score_mean, writtingscore_median, writingscore_mode))

#Standard deviation for math score and reedingscore
math score_std_deviation = statistics.stdev(math score_list)
reeding score_std_deviation = statistics.stdev(reedingscore_list)
writting score_std_deviation = statistics.stdev(writting score_list)
#1, 2 and 3 Standard Deviations for math score
math score_first_std_deviation_start, math score_first_std_deviation_end = math score_mean-math score_std_deviation, math score_mean+math score_std_deviation
math score_second_std_deviation_start, math score_second_std_deviation_end = math score_mean-(2*math score_std_deviation), math score_mean+(2*math score_std_deviation)
math score_third_std_deviation_start, math score_third_std_deviation_end = math score_mean-(3*math score_std_deviation), math score_mean+(3*math score_std_deviation)
#1, 2 and 3 Standard Deviations for reedingscore
reedingscore_first_std_deviation_start, reedingscore_first_std_deviation_end = reedingscore_mean-reedingscore_std_deviation, reedingscore_mean+reedingscore_std_deviation
reedingscore_second_std_deviation_start, reedingscore_second_std_deviation_end = reedingscore_mean-(2*reedingscore_std_deviation), reedingscore_mean+(2*reedingscore_std_deviation)
reedingscore_third_std_deviation_start, reedingscore_third_std_deviation_end = reedingscore_mean-(3*reedingscore_std_deviation), reedingscore_mean+(3*reedingscore_std_deviation)
#Percentage of data within 1, 2 and 3 Standard Deviations for math score
math score_list_of_data_within_1_std_deviation = [result for result in math score_list if result > math score_first_std_deviation_start and result < math score_first_std_deviation_end]
math score_list_of_data_within_2_std_deviation = [result for result in math score_list if result > math score_second_std_deviation_start and result < math score_second_std_deviation_end]
math score_list_of_data_within_3_std_deviation = [result for result in math score_list if result > math score_third_std_deviation_start and result < math score_third_std_deviation_end]
#Percentage of data within 1, 2 and 3 Standard Deviations for reedingscore
reedingscore_list_of_data_within_1_std_deviation = [result for result in reedingscore_list if result > reedingscore_first_std_deviation_start and result < reedingscore_first_std_deviation_end]
reedingscore_list_of_data_within_2_std_deviation = [result for result in reedingscore_list if result > reedingscore_second_std_deviation_start and result < reedingscore_second_std_deviation_end]
reedingscore_list_of_data_within_3_std_deviation = [result for result in reedingscore_list if result > reedingscore_third_std_deviation_start and result < reedingscore_third_std_deviation_end]
#Percentage of data within 1, 2 and 3 Standard Deviations for writting score
writting score_list_of_data_within_1_std_deviation = [result for result in writting score_list if result >  writting score_first_std_deviation_start and result < writting score_first_std_deviation_end]
writting score_list_of_data_within_2_std_deviation = [result for result in writting score_list if result > writting  score_second_std_deviation_start and result < writting  score_second_std_deviation_end]
writting score_list_of_data_within_3_std_deviation = [result for result in writting score_list if result > writting  score_third_std_deviation_start and result < math score_third_std_deviation_end]
#Printing data for math score and reedingscore (Standard Deviation)
print("{}% of data for math score lies within 1 standard deviation".format(len(math score_list_of_data_within_1_std_deviation)*100.0/len(math score_list)))
print("{}% of data for math score lies within 2 standard deviations".format(len(math score_list_of_data_within_2_std_deviation)*100.0/len(math score_list)))
print("{}% of data for math score lies within 3 standard deviations".format(len(math score_list_of_data_within_3_std_deviation)*100.0/len(math score_list)))
print("{}% of data for reedingscore lies within 1 standard deviation".format(len(reedingscore_list_of_data_within_1_std_deviation)*100.0/len(reedingscore_list)))
print("{}% of data for reedingscore lies within 2 standard deviations".format(len(reedingscore_list_of_data_within_2_std_deviation)*100.0/len(reedingscore_list)))
print("{}% of data for reedingscore lies within 3 standard deviations".format(len(reedingscore_list_of_data_within_3_std_deviation)*100.0/len(reedingscore_list)))
print("{}% of data for math score lies within 1 standard deviation".format(len(writting score_list_of_data_within_1_std_deviation)*100.0/len(writting score_list)))
print("{}% of data for math score lies within 2 standard deviations".format(len(writting score_list_of_data_within_2_std_deviation)*100.0/len(writting score_list)))
print("{}% of data for math score lies within 3 standard deviations".format(len(writting score_list_of_data_within_3_std_deviation)*100.0/len(writting score_list)))