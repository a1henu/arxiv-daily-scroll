---
layout: default
title: NeXT-IMDL: Build Benchmark for NeXT-Generation Image Manipulation Detection & Localization
---

# NeXT-IMDL: Build Benchmark for NeXT-Generation Image Manipulation Detection & Localization
**arXiv**：[2512.23374v1](https://arxiv.org/abs/2512.23374) · [PDF](https://arxiv.org/pdf/2512.23374.pdf)  
**作者**：Yifei Li, Haoyuan He, Yu Zheng, Bingyao Yu, Wenzhao Zheng, Lei Chen, Jie Zhou, Jiwen Lu  

**一句话要点**：提出NeXT-IMDL基准以系统评估图像篡改检测与定位方法的泛化能力

**关键词**：图像篡改检测, 基准构建, 泛化评估, AI生成内容, 跨维度协议

## 3 点简述
- 核心问题：现有图像篡改检测方法在跨数据集评估中可能高估泛化性能，难以应对多样AI生成内容。
- 方法要点：构建大规模诊断基准，基于编辑模型、篡改类型、内容语义和伪造粒度四轴分类，设计五种跨维度评估协议。
- 实验或效果：在11个代表性模型上测试，显示在模拟真实泛化场景下，模型出现系统性失败和性能显著下降。

## 摘要（原文）

> The accessibility surge and abuse risks of user-friendly image editing models have created an urgent need for generalizable, up-to-date methods for Image Manipulation Detection and Localization (IMDL). Current IMDL research typically uses cross-dataset evaluation, where models trained on one benchmark are tested on others. However, this simplified evaluation approach conceals the fragility of existing methods when handling diverse AI-generated content, leading to misleading impressions of progress. This paper challenges this illusion by proposing NeXT-IMDL, a large-scale diagnostic benchmark designed not just to collect data, but to probe the generalization boundaries of current detectors systematically. Specifically, NeXT-IMDL categorizes AIGC-based manipulations along four fundamental axes: editing models, manipulation types, content semantics, and forgery granularity. Built upon this, NeXT-IMDL implements five rigorous cross-dimension evaluation protocols. Our extensive experiments on 11 representative models reveal a critical insight: while these models perform well in their original settings, they exhibit systemic failures and significant performance degradation when evaluated under our designed protocols that simulate real-world, various generalization scenarios. By providing this diagnostic toolkit and the new findings, we aim to advance the development towards building truly robust, next-generation IMDL models.

