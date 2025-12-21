---
layout: default
title: CitySeeker: How Do VLMS Explore Embodied Urban Navigation With Implicit Human Needs?
---

# CitySeeker: How Do VLMS Explore Embodied Urban Navigation With Implicit Human Needs?
**arXiv**：[2512.16755v1](https://arxiv.org/abs/2512.16755) · [PDF](https://arxiv.org/pdf/2512.16755.pdf)  
**作者**：Siqi Wang, Chao Liang, Yunfan Gao, Erxin Yu, Sen Li, Yushi Li, Jing Li, Haofen Wang  

**一句话要点**：提出CitySeeker基准以评估VLM在隐含需求下的城市导航能力

**关键词**：隐含需求导航, 城市环境探索, 空间推理评估, 长视野决策, 视觉语言模型基准, 认知映射策略

## 3 点简述
- 核心问题：VLM在动态城市环境中处理隐含人类需求（如“我渴了”）的能力不足
- 方法要点：设计包含6,440轨迹的基准，并分析回溯机制、空间认知增强和记忆检索策略
- 实验或效果：顶级模型任务完成率仅21.1%，揭示长视野推理和空间认知等瓶颈

## 摘要（原文）

> Vision-Language Models (VLMs) have made significant progress in explicit instruction-based navigation; however, their ability to interpret implicit human needs (e.g., "I am thirsty") in dynamic urban environments remains underexplored. This paper introduces CitySeeker, a novel benchmark designed to assess VLMs' spatial reasoning and decision-making capabilities for exploring embodied urban navigation to address implicit needs. CitySeeker includes 6,440 trajectories across 8 cities, capturing diverse visual characteristics and implicit needs in 7 goal-driven scenarios. Extensive experiments reveal that even top-performing models (e.g., Qwen2.5-VL-32B-Instruct) achieve only 21.1% task completion. We find key bottlenecks in error accumulation in long-horizon reasoning, inadequate spatial cognition, and deficient experiential recall. To further analyze them, we investigate a series of exploratory strategies-Backtracking Mechanisms, Enriching Spatial Cognition, and Memory-Based Retrieval (BCR), inspired by human cognitive mapping's emphasis on iterative observation-reasoning cycles and adaptive path optimization. Our analysis provides actionable insights for developing VLMs with robust spatial intelligence required for tackling "last-mile" navigation challenges.

