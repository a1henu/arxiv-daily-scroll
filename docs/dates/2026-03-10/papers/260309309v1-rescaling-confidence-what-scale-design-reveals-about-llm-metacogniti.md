---
layout: default
title: Rescaling Confidence: What Scale Design Reveals About LLM Metacognition
---

# Rescaling Confidence: What Scale Design Reveals About LLM Metacognition
**arXiv**：[2603.09309v1](https://arxiv.org/abs/2603.09309) · [PDF](https://arxiv.org/pdf/2603.09309.pdf)  
**作者**：Yuyang Dai  

**一句话要点**：揭示LLM元认知中置信度标尺设计的影响，提出优化方案提升不确定性估计质量

**关键词**：LLM元认知, 置信度标尺设计, 不确定性估计, meta-d'评估, 口头置信度, 标尺优化

## 3 点简述
- 核心问题：LLM口头置信度（如0-100）存在严重离散化，标尺设计未被充分研究，影响不确定性估计准确性。
- 方法要点：系统操纵置信度标尺的粒度、边界位置和范围规律性，使用meta-d'评估元认知敏感性。
- 实验或效果：0-20标尺相比标准0-100提升元认知效率，边界压缩降低性能，圆数偏好持续存在。

## 摘要（原文）

> Verbalized confidence, in which LLMs report a numerical certainty score, is widely used to estimate uncertainty in black-box settings, yet the confidence scale itself (typically 0--100) is rarely examined. We show that this design choice is not neutral. Across six LLMs and three datasets, verbalized confidence is heavily discretized, with more than 78% of responses concentrating on just three round-number values. To investigate this phenomenon, we systematically manipulate confidence scales along three dimensions: granularity, boundary placement, and range regularity, and evaluate metacognitive sensitivity using meta-d'. We find that a 0--20 scale consistently improves metacognitive efficiency over the standard 0--100 format, while boundary compression degrades performance and round-number preferences persist even under irregular ranges. These results demonstrate that confidence scale design directly affects the quality of verbalized uncertainty and should be treated as a first-class experimental variable in LLM evaluation.

