---
layout: default
title: Paradoxical noise preference in RNNs
---

# Paradoxical noise preference in RNNs
**arXiv**：[2601.04539v1](https://arxiv.org/abs/2601.04539) · [PDF](https://arxiv.org/pdf/2601.04539.pdf)  
**作者**：Noah Eckstein, Manoj Srinivasan  

**一句话要点**：揭示循环神经网络在非零噪声下性能最优的悖论现象及其机制

**关键词**：循环神经网络, 噪声训练, 固定点偏移, 激活函数非线性, 随机动力学, 性能优化

## 3 点简述
- 核心问题：训练噪声移除后性能下降，与直觉相反，非零噪声时性能最佳
- 方法要点：分析噪声注入位置（激活函数内外）对固定点偏移的影响
- 实验或效果：通过函数逼近、迷宫导航等任务验证噪声依赖的固定点偏移机制

## 摘要（原文）

> In recurrent neural networks (RNNs) used to model biological neural networks, noise is typically introduced during training to emulate biological variability and regularize learning. The expectation is that removing the noise at test time should preserve or improve performance. Contrary to this intuition, we find that continuous-time recurrent neural networks (CTRNNs) often perform best at a nonzero noise level, specifically, the same level used during training. This noise preference typically arises when noise is injected inside the neural activation function; networks trained with noise injected outside the activation function perform best with zero noise. Through analyses of simple function approximation, maze navigation, and single neuron regulator tasks, we show that the phenomenon stems from noise-induced shifts of fixed points (stationary distributions) in the underlying stochastic dynamics of the RNNs. These fixed point shifts are noise-level dependent and bias the network outputs when the noise is removed, degrading performance. Analytical and numerical results show that the bias arises when neural states operate near activation function nonlinearities, where noise is asymmetrically attenuated, and that performance optimization incentivizes operation near these nonlinearities. Thus, networks can overfit to the stochastic training environment itself rather than just to the input-output data. The phenomenon is distinct from stochastic resonance, wherein nonzero noise enhances signal processing. Our findings reveal that training noise can become an integral part of the computation learned by recurrent networks, with implications for understanding neural population dynamics and for the design of robust artificial RNNs.

