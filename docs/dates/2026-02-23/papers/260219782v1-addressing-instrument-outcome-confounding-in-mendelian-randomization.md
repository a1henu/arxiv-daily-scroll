---
layout: default
title: Addressing Instrument-Outcome Confounding in Mendelian Randomization through Representation Learning
---

# Addressing Instrument-Outcome Confounding in Mendelian Randomization through Representation Learning
**arXiv**：[2602.19782v1](https://arxiv.org/abs/2602.19782) · [PDF](https://arxiv.org/pdf/2602.19782.pdf)  
**作者**：Shimeng Huang, Matthew Robinson, Francesco Locatello  

**一句话要点**：提出基于表示学习的框架以解决孟德尔随机化中工具变量与混杂因素混淆的问题

**关键词**：孟德尔随机化, 表示学习, 因果推断, 工具变量, 混杂因素, 多环境数据

## 3 点简述
- 核心问题：孟德尔随机化中工具变量与未观测混杂因素不独立，导致因果效应估计偏差
- 方法要点：利用多环境数据的跨环境不变性，学习恢复遗传工具变量的潜在外生成分
- 实验或效果：通过理论保证、模拟和半合成实验验证了方法的有效性

## 摘要（原文）

> Mendelian Randomization (MR) is a prominent observational epidemiological research method designed to address unobserved confounding when estimating causal effects. However, core assumptions -- particularly the independence between instruments and unobserved confounders -- are often violated due to population stratification or assortative mating. Leveraging the increasing availability of multi-environment data, we propose a representation learning framework that exploits cross-environment invariance to recover latent exogenous components of genetic instruments. We provide theoretical guarantees for identifying these latent instruments under various mixing mechanisms and demonstrate the effectiveness of our approach through simulations and semi-synthetic experiments using data from the All of Us Research Hub.

