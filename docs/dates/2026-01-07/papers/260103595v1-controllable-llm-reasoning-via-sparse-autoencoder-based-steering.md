---
layout: default
title: Controllable LLM Reasoning via Sparse Autoencoder-Based Steering
---

# Controllable LLM Reasoning via Sparse Autoencoder-Based Steering
**arXiv**：[2601.03595v1](https://arxiv.org/abs/2601.03595) · [PDF](https://arxiv.org/pdf/2601.03595.pdf)  
**作者**：Yi Fang, Wenjie Wang, Mingfeng Xue, Boyi Deng, Fengli Xu, Dayiheng Liu, Fuli Feng  

**一句话要点**：提出SAE-Steering方法，通过稀疏自编码器解耦隐藏状态以控制大推理模型的细粒度推理策略。

**关键词**：大推理模型, 稀疏自编码器, 推理策略控制, 特征解耦, 控制向量

## 3 点简述
- 核心问题：大推理模型自主选择推理策略易导致低效或错误路径，现有方法难以控制细粒度策略。
- 方法要点：利用稀疏自编码器解耦隐藏状态，提出两阶段特征识别管道SAE-Steering筛选策略特定特征作为控制向量。
- 实验或效果：SAE-Steering控制效果优于现有方法超15%，可纠正错误路径，提升准确率7%。

## 摘要（原文）

> Large Reasoning Models (LRMs) exhibit human-like cognitive reasoning strategies (e.g. backtracking, cross-verification) during reasoning process, which improves their performance on complex tasks. Currently, reasoning strategies are autonomously selected by LRMs themselves. However, such autonomous selection often produces inefficient or even erroneous reasoning paths. To make reasoning more reliable and flexible, it is important to develop methods for controlling reasoning strategies. Existing methods struggle to control fine-grained reasoning strategies due to conceptual entanglement in LRMs' hidden states. To address this, we leverage Sparse Autoencoders (SAEs) to decompose strategy-entangled hidden states into a disentangled feature space. To identify the few strategy-specific features from the vast pool of SAE features, we propose SAE-Steering, an efficient two-stage feature identification pipeline. SAE-Steering first recalls features that amplify the logits of strategy-specific keywords, filtering out over 99\% of features, and then ranks the remaining features by their control effectiveness. Using the identified strategy-specific features as control vectors, SAE-Steering outperforms existing methods by over 15\% in control effectiveness. Furthermore, controlling reasoning strategies can redirect LRMs from erroneous paths to correct ones, achieving a 7\% absolute accuracy improvement.

