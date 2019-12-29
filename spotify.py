import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

#loading the dataset and storing in dataframe
spotify = pd.read_csv('top50.csv', encoding='cp1252')

#cleaning the data
#renaming the data
spotify.rename(columns={'Track.Name':'track_name','Artist.Name':'artist_name','Beats.Per.Minute':'beats_per_minute','Loudness..dB..':'Loudness(dB)','Valence.':'Valence','Length.':'Length', 'Acousticness..':'Acousticness','Speechiness.':'Speechiness'},inplace=True)

#summary statistics
print("\n---------------------------------------------------------------")
print("Summary Statistics for Spotify Dataset: ")
print(spotify.describe())
print("\n")

#number of songs in each genre
print("\n---------------------------------------------------------------")
print("Number of Songs in Each Genre: ")
popular_gen = spotify.groupby('Genre').size()
print(popular_gen)

#finding the artists with the most songs on the charts
print("\n---------------------------------------------------------------")
print("Top three artists with the most songs in the top 50")
popular_art = spotify.groupby('artist_name').size().nlargest(3)
print(popular_artist)

#popularity or track name
spotify.plot(y='Popularity',x= 'track_name',kind='bar',figsize=(15,5),legend =True,title="Popularity Vs Track Name",
        fontsize=14,stacked=True)
plt.ylabel('Popularity')
plt.xlabel('Track Name')
plt.show()
#even though seniorita is the number one song, it doesn't have the highest popularity

spotify.plot(y='Speechiness',x= 'Popularity',kind='scatter',figsize=(15,5),legend =True,title="Popularity Vs Speechiness",
        fontsize=14)
plt.ylabel('Speechiness')
plt.xlabel('Popularity')
plt.show()

spotify.plot(y='Length',x= 'Popularity',kind='scatter',figsize=(15,5),legend =True,title="Popularity Vs Length",
        fontsize=14)
plt.ylabel('Length')
plt.xlabel('Popularity')
plt.show()
