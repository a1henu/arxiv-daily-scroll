---
layout: default
title: Scaling Reinforcement Learning for Content Moderation with Large Language Models
---

# Scaling Reinforcement Learning for Content Moderation with Large Language Models
**arXiv**：[2512.20061v1](https://arxiv.org/abs/2512.20061) · [PDF](https://arxiv.org/pdf/2512.20061.pdf)  
**作者**：Hamed Firooz, Rui Liu, Yuchen Lu, Zhenyu Hou, Fangzhou Xiong, Xiaoyang Zhang, Changshu Jian, Zhicheng Zhu, Jiayuan Ma, Jacob Tao, Chaitali Gupta, Xiaochang Peng, Shike Mei, Hang Cui, Yang Qin, Shuo Tang, Jason Gaedtke, Arpit Mittal  

**一句话要点**：提出基于强化学习的大语言模型内容审核方法，以解决标签稀疏和复杂推理问题。

**关键词**：内容审核, 强化学习, 大语言模型, 奖励塑造, 数据效率

## 3 点简述
- 核心问题：大规模内容审核面临标签稀疏、政策动态变化和需深度推理的挑战。
- 方法要点：系统评估强化学习训练策略和奖励塑造，将通用语言模型转化为政策对齐分类器。
- 实验或效果：强化学习在复杂任务上性能显著提升，数据效率比监督微调高100倍。

## 摘要（原文）

> Content moderation at scale remains one of the most pressing challenges in today's digital ecosystem, where billions of user- and AI-generated artifacts must be continuously evaluated for policy violations. Although recent advances in large language models (LLMs) have demonstrated strong potential for policy-grounded moderation, the practical challenges of training these systems to achieve expert-level accuracy in real-world settings remain largely unexplored, particularly in regimes characterized by label sparsity, evolving policy definitions, and the need for nuanced reasoning beyond shallow pattern matching. In this work, we present a comprehensive empirical investigation of scaling reinforcement learning (RL) for content classification, systematically evaluating multiple RL training recipes and reward-shaping strategies-including verifiable rewards and LLM-as-judge frameworks-to transform general-purpose language models into specialized, policy-aligned classifiers across three real-world content moderation tasks. Our findings provide actionable insights for industrial-scale moderation systems, demonstrating that RL exhibits sigmoid-like scaling behavior in which performance improves smoothly with increased training data, rollouts, and optimization steps before gradually saturating. Moreover, we show that RL substantially improves performance on tasks requiring complex policy-grounded reasoning while achieving up to 100x higher data efficiency than supervised fine-tuning, making it particularly effective in domains where expert annotations are scarce or costly.

