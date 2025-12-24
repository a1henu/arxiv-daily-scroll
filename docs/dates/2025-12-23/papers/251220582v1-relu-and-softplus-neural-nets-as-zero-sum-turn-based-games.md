---
layout: default
title: Relu and softplus neural nets as zero-sum turn-based games
---

# Relu and softplus neural nets as zero-sum turn-based games
**arXiv**：[2512.20582v1](https://arxiv.org/abs/2512.20582) · [PDF](https://arxiv.org/pdf/2512.20582.pdf)  
**作者**：Stephane Gaubert, Yiannis Vlassopoulos  

**一句话要点**：提出ReLU和Softplus神经网络的零和回合制博弈解释，用于输出分析和训练

**关键词**：神经网络解释, 博弈论, ReLU激活, Softplus激活, 路径积分, 鲁棒性验证

## 3 点简述
- 核心问题：将神经网络输出解释为博弈值，建立网络与游戏理论间的联系
- 方法要点：通过Shapley-Bellman递归和路径积分公式，推导输出表示和鲁棒性验证
- 实验或效果：未知，但理论框架支持输出边界推导和逆博弈训练

## 摘要（原文）

> We show that the output of a ReLU neural network can be interpreted as the value of a zero-sum, turn-based, stopping game, which we call the ReLU net game. The game runs in the direction opposite to that of the network, and the input of the network serves as the terminal reward of the game. In fact, evaluating the network is the same as running the Shapley-Bellman backward recursion for the value of the game. Using the expression of the value of the game as an expected total payoff with respect to the path measure induced by the transition probabilities and a pair of optimal policies, we derive a discrete Feynman-Kac-type path-integral formula for the network output. This game-theoretic representation can be used to derive bounds on the output from bounds on the input, leveraging the monotonicity of Shapley operators, and to verify robustness properties using policies as certificates. Moreover, training the neural network becomes an inverse game problem: given pairs of terminal rewards and corresponding values, one seeks transition probabilities and rewards of a game that reproduces them. Finally, we show that a similar approach applies to neural networks with Softplus activation functions, where the ReLU net game is replaced by its entropic regularization.

