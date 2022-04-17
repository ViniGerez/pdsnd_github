import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': r'C:\Users\vinicius.gerez\Desktop\Udacity\Github\project_03\pdsnd_github\chicago.csv',
              'new york city': r'C:\Users\vinicius.gerez\Desktop\Udacity\Github\project_03\pdsnd_github\new_york_city.csv',
              'washington': r'C:\Users\vinicius.gerez\Desktop\Udacity\Github\project_03\pdsnd_github\washington.csv' }

def get_filters():
    """Asks user to specify a city, month, and day to analyze.
    
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 '\nPlease choose one of the following: Chicago, New York City, Washington.\n').casefold()
    while True:
        if city in ('new york city', 'chicago', 'washington'):
            break
        else:
            city = input('\nInput Error. \nPlease choose one of the following: Chicago, New York City, Washington.\n').casefold()
        

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('\nWhich month data are you interested in? Please choose from:'
                  '\nJanuary, February, March, April, May, June or type \'all\' if you wish to see the fully aggregated data.\n').casefold()
    
    while True:
        if month in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            break
        else:
            month = input('\nInput Error. \nIn which month\'s data are you interested in? Please choose from:'
                      '\nJanuary, February, March, April, May, June or type \'all\' if you wish to see the fully aggregated data.\n').casefold()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\nIn which day of the week\'s data are you interested in in? Please choose from:'
                '\nSunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type \'all\' if you wish to see the fully aggregated data.\n').casefold()
    while True:
        if day in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
            break
        else:
            day = input('\nInput Error. \nIn which day of the week\'s data are you interested in in? Please choose from:'
                    '\nSunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type \'all\' if you wish to see the fully aggregated data.\n').casefold()
        

    print('-'*40)
    print('\nYou chose:\n'
          '\nCity = {} \n'.format(city.title()),
          '\nMonth = {} \n'.format(month.title()),
          '\nDay of the week = {} \n'.format(day.title()))
    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    """Loads data for the specified city and filters by month and day if applicable.
    
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

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
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most Common Month: {}'.format(most_common_month))


    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print('Most Common day: {}'.format(most_common_day_of_week))


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print('Most Common Hour: {}'.format(most_common_start_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('Most Commonly used start station: {}'.format(most_common_start_station))


    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('\nMost Commonly used end station: {}'.format(most_common_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combination'] = df['Start Station'] + ' to ' + df['End Station']
    most_common_station_combination = df['Station Combination'].mode()[0]
    print('\nMost frequent combination of start station and end station trip: {}'.format(most_common_station_combination))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is equivalent to {} days, or {} hours'.format(round(total_travel_time/86400, 2), round(total_travel_time/3600, 2)))


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The average (mean) travel time is equivalent to {} minutes'.format(round(mean_travel_time/60, 2)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_of_user_types = df['User Type'].value_counts()
    print('User Types:\n{}'.format(count_of_user_types))

    # TO DO: Display counts of gender
    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n{}'.format(gender_types))
    except KeyError:
      print("\nGender Types:\nNo gender data available for the current selection.")

    # TO DO: Display earliest year of birth
    try:
      earliest_year_of_birth = df['Birth Year'].min()
      print('\nEarliest Year of Birth: {}'.format(round(earliest_year_of_birth)))
    except KeyError:
      print("\nEarliest Year of Birth:\nNo data available for the current selection.")

    # TO DO: Display most recent year of birth
    try:
      most_recent_year_of_birth = df['Birth Year'].max()
      print('\nMost Recent Year of Birth: {}'.format(round(most_recent_year_of_birth)))
    except KeyError:
      print("\nMost Recent Year of Birth:\nNo data available for the current selection.")

    # TO DO: Display most common year of birth
    try:
      most_common_year_of_birth = df['Birth Year'].mode()[0]
      print('\nMost Common Year of Birth: {}'.format(round(most_common_year_of_birth)))
    except KeyError:
      print("\nMost Common Year of Birth:\nNo data available for the current selection.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def fetch_raw_data(df):
    """Asks user whether they want to see raw data. If answer's 'yes', 5 data rows are displayed at a time."""

    row_count = 0
    while True:
        fetch_raw_data = input('\nWould you like to see raw data? Type "yes" to see it or anything else if you do not want it.\n').casefold()
        if fetch_raw_data != 'yes':
            break
        else:
            print(df[row_count : row_count+5])
            row_count += 5
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        fetch_raw_data(df)

        restart = input('\nWould you like to restart? Type "yes" to do so, or anything else if you would like to exit.\n')
        if restart.lower() != 'yes':
            print('\nSee you next time!')
            break


if __name__ == "__main__":
    main()