import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

city_list = ['chicago', 'new york city', 'washington']
month_list = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
day_list = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']


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
    print('Would you like to explore data for Chicago, New York City or Washington?')
    city = input('Enter city name: ').lower()
    
    for city_name in city_list:
        if city in city_list:
            break
        else:
            city = input('Invalid answer. Please try again: ')

    # TO DO: get user input for month (all, january, february, ... , june)
    print('\nWhich month are you interested in examining? To include all months, input "all".')
    month = input('Enter month name: ').lower()
    
    for month_name in month_list:
        if month in month_list:
            break
        else:
            month = input('Invalid answer. Please try again: ')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('\nWhich day of the week are you interested in examining? To include all days, input "all".')
    day = input('Enter day name: ').lower()
    
    for day_name in day_list:
        if day in day_list:
            print('\nThanks! Loading your information now...\n')
            break
        else:
            day = input('Invalid answer. Please try again: ')

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
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        month = month_list.index(month) + 1
        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    try:
        df['month'] = df['Start Time'].dt.month
        popular_month = df['month'].mode()[0]
        print('Most Popular Month: ', popular_month)
    except KeyError:
        print('Most Popular Month: Sorry! No data is available for your selection.\n')
        
    # TO DO: display the most common day of week
    try:
        df['day_of_week'] = df['Start Time'].dt.weekday_name
        popular_day = df['day_of_week'].mode()[0]
        print('Most Popular Day: ', popular_day)
    except KeyError:
        print('Most Popular Day: Sorry! No data is available for your selection.\n')
        
    # TO DO: display the most common start hour
    try:
        df['hour'] = df['Start Time'].dt.hour
        popular_hour = df['hour'].mode()[0]
        print('Most Popular Starting Hour: ', popular_hour)
    except KeyError:
        print('Most Popular Hour: Sorry! No data is available for your selection.\n')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

          
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    try:
        popular_start = df['Start Station'].mode()[0]
        print('Most Popular Start Station: ', popular_start)
    except KeyError:
        print('Most Popular Start Station: Sorry! No data is available for your selection.\n')
        
    # TO DO: display most commonly used end station
    try:
        popular_end = df['End Station'].mode()[0]
        print('Most Popular End Station: ', popular_end)
    except KeyError:
        print('Most Popular End Station: Sorry! No data is available for your selection.\n')
        
    # TO DO: display most frequent combination of start station and end station trip
    try:
        df['combo'] = df['Start Station'] + " to " + df['End Station']
        popular_combo = df['combo'].mode()[0]
        print('Most Popular Combo of Start & End Stations: ', popular_combo)
    except KeyError:
        print('Most Popular Combo of Start & End Stations: Sorry! No data is available for your selection.\n')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

          
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    try:
        total_time = df['Trip Duration'].sum()
        print('Total Travel Time: ', total_time)
    except KeyError:
        print('Total Travel Time: Sorry! No data is available for your selection.\n')
        
    # TO DO: display mean travel time
    try:
        avg_time = df['Trip Duration'].mean()
        print('Average Travel Time: ', avg_time)
    except KeyError:
        print('Average Travel Time: Sorry! No data is available for your selection.\n')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

          
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        user_types = df['User Type'].value_counts()
        print('User Type Count:\n', user_types)
    except KeyError:
        print('User Type Count: Sorry! No data is available for your selection.\n')

    # TO DO: Display counts of gender
    try:
        gender_types = df['Gender'].value_counts()
        print('\nUser Gender Counts:\n', gender_types)
    except KeyError:
        print('\nUser Gender Counts: Sorry! No data is available for your selection.\n')
        
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        min_birth = df['Birth Year'].min()
        print("\nOldest User's Year of Birth: ", min_birth)
    except KeyError:
        print("Oldest User's Year of Birth: Sorry! No data is available for your selection.")
        
    try:    
        max_birth = df['Birth Year'].max()
        print("Youngest User's Year of Birth: ", max_birth)
    except KeyError:
        print("Youngest User's Year of Birth: Sorry! No data is available for your selection.")
        
    try:    
        popular_birth = df['Birth Year'].mode()
        print('Most Common Year of Birth Among Users: ', popular_birth)
    except KeyError:
        print("Most Common Year of Birth Among Users: Sorry! No data is available for your selection.")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        # TO DO: Implement a function that displays raw data upon request by user
        print('Would you like to see a slice of the raw data? (Yes/No)')
        i = 0
        
        while True:
            show_data = input('Show raw data? ').lower()
            if show_data == 'yes':
                data_row = df.iloc[i:i+5]
                i += 5
                print(data_row)
            else: 
                print('Data review completed.')
                break    
   
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Goodbye!')
            break


if __name__ == "__main__":
	main()