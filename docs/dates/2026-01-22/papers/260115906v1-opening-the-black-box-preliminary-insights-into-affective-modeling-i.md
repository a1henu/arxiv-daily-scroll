---
layout: default
title: Opening the Black Box: Preliminary Insights into Affective Modeling in Multimodal Foundation Models
---

# Opening the Black Box: Preliminary Insights into Affective Modeling in Multimodal Foundation Models
**arXiv**：[2601.15906v1](https://arxiv.org/abs/2601.15906) · [PDF](https://arxiv.org/pdf/2601.15906.pdf)  
**作者**：Zhen Zhang, Runhao Zeng, Sicheng Zhao, Xiping Hu  

**一句话要点**：揭示多模态基础模型中情感建模的机制，发现前馈门控投影是关键结构

**关键词**：多模态情感建模, 基础模型机制, 前馈门控投影, 参数效率, 情感理解与生成

## 3 点简述
- 核心问题：多模态基础模型中情感表示的位置和机制尚不明确，影响模型可解释性。
- 方法要点：通过系统机制研究，分析情感导向监督如何重塑内部参数，聚焦于前馈门控投影。
- 实验或效果：实验表明仅调整约24.5%参数即可达到AffectGPT平均性能的96.6%，参数效率高。

## 摘要（原文）

> Understanding where and how emotions are represented in large-scale foundation models remains an open problem, particularly in multimodal affective settings. Despite the strong empirical performance of recent affective models, the internal architectural mechanisms that support affective understanding and generation are still poorly understood. In this work, we present a systematic mechanistic study of affective modeling in multimodal foundation models. Across multiple architectures, training strategies, and affective tasks, we analyze how emotion-oriented supervision reshapes internal model parameters. Our results consistently reveal a clear and robust pattern: affective adaptation does not primarily focus on the attention module, but instead localizes to the feed-forward gating projection (\texttt{gate\_proj}). Through controlled module transfer, targeted single-module adaptation, and destructive ablation, we further demonstrate that \texttt{gate\_proj} is sufficient, efficient, and necessary for affective understanding and generation. Notably, by tuning only approximately 24.5\% of the parameters tuned by AffectGPT, our approach achieves 96.6\% of its average performance across eight affective tasks, highlighting substantial parameter efficiency. Together, these findings provide empirical evidence that affective capabilities in foundation models are structurally mediated by feed-forward gating mechanisms and identify \texttt{gate\_proj} as a central architectural locus of affective modeling.

