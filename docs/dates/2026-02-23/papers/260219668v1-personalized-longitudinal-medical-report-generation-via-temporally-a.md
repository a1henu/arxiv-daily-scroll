---
layout: default
title: Personalized Longitudinal Medical Report Generation via Temporally-Aware Federated Adaptation
---

# Personalized Longitudinal Medical Report Generation via Temporally-Aware Federated Adaptation
**arXiv**：[2602.19668v1](https://arxiv.org/abs/2602.19668) · [PDF](https://arxiv.org/pdf/2602.19668.pdf)  
**作者**：He Zhu, Ren Togo, Takahiro Ogawa, Kenji Hirata, Minghui Tang, Takaaki Yoshimura, Hiroyuki Sugimori, Noriko Nishioka, Yukie Shimizu, Kohsuke Kudo, Miki Haseyama  

**一句话要点**：提出FedTAR框架，通过联邦时间适应解决纵向医疗报告生成中的隐私和动态建模问题。

**关键词**：纵向医疗报告生成, 联邦学习, 时间适应, 个性化建模, 隐私保护, 元学习

## 3 点简述
- 核心问题：现有联邦学习方法忽略纵向动态，导致报告生成不稳定和次优。
- 方法要点：FedTAR结合人口统计驱动的个性化和时间感知全局聚合，使用LoRA适配器和元学习时间策略。
- 实验或效果：在J-MID和MIMIC-CXR数据集上验证了语言准确性、时间一致性和跨站点泛化能力的提升。

## 摘要（原文）

> Longitudinal medical report generation is clinically important yet remains challenging due to strict privacy constraints and the evolving nature of disease progression. Although federated learning (FL) enables collaborative training without data sharing, existing FL methods largely overlook longitudinal dynamics by assuming stationary client distributions, making them unable to model temporal shifts across visits or patient-specific heterogeneity-ultimately leading to unstable optimization and suboptimal report generation.
>   We introduce Federated Temporal Adaptation (FTA), a federated setting that explicitly accounts for the temporal evolution of client data. Building upon this setting, we propose FedTAR, a framework that integrates demographic-driven personalization with time-aware global aggregation. FedTAR generates lightweight LoRA adapters from demographic embeddings and performs temporal residual aggregation, where updates from different visits are weighted by a meta-learned temporal policy optimized via first-order MAML.
>   Experiments on J-MID (1M exams) and MIMIC-CXR demonstrate consistent improvements in linguistic accuracy, temporal coherence, and cross-site generalization, establishing FedTAR as a robust and privacy-preserving paradigm for federated longitudinal modeling.

