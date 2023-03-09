# Conversational Scripts

This file contains snippets of what a multiturn conversation between a user and the chatbot could look like, as well as a broad analysis of the snippets.
Generally, the user will initiate the conversation by first asking a question. The chatbot will then respond, either providing an answer or asking for
further clarification, until the user chooses to end the conversation. In the following snippets, messages by the user are denoted by `U:`; and messages by
the chatbot or agent are denoted by `A:`.

## Script 1

In this sample, the user begins the conversation by asking about other games that have been made by the developer of a particular game. Because games often
have multiple developers, the chatbot should first name all the developers and ask which developer the user is interested in. The user can then respond in
a number of ways--specifying either a particular developer, multiple developers, or no preference. The chatbot should mention games based on the user's
response. In the rather unique situation presented by the sample below, the chatbot is unable to find other games made by the developer chosen by the user.
In such cases, the chatbot should attempt to continue the conversation by asking if it should try to find games by the other developers.

```
U: What are other games made by the developers of Omori?  
A: Omori has two developers, Omocat and MP2 Games. Which developer’s games would you like to see?  
U: Omocat  
A: I could not find any other games developed by Omocat. Would you like to see games developed by MP2 Games instead?  
U: Yes  
A: Games developed by MP2 Games include Mighty Goose and Noitu Love. Would you like to see more games?  
U: No  
```

## Script 2

In this sample, the user begins the conversation by asking about other games that have the same genre as a particular game. Because games often have
multiple genres, the chatbot should first name all the genres and ask which genre the user is interested in. The user can then respond in a number of
ways--specifying either a particular genre, multiple genres, or no preference. The chatbot should then mention games with genres mentioned by the user.
In the situation presented by the sample below, the chatbot is only able to find one genre for the mentioned game. In such cases, the chatbot should
mention the genre and ask if it should try to find other games in that genre.

```
U: What are some games in the same genres as Outlast?  
A: Outlast is a survival horror game. Would like to see some survival horror games?  
U: Yes  
A: Some survival horror games are Amnesia: The Dark Descent and The Mortuary Assistant. Would you like to see more games?  
U: No  
```

## Script 3

In this somewhat more complex sample due to combining multiple game characteristics, the user begins the conversation by asking about games in a
particular genre that contain (or do not contain) potentially objectionable content. The chatbot should first find games in that particular genre and then
filter through them based on the mentioned restrictions (potentially based on ESRB ratings--rating categories and content descriptors). The chatbot can
then output to the user games that meet all the requirements. In the situation presented by the sample below, the chatbot was unable to find a game that
met the described restrictions in its second response. It still mentioned the game to the user but explicity stated its failure to comply with the
restrictions.

```
U: What is a family-friendly third-person shooter without blood?  
A: Splatoon is a family friendly third-person shooter that does not contain any blood. Would you like to see more suggestions?  
U: Yes  
A: Ratchet and Clank: Rift Apart is another family friendly third-person shooter but contains animated blood. Would you like to see more suggestions?  
U: No  
```

## Script 4

In this sample, the user begins the conversation by asking about games that can only be found on a particular platform. The chatbot should then find games
only on that platform and output them to the user. The situation presented by the sample below is unique in that the user asks for a platform that can also
be considered a series of platforms. In such cases, it may be ideal for the chatbot to initally assume the user is asking about the entire series of
platforms and ask for clarification (i.e., whether any platform in the series or a particular one is desired). The concept of backwards compatibility may
also complicate these kinds of questions. It may be ideal to ignore those cases, however, as such games are not intended to run natively on the future
platforms as much as it is an additional feature to compel consumers to purchase them.

```
U: What are some Xbox-exclusive games?  
A: Would you like to see games exclusive to any Xbox console or specifically the Xbox, Xbox 360, Xbox One, or Xbox Series X and S?  
U: Any Xbox console  
A: Some games that can only be found on the Xbox series of consoles are Fantasia: Music Evolved and Forza Horizon 2. Would you like to see more games?  
U: No  
```

## Script 5

In this sample, the user begins the conversation by asking about games based on release date information. the chatbot should then find games that meet
the requirements and output them to the user. Potential questions relating to release dates could include asking about games released before a particular
date, after a particular date, in a particular year, etc. In the situation presented by the sample below, it may be necessary for the chatbot to implement
more arbitrary requirements (i.e., the past month, two months, etc.). The age of the collected data and how often it is updated may complicate these kinds
of questions.

```
U: What are some games that released recently?  
A: Hogwarts Legacy released on February 10, 2023; and Hi-Fi Rush released on January 25, 2023. Would you like to see more games that released recently?  
U: Yes  
A: One Piece Odyssey released on January 13, 2023; and Fire Emblem Engage released on January 20, 2023. Would you like to see more games that released recently?  
U: No  
```
