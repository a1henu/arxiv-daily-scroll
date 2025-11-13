---
layout: default
title: Asymmetric Cross-Modal Knowledge Distillation: Bridging Modalities with Weak Semantic Consistency
---

# Asymmetric Cross-Modal Knowledge Distillation: Bridging Modalities with Weak Semantic Consistency
**arXiv**：[2511.08901v1](https://arxiv.org/abs/2511.08901) · [PDF](https://arxiv.org/pdf/2511.08901.pdf)  
**作者**：Riling Wei, Kelu Yao, Chuanguang Yang, Jin Wang, Zhuoyan Gao, Chao Li  

**一句话要点**：提出非对称跨模态知识蒸馏框架以解决弱语义一致性下的模态桥接问题

**关键词**：跨模态知识蒸馏, 弱语义一致性, 最优传输理论, 遥感场景分类, 学生友好匹配, 语义感知对齐

## 3 点简述
- 核心问题：现实场景中配对模态稀缺，弱语义一致性增加知识传输成本
- 方法要点：集成学生友好匹配和语义感知知识对齐模块，优化传输路径
- 实验或效果：在遥感场景分类数据集上优于7种现有方法，实现SOTA性能

## 摘要（原文）

> Cross-modal Knowledge Distillation has demonstrated promising performance on paired modalities with strong semantic connections, referred to as Symmetric Cross-modal Knowledge Distillation (SCKD). However, implementing SCKD becomes exceedingly constrained in real-world scenarios due to the limited availability of paired modalities. To this end, we investigate a general and effective knowledge learning concept under weak semantic consistency, dubbed Asymmetric Cross-modal Knowledge Distillation (ACKD), aiming to bridge modalities with limited semantic overlap. Nevertheless, the shift from strong to weak semantic consistency improves flexibility but exacerbates challenges in knowledge transmission costs, which we rigorously verified based on optimal transport theory. To mitigate the issue, we further propose a framework, namely SemBridge, integrating a Student-Friendly Matching module and a Semantic-aware Knowledge Alignment module. The former leverages self-supervised learning to acquire semantic-based knowledge and provide personalized instruction for each student sample by dynamically selecting the relevant teacher samples. The latter seeks the optimal transport path by employing Lagrangian optimization. To facilitate the research, we curate a benchmark dataset derived from two modalities, namely Multi-Spectral (MS) and asymmetric RGB images, tailored for remote sensing scene classification. Comprehensive experiments exhibit that our framework achieves state-of-the-art performance compared with 7 existing approaches on 6 different model architectures across various datasets.

