import re

def get_total(a):
    k = re.split('\n', a)
    k = [i for i in k if not i in ('','  ',' ')]

    def history_stat(k, team_main_name, min_point_4_set):
        data = []
        for i in range(len(k)):
            if k[i] == ' - ':
                if k[i+1] in ['Гости', 'Хозяева']:
                    continue
                points = ''.join([i for i in k[i+2] if i in [' ', ':'] or i.isdigit()])
                points = [i.split(':') for i in points.split(' ')[1:] if i.split(':') != ['']]
                print(points)
                team1 = [int(i[0]) for i in points]
                team2 = [int(i[1]) for i in points]
                dt = [[k[i-1], team1], [k[i+1], team2]]
                if k[i-1] == team_main_name:
                    data.extend(team1)
                elif k[i+1] == team_main_name:
                    data.extend(team2)
        data.sort()
        min_hist_point = data[:2]
        dt = all([i<=min_point_4_set for i in min_hist_point])
        return dt


    def main(k):
        t1 = k[0].split('.')[1]
        t2 = k[1].split('.')[1]
        points = ''.join([i for i in k[ 2] if i in [' ', ':'] or i.isdigit()]) 
        points = [i.split(':') for i in points.split(' ')[1:]] 
        team1 = [int(i[0]) for i in points]
        team1.append(t1)
        team2 = [int(i[1]) for i in points]
        team2.append(t2)
        percent = 20
        team_mains = []
        ab1 = abs(team1[0] - team1[1])
        bc1 = abs(team1[1] - team2[2])
        ab2 = abs(team2[0] - team2[1])
        bc2 = abs(team2[1] - team2[2])
        team22 = team2[:]
        team11 = team1[:]
        if ab1 in (0,1,2,3,4):
            ab1 = 80
        elif ab1 in (5, 6):
            ab1 = 65
        elif ab1 in (7, 8):
            ab1 = 50
        else:
            ab1 = 40 
        if bc1 in (0,1,2,3,4):
            bc1 = 80
        elif bc1 in (5, 6):
            bc1 = 65
        elif bc1 in (7, 8):
            bc1 = 50
        else:
            bc1 = 40   
        if ab2 in (0,1,2,3,4):
            ab2 = 80
        elif ab2 in (5, 6):
            ab2 = 65
        elif ab2 in (7, 8):
            ab2 = 50
        else:
            ab2 = 40 
        if bc2 in (0,1,2,3,4):
            bc2 = 80
        elif bc2 in (5, 6):
            bc2 = 65
        elif bc2 in (7, 8):
            bc2 = 50
        else:
            bc2 = 40
        team11.append([ab1, bc1])
        team11.append(team2)
        team_mains.append(team11)
        team22.append([ab2, bc2])
        team22.append(team1)
        team_mains.append(team22)
        dtqq = []
        for team_main in team_mains:
            if abs(sum(team_main[:3]) - sum(team_main[-1][:3])) <= 4:
                percent -= 7
            min_point_4_set = (sum(team_main[:3])/len(team_main[:3]))*((100-percent)/100)
            dt = history_stat(k, team_main_name=team_main[3], min_point_4_set=min_point_4_set)
            if dt:
                percent += 5
            min_point_4_set = (sum(team_main[:3])/len(team_main[:3]))*((100-percent)/100)
            total_point_4_set = min_point_4_set + sum(team_main[:3])
            k = f'{team_main[-3]} {total_point_4_set}\nВероятность: {sum(team_main[-2])/2}'
            
            dtqq.append(k)
        return '\n\n'.join(dtqq)


    return main(k)

