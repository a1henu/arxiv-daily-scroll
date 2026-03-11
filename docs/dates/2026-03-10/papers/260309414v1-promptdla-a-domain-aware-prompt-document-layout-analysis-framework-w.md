---
layout: default
title: PromptDLA: A Domain-aware Prompt Document Layout Analysis Framework with Descriptive Knowledge as a Cue
---

# PromptDLA: A Domain-aware Prompt Document Layout Analysis Framework with Descriptive Knowledge as a Cue
**arXiv**：[2603.09414v1](https://arxiv.org/abs/2603.09414) · [PDF](https://arxiv.org/pdf/2603.09414.pdf)  
**作者**：Zirui Zhang, Yaping Zhang, Lu Xiang, Yang Zhao, Feifei Zhai, Yu Zhou, Chengqing Zong  

**一句话要点**：提出PromptDLA框架，利用描述性知识作为提示，解决多领域文档布局分析中因忽略领域差异导致的性能下降问题。

**关键词**：文档布局分析, 领域感知, 提示学习, 多领域泛化, 描述性知识

## 3 点简述
- 核心问题：现有方法直接合并多领域数据集训练，忽视布局结构差异，导致模型性能不佳。
- 方法要点：设计领域感知提示器，基于数据域属性定制提示，引导模型关注关键特征和结构。
- 实验或效果：在DocLayNet、PubLayNet、M6Doc和D$^4$LA数据集上实现最先进性能。

## 摘要（原文）

> Document Layout Analysis (DLA) is crucial for document artificial intelligence and has recently received increasing attention, resulting in an influx of large-scale public DLA datasets. Existing work often combines data from various domains in recent public DLA datasets to improve the generalization of DLA. However, directly merging these datasets for training often results in suboptimal model performance, as it overlooks the different layout structures inherent to various domains. These variations include different labeling styles, document types, and languages. This paper introduces PromptDLA, a domain-aware Prompter for Document Layout Analysis that effectively leverages descriptive knowledge as cues to integrate domain priors into DLA. The innovative PromptDLA features a unique domain-aware prompter that customizes prompts based on the specific attributes of the data domain. These prompts then serve as cues that direct the DLA toward critical features and structures within the data, enhancing the model's ability to generalize across varied domains. Extensive experiments show that our proposal achieves state-of-the-art performance among DocLayNet, PubLayNet, M6Doc, and D$^4$LA. Our code is available at https://github.com/Zirui00/PromptDLA.

