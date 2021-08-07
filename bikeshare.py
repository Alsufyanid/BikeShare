import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
              
Month_List = ['All','January','Februry','March','April','May','June']
Days_Of_The_Week=['All','Monday','Tuesday','Wednesday','Thursday', 'Friday','Saturday','Sunday']

def get_filters():
    
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city= input('write the city name')
        city= city.lower()
        if city not in CITY_DATA.keys():
            user_error_message="Unfortunately {} is either an invalid entry or not in our service range yet"
            print(user_error_message.format(city))
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month= input('What month are you interested in? Write all for the whole 6 months period\n')
        month= month.capitalize()
        if month not in Month_List:
            user_errormonth_message="Unfortunately {} is either invalid entry or not in our data time range"
            print(user_errormonth_message.format(month))
        else:
            break
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day= input('What day are you interested in?\n')
        day= day.capitalize()
        if day not in Days_Of_The_Week:
            print('Invalid entry. Please try again')
        else:
            break


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'All':
        month = Month_List.index(month)
        df = df[df['month'] == month]

    if day != 'All':
        df = df[df['day_of_week'] == day]
        
    return df


def time_stats(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    the_most_common_month=df['month'].mode()[0]
    print('The most common month is: {}'.format(Month_List[the_most_common_month]))
    
    # TO DO: display the most common day of week
    the_most_common_day=df['day_of_week'].mode()[0]
    print('User favourite day for cycling is: {}'.format(the_most_common_day))

    # TO DO: display the most common start hour
    the_most_common_hour=df['hour'].mode()[0]
    print('Bike rush hour is: {}'.format(the_most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Most_Common_START_Station=df['Start Station'].mode()[0]
    print('Bike common pick up station: {}'.format(Most_Common_START_Station))

    # TO DO: display most commonly used end station
    Most_Common_End_Station=df['End Station'].mode()[0]
    print('Bike common drop off station: {}'.format(Most_Common_End_Station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Start to end Station'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    Start_to_end_Station = df['Start to end Station'].mode()[0]
    print('Customers common trip is from {} '.format(Start_to_end_Station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_min,total_sec = divmod(df['Trip Duration'].sum(), 60)
    total_hour,total_min = divmod(total_min, 60)
    print ('The total travel time is: {} hour and {} minutes and {} seconds'.format(total_hour,total_min,round(total_sec)))

    # TO DO: display mean travel time
    Average_min,average_sec = divmod(df['Trip Duration'].mean(),60)
    Average_hour,total_min = divmod(Average_min,60)
    print('Trip average duration is : {} hour and {} minutes and {} seconds'.format(Average_hour,Average_min,round(average_sec)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
   
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    Counts_of_user_type=df['User Type'].value_counts()
    print('Registered users types are:\n{}'.format(Counts_of_user_type))

    # TO DO: Display counts of gender
    if city != 'washington':
        Counts_of_user_gender=df['Gender'].value_counts()
        print('users gender :\n{}'.format(Counts_of_user_gender))
    else:
            print('Unfortunately, gender type is not available for this entry') 

    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        earliest_birth_year=df['Birth Year'].min()
        most_recent_birth_year=df['Birth Year'].max()
        most_common_birth_year=df['Birth Year'].mode()
        print('Earlist birth year is {} \nRecent birth year is {} \nMost common birth year is {}'.format(int(earliest_birth_year),int(most_recent_birth_year),int(most_common_birth_year)))
    else:
            print('Unfortunately, birth year information is not available') 


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
      

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()