---
layout: default
title: A Parameter-Efficient Mixture-of-Experts Framework for Cross-Modal Geo-Localization
---

# A Parameter-Efficient Mixture-of-Experts Framework for Cross-Modal Geo-Localization
**arXiv**：[2510.20291v1](https://arxiv.org/abs/2510.20291) · [PDF](https://arxiv.org/pdf/2510.20291.pdf)  
**作者**：LinFeng Li, Jian Zhao, Zepeng Yang, Yuhang Song, Bojun Lin, Tianle Zhang, Yuchen Yuan, Chi Zhang, Xuelong Li  

**一句话要点**：提出参数高效专家混合框架以解决跨模态地理定位中的平台异构问题

**关键词**：跨模态地理定位, 专家混合框架, 领域对齐预处理, 硬负样本挖掘, 平台异构处理, 多模态检索

## 3 点简述
- 核心问题：跨模态地理定位中平台间视觉异构和文本-视觉领域差距
- 方法要点：使用领域对齐预处理和MoE框架，训练平台专家增强判别力
- 实验或效果：在RoboSense 2025竞赛中排名第一，验证了异构视角下的鲁棒性

## 摘要（原文）

> We present a winning solution to RoboSense 2025 Track 4: Cross-Modal Drone
> Navigation. The task retrieves the most relevant geo-referenced image from a
> large multi-platform corpus (satellite/drone/ground) given a natural-language
> query. Two obstacles are severe inter-platform heterogeneity and a domain gap
> between generic training descriptions and platform-specific test queries. We
> mitigate these with a domain-aligned preprocessing pipeline and a
> Mixture-of-Experts (MoE) framework: (i) platform-wise partitioning, satellite
> augmentation, and removal of orientation words; (ii) an LLM-based caption
> refinement pipeline to align textual semantics with the distinct visual
> characteristics of each platform. Using BGE-M3 (text) and EVA-CLIP (image), we
> train three platform experts using a progressive two-stage, hard-negative
> mining strategy to enhance discriminative power, and fuse their scores at
> inference. The system tops the official leaderboard, demonstrating robust
> cross-modal geo-localization under heterogeneous viewpoints.

