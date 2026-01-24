---
layout: default
title: CoNRec: Context-Discerning Negative Recommendation with LLMs
---

# CoNRec: Context-Discerning Negative Recommendation with LLMs
**arXiv**：[2601.15721v1](https://arxiv.org/abs/2601.15721) · [PDF](https://arxiv.org/pdf/2601.15721.pdf)  
**作者**：Xinda Chen, Jiawei Wu, Yishuang Liu, Jialin Zhu, Shuwen Xiao, Junjun Zheng, Xiangheng Kong, Yuning Jiang  

**一句话要点**：提出CoNRec框架，利用LLMs建模用户负面偏好以解决推荐系统中负面反馈稀疏与上下文理解偏差问题。

**关键词**：负面推荐, 大语言模型, 上下文理解, 语义ID表示, 渐进式训练, 奖励函数设计

## 3 点简述
- 核心问题：现有推荐系统忽视直接建模用户负面兴趣，且负面反馈稀疏导致模型受正面反馈主导的上下文理解偏差。
- 方法要点：设计上下文辨别模块，使用语义ID表示和项目级对齐任务增强LLM对负面反馈语义上下文的理解，并引入渐进式GRPO训练范式动态平衡正负行为上下文利用。
- 实验或效果：提出基于多日未来负面反馈及其协同信号的新奖励函数和评估指标，以缓解传统预测目标与用户真实负面偏好之间的错位。

## 摘要（原文）

> Understanding what users like is relatively straightforward; understanding what users dislike, however, remains a challenging and underexplored problem. Research into users' negative preferences has gained increasing importance in modern recommendation systems. Numerous platforms have introduced explicit negative feedback mechanisms and leverage such signals to refine their recommendation models. Beyond traditional business metrics, user experience-driven metrics, such as negative feedback rates, have become critical indicators for evaluating system performance. However, most existing approaches primarily use negative feedback as an auxiliary signal to enhance positive recommendations, paying little attention to directly modeling negative interests, which can be highly valuable in offline applications. Moreover, due to the inherent sparsity of negative feedback data, models often suffer from context understanding biases induced by positive feedback dominance. To address these challenges, we propose the first large language model framework for negative feedback modeling with special designed context-discerning modules. We use semantic ID Representation to replace text-based item descriptions and introduce an item-level alignment task that enhances the LLM's understanding of the semantic context behind negative feedback. Furthermore, we design a Progressive GRPO training paradigm that enables the model to dynamically balance the positive and negative behavioral context utilization. Besides, our investigation further reveals a fundamental misalignment between the conventional next-negative-item prediction objective and users' true negative preferences, which is heavily influenced by the system's recommendation order. To mitigate this, we propose a novel reward function and evaluation metric grounded in multi-day future negative feedback and their collaborative signals.

