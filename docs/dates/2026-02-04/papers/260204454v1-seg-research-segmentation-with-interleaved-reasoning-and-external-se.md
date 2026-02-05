---
layout: default
title: Seg-ReSearch: Segmentation with Interleaved Reasoning and External Search
---

# Seg-ReSearch: Segmentation with Interleaved Reasoning and External Search
**arXiv**：[2602.04454v1](https://arxiv.org/abs/2602.04454) · [PDF](https://arxiv.org/pdf/2602.04454.pdf)  
**作者**：Tianming Liang, Qirui Du, Jian-Fang Hu, Haichao Jiang, Zicheng Lin, Wei-Shi Zheng  

**一句话要点**：提出Seg-ReSearch以解决基于语言的图像分割中MLLMs知识冻结限制动态开放世界查询的问题

**关键词**：图像分割, 多模态大语言模型, 外部知识搜索, 分层奖励设计, 视频对象分割, 开放世界查询

## 3 点简述
- 核心问题：现有基于多模态大语言模型的图像分割方法受限于其内部冻结知识，难以处理涉及最新信息或领域特定概念的动态开放世界查询。
- 方法要点：Seg-ReSearch通过交织推理与外部搜索，突破知识瓶颈，并采用分层奖励设计协调初始指导与渐进激励，以缓解稀疏结果信号与严格逐步监督间的困境。
- 实验或效果：在OK-VOS基准及两个现有推理分割基准上，Seg-ReSearch显著提升了最先进方法的性能。

## 摘要（原文）

> Segmentation based on language has been a popular topic in computer vision. While recent advances in multimodal large language models (MLLMs) have endowed segmentation systems with reasoning capabilities, these efforts remain confined by the frozen internal knowledge of MLLMs, which limits their potential for real-world scenarios that involve up-to-date information or domain-specific concepts. In this work, we propose \textbf{Seg-ReSearch}, a novel segmentation paradigm that overcomes the knowledge bottleneck of existing approaches. By enabling interleaved reasoning and external search, Seg-ReSearch empowers segmentation systems to handle dynamic, open-world queries that extend beyond the frozen knowledge of MLLMs. To effectively train this capability, we introduce a hierarchical reward design that harmonizes initial guidance with progressive incentives, mitigating the dilemma between sparse outcome signals and rigid step-wise supervision. For evaluation, we construct OK-VOS, a challenging benchmark that explicitly requires outside knowledge for video object segmentation. Experiments on OK-VOS and two existing reasoning segmentation benchmarks demonstrate that our Seg-ReSearch improves state-of-the-art approaches by a substantial margin. Code and data will be released at https://github.com/iSEE-Laboratory/Seg-ReSearch.

