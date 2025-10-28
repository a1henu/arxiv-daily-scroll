---
layout: default
title: Omni-Reward: Towards Generalist Omni-Modal Reward Modeling with Free-Form Preferences
---

# Omni-Reward: Towards Generalist Omni-Modal Reward Modeling with Free-Form Preferences
**arXiv**：[2510.23451v1](https://arxiv.org/abs/2510.23451) · [PDF](https://arxiv.org/pdf/2510.23451.pdf)  
**作者**：Zhuoran Jin, Hongbang Yuan, Kejian Zhu, Jiachun Li, Pengfei Cao, Yubo Chen, Kang Liu, Jun Zhao  

**一句话要点**：提出Omni-Reward以解决多模态奖励模型中的模态不平衡和偏好僵化问题

**关键词**：多模态奖励建模, 自由形式偏好, 奖励模型基准, 多模态数据集, 生成式奖励模型

## 3 点简述
- 核心问题：现有奖励模型模态不平衡，偏好僵化，难以处理个性化偏好
- 方法要点：构建多模态基准、数据集和模型，支持自由形式偏好
- 实验或效果：在Omni-RewardBench等基准上表现优异，覆盖五种模态

## 摘要（原文）

> Reward models (RMs) play a critical role in aligning AI behaviors with human
> preferences, yet they face two fundamental challenges: (1) Modality Imbalance,
> where most RMs are mainly focused on text and image modalities, offering
> limited support for video, audio, and other modalities; and (2) Preference
> Rigidity, where training on fixed binary preference pairs fails to capture the
> complexity and diversity of personalized preferences. To address the above
> challenges, we propose Omni-Reward, a step toward generalist omni-modal reward
> modeling with support for free-form preferences, consisting of: (1) Evaluation:
> We introduce Omni-RewardBench, the first omni-modal RM benchmark with free-form
> preferences, covering nine tasks across five modalities including text, image,
> video, audio, and 3D; (2) Data: We construct Omni-RewardData, a multimodal
> preference dataset comprising 248K general preference pairs and 69K
> instruction-tuning pairs for training generalist omni-modal RMs; (3) Model: We
> propose Omni-RewardModel, which includes both discriminative and generative
> RMs, and achieves strong performance on Omni-RewardBench as well as other
> widely used reward modeling benchmarks.

