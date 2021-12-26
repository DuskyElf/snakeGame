import myPygameWorkflow
from config import *
from scene_game import SceneGame
from scene_start import SceneStart

# Whole game variable
whole_game = myPygameWorkflow.game.Game((WIN_WID, WIN_HEI))

sceneStart = SceneStart(whole_game)
sceneGame = SceneGame(whole_game, fps=120)

whole_game.start(sceneStart)
whole_game.start(sceneGame)
