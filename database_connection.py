from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime

engine = create_engine('sqlite:///khl_stats.sqlite')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class GoalkeeperStats(Base):
	__tablename__ = 'goalkeeper_stats'
	id = Column (Integer, primary_key=True)
	player_name = Column(String(50))
	shirt_num = Column(Integer)
	player_club = Column(String(10))
	games_played = Column(Integer)
	games_won = Column(Integer)
	games_lost = Column(Integer)
	games_bullit = Column(Integer)
	shots_on_goal = Column(Integer)
	goals = Column(Integer)
	goals_denied = Column(Integer)
	percent_of_denied = Column(Float)
	quality_coef = Column(Float)
	goals_scored = Column(Integer)
	pass_with_goal = Column(Integer)
	games_no_goal = Column(Integer)
	penaly_time = Column(Integer)
	time_on_ice = Column(String(50))
	version_datetime = Column(DateTime)


	def __init__(self, player_name=None, shirt_num=None, player_club=None, games_played=None, 
		games_won=None, games_lost=None, games_bullit=None, shots_on_goal=None, 
		goals=None, goals_denied=None, percent_of_denied=None, quality_coef=None, 
		goals_scored=None, pass_with_goal=None, games_no_goal=None, penaly_time=None,
		time_on_ice=None, version_datetime=None):
		
		self.player_name = player_name
		self.shirt_num = shirt_num
		self.player_club = player_club
		self.games_played = games_played
		self.games_won = games_won
		self.games_lost = games_lost
		self.games_bullit = games_bullit
		self.shots_on_goal = shots_on_goal
		self.goals = goals
		self.goals_denied = goals_denied
		self.percent_of_denied = percent_of_denied
		self.quality_coef = quality_coef
		self.goals_scored = goals_scored
		self.pass_with_goal = pass_with_goal
		self.games_no_goal = games_no_goal
		self.penaly_time = penaly_time
		self.time_on_ice = time_on_ice
		self.version_datetime = version_datetime

	def __repr__(self):
		return '<User {} {}>'.format(self.player_name, self.player_club)

class PlayersStats(Base):
	__tablename__ = 'player_stats'
	id = Column (Integer, primary_key=True)
	player_name = Column(String(50))
	shirt_num = Column(Integer)
	player_club = Column(String(10))
	games_played = Column(Integer)
	goals_scored = Column(Integer)
	passes_on_goal = Column(Integer)
	gp_points = Column(Integer)
	plus_minus = Column(Integer)
	penaly_time = Column(Integer)
	goals_equal_teams = Column(Integer)
	goals_advantage = Column(Integer)
	goals_disadvantage = Column(Integer)
	goals_overtime = Column(Integer)
	goals_decisive = Column(Integer)
	bullit_decisive = Column(Integer)
	shots_on_goal = Column(Integer)
	percent_of_shots_scored = Column(Float)
	average_shots = Column(Float)
	faceoffs_taken = Column(Integer)
	faceoff_won = Column(Integer)
	faceoff_percentage = Column(Float)
	average_time_on_ice = Column(String(10))
	average_substitutes = Column(Float)
	opponent_hits = Column(Integer)
	blocked_shots = Column(Integer)
	fouls_accepted = Column(Integer)
	version_datetime = Column(DateTime)
	player_position = Column(String(15))
	
	def __init__(self, player_name=None, shirt_num=None, player_club=None, games_played=None, 
		goals_scored=None, passes_on_goal=None, gp_points=None, plus_minus=None, 
		penaly_time=None, goals_equal_teams=None, goals_advantage=None, goals_disadvantage=None, 
		goals_overtime=None, goals_decisive=None, bullit_decisive=None, shots_on_goal=None,
		percent_of_shots_scored=None, average_shots=None, faceoffs_taken=None, faceoff_won=None, 
		faceoff_percentage=None, average_time_on_ice=None, average_substitutes=None, opponent_hits=None,
		blocked_shots=None, fouls_accepted=None, version_datetime=None, player_position=None):
		
		self.player_name = player_name
		self.shirt_num = shirt_num
		self.player_club = player_club
		self.games_played = games_played
		self.goals_scored = goals_scored
		self.passes_on_goal = passes_on_goal
		self.gp_points = gp_points
		self.plus_minus = plus_minus
		self.penaly_time = penaly_time
		self.goals_equal_teams = goals_equal_teams
		self.goals_advantage = goals_advantage
		self.goals_disadvantage = goals_disadvantage
		self.goals_overtime = goals_overtime
		self.goals_decisive = goals_decisive
		self.bullit_decisive = bullit_decisive
		self.shots_on_goal = shots_on_goal
		self.percent_of_shots_scored = percent_of_shots_scored
		self.average_shots = average_shots
		self.faceoffs_taken = faceoffs_taken
		self.faceoff_won = faceoff_won
		self.faceoff_percentage = faceoff_percentage
		self.average_time_on_ice = average_time_on_ice
		self.average_substitutes = average_substitutes
		self.opponent_hits = opponent_hits
		self.blocked_shots = blocked_shots
		self.fouls_accepted = fouls_accepted
		self.version_datetime = version_datetime
		self.player_position = player_position
		
	def __repr__(self):
		return '<User {} {}>'.format(self.player_name, self.player_club)

if __name__ == "__main__":
	Base.metadata.create_all(bind=engine)

