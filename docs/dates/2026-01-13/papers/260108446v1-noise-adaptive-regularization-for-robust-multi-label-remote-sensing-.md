---
layout: default
title: Noise-Adaptive Regularization for Robust Multi-Label Remote Sensing Image Classification
---

# Noise-Adaptive Regularization for Robust Multi-Label Remote Sensing Image Classification
**arXiv**：[2601.08446v1](https://arxiv.org/abs/2601.08446) · [PDF](https://arxiv.org/pdf/2601.08446.pdf)  
**作者**：Tom Burgert, Julia Henkel, Begüm Demir  

**一句话要点**：提出噪声自适应正则化方法NAR，以解决遥感多标签分类中的标注噪声问题。

**关键词**：遥感多标签分类, 标注噪声, 噪声自适应正则化, 半监督学习, 早期学习正则化, 鲁棒学习

## 3 点简述
- 核心问题：遥感多标签分类中，成本效益标注策略常引入加性、减性或混合噪声，现有方法缺乏对不同噪声类型的自适应处理。
- 方法要点：NAR在半监督学习框架下，基于置信度动态处理标签，结合早期学习正则化稳定训练，自适应抑制噪声监督。
- 实验或效果：在加性、减性和混合噪声场景下，NAR相比现有方法提升鲁棒性，尤其在减性和混合噪声中效果显著。

## 摘要（原文）

> The development of reliable methods for multi-label classification (MLC) has become a prominent research direction in remote sensing (RS). As the scale of RS data continues to expand, annotation procedures increasingly rely on thematic products or crowdsourced procedures to reduce the cost of manual annotation. While cost-effective, these strategies often introduce multi-label noise in the form of partially incorrect annotations. In MLC, label noise arises as additive noise, subtractive noise, or a combination of both in the form of mixed noise. Previous work has largely overlooked this distinction and commonly treats noisy annotations as supervised signals, lacking mechanisms that explicitly adapt learning behavior to different noise types. To address this limitation, we propose NAR, a noise-adaptive regularization method that explicitly distinguishes between additive and subtractive noise within a semi-supervised learning framework. NAR employs a confidence-based label handling mechanism that dynamically retains label entries with high confidence, temporarily deactivates entries with moderate confidence, and corrects low confidence entries via flipping. This selective attenuation of supervision is integrated with early-learning regularization (ELR) to stabilize training and mitigate overfitting to corrupted labels. Experiments across additive, subtractive, and mixed noise scenarios demonstrate that NAR consistently improves robustness compared with existing methods. Performance improvements are most pronounced under subtractive and mixed noise, indicating that adaptive suppression and selective correction of noisy supervision provide an effective strategy for noise robust learning in RS MLC.

