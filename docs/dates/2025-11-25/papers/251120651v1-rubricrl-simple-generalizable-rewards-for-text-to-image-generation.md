---
layout: default
title: RubricRL: Simple Generalizable Rewards for Text-to-Image Generation
---

# RubricRL: Simple Generalizable Rewards for Text-to-Image Generation
**arXiv**：[2511.20651v1](https://arxiv.org/abs/2511.20651) · [PDF](https://arxiv.org/pdf/2511.20651.pdf)  
**作者**：Xuelu Feng, Yunsheng Li, Ziyu Wan, Zixuan Gao, Junsong Yuan, Dongdong Chen, Chunming Qiao  

**一句话要点**：提出RubricRL框架以解决文本到图像生成中奖励设计缺乏可解释性和灵活性的问题

**关键词**：强化学习对齐, 文本到图像生成, 可解释奖励设计, 多模态评估, 结构化评分表

## 3 点简述
- 核心问题：现有奖励方法依赖固定权重复合指标或黑盒标量，限制可解释性和用户控制
- 方法要点：动态构建结构化评分表，分解为细粒度视觉标准，并使用多模态评估器独立评分
- 实验或效果：在自回归模型中提升提示忠实度、视觉细节和泛化性，提供可扩展对齐基础

## 摘要（原文）

> Reinforcement learning (RL) has recently emerged as a promising approach for aligning text-to-image generative models with human preferences. A key challenge, however, lies in designing effective and interpretable rewards. Existing methods often rely on either composite metrics (e.g., CLIP, OCR, and realism scores) with fixed weights or a single scalar reward distilled from human preference models, which can limit interpretability and flexibility. We propose RubricRL, a simple and general framework for rubric-based reward design that offers greater interpretability, composability, and user control. Instead of using a black-box scalar signal, RubricRL dynamically constructs a structured rubric for each prompt--a decomposable checklist of fine-grained visual criteria such as object correctness, attribute accuracy, OCR fidelity, and realism--tailored to the input text. Each criterion is independently evaluated by a multimodal judge (e.g., o4-mini), and a prompt-adaptive weighting mechanism emphasizes the most relevant dimensions. This design not only produces interpretable and modular supervision signals for policy optimization (e.g., GRPO or PPO), but also enables users to directly adjust which aspects to reward or penalize. Experiments with an autoregressive text-to-image model demonstrate that RubricRL improves prompt faithfulness, visual detail, and generalizability, while offering a flexible and extensible foundation for interpretable RL alignment across text-to-image architectures.

