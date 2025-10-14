---
layout: default
title: Investigating Identity Signals in Conversational Facial Dynamics via Disentangled Expression Features
---

# Investigating Identity Signals in Conversational Facial Dynamics via Disentangled Expression Features
**arXiv**：[2510.11223v1](https://arxiv.org/abs/2510.11223) · [PDF](https://arxiv.org/pdf/2510.11223.pdf)  
**作者**：Masoumeh Chapariniya, Pierre Vuillecard, Jean-Marc Odobez, Volker Dellwo, Teodora Vukovic  

**一句话要点**：提出基于解耦表达特征的动态面部识别方法，在自然对话中验证身份信号。

**关键词**：面部动态识别, 表达特征解耦, 对比学习, 身份信号分析, 3D形态模型

## 3 点简述
- 研究问题：个体能否仅通过面部表情动态成分识别，独立于静态外观。
- 方法要点：使用FLAME模型解耦面部形状与表达动态，提取表达和下颌系数。
- 实验效果：在CANDOR数据集上，模型准确率达61.14%，远高于随机水平。

## 摘要（原文）

> This work investigates whether individuals can be identified solely through
> the pure dynamical components of their facial expressions, independent of
> static facial appearance. We leverage the FLAME 3D morphable model to achieve
> explicit disentanglement between facial shape and expression dynamics,
> extracting frame-by-frame parameters from conversational videos while retaining
> only expression and jaw coefficients. On the CANDOR dataset of 1,429 speakers
> in naturalistic conversations, our Conformer model with supervised contrastive
> learning achieves 61.14\%accuracy on 1,429-way classification -- 458 times
> above chance -- demonstrating that facial dynamics carry strong identity
> signatures. We introduce a drift-to-noise ratio (DNR) that quantifies the
> reliability of shape expression separation by measuring across-session shape
> changes relative to within-session variability. DNR strongly negatively
> correlates with recognition performance, confirming that unstable shape
> estimation compromises dynamic identification. Our findings reveal
> person-specific signatures in conversational facial dynamics, with implications
> for social perception and clinical assessment.

