---
layout: default
title: Asynchronous Heavy-Tailed Optimization
---

# Asynchronous Heavy-Tailed Optimization
**arXiv**：[2602.18002v1](https://arxiv.org/abs/2602.18002) · [PDF](https://arxiv.org/pdf/2602.18002.pdf)  
**作者**：Junfei Sun, Dixi Yao, Xuchen Gong, Tahseen Rabbani, Manzil Zaheer, Tian Li  

**一句话要点**：提出异步优化算法改进以处理重尾梯度噪声，提升延迟容忍度

**关键词**：重尾梯度噪声, 异步优化, 延迟补偿, 学习率调度, 收敛分析, 深度学习优化

## 3 点简述
- 研究重尾梯度噪声与异步优化的交互，填补现有研究空白
- 基于延迟感知学习率调度和延迟补偿提出算法修改，理论分析收敛性
- 实验在图像和语言任务中优于现有方法，对超参数更鲁棒

## 摘要（原文）

> Heavy-tailed stochastic gradient noise, commonly observed in transformer models, can destabilize the optimization process. Recent works mainly focus on developing and understanding approaches to address heavy-tailed noise in the centralized or distributed, synchronous setting, leaving the interactions between such noise and asynchronous optimization underexplored. In this work, we investigate two communication schemes that handle stragglers with asynchronous updates in the presence of heavy-tailed gradient noise. We propose and theoretically analyze algorithmic modifications based on delay-aware learning rate scheduling and delay compensation to enhance the performance of asynchronous algorithms. Our convergence guarantees under heavy-tailed noise match the rate of the synchronous counterparts and improve delay tolerance compared with existing asynchronous approaches. Empirically, our approaches outperform prior synchronous and asynchronous methods in terms of accuracy/runtime trade-offs and are more robust to hyperparameters in both image and language tasks.

