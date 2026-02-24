---
layout: default
title: Scale-PINN: Learning Efficient Physics-Informed Neural Networks Through Sequential Correction
---

# Scale-PINN: Learning Efficient Physics-Informed Neural Networks Through Sequential Correction
**arXiv**：[2602.19475v1](https://arxiv.org/abs/2602.19475) · [PDF](https://arxiv.org/pdf/2602.19475.pdf)  
**作者**：Pao-Hsiung Chiu, Jian Cheng Wong, Chin Chun Ooi, Chang Wei, Yuchen Fan, Yew-Soon Ong  

**一句话要点**：提出Scale-PINN，通过序列校正算法提升PINN训练效率与精度，应用于流体动力学等领域。

**关键词**：物理信息神经网络, 序列校正算法, 偏微分方程求解, 训练效率优化, 流体动力学应用

## 3 点简述
- PINN训练慢、精度低，限制其在科学与工程中的应用。
- Scale-PINN将数值求解器的残差校正原理融入损失函数，实现范式转变。
- 实验显示，在流体动力学问题中训练时间从小时级降至2分钟内，保持高精度。

## 摘要（原文）

> Physics-informed neural networks (PINNs) have emerged as a promising mesh-free paradigm for solving partial differential equations, yet adoption in science and engineering is limited by slow training and modest accuracy relative to modern numerical solvers. We introduce the Sequential Correction Algorithm for Learning Efficient PINN (Scale-PINN), a learning strategy that bridges modern physics-informed learning with numerical algorithms. Scale-PINN incorporates the iterative residual-correction principle, a cornerstone of numerical solvers, directly into the loss formulation, marking a paradigm shift in how PINN losses can be conceived and constructed. This integration enables Scale-PINN to achieve unprecedented convergence speed across PDE problems from different physics domain, including reducing training time on a challenging fluid-dynamics problem for state-of-the-art PINN from hours to sub-2 minutes while maintaining superior accuracy, and enabling application to representative problems in aerodynamics and urban science. By uniting the rigor of numerical methods with the flexibility of deep learning, Scale-PINN marks a significant leap toward the practical adoption of PINNs in science and engineering through scalable, physics-informed learning. Codes are available at https://github.com/chiuph/SCALE-PINN.

