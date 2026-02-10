---
layout: default
title: Constructive conditional normalizing flows
---

# Constructive conditional normalizing flows
**arXiv**：[2602.08606v1](https://arxiv.org/abs/2602.08606) · [PDF](https://arxiv.org/pdf/2602.08606.pdf)  
**作者**：Borjan Geshkovski, Domènec Ruiz-Balet  

**一句话要点**：提出基于连续性方程流的构造性条件归一化流，用于近似微分同胚及其推前测度。

**关键词**：条件采样, 归一化流, 连续性方程, 微分同胚, 神经网络构造, 概率方法

## 3 点简述
- 研究条件采样中近似微分同胚及其推前测度的问题。
- 通过感知器神经网络构建连续性方程流，基于拉格朗日插值的极分解实现构造。
- 对更规则映射提供概率构造，权重不连续数不随维度反比缩放。

## 摘要（原文）

> Motivated by applications in conditional sampling, given a probability measure $μ$ and a diffeomorphism $φ$, we consider the problem of simultaneously approximating $φ$ and the pushforward $φ_{\#}μ$ by means of the flow of a continuity equation whose velocity field is a perceptron neural network with piecewise constant weights. We provide an explicit construction based on a polar-like decomposition of the Lagrange interpolant of $φ$. The latter involves a compressible component, given by the gradient of a particular convex function, which can be realized exactly, and an incompressible component, which -- after approximating via permutations -- can be implemented through shear flows intrinsic to the continuity equation. For more regular maps $φ$ -- such as the Knöthe-Rosenblatt rearrangement -- we provide an alternative, probabilistic construction inspired by the Maurey empirical method, in which the number of discontinuities in the weights doesn't scale inversely with the ambient dimension.

