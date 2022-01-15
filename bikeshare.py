import time
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
    print("Hello! Let's explore some US bikeshare data!\nWould you like to see data for Chicago, New York, or Washington?")
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = str(input())
    
               
      

    # TO DO: get user input for month (all, january, february, ... , june)
    print("By which month would you like to fillter the data? January, February, March, April, May, June")
   
    month = str(input())
    month = month.title()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print("By which day of the week would you like to fillter the data?")
    day = str(input())
    day = day.title()

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
    while True:
        try:
            info = pd.read_csv(CITY_DATA[city.lower()])
            break
        except KeyError:
            print("Enter a valid city name eaither Chicago, New York, or Washington?")
            city = str(input())

    df= pd.DataFrame(info)

    df['Start Time'] = pd.to_datetime(df['Start Time'], infer_datetime_format=True)
    df['month'] = df['Start Time'].dt.month
    df['hour'] = df['Start Time'].dt.hour
    df['day_of_week']=df['Start Time'].dt.strftime("%A")
    
    while True :
        try:
            if month != 'all':
                months = ['January', 'February', 'March', 'April', 'May', 'June']
                month = months.index(month)+1
                df = df[df['month']==month]
                break
        except:
            print("Please enter a valid month")
            month = str(input())

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].value_counts().idxmax()
    print("The most common month is : ",common_month)
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].value_counts().idxmax()
    print("The most common day of the week is : {}".format(common_day))

    # TO DO: display the most common start hour

    common_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is : {}".format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    famous_start = df['Start Station'].value_counts().idxmax()
    print(" The most commonly used start station is : ",famous_start)

    # TO DO: display most commonly used end station
    famous_End = df['End Station'].value_counts().idxmax()
    print(" The most commonly used start station is : ",famous_End )

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination =df['Start Station'].groupby(df['End Station']).value_counts().idxmax()
    print("The most frequent combination of start station and end station trip is:", frequent_combination)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("The total travel time is :", total_travel)

    # TO DO: display mean travel time
    mean_travel = total_travel / df['Trip Duration'].count()
    print("The mean travel time is :", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print("The count of each user type is: ", user_type)

    # TO DO: Display counts of gender
    try :
        if df['Gender'] in df:
            gender = df['Gender'].value_counts()
            print("The count of gender is: ", gender)
    except:
        print('')

    # TO DO: Display earliest, most recent, and most common year of birth
    try :
        if df['Birth Year'] in df:
            df['Birth Year'] = pd.to_datetime(df['Birth Year'], infer_datetime_format=True)

            earliest_year = df['Birth Year'].dt.year.min()
            print("The earliest year of birth is :", earliest_year)
            
            most_common_year = df['Birth Year'].dt.year.value_counts().idxmax()
            print("The most common year of birth is :", most_common_year)
    except:
        print('')


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
        
        
        print_data = input('would you like to view indivual trip data? Enter yes or no\n')
        while print_data.lower()=='yes':
            print(df.sample(n=5))
            print_data = input('would you like to view indivual trip data? Enter yes or no\n')

        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
