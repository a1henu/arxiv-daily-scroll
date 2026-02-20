---
layout: default
title: Learning with Boolean threshold functions
---

# Learning with Boolean threshold functions
**arXiv**：[2602.17493v1](https://arxiv.org/abs/2602.17493) · [PDF](https://arxiv.org/pdf/2602.17493.pdf)  
**作者**：Veit Elser, Manish Krishan Lal  

**一句话要点**：提出基于布尔阈值函数和约束满足的神经网络训练方法，用于处理布尔数据并提升可解释性。

**关键词**：布尔神经网络, 约束满足学习, 投影算法, 可解释性, 离散系统训练

## 3 点简述
- 核心问题：标准梯度方法在布尔数据上训练神经网络时面临困难，难以获得精确解或强泛化。
- 方法要点：采用非凸约束公式，通过布尔阈值函数和反射-反射-松弛投影算法实现分治-并发分解训练。
- 实验或效果：在乘法电路发现、二进制自编码等任务中实现精确解或强泛化，优于梯度方法。

## 摘要（原文）

> We develop a method for training neural networks on Boolean data in which the values at all nodes are strictly $\pm 1$, and the resulting models are typically equivalent to networks whose nonzero weights are also $\pm 1$. The method replaces loss minimization with a nonconvex constraint formulation. Each node implements a Boolean threshold function (BTF), and training is expressed through a divide-and-concur decomposition into two complementary constraints: one enforces local BTF consistency between inputs, weights, and output; the other imposes architectural concurrence, equating neuron outputs with downstream inputs and enforcing weight equality across training-data instantiations of the network. The reflect-reflect-relax (RRR) projection algorithm is used to reconcile these constraints.
>   Each BTF constraint includes a lower bound on the margin. When this bound is sufficiently large, the learned representations are provably sparse and equivalent to networks composed of simple logical gates with $\pm 1$ weights. Across a range of tasks -- including multiplier-circuit discovery, binary autoencoding, logic-network inference, and cellular automata learning -- the method achieves exact solutions or strong generalization in regimes where standard gradient-based methods struggle. These results demonstrate that projection-based constraint satisfaction provides a viable and conceptually distinct foundation for learning in discrete neural systems, with implications for interpretability and efficient inference.

