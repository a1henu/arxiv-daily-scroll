---
layout: default
title: BLM-Guard: Explainable Multimodal Ad Moderation with Chain-of-Thought and Policy-Aligned Rewards
---

# BLM-Guard: Explainable Multimodal Ad Moderation with Chain-of-Thought and Policy-Aligned Rewards
**arXiv**：[2602.18193v1](https://arxiv.org/abs/2602.18193) · [PDF](https://arxiv.org/pdf/2602.18193.pdf)  
**作者**：Yiran Yang, Zhaowei Liu, Yuan Yuan, Yukun Song, Xiong Ma, Yinghao Song, Xiangji Zeng, Lu Sun, Yulu Wang, Hai Zhou, Shuai Cui, Zhaohan Gong, Jiefei Zhang  

**一句话要点**：提出BLM-Guard框架，通过链式思维推理与策略对齐奖励，解决短视频广告多模态内容审核问题。

**关键词**：多模态内容审核, 链式思维推理, 强化学习, 策略对齐奖励, 短视频广告, 数据合成

## 3 点简述
- 核心问题：短视频广告中视觉、语音和字幕的欺骗性内容需要比社区安全过滤器更细粒度的策略驱动审核。
- 方法要点：结合链式思维推理、基于规则的策略原则和批评者引导的奖励，采用多任务架构建模模态内操纵和跨模态不匹配。
- 实验或效果：在真实短视频广告数据集上，BLM-Guard在准确性、一致性和泛化性方面超越强基线。

## 摘要（原文）

> Short-video platforms now host vast multimodal ads whose deceptive visuals, speech and subtitles demand finer-grained, policy-driven moderation than community safety filters. We present BLM-Guard, a content-audit framework for commercial ads that fuses Chain-of-Thought reasoning with rule-based policy principles and a critic-guided reward. A rule-driven ICoT data-synthesis pipeline jump-starts training by generating structured scene descriptions, reasoning chains and labels, cutting annotation costs. Reinforcement learning then refines the model using a composite reward balancing causal coherence with policy adherence. A multitask architecture models intra-modal manipulations (e.g., exaggerated imagery) and cross-modal mismatches (e.g., subtitle-speech drift), boosting robustness. Experiments on real short-video ads show BLM-Guard surpasses strong baselines in accuracy, consistency and generalization.

