---
layout: default
title: UniG2U-Bench: Do Unified Models Advance Multimodal Understanding?
---

# UniG2U-Bench: Do Unified Models Advance Multimodal Understanding?
**arXiv**：[2603.03241v1](https://arxiv.org/abs/2603.03241) · [PDF](https://arxiv.org/pdf/2603.03241.pdf)  
**作者**：Zimo Wen, Boxiu Li, Wanbo Zhang, Junxiang Lei, Xiaoyu Chen, Yijia Fan, Qi Zhang, Yujiang Wang, Lili Qiu, Bo Li, Ziwei Liu, Caihua Shan, Yifan Yang, Yifei Shen  

**一句话要点**：提出UniG2U-Bench基准以系统评估生成式统一模型在理解任务中的表现

**关键词**：多模态理解, 生成式模型, 基准评估, 视觉语言模型, 空间智能

## 3 点简述
- 核心问题：生成式统一模型是否及何时能提升多模态理解能力尚不明确
- 方法要点：构建包含7个领域30个子任务的生成到理解评估基准
- 实验效果：发现统一模型通常弱于基础模型，但在空间智能等特定任务中表现提升

## 摘要（原文）

> Unified multimodal models have recently demonstrated strong generative capabilities, yet whether and when generation improves understanding remains unclear. Existing benchmarks lack a systematic exploration of the specific tasks where generation facilitates understanding. To this end, we introduce UniG2U-Bench, a comprehensive benchmark categorizing generation-to-understanding (G2U) evaluation into 7 regimes and 30 subtasks, requiring varying degrees of implicit or explicit visual transformations. Extensive evaluation of over 30 models reveals three core findings: 1) Unified models generally underperform their base Vision-Language Models (VLMs), and Generate-then-Answer (GtA) inference typically degrades performance relative to direct inference. 2) Consistent enhancements emerge in spatial intelligence, visual illusions, or multi-round reasoning subtasks, where enhanced spatial and shape perception, as well as multi-step intermediate image states, prove beneficial. 3) Tasks with similar reasoning structures and models sharing architectures exhibit correlated behaviors, suggesting that generation-understanding coupling induces class-consistent inductive biases over tasks, pretraining data, and model architectures. These findings highlight the necessity for more diverse training data and novel paradigms to fully unlock the potential of unified multimodal modeling.

