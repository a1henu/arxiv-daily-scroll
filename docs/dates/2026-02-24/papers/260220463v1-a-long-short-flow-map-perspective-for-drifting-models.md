---
layout: default
title: A Long-Short Flow-Map Perspective for Drifting Models
---

# A Long-Short Flow-Map Perspective for Drifting Models
**arXiv**：[2602.20463v1](https://arxiv.org/abs/2602.20463) · [PDF](https://arxiv.org/pdf/2602.20463.pdf)  
**作者**：Zhiqi Li, Bo Zhu  

**一句话要点**：提出长-短流图分解视角以重新解释漂移模型并优化似然学习

**关键词**：漂移模型, 流图分解, 似然学习, 传输过程, 半群一致性, 特征空间优化

## 3 点简述
- 核心问题：漂移模型的全局传输过程缺乏流图一致性的分解视角
- 方法要点：通过半群一致的长-短流图分解，将传输分解为长时程流图和短时终端流图
- 实验或效果：理论分析和基准测试验证了框架有效性，并解释特征空间优化

## 摘要（原文）

> This paper provides a reinterpretation of the Drifting Model~\cite{deng2026generative} through a semigroup-consistent long-short flow-map factorization. We show that a global transport process can be decomposed into a long-horizon flow map followed by a short-time terminal flow map admitting a closed-form optimal velocity representation, and that taking the terminal interval length to zero recovers exactly the drifting field together with a conservative impulse term required for flow-map consistency. Based on this perspective, we propose a new likelihood learning formulation that aligns the long-short flow-map decomposition with density evolution under transport. We validate the framework through both theoretical analysis and empirical evaluations on benchmark tests, and further provide a theoretical interpretation of the feature-space optimization while highlighting several open problems for future study.

