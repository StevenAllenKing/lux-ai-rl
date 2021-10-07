from kaggle_environments import make
import json
# run another match but with our empty agent
env = make("lux_ai_2021", configuration={"seed": 5621242, "loglevel": 2, "annotations": True}, debug=True)

# Play the environment where the RL agent plays against itself
steps = env.run(["./kaggle_submissions/main.py", "./kaggle_submissions/main.py"])

# Render the match
# env.render(mode="ipython", width=1200, height=800)

env.render(mode='json',width=1200, height=800)