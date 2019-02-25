import time
import datetime as dt
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input('Would you like to see data for Chicago, New York, or Washington ?\n').lower() # editing after review 1 - .lower()
    while city.lower()!='chicago' and city.lower()!='new york' and city.lower()!='washington':
        city=input('Incorrect city, Please choose from those cities: Chicago, New York, Washington \n').lower() # editing after review 1 - .lower()
    # get user input for month (all, january, february, ... , june)
    # get user input for day of week (all, monday, tuesday, ... sunday)
    qa=input('Would you like to filter the data by month, day, both, or not at all? Type \'none\' for no time filters \n')
    if qa.lower()=='month':
        month=input('Which month? January, February, March, April, May, or June?\n').lower() # editing after review 1 - .lower()
        day='all'
    if qa.lower()=='day':
        month='all'
        day=int(input('Which day? Please type your response as an integer (e.g. 1=Sunday)\n'))
    if qa.lower()=='none':
        month='all'
        day='all'
    if qa.lower()=='both':
        month=input('Which month? January, February, March, April, May, or June?\n').lower() # editing after review 1 - .lower()
        day=int(input('Which day? Please type your response as an integer (e.g. 1=Sunday)\n'))
    print('-'*40)
    return city, month, day, qa


def load_data(city, month, day, qa):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
     # load data file into a dataframe
    if city.lower() == 'new york':
        city = 'new york city'

    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        days = {1:'sunday', 2:'monday', 3:'tuesday', 4:'wednesday', 5:'thursday', 6:'friday', 7:'saturday'}
        day = days[day]
        print(day)
        df = df[df['day_of_week'] == day.title()]

    return df,qa

def time_stats(df,qa):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['hour'] = df['Start Time'].dt.hour
    # display the most common month
    # display the most common day of week
    # display the most common start hour
    if qa=='month':
        common_day = df['day_of_week'].mode()[0]
        print('The most common day of week',common_day, 'Filter', qa)
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    if qa.lower()=='day':
        common_month=df['month'].mode()[0]
        print('The most common month',common_month, 'Filter', qa)
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    if qa.lower()=='none':
        common_month=df['month'].mode()[0]
        print('The most common month',common_month, 'Filter', qa)
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        common_day = df['day_of_week'].mode()[0]
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('The most common day of week',common_day, 'Filter', qa)
        print('-'*40)

    common_hour = df['hour'].mode()[0]
    print('The most common start hour',common_hour, 'Filter', qa)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print(df)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station:',common_start_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station:',common_end_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    # display most frequent combination of start station and end station trip
    df['comb station']=df['Start Station']+' - '+df['End Station']
    comb_station=df['comb station'].mode()[0]
    print('The most frequent combination of start station and end station trip:',comb_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # display total travel time
    trip_dur_in_s=df['Trip Duration'].sum() # editing after review 1 - .lower()
    trip_dur_in_m=trip_dur_in_s//60
    trip_dur_in_h=trip_dur_in_m//60
    print('Total travel time: ', trip_dur_in_h, 'hour(-s)', trip_dur_in_m%60, 'minut(-es)', trip_dur_in_s%60, 'second(-s)' )
    # display mean travel time
    mean_dur_s=round(df['Trip Duration'].mean())
    mean_dur_m=mean_dur_s//60
    mean_dur_h=mean_dur_m//60
    print('Mean travel time: ', mean_dur_h, 'hour(-s)',mean_dur_m%60, 'minut(-es)', mean_dur_s%60, 'second(-s)')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    print('Counts of user types: \n',df['User Type'].value_counts())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    # Display counts of gender
    # Display earliest, most recent, and most common year of birth
    check=df.columns.values.tolist()
    if 'Birth Year' in check and 'Gender' in check:
        gender = df['Gender'].value_counts()
        print('Counts of gender: \n',gender)
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        print('Most common year of birth: ',df['Birth Year'].mode()[0])
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        print('Most earliest year of birth: ',df['Birth Year'].min())
        print('Most recent year of birth: ',df['Birth Year'].max())
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    else:
        print('There is no information about Gender and Birth Year in Washington statistics')
def display_data_function(df):              # editing after review 1 - .lower()
    i=0
    for j in range(5,len(df),5):
        q=input('Do you want to see raw data? Type \'no\' or \'yes\'\n').lower()
        if q=='yes':
            print(df[i:j])
            i+=5
        else:
            break
def main():
    while True:
        city, month, day, qa = get_filters()
        df,qa = load_data(city, month, day, qa)
        time_stats(df,qa)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data_function(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
