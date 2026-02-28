---
layout: default
title: SPATIALALIGN: Aligning Dynamic Spatial Relationships in Video Generation
---

# SPATIALALIGN: Aligning Dynamic Spatial Relationships in Video Generation
**arXiv**：[2602.22745v1](https://arxiv.org/abs/2602.22745) · [PDF](https://arxiv.org/pdf/2602.22745.pdf)  
**作者**：Fengming Liu, Tat-Jen Cham, Chuanxia Zheng  

**一句话要点**：提出SPATIALALIGN框架以增强文本到视频模型对动态空间关系的对齐能力

**关键词**：文本到视频生成, 动态空间关系, 直接偏好优化, 几何评估指标, 微调框架

## 3 点简述
- 核心问题：现有文本到视频生成器常忽略文本提示中的动态空间约束，导致视频空间关系不准确。
- 方法要点：采用零阶正则化直接偏好优化微调模型，并设计基于几何的DSR-SCORE指标量化评估对齐度。
- 实验或效果：微调模型在空间关系对齐上显著优于基线，代码将公开。

## 摘要（原文）

> Most text-to-video (T2V) generators prioritize aesthetic quality, but often ignoring the spatial constraints in the generated videos. In this work, we present SPATIALALIGN, a self-improvement framework that enhances T2V models capabilities to depict Dynamic Spatial Relationships (DSR) specified in text prompts. We present a zeroth-order regularized Direct Preference Optimization (DPO) to fine-tune T2V models towards better alignment with DSR. Specifically, we design DSR-SCORE, a geometry-based metric that quantitatively measures the alignment between generated videos and the specified DSRs in prompts, which is a step forward from prior works that rely on VLM for evaluation. We also conduct a dataset of text-video pairs with diverse DSRs to facilitate the study. Extensive experiments demonstrate that our fine-tuned model significantly out performs the baseline in spatial relationships. The code will be released in Link.

