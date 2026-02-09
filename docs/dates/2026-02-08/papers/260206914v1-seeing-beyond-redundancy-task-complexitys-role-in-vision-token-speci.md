---
layout: default
title: Seeing Beyond Redundancy: Task Complexity's Role in Vision Token Specialization in VLLMs
---

# Seeing Beyond Redundancy: Task Complexity's Role in Vision Token Specialization in VLLMs
**arXiv**：[2602.06914v1](https://arxiv.org/abs/2602.06914) · [PDF](https://arxiv.org/pdf/2602.06914.pdf)  
**作者**：Darryl Hannan, John Cooper, Dylan White, Yijing Watkins  

**一句话要点**：探究任务复杂度对视觉大语言模型中视觉令牌专业化的影响，以提升复杂视觉任务性能

**关键词**：视觉大语言模型, 视觉冗余, 任务复杂度, 视觉令牌专业化, 合成基准数据集, 微调策略

## 3 点简述
- 核心问题：视觉大语言模型在细粒度视觉信息或空间推理任务上表现不佳，原因可能与视觉冗余有关
- 方法要点：引入合成基准数据集和度量指标，分析视觉信息处理与冗余关系，并基于复杂任务微调模型
- 实验或效果：发现任务复杂度与视觉压缩相关，高复杂度数据比例对改善视觉表示分布和性能至关重要

## 摘要（原文）

> Vision capabilities in vision large language models (VLLMs) have consistently lagged behind their linguistic capabilities. In particular, numerous benchmark studies have demonstrated that VLLMs struggle when fine-grained visual information or spatial reasoning is required. However, we do not yet understand exactly why VLLMs struggle so much with these tasks relative to others. Some works have focused on visual redundancy as an explanation, where high-level visual information is uniformly spread across numerous tokens and specific, fine-grained visual information is discarded. In this work, we investigate this premise in greater detail, seeking to better understand exactly how various types of visual information are processed by the model and what types of visual information are discarded. To do so, we introduce a simple synthetic benchmark dataset that is specifically constructed to probe various visual features, along with a set of metrics for measuring visual redundancy, allowing us to better understand the nuances of their relationship. Then, we explore fine-tuning VLLMs on a number of complex visual tasks to better understand how redundancy and compression change based upon the complexity of the data that a model is trained on. We find that there is a connection between task complexity and visual compression, implying that having a sufficient ratio of high complexity visual data is crucial for altering the way that VLLMs distribute their visual representation and consequently improving their performance on complex visual tasks. We hope that this work will provide valuable insights for training the next generation of VLLMs.

