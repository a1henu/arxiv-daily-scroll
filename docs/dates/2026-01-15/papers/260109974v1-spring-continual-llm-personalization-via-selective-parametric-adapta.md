---
layout: default
title: SPRInG: Continual LLM Personalization via Selective Parametric Adaptation and Retrieval-Interpolated Generation
---

# SPRInG: Continual LLM Personalization via Selective Parametric Adaptation and Retrieval-Interpolated Generation
**arXiv**：[2601.09974v1](https://arxiv.org/abs/2601.09974) · [PDF](https://arxiv.org/pdf/2601.09974.pdf)  
**作者**：Seoyeon Kim, Jaehyung Kim  

**一句话要点**：提出SPRInG框架，通过选择性参数适应和检索插值生成解决持续个性化中的偏好漂移问题

**关键词**：持续学习, 大语言模型个性化, 偏好漂移, 半参数框架, 选择性适应, 检索插值生成

## 3 点简述
- 核心问题：用户偏好随时间动态变化，传统方法易导致灾难性遗忘或噪声更新
- 方法要点：使用基于似然的评分函数识别高新颖性交互，选择性更新适配器并融合参数化知识与检索历史
- 实验或效果：在长文本个性化生成基准上优于现有基线，验证了持续个性化中的鲁棒性

## 摘要（原文）

> Personalizing Large Language Models typically relies on static retrieval or one-time adaptation, assuming user preferences remain invariant over time. However, real-world interactions are dynamic, where user interests continuously evolve, posing a challenge for models to adapt to preference drift without catastrophic forgetting. Standard continual learning approaches often struggle in this context, as they indiscriminately update on noisy interaction streams, failing to distinguish genuine preference shifts from transient contexts. To address this, we introduce SPRInG, a novel semi-parametric framework designed for effective continual personalization. During training, SPRInG employs drift-driven selective adaptation, which utilizes a likelihood-based scoring function to identify high-novelty interactions. This allows the model to selectively update the user-specific adapter on drift signals while preserving hard-to-learn residuals in a replay buffer. During inference, we apply strict relevance gating and fuse parametric knowledge with retrieved history via logit interpolation. Experiments on the long-form personalized generation benchmark demonstrate that SPRInG outperforms existing baselines, validating its robustness for real-world continual personalization.

