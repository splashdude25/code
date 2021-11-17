''' Briggs '''


from numpy import dot
from numpy.matlib import randn

'''
kf_predict performs the prediction of these outputs (X and P) when giving
six input:

covariance (def): a measure of how much two random variables vary together.

X: the mean estimate of the previous step (k-1).
P: the state covariance of previous step (k-1).
A: the transition nxn matrix.
Q: the process noise covariance matrix.
B: the input effect matrix.
U: the control input.
'''

def kfPredict(X, P, A, Q, B, U):
    X = dot(A, X) + dot(B, U)
    P = dot(A, dot(P, A.T)) + Q #A.T is transposing matrix A.
    return(X, P)

'''
kf_update performs the update of X and P giving the predicted X and P
matrices, the measurement vector Y, the measurement matrix H and the
measurement covariance matrix R. The additional input will be:

K: the Kalman Gain matrix.
IM: the Mean of predictive distribution of Y.
IS: the Covariance or predictive mean of Y.
LH: the Predictive probability (likelihood) of measurement which is computed
using the Python function gauss_pdf.
'''
from numpy import dot, sum, tile, linalg, eye
from numpy.linalg import inv, det

def kfUpdate(X, P, Y, H, R):
    print("H",H.shape,"and", "X", X.shape)
    IM = dot(H, X)
    print("IM",IM.shape)
    IS = R + dot(H, dot(P, H.T))
    K = dot(P, dot(H.T, inv(IS)))
    print("K", K.shape)
    X = X + dot(K, (Y-IM))
    print("New X", X.shape)
    P = P - dot(K, dot(IS, K.T))
    LH = gaussPDF(Y, IM, IS)
    return (X, P, K, IM, IS, LH)

#gauss_pdf is computing the predictive probability of measurement
def gaussPDF(X, M, S):
    if M.shape[1] == 1: #shape returns the shape of the array as a tuple of integers
        DX = X - tile(M, X.shape[1]) #tile constructs an array by repeating M X.shape() amount of times
        E = 0.5*sum(DX*(dot(inv(S), DX)), axis=0)
        E = E + 0.5*M.shape[0]*log(2*pi)+0.5*log(det(S))
        P = exp(-E)
    elif X.shape[1] == 1:
        DX = tile(X, M.shape[1]) - M
        E = 0.5*sum(DX*(dot(inv(S), DX)), axis=0)
        E = E + 0.5*M.shape[0]*log(2*pi)+0.5*log(det(S))
        P = exp(-E)
    else:
        DX = X - M
        E = 0.5*dot(DX.T, dot(inv(S), DX))
        E = E + 0.5*M.shape[0]*log(2*pi)+0.5*log(det(S))
        P = exp(-E)

    return (P[0], E[0])



from numpy import *
from numpy.linalg import inv

#time step of mobile movement
dt = 0.1

##Initialization of state matrices
X = array([[0.0], [0.0], [0.1], [0.1]])
P = diag((0.01, 0.01, 0.01, 0.01))
A = array([[1, 0, dt, 0], [0, 1, 0, dt], [0, 0, 1, 0], [0, 0, 0, 1]])
'''
The eye tool returns a 2-D array with 1's as the diagonal and 0's elsewhere.
The diagonal can be main, upper, or lower depending on the optional 
parameter k.
'''

Q = eye(X.shape[0])
B = eye(X.shape[0])

'''
The numpy.zeros() function returns a new array of given shape and type,
with zeros.
'''
U = zeros(X.shape[0])

#Measurement matrices
Y = array([[X[0,0] + abs(randn(1)[0])], [X[1,0] + abs(randn(1)[0])]])
print("Y", Y.shape)
H = array([[1, 0, 0, 0], [0, 1, 0, 0]])
print("H", H.shape)
R = eye(Y.shape[0], 1)

#Number of iterations in Kalman Filter
N_iter = 100

#Applying the Kalman Filter
for i in range(0, N_iter):
    (X, P) = kfPredict(X, P, A, Q, B, U)
    (X, P, K, IM, IS, LH) = kfUpdate(X, P, Y, H, R)
    Y = array([[X[0,0] + abs(0.1*randn(1)[0])], [X[1, 0] + abs(0.1*randn(1)[0])]])
    print("Y", Y.shape)


