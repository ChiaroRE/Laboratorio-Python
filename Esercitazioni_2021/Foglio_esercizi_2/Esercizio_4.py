import numpy as np

class LinearModel():
    def __init__(self):
        self.angular_coeff = None
        self.intercept = None
        self.train_data = None

    def fit(self, train_data):
        x = train_data[:,0]
        y = train_data[:,1]
        
        media_x = np.mean(x)
        media_y = np.mean(y)

        Cov_xy = 0
        for i in range(len(train_data)):
            Cov_xy = Cov_xy + ((x[i] - media_x) * (y[i] - media_y))
        Cov_xy = Cov_xy/(len(x) - 1)

        sd_x = np.std(x,ddof = 1)
        sd_y = np.std(y,ddof = 1)
        
        Corr_xy = Cov_xy/(sd_x * sd_y)

        self.angular_coeff = Corr_xy * (sd_y/sd_x)
        self.intercept = media_y - self.angular_coeff * media_x
        self.train_data = train_data
        print("Average x = {}".format(media_x))
        print("Average y = {}".format(media_y))
        print("Standard deviation x = {}".format(sd_x))
        print("Standard deviation y = {}".format(sd_y))
        print("Covariance x and y = {}".format(Cov_xy))
        print("Correlation x and y = {}".format(Corr_xy))
        print("Angular coefficient = {}".format(self.angular_coeff))
        print("Intercept = {}".format(self.intercept))

    def predict(self,xp):
        try:
            yp = xp * self.angular_coeff + self.intercept
            return yp
        except self.angular_coeff is None or self.intercept is None:
            raise Exception("The values of the linear model are None")
            
            


train_data = np.array([[833,37.0],[987,41.6],[883,37.2],[378,15.2],[84,3.4],[483,19.6],[835,35.1],[646,28.9],[508,22.6],[90,3.7]])
xp = x = train_data[:,0]
km = 2500
cost = 1.4 #€/L

mod = LinearModel()
mod.fit(train_data)
total = float(mod.predict(km)) * cost
print("The total cost of the journey is {} €. Everyone will spend {} €".format(total,total/3))