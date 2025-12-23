---
layout: default
title: Finer-Personalization Rank: Fine-Grained Retrieval Examines Identity Preservation for Personalized Generation
---

# Finer-Personalization Rank: Fine-Grained Retrieval Examines Identity Preservation for Personalized Generation
**arXiv**：[2512.19026v1](https://arxiv.org/abs/2512.19026) · [PDF](https://arxiv.org/pdf/2512.19026.pdf)  
**作者**：Connor Kilrain, David Carlyn, Julia Chae, Sara Beery, Wei-Lun Chao, Jianyang Gu  

**一句话要点**：提出Finer-Personalization Rank以评估个性化生成中的身份保留问题

**关键词**：个性化生成, 身份保留评估, 细粒度检索, 图像生成, 评估协议, 检索指标

## 3 点简述
- 核心问题：现有生成评估指标忽视细粒度身份细节，难以准确衡量个性化生成的身份保留。
- 方法要点：采用基于检索的排名视图，将生成图像作为查询，在身份标记的真实图像库中评估检索性能。
- 实验或效果：在CUB、Stanford Cars和动物Re-ID基准上，该方法比语义相似性指标更忠实反映身份保留，并揭示流行方法的身份漂移。

## 摘要（原文）

> The rise of personalized generative models raises a central question: how should we evaluate identity preservation? Given a reference image (e.g., one's pet), we expect the generated image to retain precise details attached to the subject's identity. However, current generative evaluation metrics emphasize the overall semantic similarity between the reference and the output, and overlook these fine-grained discriminative details. We introduce Finer-Personalization Rank, an evaluation protocol tailored to identity preservation. Instead of pairwise similarity, Finer-Personalization Rank adopts a ranking view: it treats each generated image as a query against an identity-labeled gallery consisting of visually similar real images. Retrieval metrics (e.g., mean average precision) measure performance, where higher scores indicate that identity-specific details (e.g., a distinctive head spot) are preserved. We assess identity at multiple granularities -- from fine-grained categories (e.g., bird species, car models) to individual instances (e.g., re-identification). Across CUB, Stanford Cars, and animal Re-ID benchmarks, Finer-Personalization Rank more faithfully reflects identity retention than semantic-only metrics and reveals substantial identity drift in several popular personalization methods. These results position the gallery-based protocol as a principled and practical evaluation for personalized generation.

