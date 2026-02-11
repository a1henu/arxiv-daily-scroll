---
layout: default
title: Tracking Finite-Time Lyapunov Exponents to Robustify Neural ODEs
---

# Tracking Finite-Time Lyapunov Exponents to Robustify Neural ODEs
**arXiv**：[2602.09613v1](https://arxiv.org/abs/2602.09613) · [PDF](https://arxiv.org/pdf/2602.09613.pdf)  
**作者**：Tobias Wöhrer, Christian Kuehn  

**一句话要点**：提出基于有限时间李雅普诺夫指数的正则化训练算法，以增强神经ODE的对抗鲁棒性

**关键词**：神经ODE, 有限时间李雅普诺夫指数, 对抗鲁棒性, 正则化训练, 输入动态分析

## 3 点简述
- 研究神经ODE中有限时间李雅普诺夫指数，揭示其与对抗脆弱性的直接联系
- 提出抑制早期输入动态中远离零的指数，通过正则化提升模型鲁棒性
- 相比全区间正则化，该方法减少计算成本，避免完整双重反向传播

## 摘要（原文）

> We investigate finite-time Lyapunov exponents (FTLEs), a measure for exponential separation of input perturbations, of deep neural networks within the framework of continuous-depth neural ODEs. We demonstrate that FTLEs are powerful organizers for input-output dynamics, allowing for better interpretability and the comparison of distinct model architectures. We establish a direct connection between Lyapunov exponents and adversarial vulnerability, and propose a novel training algorithm that improves robustness by FTLE regularization. The key idea is to suppress exponents far from zero in the early stage of the input dynamics. This approach enhances robustness and reduces computational cost compared to full-interval regularization, as it avoids a full ``double'' backpropagation.

