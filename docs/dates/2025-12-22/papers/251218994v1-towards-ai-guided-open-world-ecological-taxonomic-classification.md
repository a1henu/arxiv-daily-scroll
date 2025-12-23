---
layout: default
title: Towards AI-Guided Open-World Ecological Taxonomic Classification
---

# Towards AI-Guided Open-World Ecological Taxonomic Classification
**arXiv**：[2512.18994v1](https://arxiv.org/abs/2512.18994) · [PDF](https://arxiv.org/pdf/2512.18994.pdf)  
**作者**：Cheng Yaw Low, Heejoon Koo, Jaewoo Park, Kaleb Mesfin Asfaw, Meeyoung Cha  

**一句话要点**：提出TaxoNet框架以解决开放世界生态分类中的长尾分布与领域偏移问题

**关键词**：开放世界分类, 长尾分布, 生态监测, TaxoNet, 双边缘损失, 植物分类

## 3 点简述
- 核心问题：生态分类面临长尾分布、细粒度差异、时空域偏移和封闭集假设的挑战
- 方法要点：TaxoNet采用嵌入编码器和双边缘惩罚损失，增强稀有类学习并抑制过代表类
- 实验或效果：在多个生态数据集上优于基线，尤其提升稀有类性能，支持开放世界监测

## 摘要（原文）

> AI-guided classification of ecological families, genera, and species underpins global sustainability efforts such as biodiversity monitoring, conservation planning, and policy-making. Progress toward this goal is hindered by long-tailed taxonomic distributions from class imbalance, along with fine-grained taxonomic variations, test-time spatiotemporal domain shifts, and closed-set assumptions that can only recognize previously seen taxa. We introduce the Open-World Ecological Taxonomy Classification, a unified framework that captures the co-occurrence of these challenges in realistic ecological settings. To address them, we propose TaxoNet, an embedding-based encoder with a dual-margin penalization loss that strengthens learning signals from rare underrepresented taxa while mitigating the dominance of overrepresented ones, directly confronting interrelated challenges. We evaluate our method on diverse ecological domains: Google Auto-Arborist (urban trees), iNat-Plantae (Plantae observations from various ecosystems in iNaturalist-2019), and NAFlora-Mini (a curated herbarium collection). Our model consistently outperforms baselines, particularly for rare taxa, establishing a strong foundation for open-world plant taxonomic monitoring. Our findings further show that general-purpose multimodal foundation models remain constrained in plant-domain applications.

