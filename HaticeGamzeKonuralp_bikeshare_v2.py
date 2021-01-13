#Hatice Gamze Konuralp
#14.01.2021
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


valid_months = ["all","january","february","march","april","may","june"]

valid_days = ["all","monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    city = input('Which city see data for ' + ', '.join(CITY_DATA.keys()) + '\n').lower()
       
    while (city not in CITY_DATA.keys()) :

        city = input('Valid options are ' + ', '.join(CITY_DATA.keys()) + '\n').lower()
     
    month = input('Which month see data for ' + ', '.join(valid_months) + '\n').lower()
       
    while (month not in valid_months) :

        month = input('Valid options are ' + ', '.join(valid_months) + '\n').lower()   
    
    day = input('Which day? ' + ', '.join(valid_days) + '\n').lower()
    
    while (day not in valid_days) :

        day = input('Valid options are ' + ', '.join(valid_days) + '\n').lower()
         

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.dayofweek

    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':

        month = valid_months.index(month)

        df = df[df['month'] == month]

    if day != 'all':

        day = valid_days.index(day) - 1

        df = df[df['day_of_week'] == day]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    most_freq_month = df['month'].value_counts().idxmax()

    print("The most frequent month is :", most_freq_month)

    most_freq_day_of_week = df['day_of_week'].value_counts().idxmax()

    print("The most frequent day of week is :", most_freq_day_of_week)

    most_freq_start_hour = df['hour'].value_counts().idxmax()

    print("The most frequent start hour is :", most_freq_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    most_freq_start_station = df['Start Station'].value_counts().idxmax()

    print("The most commonly used start station :", most_freq_start_station)

    most_freq_end_station = df['End Station'].value_counts().idxmax()

    print("The most freq used end station :", most_freq_end_station)

    most_freq_start_end_station = df.groupby(['Start Station', 'End Station']).size().reset_index(name='cnt').nlargest(columns=['cnt'],n=1)#.sort_values('cnt', ascending=False)
   
    print("The most commonly used start station and end station : {}, {}"\
           .format(most_freq_start_end_station['Start Station'], most_freq_start_end_station['End Station']))

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    sum_travel = df['Trip Duration'].sum()

    print("Sum travel time :", sum_travel)

    avg_travel = df['Trip Duration'].mean()

    print("Average travel time :", avg_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_counts = df['User Type'].value_counts()

    print("Number of user types:", user_counts )

    if 'Gender' in df.columns:

        gender_counts = df['Gender'].value_counts()

        print("Number of genders:", gender_counts)

    if 'Birth Year' in df.columns:

        birth_year = df['Birth Year']

        min_year = df['Birth Year'].min()
        print("Min birth year:", min_year)

        max_year = df['Birth Year'].max()
        print("Max birth year:", max_year)

        most_freq_year = df['Birth Year'].value_counts().idxmax()
        print("The most Frequent birth year:", most_freq_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_data(df):

    start_loc = 0
    view_display = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()

    while view_display == 'yes':
        
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
