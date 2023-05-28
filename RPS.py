# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import tensorflow as tf
import tensorflow_probability as tfp
import numpy as np
import time
from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player


def player(prev_opponent_play, opponent_history=[],
          play_order=[{
              "RRR": 0,
              "RRP": 0,
              "RRS": 0,
              "RPR": 0,
              "RPP": 0,
              "RPS": 0,
              "RSR": 0,
              "RSP": 0,
              "RSS": 0,
              "PRR": 0,
              "PRP": 0,
              "PRS": 0,
              "PPR": 0,
              "PPP": 0,
              "PPS": 0,
              "PSR": 0,
              "PSP": 0,
              "PSS": 0,
              "SRR": 0,
              "SRP": 0,
              "SRS": 0,
              "SPR": 0,
              "SPP": 0,
              "SPS": 0,
              "SSR": 0,
              "SSP": 0,
              "SSS": 0,
          }]):

    if not prev_opponent_play:
        prev_opponent_play = 'P'
    opponent_history.append(prev_opponent_play)

    last_three = "".join(opponent_history[-3:])
    if len(last_three) == 3:
        play_order[0][last_three] += 1
      

    # Limiting memory of opponent history:
    if len(opponent_history) > 81:
        first_three = "".join(opponent_history[0:3])
        opponent_history.pop(0)
        play_order[0][first_three] -= 1
    # 
            
    if len(opponent_history) >= 2:
      potential_plays = [
          opponent_history[-2] + prev_opponent_play + "R",
          opponent_history[-2] + prev_opponent_play + "P",
          opponent_history[-2] + prev_opponent_play + "S",
      ]
          
      sub_order = {
          k: play_order[0][k]
          for k in potential_plays if k in play_order[0]
      }
  
      prediction = max(sub_order, key=sub_order.get)[-1:]
  
      ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
      return ideal_response[prediction]

    else:
      return 'S'

      
  
  





  
  # if len(opponent_history) > 2:
  #   guess = opponent_history[-2]

  

  
