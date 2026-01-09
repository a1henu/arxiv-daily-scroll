---
layout: default
title: Enhancing Multimodal Retrieval via Complementary Information Extraction and Alignment
---

# Enhancing Multimodal Retrieval via Complementary Information Extraction and Alignment
**arXiv**：[2601.04571v1](https://arxiv.org/abs/2601.04571) · [PDF](https://arxiv.org/pdf/2601.04571.pdf)  
**作者**：Delong Zeng, Yuexiang Xie, Yaliang Li, Ying Shen  

**一句话要点**：提出CIEA方法，通过互补信息提取与对齐增强多模态检索性能。

**关键词**：多模态检索, 互补信息提取, 对比学习, 图像文本对齐, 统一潜在空间

## 3 点简述
- 核心问题：现有方法忽略多模态数据中的互补信息，影响检索效果。
- 方法要点：设计互补信息提取器，将文本和图像映射到统一空间，使用对比损失优化。
- 实验或效果：在实验中显著优于现有模型，提供消融研究和案例验证。

## 摘要（原文）

> Multimodal retrieval has emerged as a promising yet challenging research direction in recent years. Most existing studies in multimodal retrieval focus on capturing information in multimodal data that is similar to their paired texts, but often ignores the complementary information contained in multimodal data. In this study, we propose CIEA, a novel multimodal retrieval approach that employs Complementary Information Extraction and Alignment, which transforms both text and images in documents into a unified latent space and features a complementary information extractor designed to identify and preserve differences in the image representations. We optimize CIEA using two complementary contrastive losses to ensure semantic integrity and effectively capture the complementary information contained in images. Extensive experiments demonstrate the effectiveness of CIEA, which achieves significant improvements over both divide-and-conquer models and universal dense retrieval models. We provide an ablation study, further discussions, and case studies to highlight the advancements achieved by CIEA. To promote further research in the community, we have released the source code at https://github.com/zengdlong/CIEA.

