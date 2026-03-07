---
layout: default
title: MCEL: Margin-Based Cross-Entropy Loss for Error-Tolerant Quantized Neural Networks
---

# MCEL: Margin-Based Cross-Entropy Loss for Error-Tolerant Quantized Neural Networks
**arXiv**：[2603.05048v1](https://arxiv.org/abs/2603.05048) · [PDF](https://arxiv.org/pdf/2603.05048.pdf)  
**作者**：Mikail Yayla, Akash Kumar  

**一句话要点**：提出基于边界的交叉熵损失函数以提升量化神经网络在近似计算平台上的容错能力

**关键词**：量化神经网络, 比特错误容错, 边界损失函数, 近似计算, 内存技术, 交叉熵损失

## 3 点简述
- 量化神经网络在近似计算平台和易错内存技术中面临比特错误容错性不足的问题
- 通过建立比特错误容错性与输出层分类边界的直接联系，设计了显式促进对数级别边界分离的损失函数
- 实验表明该方法在多种数据集和架构上显著提升容错性，最高在1%错误率下提升15%准确率

## 摘要（原文）

> Robustness to bit errors is a key requirement for the reliable use of neural networks (NNs) on emerging approximate computing platforms and error-prone memory technologies. A common approach to achieve bit error tolerance in NNs is injecting bit flips during training according to a predefined error model. While effective in certain scenarios, training-time bit flip injection introduces substantial computational overhead, often degrades inference accuracy at high error rates, and scales poorly for larger NN architectures. These limitations make error injection an increasingly impractical solution for ensuring robustness on future approximate computing platforms and error-prone memory technologies. In this work, we investigate the mechanisms that enable NNs to tolerate bit errors without relying on error-aware training. We establish a direct connection between bit error tolerance and classification margins at the output layer. Building on this insight, we propose a novel loss function, the Margin Cross-Entropy Loss (MCEL), which explicitly promotes logit-level margin separation while preserving the favorable optimization properties of the standard cross-entropy loss. Furthermore, MCEL introduces an interpretable margin parameter that allows robustness to be tuned in a principled manner. Extensive experimental evaluations across multiple datasets of varying complexity, diverse NN architectures, and a range of quantization schemes demonstrate that MCEL substantially improves bit error tolerance, up to 15 % in accuracy for an error rate of 1 %. Our proposed MCEL method is simple to implement, efficient, and can be integrated as a drop-in replacement for standard CEL. It provides a scalable and principled alternative to training-time bit flip injection, offering new insights into the origins of NN robustness and enabling more efficient deployment on approximate computing and memory systems.

