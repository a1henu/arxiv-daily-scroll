---
layout: default
title: Learnability Window in Gated Recurrent Neural Networks
---

# Learnability Window in Gated Recurrent Neural Networks
**arXiv**：[2512.05790v1](https://arxiv.org/abs/2512.05790) · [PDF](https://arxiv.org/pdf/2512.05790.pdf)  
**作者**：Lorenzo Livi  

**一句话要点**：提出门控循环神经网络中可学习性窗口的理论框架，解释门控机制如何影响长期依赖学习。

**关键词**：门控循环神经网络, 可学习性窗口, 梯度传输, 有效学习率, 重尾噪声, 样本复杂度

## 3 点简述
- 核心问题：门控机制如何决定循环神经网络的可学习性窗口，即梯度信息可统计恢复的最大时间范围。
- 方法要点：通过一阶展开定义有效学习率，作为梯度传输的乘性滤波器，控制梯度幅度和各向异性。
- 实验或效果：在重尾梯度噪声下，推导样本复杂度公式，预测门控谱和噪声对可学习性窗口的影响。

## 摘要（原文）

> We develop a theoretical framework that explains how gating mechanisms determine the learnability window $\mathcal{H}_N$ of recurrent neural networks, defined as the largest temporal horizon over which gradient information remains statistically recoverable. While classical analyses emphasize numerical stability of Jacobian products, we show that stability alone is insufficient: learnability is governed instead by the \emph{effective learning rates} $μ_{t,\ell}$, per-lag and per-neuron quantities obtained from first-order expansions of gate-induced Jacobian products in Backpropagation Through Time. These effective learning rates act as multiplicative filters that control both the magnitude and anisotropy of gradient transport. Under heavy-tailed ($α$-stable) gradient noise, we prove that the minimal sample size required to detect a dependency at lag~$\ell$ satisfies $N(\ell)\propto f(\ell)^{-α}$, where $f(\ell)=\\|μ_{t,\ell}\\|_1$ is the effective learning rate envelope. This leads to an explicit formula for $\mathcal{H}_N$ and closed-form scaling laws for logarithmic, polynomial, and exponential decay of $f(\ell)$. The theory predicts that broader or more heterogeneous gate spectra produce slower decay of $f(\ell)$ and hence larger learnability windows, whereas heavier-tailed noise compresses $\mathcal{H}_N$ by slowing statistical concentration. By linking gate-induced time-scale structure, gradient noise, and sample complexity, the framework identifies the effective learning rates as the fundamental quantities that govern when -- and for how long -- gated recurrent networks can learn long-range temporal dependencies.

