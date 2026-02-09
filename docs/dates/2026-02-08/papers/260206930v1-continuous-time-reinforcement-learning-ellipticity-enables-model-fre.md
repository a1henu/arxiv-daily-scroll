---
layout: default
title: Continuous-time reinforcement learning: ellipticity enables model-free value function approximation
---

# Continuous-time reinforcement learning: ellipticity enables model-free value function approximation
**arXiv**：[2602.06930v1](https://arxiv.org/abs/2602.06930) · [PDF](https://arxiv.org/pdf/2602.06930.pdf)  
**作者**：Wenlong Mou  

**一句话要点**：提出Sobolev-prox fitted q-learning算法，利用椭圆性实现连续时间扩散过程的模型无关值函数近似

**关键词**：连续时间强化学习, 模型无关学习, 椭圆扩散, 值函数近似, Sobolev空间, 离策略学习

## 3 点简述
- 研究离散观测与动作下连续时间马尔可夫扩散过程的离策略强化学习，避免对动态结构的不切实际假设
- 基于扩散的椭圆性，建立贝尔曼算子的希尔伯特空间正定性与有界性，提出迭代最小二乘回归算法
- 推导估计误差的oracle不等式，显示椭圆性使函数近似强化学习难度不高于监督学习

## 摘要（原文）

> We study off-policy reinforcement learning for controlling continuous-time Markov diffusion processes with discrete-time observations and actions. We consider model-free algorithms with function approximation that learn value and advantage functions directly from data, without unrealistic structural assumptions on the dynamics.
>   Leveraging the ellipticity of the diffusions, we establish a new class of Hilbert-space positive definiteness and boundedness properties for the Bellman operators. Based on these properties, we propose the Sobolev-prox fitted $q$-learning algorithm, which learns value and advantage functions by iteratively solving least-squares regression problems. We derive oracle inequalities for the estimation error, governed by (i) the best approximation error of the function classes, (ii) their localized complexity, (iii) exponentially decaying optimization error, and (iv) numerical discretization error. These results identify ellipticity as a key structural property that renders reinforcement learning with function approximation for Markov diffusions no harder than supervised learning.

