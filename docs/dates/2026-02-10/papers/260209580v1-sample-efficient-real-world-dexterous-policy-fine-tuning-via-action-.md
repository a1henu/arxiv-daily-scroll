---
layout: default
title: Sample-Efficient Real-World Dexterous Policy Fine-Tuning via Action-Chunked Critics and Normalizing Flows
---

# Sample-Efficient Real-World Dexterous Policy Fine-Tuning via Action-Chunked Critics and Normalizing Flows
**arXiv**：[2602.09580v1](https://arxiv.org/abs/2602.09580) · [PDF](https://arxiv.org/pdf/2602.09580.pdf)  
**作者**：Chenyu Yang, Denis Tarasov, Davide Liconti, Hehui Zheng, Robert K. Katzschmann  

**一句话要点**：提出SOFT-FLOW框架，结合归一化流与动作分块评论家，实现真实世界灵巧策略的高效微调。

**关键词**：灵巧操作, 策略微调, 归一化流, 动作分块, 样本效率, 真实机器人

## 3 点简述
- 核心问题：真实世界灵巧操作策略微调面临样本效率低、动作分布多模态及分块执行下的信用分配困难。
- 方法要点：使用归一化流策略提供精确似然，支持保守更新；引入动作分块评论家，改善长期信用分配。
- 实验或效果：在剪刀剪胶带和手掌下立方体旋转任务中，SOFT-FLOW实现稳定高效适应，优于标准方法。

## 摘要（原文）

> Real-world fine-tuning of dexterous manipulation policies remains challenging due to limited real-world interaction budgets and highly multimodal action distributions. Diffusion-based policies, while expressive, do not permit conservative likelihood-based updates during fine-tuning because action probabilities are intractable. In contrast, conventional Gaussian policies collapse under multimodality, particularly when actions are executed in chunks, and standard per-step critics fail to align with chunked execution, leading to poor credit assignment. We present SOFT-FLOW, a sample-efficient off-policy fine-tuning framework with normalizing flow (NF) to address these challenges. The normalizing flow policy yields exact likelihoods for multimodal action chunks, allowing conservative, stable policy updates through likelihood regularization and thereby improving sample efficiency. An action-chunked critic evaluates entire action sequences, aligning value estimation with the policy's temporal structure and improving long-horizon credit assignment. To our knowledge, this is the first demonstration of a likelihood-based, multimodal generative policy combined with chunk-level value learning on real robotic hardware. We evaluate SOFT-FLOW on two challenging dexterous manipulation tasks in the real world: cutting tape with scissors retrieved from a case, and in-hand cube rotation with a palm-down grasp -- both of which require precise, dexterous control over long horizons. On these tasks, SOFT-FLOW achieves stable, sample-efficient adaptation where standard methods struggle.

