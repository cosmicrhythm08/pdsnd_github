import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

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
    while True:
        try:
            city = str(input("Enter city name (chicago,new york city or washington):")).lower()
            if city in CITY_DATA:
                break
            else:
                print("please enter a valid input")
            
        except:
            print("That\'s not a valid entry!")
       
      # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = str(input("Enter month name (all or anything in between january-june):")).lower()
            if month in months:
                break
            else:
                print("please enter a valid input")
            
        except:
            print("That\'s not a valid entry")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = str(input("Enter day of the week (all or any day of the week(eg: monday,tuesday.. ):")).lower()
            if day in days:
                break
            else:
                print("please enter a valid input")
            
        except:
            print("That\'s not a valid entry")
    


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
    df["Start Time"] = pd.to_datetime(df["Start Time"]) #Converting Start Time column to date time
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.weekday_name
    
    if month != 'all': #Checking for individual months
        
        month = months.index(month) + 1
        
        df = df[df['month'] == month]
        
    if day != 'all': #Checking for individual days
        df = df[df['day_of_week'] == day.title()]
        
        

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    com_month = df["month"].mode()[0]
    print("most common month:",months[com_month - 1])
    
    
    # TO DO: display the most common day of week
    com_dow = df["day_of_week"].mode()[0]
    print("most common day of the week:",com_dow)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    com_sthour = df["hour"].mode()[0]
    print('Most common Start Hour:',com_sthour)
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    pop_st_station = df["Start Station"].mode()[0]
    print("Most commonly used start station:",pop_st_station)


    # TO DO: display most commonly used end station
    pop_end_station = df["End Station"].mode()[0]
    print("Most commonly used end station:",pop_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df["combination"] = df["Start Station"] + "," + df["End Station"]
    print("Most frequent combination of start and end station trips:",df["combination"].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_travel_time = df["Trip Duration"].sum()
    print("Total travel time:",tot_travel_time)
    
    # TO DO: display mean travel time
    mean_traveltime = df["Trip Duration"].mean()
    print("Mean Travel Time:",mean_traveltime)
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    ustype_count = df["User Type"].value_counts()
    print("Counts of user types:",ustype_count)


    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        gender_count = df["Gender"].value_counts()
        print("Gender count:",gender_count)
    else:
        print("Gender column does not exist")
        
        
   
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        earliest = df["Birth Year"].min()
        print("earliest year of birth:",int(earliest))
    
        most_recent = df["Birth Year"].max()
        print("Most recent year of birth:",int(most_recent))
    
        most_com = df["Birth Year"].mode()[0]
        print("Most common year of birth:",int(most_com))
    else:
        print("Birth Year column does not exist")
        
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)       


#To display raw data as requested by the user
def display_data(df):
    while True:
        try:
            row_data = str(input("Would you like to see raw data from the table?(type yes or no):")).lower()
            break
        except:
            print("That's not a valid input...please try again")
        
           

    if row_data == "yes":
        print(df.iloc[:5])
        c = 5
        while c < len(df.index):
            
            try:
                row_next_data = str(input("Would you like to see 5 more rows of data?(type yes or no):")).lower()
                if row_next_data == "yes":
                    print(df.iloc[c-5:c])
                    c += 5
                else:
                    break    
                
            except:
                print("That's not a valid input...please try again")
            
            

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
