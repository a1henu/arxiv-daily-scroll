---
layout: default
title: LongVPO: From Anchored Cues to Self-Reasoning for Long-Form Video Preference Optimization
---

# LongVPO: From Anchored Cues to Self-Reasoning for Long-Form Video Preference Optimization
**arXiv**：[2602.02341v1](https://arxiv.org/abs/2602.02341) · [PDF](https://arxiv.org/pdf/2602.02341.pdf)  
**作者**：Zhenpeng Huang, Jiaqi Li, Zihan Jia, Xinhao Li, Desen Meng, Lingxue Song, Xi Chen, Liang Li, Limin Wang  

**一句话要点**：提出LongVPO两阶段框架，使短上下文视觉语言模型无需长视频标注即可理解超长视频。

**关键词**：长视频理解, 偏好优化, 合成数据, 视觉语言模型, 多段推理

## 3 点简述
- 核心问题：短上下文视觉语言模型难以处理超长视频，且缺乏长视频标注数据。
- 方法要点：第一阶段合成偏好三元组锚定短片段，第二阶段通过递归字幕生成多段推理查询进行偏好对齐。
- 实验或效果：仅用16K合成样本，在多个长视频基准上超越开源模型，保持短视频性能。

## 摘要（原文）

> We present LongVPO, a novel two-stage Direct Preference Optimization framework that enables short-context vision-language models to robustly understand ultra-long videos without any long-video annotations. In Stage 1, we synthesize preference triples by anchoring questions to individual short clips, interleaving them with distractors, and applying visual-similarity and question-specificity filtering to mitigate positional bias and ensure unambiguous supervision. We also approximate the reference model's scoring over long contexts by evaluating only the anchor clip, reducing computational overhead. In Stage 2, we employ a recursive captioning pipeline on long videos to generate scene-level metadata, then use a large language model to craft multi-segment reasoning queries and dispreferred responses, aligning the model's preferences through multi-segment reasoning tasks. With only 16K synthetic examples and no costly human labels, LongVPO outperforms the state-of-the-art open-source models on multiple long-video benchmarks, while maintaining strong short-video performance (e.g., on MVBench), offering a scalable paradigm for efficient long-form video understanding.

