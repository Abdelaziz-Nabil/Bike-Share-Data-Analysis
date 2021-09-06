import time
import pandas as pd
import numpy as np
filter_date = ['Month', 'Day', 'Both', 'None']
months = ['January', 'February', 'March', 'April', 'May', 'June','All']
CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }


#get_filters
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    
    
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input('\nWould you like to see data from "Chicago", "New York", or "Washington"?\n')
        city=(city.strip()).title()
        if city in CITY_DATA.keys():
            break
    month, day="All",0
    
    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        ask_filter_date=input('Would you like to filter the data by "month", "day", "both", or not at all? Type "none" for no time filter. ')
        ask_filter_date=(ask_filter_date.strip()).title()
        if ask_filter_date in filter_date:
            if (ask_filter_date=='Month'):
                while True:
                    month=input('Which month? "all","January", "February", "March", "April", "May" or "June"?\n')
                    month=(month.strip()).title()
                    if month in months:
                        break
                    else:
                        print("error in month name, please try again")
            elif(ask_filter_date=='Day'):
                while True:
                    day=input('Which day? please type your response as an integer [0:7] .(e.g.. 0=all, 1=Sunday.. 7=Saturday).\n')
                    day=int(day.strip())
                    if (day <8) and(day >=0):
                        break
                    else:
                        print("error in day number, please try again")
            elif(ask_filter_date=='Both'):
                while True:
                    month=input('Which month? "all","January", "February", "March", "April", "May" or "June"?\n')
                    month=(month.strip()).title()
                    if month in months:
                        break
                    else:
                        print("error in month name, please try again")
                        
                while True:
                    day=input('Which day? please type your response as an integer [0:7] .(e.g.. 0=all, 1=Sunday.. 7=Saturday).\n')
                    day=int(day.strip())
                    if (day <8) and(day >=0):
                        break
                    else:
                        print("error in day number, please try again")
            break
        else:
            print("error in filter name, please try again")

    print('-'*40)
    return city, month, day


#load_data
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] =pd.to_datetime(df['End Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].apply(lambda time:time.month)
    df['month name'] = df['Start Time'].dt.month_name()
    df['day name'] = df['Start Time'].dt.day_name()
    df['Start hour'] = df['Start Time'].apply(lambda time:time.hour)
    # filter by month if applicable
    if month != 'All':
        # filter by month to create the new dataframe
        df = df[df['month name']==month.title()]

    # filter by day of week if applicable
    if day != 0:
        day=day-1
        days=('sunday','monday','tuesday','wednesday','thursday','friday','saturday')
        # filter by day of week to create the new dataframe
        df = df[df['day name']==days[day].title()]
    
    return df


#time_stats
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month_name=df['month name'].mode()[0]
    common_month_name_count=(df['month name'].value_counts())[common_month_name]
    common_month_number=df['month'].mode()[0]
    
    print("the most common month is {} ({}) Count: {}\n".format(common_month_name,common_month_number,common_month_name_count))
    
    # TO DO: display the most common day of week
    common_day=df['day name'].mode()[0]
    common_day_count=(df['day name'].value_counts())[common_day]
    
    print("the most common day of week is {} Count: {}\n".format(common_day,common_day_count))
    
    # TO DO: display the most common start hour
    common_hour=df['Start hour'].mode()[0]
    common_hour_count=(df['Start hour'].value_counts())[common_hour]
    
    print("the most common start hour is {} Count: {}\n".format(common_hour,common_hour_count))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


    
#station_stats
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    common_start=df['Start Station'].mode()[0]
    common_start_count=(df['Start Station'].value_counts())[common_start]
    
    print("most commonly used Start station is {} Count: {}\n".format(common_start,common_start_count))
    
    # TO DO: display most commonly used end station
    common_end=df['End Station'].mode()[0]
    common_end_count=(df['End Station'].value_counts())[common_end]
    
    print("most commonly used End station is {} Count: {}\n".format(common_end,common_end_count))
    
    # TO DO: display most frequent combination of start station and end station trip
    common_station=(df['Start Station']+'" to "'+df['End Station']).mode()[0]
    common_station_count=(((df['Start Station']+'" to "'+df['End Station'])).value_counts())[common_station]
    
    print('most frequent combination of start station and end station trip is \nfrom "{}" Count: {}\n'.format(common_station,common_station_count))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    

#trip_duration_stats
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=((df['End Time'] -df['Start Time'] ).sum()).total_seconds()
    count=(df['End Time'].value_counts()).sum()
    
    print("total travel time is",total_travel_time,"seconds","Count: ",count,'\n')
    # TO DO: display mean travel time
    mean_travel_time=((df['End Time'] -df['Start Time'] ).mean()).total_seconds()
    print("mean travel time is",mean_travel_time,"seconds\n")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
    
#user_stats
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts()
    print("counts of user types\n",user_types)
    # TO DO: Display counts of gender
    try:
        gender=df["Gender"].value_counts()
        print("\ncounts of gender\n",gender)
    except:
        print("\nno gender data to share")
    
    try:
        # TO DO: Display earliest, most recent, and most common year of birth
        recent=int(df["Birth Year"].max())
        earliest=int(df["Birth Year"].min())
        common_year_birth=int(df["Birth Year"].mode()[0])
        print("\nearliest year of birth ",earliest,"\nmost recent year of birth ",recent,"\nmost common year of birth",common_year_birth)
    except:
        print("\nno birth year data to share")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
#main
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        df.drop('Start hour', inplace = True,axis=1)
        x=True
        while x:
            print(df.sample(5))
            view=input("Would you like to view individual trip data? type 'yes' or 'no'.\n")
            if (view.strip()).title()=="No":
                break
        restart=input("Would you like to restart? type 'yes' or 'no'.\n")
        if((restart.strip()).title()=="No"):
            break
            
            

if __name__ == "__main__":
    pd.set_option("display.max_columns",None)
    main()
