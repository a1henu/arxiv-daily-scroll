---
layout: default
title: GAVINA: flexible aggressive undervolting for bit-serial mixed-precision DNN acceleration
---

# GAVINA: flexible aggressive undervolting for bit-serial mixed-precision DNN acceleration
**arXiv**：[2511.23203v1](https://arxiv.org/abs/2511.23203) · [PDF](https://arxiv.org/pdf/2511.23203.pdf)  
**作者**：Jordi Fornt, Pau Fontova-Musté, Adrian Gras, Omar Lahyani, Martí Caro, Jaume Abella, Francesc Moll, Josep Altet  

**一句话要点**：提出GAVINA架构，结合欠压与位串行计算，实现高效混合精度DNN加速。

**关键词**：欠压技术, 位串行计算, 混合精度加速, DNN加速器, 能效优化

## 3 点简述
- 问题：欠压技术误差率高，现有8位加速器难与低精度架构竞争。
- 方法：GAV技术选择性欠压最低有效位组合，支持灵活混合精度。
- 效果：GAVINA能效达89 TOP/sW，ResNet-18上精度损失可忽略。

## 摘要（原文）

> Voltage overscaling, or undervolting, is an enticing approximate technique in the context of energy-efficient Deep Neural Network (DNN) acceleration, given the quadratic relationship between power and voltage. Nevertheless, its very high error rate has thwarted its general adoption. Moreover, recent undervolting accelerators rely on 8-bit arithmetic and cannot compete with state-of-the-art low-precision (<8b) architectures. To overcome these issues, we propose a new technique called Guarded Aggressive underVolting (GAV), which combines the ideas of undervolting and bit-serial computation to create a flexible approximation method based on aggressively lowering the supply voltage on a select number of least significant bit combinations. Based on this idea, we implement GAVINA (GAV mIxed-precisioN Accelerator), a novel architecture that supports arbitrary mixed precision and flexible undervolting, with an energy efficiency of up to 89 TOP/sW in its most aggressive configuration. By developing an error model of GAVINA, we show that GAV can achieve an energy efficiency boost of 20% via undervolting, with negligible accuracy degradation on ResNet-18.

