---
layout: default
title: A Parameter-Efficient Mixture-of-Experts Framework for Cross-Modal Geo-Localization
---

# A Parameter-Efficient Mixture-of-Experts Framework for Cross-Modal Geo-Localization
**arXiv**：[2510.20291v1](https://arxiv.org/abs/2510.20291) · [PDF](https://arxiv.org/pdf/2510.20291.pdf)  
**作者**：LinFeng Li, Jian Zhao, Zepeng Yang, Yuhang Song, Bojun Lin, Tianle Zhang, Yuchen Yuan, Chi Zhang, Xuelong Li  

**一句话要点**：提出参数高效专家混合框架，解决跨模态异构平台地理定位问题。

**关键词**：跨模态检索, 专家混合框架, 地理定位, 领域对齐, 异构平台, 图像检索

## 3 点简述
- 核心问题：跨平台异构性和领域差距阻碍自然语言查询与地理图像检索。
- 方法要点：采用领域对齐预处理和专家混合框架，增强语义与视觉对齐。
- 实验或效果：在RoboSense 2025竞赛中排名第一，验证了鲁棒性。

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

