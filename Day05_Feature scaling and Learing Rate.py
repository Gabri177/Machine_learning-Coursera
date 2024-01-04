import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=2)
plt.style.use('ggplot')

# load the dataset
X_train = np.array([
    [ 952, 2, 1, 65],
    [1244, 3, 2, 64],
    [1947, 3, 2, 17],
    [1500, 2, 1, 30],
    [1647, 3, 2, 26],
    [1839, 3, 2, 78],
    [1580, 3, 2, 13],
    [1349, 3, 2, 10],
    [1912, 4, 2, 70]
])
y_train = np.array(
    [271.5, 232, 509.8, 341, 423, 654, 235, 158, 789]
)
X_features = ['size(sqft)', 'bedrooms', 'floors', 'age']
fig, ax = plt.subplots(1, 4, figsize = (12, 3), sharey = True)
for i in range(len(ax)):
    ax[i].scatter(X_train[:, i], y_train)
    ax[i].set_xlabel(X_features[i])
ax[0].set_ylabel("price(1000's)")
plt.show()

def zscore_normalize_features(X):
    mu = np.mean(X, axis = 0)
    sigma = np.std(X, axis = 0)
    X_norm = (X - mu) / sigma
    return (X_norm, mu, sigma)

mu      = np.mean(X_train, axis = 0)
sigma   = np.std (X_train, axis = 0)
X_mean  = X_train - mu
X_norm = (X_train - mu) / sigma

# normalize the original features
X_norm, X_mu, X_sigma = zscore_normalize_features(X_train)
print(f"X_mu = {X_mu}, \nX_sigma = {X_sigma}")
print(f"Peak to Peak range by column in Raw        X:{np.ptp(X_train,axis=0)}")
print(f"Peak to Peak range by column in Normalized X:{np.ptp(X_norm,axis=0)}")

