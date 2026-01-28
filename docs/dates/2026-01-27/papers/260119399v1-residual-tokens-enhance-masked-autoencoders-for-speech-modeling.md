---
layout: default
title: Residual Tokens Enhance Masked Autoencoders for Speech Modeling
---

# Residual Tokens Enhance Masked Autoencoders for Speech Modeling
**arXiv**：[2601.19399v1](https://arxiv.org/abs/2601.19399) · [PDF](https://arxiv.org/pdf/2601.19399.pdf)  
**作者**：Samir Sadok, Stéphane Lathuilière, Xavier Alameda-Pineda  

**一句话要点**：提出RT-MAE，通过残差可训练令牌增强掩码自编码器，以解决语音建模中显式属性无法捕捉全部信息的问题。

**关键词**：语音建模, 掩码自编码器, 残差学习, 语音增强, 无监督学习

## 3 点简述
- 核心问题：现有语音建模依赖显式属性（如音高、内容），但无法完全捕捉自然语音的丰富性。
- 方法要点：引入RT-MAE，结合监督属性建模与无监督残差可训练令牌，编码未由显式标签因素解释的信息。
- 实验或效果：RT-MAE提升重建质量，保持内容和说话人相似性，增强表达力，并适用于语音增强任务。

## 摘要（原文）

> Recent speech modeling relies on explicit attributes such as pitch, content, and speaker identity, but these alone cannot capture the full richness of natural speech. We introduce RT-MAE, a novel masked autoencoder framework that augments the supervised attributes-based modeling with unsupervised residual trainable tokens, designed to encode the information not explained by explicit labeled factors (e.g., timbre variations, noise, emotion etc). Experiments show that RT-MAE improves reconstruction quality, preserving content and speaker similarity while enhancing expressivity. We further demonstrate its applicability to speech enhancement, removing noise at inference while maintaining controllability and naturalness.

