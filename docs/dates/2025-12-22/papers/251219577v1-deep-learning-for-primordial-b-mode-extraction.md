---
layout: default
title: Deep Learning for Primordial $B$-mode Extraction
---

# Deep Learning for Primordial $B$-mode Extraction
**arXiv**：[2512.19577v1](https://arxiv.org/abs/2512.19577) · [PDF](https://arxiv.org/pdf/2512.19577.pdf)  
**作者**：Eric Guzman, Joel Meyers  

**一句话要点**：提出深度学习网络ResUNet-CMB以估计和移除宇宙微波背景中的次级B模式偏振，优化原初引力波振幅约束

**关键词**：宇宙微波背景, B模式偏振, 深度学习, 引力透镜, 原初引力波, 信号提取

## 3 点简述
- 核心问题：原初引力波B模式信号提取受次级B模式（如引力透镜）污染，导致统计复杂和非高斯性
- 方法要点：应用深度学习网络ResUNet-CMB同时估计和移除多种次级B模式偏振源，提升信号分离精度
- 实验或效果：在似然分析中实现近乎最优、无偏的原初引力波振幅估计，减少透镜B模式混淆

## 摘要（原文）

> The search for primordial gravitational waves is a central goal of cosmic microwave background (CMB) surveys. Isolating the characteristic $B$-mode polarization signal sourced by primordial gravitational waves is challenging for several reasons: the amplitude of the signal is inherently small; astrophysical foregrounds produce $B$-mode polarization contaminating the signal; and secondary $B$-mode polarization fluctuations are produced via the conversion of $E$ modes. Current and future low-noise, multi-frequency observations enable sufficient precision to address the first two of these challenges such that secondary $B$ modes will become the bottleneck for improved constraints on the amplitude of primordial gravitational waves. The dominant source of secondary $B$-mode polarization is gravitational lensing by large scale structure. Various strategies have been developed to estimate the lensing deflection and to reverse its effects the CMB, thus reducing confusion from lensing $B$ modes in the search for primordial gravitational waves. However, a few complications remain. First, there may be additional sources of secondary $B$-mode polarization, for example from patchy reionization or from cosmic polarization rotation. Second, the statistics of delensed CMB maps can become complicated and non-Gaussian, especially when advanced lensing reconstruction techniques are applied. We previously demonstrated how a deep learning network, ResUNet-CMB, can provide nearly optimal simultaneous estimates of multiple sources of secondary $B$-mode polarization. In this paper, we show how deep learning can be applied to estimate and remove multiple sources of secondary $B$-mode polarization, and we further show how this technique can be used in a likelihood analysis to produce nearly optimal, unbiased estimates of the amplitude of primordial gravitational waves.

