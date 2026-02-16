---
layout: default
title: Self-EvolveRec: Self-Evolving Recommender Systems with LLM-based Directional Feedback
---

# Self-EvolveRec: Self-Evolving Recommender Systems with LLM-based Directional Feedback
**arXiv**：[2602.12612v1](https://arxiv.org/abs/2602.12612) · [PDF](https://arxiv.org/pdf/2602.12612.pdf)  
**作者**：Sein Kim, Sangwu Park, Hongseok Kang, Wonjoong Kim, Jimin Seo, Yeonjun In, Kanghoon Yoon, Chanyoung Park  

**一句话要点**：提出Self-EvolveRec框架，通过定向反馈循环解决推荐系统自动化设计中缺乏定性指导的问题。

**关键词**：推荐系统自动化, LLM驱动进化, 定向反馈循环, 用户模拟器, 模型诊断工具, 动态评估适应

## 3 点简述
- 核心问题：传统自动化方法如NAS受限于固定搜索空间，LLM驱动框架依赖标量指标，缺乏定性分析和改进方向。
- 方法要点：集成用户模拟器提供定性批判和模型诊断工具进行定量验证，实现定向反馈循环和动态评估标准适应。
- 实验或效果：在推荐性能和用户满意度上显著优于现有NAS和LLM驱动基线，代码已开源。

## 摘要（原文）

> Traditional methods for automating recommender system design, such as Neural Architecture Search (NAS), are often constrained by a fixed search space defined by human priors, limiting innovation to pre-defined operators. While recent LLM-driven code evolution frameworks shift fixed search space target to open-ended program spaces, they primarily rely on scalar metrics (e.g., NDCG, Hit Ratio) that fail to provide qualitative insights into model failures or directional guidance for improvement. To address this, we propose Self-EvolveRec, a novel framework that establishes a directional feedback loop by integrating a User Simulator for qualitative critiques and a Model Diagnosis Tool for quantitative internal verification. Furthermore, we introduce a Diagnosis Tool - Model Co-Evolution strategy to ensure that evaluation criteria dynamically adapt as the recommendation architecture evolves. Extensive experiments demonstrate that Self-EvolveRec significantly outperforms state-of-the-art NAS and LLM-driven code evolution baselines in both recommendation performance and user satisfaction. Our code is available at https://github.com/Sein-Kim/self_evolverec.

