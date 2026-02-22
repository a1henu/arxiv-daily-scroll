---
layout: default
title: Patch-Based Spatial Authorship Attribution in Human-Robot Collaborative Paintings
---

# Patch-Based Spatial Authorship Attribution in Human-Robot Collaborative Paintings
**arXiv**：[2602.17030v1](https://arxiv.org/abs/2602.17030) · [PDF](https://arxiv.org/pdf/2602.17030.pdf)  
**作者**：Eric Chen, Patricia Alves-Oliveira  

**一句话要点**：提出基于图像块的框架，用于人机协作绘画中的空间作者归属分析。

**关键词**：空间作者归属, 人机协作绘画, 图像块分类, 条件香农熵, 创意AI, 法证分析

## 3 点简述
- 核心问题：在AI参与创意生产时，如何准确记录人机协作绘画中的作者归属。
- 方法要点：使用商品平板扫描仪和留一交叉验证，通过图像块分类实现空间作者归属。
- 实验或效果：在15幅抽象画上达到88.8%的图像块级准确率，并量化风格重叠以处理模糊区域。

## 摘要（原文）

> As agentic AI becomes increasingly involved in creative production, documenting authorship has become critical for artists, collectors, and legal contexts. We present a patch-based framework for spatial authorship attribution within human-robot collaborative painting practice, demonstrated through a forensic case study of one human artist and one robotic system across 15 abstract paintings. Using commodity flatbed scanners and leave-one-painting-out cross-validation, the approach achieves 88.8% patch-level accuracy (86.7% painting-level via majority vote), outperforming texture-based and pretrained-feature baselines (68.0%-84.7%). For collaborative artworks, where ground truth is inherently ambiguous, we use conditional Shannon entropy to quantify stylistic overlap; manually annotated hybrid regions exhibit 64% higher uncertainty than pure paintings (p=0.003), suggesting the model detects mixed authorship rather than classification failure. The trained model is specific to this human-robot pair but provides a methodological grounding for sample-efficient attribution in data-scarce human-AI creative workflows that, in the future, has the potential to extend authorship attribution to any human-robot collaborative painting.

