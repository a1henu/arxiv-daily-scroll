---
layout: default
title: PSR: Scaling Multi-Subject Personalized Image Generation with Pairwise Subject-Consistency Rewards
---

# PSR: Scaling Multi-Subject Personalized Image Generation with Pairwise Subject-Consistency Rewards
**arXiv**：[2512.01236v1](https://arxiv.org/abs/2512.01236) · [PDF](https://arxiv.org/pdf/2512.01236.pdf)  
**作者**：Shulei Wang, Longhui Wei, Xin He, Jianbo Ouyang, Hui Lu, Zhou Zhao, Qi Tian  

**一句话要点**：提出PSR方法，通过成对主题一致性奖励和强化学习，提升多主题个性化图像生成的质量与可控性。

**关键词**：多主题个性化图像生成, 成对主题一致性奖励, 强化学习优化, 数据生成管道, 文本可控性, 基准评估

## 3 点简述
- 核心问题：现有模型在多主题生成中主题一致性和文本控制能力下降，缺乏高质量数据集和训练策略。
- 方法要点：构建可扩展的多主题数据生成管道，并设计成对主题一致性奖励和通用奖励，结合强化学习优化模型。
- 实验或效果：引入新基准评估，实验证明PSR在多主题个性化图像生成中有效提升性能。

## 摘要（原文）

> Personalized generation models for a single subject have demonstrated remarkable effectiveness, highlighting their significant potential. However, when extended to multiple subjects, existing models often exhibit degraded performance, particularly in maintaining subject consistency and adhering to textual prompts. We attribute these limitations to the absence of high-quality multi-subject datasets and refined post-training strategies. To address these challenges, we propose a scalable multi-subject data generation pipeline that leverages powerful single-subject generation models to construct diverse and high-quality multi-subject training data. Through this dataset, we first enable single-subject personalization models to acquire knowledge of synthesizing multi-image and multi-subject scenarios. Furthermore, to enhance both subject consistency and text controllability, we design a set of Pairwise Subject-Consistency Rewards and general-purpose rewards, which are incorporated into a refined reinforcement learning stage. To comprehensively evaluate multi-subject personalization, we introduce a new benchmark that assesses model performance using seven subsets across three dimensions. Extensive experiments demonstrate the effectiveness of our approach in advancing multi-subject personalized image generation. Github Link: https://github.com/wang-shulei/PSR

