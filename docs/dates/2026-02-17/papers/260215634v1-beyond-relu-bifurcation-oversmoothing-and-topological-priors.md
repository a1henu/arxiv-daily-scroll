---
layout: default
title: Beyond ReLU: Bifurcation, Oversmoothing, and Topological Priors
---

# Beyond ReLU: Bifurcation, Oversmoothing, and Topological Priors
**arXiv**：[2602.15634v1](https://arxiv.org/abs/2602.15634) · [PDF](https://arxiv.org/pdf/2602.15634.pdf)  
**作者**：Erkan Turan, Gaspard Abel, Maysam Behmanesh, Emery Pierson, Maks Ovsjanikov  

**一句话要点**：提出非单调激活函数以解决图神经网络过平滑问题

**关键词**：图神经网络, 过平滑问题, 分岔理论, 激活函数, 拓扑先验

## 3 点简述
- 从分岔理论视角分析图神经网络过平滑现象
- 理论证明非单调激活函数可破坏均匀稳定态
- 实验验证模式振幅缩放定律及初始化方法

## 摘要（原文）

> Graph Neural Networks (GNNs) learn node representations through iterative network-based message-passing. While powerful, deep GNNs suffer from oversmoothing, where node features converge to a homogeneous, non-informative state. We re-frame this problem of representational collapse from a \emph{bifurcation theory} perspective, characterizing oversmoothing as convergence to a stable ``homogeneous fixed point.'' Our central contribution is the theoretical discovery that this undesired stability can be broken by replacing standard monotone activations (e.g., ReLU) with a class of functions. Using Lyapunov-Schmidt reduction, we analytically prove that this substitution induces a bifurcation that destabilizes the homogeneous state and creates a new pair of stable, non-homogeneous \emph{patterns} that provably resist oversmoothing. Our theory predicts a precise, nontrivial scaling law for the amplitude of these emergent patterns, which we quantitatively validate in experiments. Finally, we demonstrate the practical utility of our theory by deriving a closed-form, bifurcation-aware initialization and showing its utility in real benchmark experiments.

