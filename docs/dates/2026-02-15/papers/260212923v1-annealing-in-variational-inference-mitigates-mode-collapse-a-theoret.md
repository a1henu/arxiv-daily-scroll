---
layout: default
title: Annealing in variational inference mitigates mode collapse: A theoretical study on Gaussian mixtures
---

# Annealing in variational inference mitigates mode collapse: A theoretical study on Gaussian mixtures
**arXiv**：[2602.12923v1](https://arxiv.org/abs/2602.12923) · [PDF](https://arxiv.org/pdf/2602.12923.pdf)  
**作者**：Luigi Fogliani, Bruno Loureiro, Marylou Gabrié  

**一句话要点**：提出退火策略以解决高斯混合模型中的模态崩溃问题

**关键词**：变分推断, 模态崩溃, 高斯混合模型, 退火策略, RealNVP流模型, 理论分析

## 3 点简述
- 核心问题：变分推断中模态崩溃导致多模态分布学习失败
- 方法要点：基于低维统计量分析退火初始温度与速率的相互作用
- 实验或效果：理论分析显示退火可预防模态崩溃，数值实验扩展至RealNVP流模型

## 摘要（原文）

> Mode collapse, the failure to capture one or more modes when targetting a multimodal distribution, is a central challenge in modern variational inference. In this work, we provide a mathematical analysis of annealing based strategies for mitigating mode collapse in a tractable setting: learning a Gaussian mixture, where mode collapse is known to arise. Leveraging a low dimensional summary statistics description, we precisely characterize the interplay between the initial temperature and the annealing rate, and derive a sharp formula for the probability of mode collapse. Our analysis shows that an appropriately chosen annealing scheme can robustly prevent mode collapse. Finally, we present numerical evidence that these theoretical tradeoffs qualitatively extend to neural network based models, RealNVP normalizing flows, providing guidance for designing annealing strategies mitigating mode collapse in practical variational inference pipelines.

