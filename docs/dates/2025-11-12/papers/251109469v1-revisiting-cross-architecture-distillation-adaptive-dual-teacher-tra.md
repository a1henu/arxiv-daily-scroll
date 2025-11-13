---
layout: default
title: Revisiting Cross-Architecture Distillation: Adaptive Dual-Teacher Transfer for Lightweight Video Models
---

# Revisiting Cross-Architecture Distillation: Adaptive Dual-Teacher Transfer for Lightweight Video Models
**arXiv**：[2511.09469v1](https://arxiv.org/abs/2511.09469) · [PDF](https://arxiv.org/pdf/2511.09469.pdf)  
**作者**：Ying Peng, Hongsen Ye, Changxin Huang, Xiping Hu, Jian Chen, Runhao Zeng  

**一句话要点**：提出双教师知识蒸馏框架以解决轻量视频模型精度不足问题

**关键词**：知识蒸馏, 视频动作识别, 轻量模型, 异构架构, 双教师学习

## 3 点简述
- 核心问题：轻量CNN在视频动作识别中精度低，异构架构蒸馏存在不匹配
- 方法要点：使用ViT和CNN双教师，动态加权融合预测与残差特征学习
- 实验或效果：在HMDB51等基准上优于现有方法，最高精度提升5.95%

## 摘要（原文）

> Vision Transformers (ViTs) have achieved strong performance in video action recognition, but their high computational cost limits their practicality. Lightweight CNNs are more efficient but suffer from accuracy gaps. Cross-Architecture Knowledge Distillation (CAKD) addresses this by transferring knowledge from ViTs to CNNs, yet existing methods often struggle with architectural mismatch and overlook the value of stronger homogeneous CNN teachers. To tackle these challenges, we propose a Dual-Teacher Knowledge Distillation framework that leverages both a heterogeneous ViT teacher and a homogeneous CNN teacher to collaboratively guide a lightweight CNN student. We introduce two key components: (1) Discrepancy-Aware Teacher Weighting, which dynamically fuses the predictions from ViT and CNN teachers by assigning adaptive weights based on teacher confidence and prediction discrepancy with the student, enabling more informative and effective supervision; and (2) a Structure Discrepancy-Aware Distillation strategy, where the student learns the residual features between ViT and CNN teachers via a lightweight auxiliary branch, focusing on transferable architectural differences without mimicking all of ViT's high-dimensional patterns. Extensive experiments on benchmarks including HMDB51, EPIC-KITCHENS-100, and Kinetics-400 demonstrate that our method consistently outperforms state-of-the-art distillation approaches, achieving notable performance improvements with a maximum accuracy gain of 5.95% on HMDB51.

