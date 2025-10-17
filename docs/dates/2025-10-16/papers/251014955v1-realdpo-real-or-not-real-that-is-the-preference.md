---
layout: default
title: RealDPO: Real or Not Real, that is the Preference
---

# RealDPO: Real or Not Real, that is the Preference
**arXiv**：[2510.14955v1](https://arxiv.org/abs/2510.14955) · [PDF](https://arxiv.org/pdf/2510.14955.pdf)  
**作者**：Guo Cheng, Danni Yang, Ziqi Huang, Jianlou Si, Chenyang Si, Ziwei Liu  

**一句话要点**：提出RealDPO对齐范式，利用真实世界数据优化视频生成中的复杂运动合成。

**关键词**：视频生成, 偏好优化, 运动合成, 真实世界数据, 对齐范式

## 3 点简述
- 核心问题：视频生成模型在复杂运动合成中难以产生自然、流畅和上下文一致的运动。
- 方法要点：引入RealDPO，使用真实视频作为正样本进行偏好学习，结合定制损失函数提升运动真实感。
- 实验或效果：在RealAction-5K数据集上验证，RealDPO显著改善视频质量、文本对齐和运动真实感。

## 摘要（原文）

> Video generative models have recently achieved notable advancements in
> synthesis quality. However, generating complex motions remains a critical
> challenge, as existing models often struggle to produce natural, smooth, and
> contextually consistent movements. This gap between generated and real-world
> motions limits their practical applicability. To address this issue, we
> introduce RealDPO, a novel alignment paradigm that leverages real-world data as
> positive samples for preference learning, enabling more accurate motion
> synthesis. Unlike traditional supervised fine-tuning (SFT), which offers
> limited corrective feedback, RealDPO employs Direct Preference Optimization
> (DPO) with a tailored loss function to enhance motion realism. By contrasting
> real-world videos with erroneous model outputs, RealDPO enables iterative
> self-correction, progressively refining motion quality. To support
> post-training in complex motion synthesis, we propose RealAction-5K, a curated
> dataset of high-quality videos capturing human daily activities with rich and
> precise motion details. Extensive experiments demonstrate that RealDPO
> significantly improves video quality, text alignment, and motion realism
> compared to state-of-the-art models and existing preference optimization
> techniques.

