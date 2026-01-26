---
layout: default
title: CORD: Bridging the Audio-Text Reasoning Gap via Weighted On-policy Cross-modal Distillation
---

# CORD: Bridging the Audio-Text Reasoning Gap via Weighted On-policy Cross-modal Distillation
**arXiv**：[2601.16547v1](https://arxiv.org/abs/2601.16547) · [PDF](https://arxiv.org/pdf/2601.16547.pdf)  
**作者**：Jing Hu, Danxiang Zhu, Xianlong Luo, Dan Zhang, Shuwei He, Yishu Lei, Haitao Zheng, Shikun Feng, Jingzhou He, Yu Sun, Hua Wu, Haifeng Wang  

**一句话要点**：提出CORD框架，通过加权在线跨模态蒸馏解决音频语言模型中的音频-文本推理差距问题。

**关键词**：音频语言模型, 跨模态对齐, 在线蒸馏, 多粒度优化, 推理能力提升, 数据效率

## 3 点简述
- 核心问题：音频语言模型在知识推理能力上常出现退化，源于特征表示空间中的音频-语义差距未被有效弥合。
- 方法要点：采用在线跨模态自蒸馏，以文本模态为内部教师，在音频生成过程中进行多粒度对齐，包括基于重要性加权的令牌级对齐和基于全局奖励的序列级优化。
- 实验或效果：在多个基准测试中，CORD显著提升音频条件推理性能，仅用80k合成训练样本即大幅缩小音频-文本性能差距，验证了方法的有效性和数据效率。

## 摘要（原文）

> Large Audio Language Models (LALMs) have garnered significant research interest. Despite being built upon text-based large language models (LLMs), LALMs frequently exhibit a degradation in knowledge and reasoning capabilities. We hypothesize that this limitation stems from the failure of current training paradigms to effectively bridge the acoustic-semantic gap within the feature representation space. To address this challenge, we propose CORD, a unified alignment framework that performs online cross-modal self-distillation. Specifically, it aligns audio-conditioned reasoning with its text-conditioned counterpart within a unified model. Leveraging the text modality as an internal teacher, CORD performs multi-granularity alignment throughout the audio rollout process. At the token level, it employs on-policy reverse KL divergence with importance-aware weighting to prioritize early and semantically critical tokens. At the sequence level, CORD introduces a judge-based global reward to optimize complete reasoning trajectories via Group Relative Policy Optimization (GRPO). Empirical results across multiple benchmarks demonstrate that CORD consistently enhances audio-conditioned reasoning and substantially bridges the audio-text performance gap with only 80k synthetic training samples, validating the efficacy and data efficiency of our on-policy, multi-level cross-modal alignment approach.

