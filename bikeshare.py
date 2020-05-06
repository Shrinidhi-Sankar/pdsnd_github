import time
import pandas as pd
import numpy as np
import statistics 

months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday'];

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    valid_cities = ['chicago','new york city','washington']
    while True:
        city = input("Please select one of these cities - Chicago, New York City or Washington: ").lower();
        print(city);
        try:
            if valid_cities.index(city) > -1:
                break;
        except ValueError:
            print("Sorry the city you entered is not supported");
            continue;
    print("Now let's add some filters to the data set")
    # TO DO: get user input for month (all, january, february, ... , june)
    valid_months = ['all', 'january', 'february', 'march', 'april', 'may' , 'june'];
    while True:
        month = input("Please enter a month from january to june, if you don't require a filter enter 'all': ");
        print(month);
        try:
            if valid_months.index(month) > -1:
                break;
        except ValueError:
            print("Sorry the month you entered is not supported");
            continue;

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    valid_days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday' , 'saturday','sunday'];
    while True:
        day = input("Please enter a day to filter, if you don't require a filter enter 'all': ");
        print(day);
        try:
            if valid_days.index(day) > -1:
                break;
        except ValueError:
            print("Sorry the day you entered is not supported");
            continue;

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
    # load data file into a dataframe
    underscore = '_'
    city_list = city.split(' ')
    csvName = '_'.join(city_list)
    df = pd.read_csv(csvName+'.csv')

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month];

    # filter by day of week if applicable
    if day != 'all':
        day = days.index(day)
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day];
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    df['hour'] = df['Start Time'].dt.hour
    

    # TO DO: display the most common month
   
    #most_common_month_int = df['month'].mode()[0]
    most_common_month = months[df['month'].mode()[0]-1]
    print("The most common month is",most_common_month);

    # TO DO: display the most common day of week
    #most_common_day_int = 
    most_common_day = days[df['day_of_week'].mode()[0]]
    print("The most common day is",most_common_day);

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print("The most common hour is",most_common_hour);

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
            
    start_station_mode = statistics.mode(df['Start Station'])
    print("The most common start station is",start_station_mode);

    # TO DO: display most commonly used end station
    end_station_mode = statistics.mode(df['End Station'])
    print("The most common end station is",end_station_mode);

    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration']);
    print('Total travel time:',total_travel_time);
    
    # TO DO: display mean travel time
    mean_travel_time = total_travel_time/df.shape[0]
    print('Mean travel time:',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df['User Type'].value_counts();
    print('Count of each user type:', user_types_count); 
    
    if city != 'washington':
        # TO DO: Display counts of gender
        gender_count = df['Gender'].value_counts();
        print('Count of each gender:', gender_count);

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_yob = min(df['Birth Year']);
        most_recent_yob = max(df['Birth Year']);
        most_common_yob = df['Birth Year'].mode()[0];
        print('Earliest year of birth:',earliest_yob);
        print('Most recent year of birth:',most_recent_yob);
        print('Most common year of birth:',most_common_yob);
    
    else:
        print("No gender and Birth related details present in the data set for",city);    
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        # To display 5 rows of raw data
        i = 0
        raw = input("\nWould you like to see first 5 rows of raw data; type 'yes' or 'no'?\n").lower()
        pd.set_option('display.max_columns',200)

        while True:            
            if raw == 'no':
                break
            elif i > df.shape[0]:
                print('All the rows in the data set are already displayed. No more data to display')
                break;
            elif i+5 >df.shape[0]:
                print(df[i:df.shape[0]])
                print('No more data to display')
                break;
            else:
                print(df[i:i+5])
                raw = input('\nWould you like to see next rows of raw data?\n').lower()
                i += 5
    
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
