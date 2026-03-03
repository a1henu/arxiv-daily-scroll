---
layout: default
title: NextAds: Towards Next-generation Personalized Video Advertising
---

# NextAds: Towards Next-generation Personalized Video Advertising
**arXiv**：[2603.02137v1](https://arxiv.org/abs/2603.02137) · [PDF](https://arxiv.org/pdf/2603.02137.pdf)  
**作者**：Yiyan Xu, Ruoxuan Xia, Wuqiang Zheng, Fengbin Zhu, Wenjie Wang, Fuli Feng  

**一句话要点**：提出NextAds生成式范式以解决个性化视频广告中静态库存限制问题

**关键词**：个性化视频广告, 生成式AI, 创意生成, 创意集成, 连续空间优化

## 3 点简述
- 核心问题：基于检索的个性化视频广告系统受限于静态创意库，导致粒度粗、时效差且无法实时优化。
- 方法要点：NextAds采用生成式AI范式，在服务时于连续空间优化视频创意，包含四个核心组件。
- 实验或效果：通过构建端到端管道和初步实验，验证生成式AI能生成和集成个性化创意，性能表现积极。

## 摘要（原文）

> With the rapid growth of online video consumption, video advertising has become increasingly dominant in the digital advertising landscape. Yet diverse users and viewing contexts makes one-size-fits-all ad creatives insufficient for consistent effectiveness, underlining the importance of personalization. In practice, most personalized video advertising systems follow a retrieval-based paradigm, selecting the optimal one from a small set of professionally pre-produced creatives for each user. Such static and finite inventories limits both the granularity and the timeliness of personalization, and prevents the creatives from being continuously refined based on online user feedback. Recent advances in generative AI make it possible to move beyond retrieval toward optimizing video creatives in a continuous space at serving time.
>   In this light, we propose NextAds, a generation-based paradigm for next-generation personalized video advertising, and conceptualize NextAds with four core components. To enable comparable research progress, we formulate two representative tasks: personalized creative generation and personalized creative integration, and introduce corresponding lightweight benchmarks. To assess feasibility, we instantiate end-to-end pipelines for both tasks and conduct initial exploratory experiments, demonstrating that GenAI can generate and integrate personalized creatives with encouraging performance. Moreover, we discuss the key challenges and opportunities under this paradigm, aiming to provide actionable insights for both researchers and practitioners and to catalyze progress in personalized video advertising.

