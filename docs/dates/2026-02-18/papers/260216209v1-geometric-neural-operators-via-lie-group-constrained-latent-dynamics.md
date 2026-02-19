---
layout: default
title: Geometric Neural Operators via Lie Group-Constrained Latent Dynamics
---

# Geometric Neural Operators via Lie Group-Constrained Latent Dynamics
**arXiv**：[2602.16209v1](https://arxiv.org/abs/2602.16209) · [PDF](https://arxiv.org/pdf/2602.16209.pdf)  
**作者**：Jiaquan Zhang, Fachrina Dewi Puspitasari, Songbo Zhang, Yibei Liu, Kuien Liu, Caiyan Qin, Fan Mo, Peng Wang, Yang Yang, Chaoning Zhang  

**一句话要点**：提出基于李群约束的流形约束模块，以提升神经算子在长期预测中的几何保真度。

**关键词**：神经算子, 几何约束, 李群学习, 偏微分方程求解, 长期预测, 流形优化

## 3 点简述
- 现有神经算子在多层迭代和长期推演中不稳定，源于欧几里得潜在空间更新违反几何和守恒定律。
- 通过低秩李代数参数化约束流形，在潜在表示上执行群作用更新，作为即插即用模块增强几何归纳偏置。
- 在多种偏微分方程上实验，相对预测误差降低30-50%，参数仅增加2.26%，提升长期预测可扩展性。

## 摘要（原文）

> Neural operators offer an effective framework for learning solutions of partial differential equations for many physical systems in a resolution-invariant and data-driven manner. Existing neural operators, however, often suffer from instability in multi-layer iteration and long-horizon rollout, which stems from the unconstrained Euclidean latent space updates that violate the geometric and conservation laws. To address this challenge, we propose to constrain manifolds with low-rank Lie algebra parameterization that performs group action updates on the latent representation. Our method, termed Manifold Constraining based on Lie group (MCL), acts as an efficient \emph{plug-and-play} module that enforces geometric inductive bias to existing neural operators. Extensive experiments on various partial differential equations, such as 1-D Burgers and 2-D Navier-Stokes, over a wide range of parameters and steps demonstrate that our method effectively lowers the relative prediction error by 30-50\% at the cost of 2.26\% of parameter increase. The results show that our approach provides a scalable solution for improving long-term prediction fidelity by addressing the principled geometric constraints absent in the neural operator updates.

