import sqlite3, operator, time

class MyDataBase():
    def __init__(self):
        self.connection = sqlite3.connect('aut-db.db')
    def insertTeam(self, teamName, leagueName, depName):
        self.connection.execute(
            '''INSERT INTO teams (team_name, league_name, dependency_name) VALUES (:t_name, :l_name, :d_name)''',
            {"t_name" : teamName, "l_name" : leagueName, "d_name" : depName})
        self.connection.commit()
        return "done"

    def insertRecord(self, level, teamName, leagueName, fTime, sTime, tTime, bRec):

        if(level == "Prepration"):
            self.connection.execute(
                '''INSERT INTO pre_result (league_name, team_name, rec_one_time,'''
                '''rec_two_time,rec_three_time, best_record) VALUES (:l_name,'''
                ''':t_name,:f_time,:s_time,:t_time, :b_rec)''',
                {"l_name" : leagueName, "t_name" : teamName, "f_time" : fTime,
                 "s_time" : sTime,"t_time" : tTime, "b_rec" : bRec})
            self.connection.commit()
            return "done"

        elif(level == "Semi-Final"):
            self.connection.execute(
                '''INSERT INTO semi_result (league_name, team_name, rec_one_time,'''
                '''rec_two_time,rec_three_time, best_record) VALUES (:l_name,'''
                ''':t_name,:f_time,:s_time,:t_time, :b_rec)''',
                {"l_name": leagueName, "t_name": teamName, "f_time": fTime,
                 "s_time": sTime, "t_time": tTime, "b_rec" : bRec})
            self.connection.commit()
            return "done"
        else:
            self.connection.execute(
                '''INSERT INTO final_result (league_name, team_name, rec_one_time,'''
                '''rec_two_time,rec_three_time, best_record) VALUES (:l_name,'''
                ''':t_name,:f_time,:s_time,:t_time, :b_rec)''',
                {"l_name": leagueName, "t_name": teamName, "f_time": fTime,
                 "s_time": sTime, "t_time": tTime, "b_rec" : bRec})
            self.connection.commit()
            return "done"

    def getTeams(self, leagueName):
        cursor = self.connection.execute('''SELECT * FROM teams WHERE league_name=(:l_name)''', {"l_name" : leagueName})
        rows = cursor.fetchall()
        if(rows is None):
            return False
        else:
            return rows

    def getRecords(self, leagueName, level):
        if(level == "Prepration"):
            cursor = self.connection.execute('''SELECT * FROM pre_result WHERE league_name = (:l_name) ORDER BY best_record''',
                                             {"l_name" : leagueName})
        elif(level == "Semi Final"):
            cursor = self.connection.execute('''SELECT * FROM semi_result WHERE league_name = (:l_name) ORDER BY best_record''',
                                             {"l_name" : leagueName})
        else:
            cursor = self.connection.execute('''SELECT * FROM final_result WHERE league_name = (:l_name) ORDER BY best_record''',
                                             {"l_name" : leagueName})
        rows = cursor.fetchall()
        if(rows is None):
            return False
        else:
            return rows