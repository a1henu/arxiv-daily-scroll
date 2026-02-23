---
layout: default
title: Leakage and Second-Order Dynamics Improve Hippocampal RNN Replay
---

# Leakage and Second-Order Dynamics Improve Hippocampal RNN Replay
**arXiv**：[2602.18401v1](https://arxiv.org/abs/2602.18401) · [PDF](https://arxiv.org/pdf/2602.18401.pdf)  
**作者**：Josue Casco-Rodriguez, Nanda H. Krishna, Richard G. Baraniuk  

**一句话要点**：提出泄漏与二阶动力学改进海马RNN重放，通过隐藏状态动量和适应平衡探索与速度。

**关键词**：海马重放, 噪声循环神经网络, 路径积分, 朗之万采样, 隐藏状态动力学, 时间压缩

## 3 点简述
- 研究海马生物神经网络重放，分析噪声RNN作为采样模型，揭示梯度估计困难。
- 证明隐藏状态泄漏和适应促进重放探索，但适应导致非马尔可夫采样减慢速度。
- 提出隐藏状态动量模型实现时间压缩重放，结合适应在路径积分实验中验证效果。

## 摘要（原文）

> Biological neural networks (like the hippocampus) can internally generate "replay" resembling stimulus-driven activity. Recent computational models of replay use noisy recurrent neural networks (RNNs) trained to path-integrate. Replay in these networks has been described as Langevin sampling, but new modifiers of noisy RNN replay have surpassed this description. We re-examine noisy RNN replay as sampling to understand or improve it in three ways: (1) Under simple assumptions, we prove that the gradients replay activity should follow are time-varying and difficult to estimate, but readily motivate the use of hidden state leakage in RNNs for replay. (2) We confirm that hidden state adaptation (negative feedback) encourages exploration in replay, but show that it incurs non-Markov sampling that also slows replay. (3) We propose the first model of temporally compressed replay in noisy path-integrating RNNs through hidden state momentum, connect it to underdamped Langevin sampling, and show that, together with adaptation, it counters slowness while maintaining exploration. We verify our findings via path-integration of 2D triangular and T-maze paths and of high-dimensional paths of synthetic rat place cell activity.

