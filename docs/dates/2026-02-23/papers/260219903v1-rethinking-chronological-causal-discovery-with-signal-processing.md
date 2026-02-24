---
layout: default
title: Rethinking Chronological Causal Discovery with Signal Processing
---

# Rethinking Chronological Causal Discovery with Signal Processing
**arXiv**：[2602.19903v1](https://arxiv.org/abs/2602.19903) · [PDF](https://arxiv.org/pdf/2602.19903.pdf)  
**作者**：Kurt Butler, Damian Machlanski, Panagiotis Dimitrakopoulos, Sotirios A. Tsaftaris  

**一句话要点**：分析采样率与窗口长度对因果发现方法性能的影响

**关键词**：因果发现, 信号处理, 采样率, 窗口长度, 时间序列分析

## 3 点简述
- 核心问题：观测记录时间与真实事件时间不匹配影响因果发现准确性
- 方法要点：结合信号处理理论，评估经典与近期方法对超参数的敏感性
- 实验或效果：通过实证与理论证据，展示方法性能随采样率和窗口长度变化

## 摘要（原文）

> Causal discovery problems use a set of observations to deduce causality between variables in the real world, typically to answer questions about biological or physical systems. These observations are often recorded at regular time intervals, determined by a user or a machine, depending on the experiment design. There is generally no guarantee that the timing of these recordings matches the timing of the underlying biological or physical events. In this paper, we examine the sensitivity of causal discovery methods to this potential mismatch. We consider empirical and theoretical evidence to understand how causal discovery performance is impacted by changes of sampling rate and window length. We demonstrate that both classical and recent causal discovery methods exhibit sensitivity to these hyperparameters, and we discuss how ideas from signal processing may help us understand these phenomena.

