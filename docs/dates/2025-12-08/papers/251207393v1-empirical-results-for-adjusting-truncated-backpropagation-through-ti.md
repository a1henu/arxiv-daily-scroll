---
layout: default
title: Empirical Results for Adjusting Truncated Backpropagation Through Time while Training Neural Audio Effects
---

# Empirical Results for Adjusting Truncated Backpropagation Through Time while Training Neural Audio Effects
**arXiv**：[2512.07393v1](https://arxiv.org/abs/2512.07393) · [PDF](https://arxiv.org/pdf/2512.07393.pdf)  
**作者**：Yann Bourdin, Pierrick Legrand, Fanny Roche  

**一句话要点**：优化截断时间反向传播以提升神经音频效果建模性能

**关键词**：截断时间反向传播, 神经音频效果, 动态范围压缩, 超参数优化, 卷积-循环网络, 音频建模

## 3 点简述
- 研究截断时间反向传播在神经音频效果训练中的优化问题，聚焦动态范围压缩场景
- 评估序列数、批次大小和序列长度等超参数对模型性能的影响，采用卷积-循环架构
- 实验表明调优参数可提高准确性和训练稳定性，同时降低计算成本，客观和主观评估均验证改进

## 摘要（原文）

> This paper investigates the optimization of Truncated Backpropagation Through Time (TBPTT) for training neural networks in digital audio effect modeling, with a focus on dynamic range compression. The study evaluates key TBPTT hyperparameters -- sequence number, batch size, and sequence length -- and their influence on model performance. Using a convolutional-recurrent architecture, we conduct extensive experiments across datasets with and without conditionning by user controls. Results demonstrate that carefully tuning these parameters enhances model accuracy and training stability, while also reducing computational demands. Objective evaluations confirm improved performance with optimized settings, while subjective listening tests indicate that the revised TBPTT configuration maintains high perceptual quality.

