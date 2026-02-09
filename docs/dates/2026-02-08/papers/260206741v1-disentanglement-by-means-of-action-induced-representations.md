---
layout: default
title: Disentanglement by means of action-induced representations
---

# Disentanglement by means of action-induced representations
**arXiv**：[2602.06741v1](https://arxiv.org/abs/2602.06741) · [PDF](https://arxiv.org/pdf/2602.06741.pdf)  
**作者**：Gorka Muñoz-Gil, Hendrik Poulsen Nautrup, Arunava Majumder, Paulin de Schoulepnikoff, Florian Fürrutter, Marius Krumm, Hans J. Briegel  

**一句话要点**：提出动作诱导表示框架以在物理系统中实现可证明的解耦表示学习

**关键词**：解耦表示学习, 变分自编码器, 动作诱导表示, 物理系统建模, 非线性独立成分分析

## 3 点简述
- 核心问题：变分自编码器难以实现非线性独立成分分析，导致解耦表示学习困难
- 方法要点：引入动作诱导表示框架，通过建模物理系统的实验或动作来定义表示
- 实验或效果：提出变分动作诱导表示架构，在标准变分自编码器失败处实现可证明的解耦

## 摘要（原文）

> Learning interpretable representations with variational autoencoders (VAEs) is a major goal of representation learning. The main challenge lies in obtaining disentangled representations, where each latent dimension corresponds to a distinct generative factor. This difficulty is fundamentally tied to the inability to perform nonlinear independent component analysis. Here, we introduce the framework of action-induced representations (AIRs) which models representations of physical systems given experiments (or actions) that can be performed on them. We show that, in this framework, we can provably disentangle degrees of freedom w.r.t. their action dependence. We further introduce a variational AIR architecture (VAIR) that can extract AIRs and therefore achieve provable disentanglement where standard VAEs fail. Beyond state representation, VAIR also captures the action dependence of the underlying generative factors, directly linking experiments to the degrees of freedom they influence.

