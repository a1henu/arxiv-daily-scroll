---
layout: default
title: ImagerySearch: Adaptive Test-Time Search for Video Generation Beyond Semantic Dependency Constraints
---

# ImagerySearch: Adaptive Test-Time Search for Video Generation Beyond Semantic Dependency Constraints
**arXiv**：[2510.14847v1](https://arxiv.org/abs/2510.14847) · [PDF](https://arxiv.org/pdf/2510.14847.pdf)  
**作者**：Meiqi Wu, Jiashu Zhu, Xiaokun Feng, Chubin Chen, Chen Zhu, Bingze Song, Fangyuan Mao, Jiahong Wu, Xiangxiang Chu, Kaiqi Huang  

**一句话要点**：提出ImagerySearch自适应测试时搜索策略以提升想象力场景视频生成质量

**关键词**：视频生成, 测试时搜索, 自适应策略, 长距离语义, 想象力场景, 基准评估

## 3 点简述
- 核心问题：视频生成模型在想象力场景中性能下降，因提示包含罕见共现概念和长距离语义关系。
- 方法要点：动态调整推理搜索空间和奖励函数，适应提示语义关系，提升视频连贯性和视觉合理性。
- 实验或效果：在LDT-Bench和VBench上优于基线方法，验证了策略的有效性和泛化能力。

## 摘要（原文）

> Video generation models have achieved remarkable progress, particularly
> excelling in realistic scenarios; however, their performance degrades notably
> in imaginative scenarios. These prompts often involve rarely co-occurring
> concepts with long-distance semantic relationships, falling outside training
> distributions. Existing methods typically apply test-time scaling for improving
> video quality, but their fixed search spaces and static reward designs limit
> adaptability to imaginative scenarios. To fill this gap, we propose
> ImagerySearch, a prompt-guided adaptive test-time search strategy that
> dynamically adjusts both the inference search space and reward function
> according to semantic relationships in the prompt. This enables more coherent
> and visually plausible videos in challenging imaginative settings. To evaluate
> progress in this direction, we introduce LDT-Bench, the first dedicated
> benchmark for long-distance semantic prompts, consisting of 2,839 diverse
> concept pairs and an automated protocol for assessing creative generation
> capabilities. Extensive experiments show that ImagerySearch consistently
> outperforms strong video generation baselines and existing test-time scaling
> approaches on LDT-Bench, and achieves competitive improvements on VBench,
> demonstrating its effectiveness across diverse prompt types. We will release
> LDT-Bench and code to facilitate future research on imaginative video
> generation.

