---
layout: default
title: BioMedGPT-Mol: Multi-task Learning for Molecular Understanding and Generation
---

# BioMedGPT-Mol: Multi-task Learning for Molecular Understanding and Generation
**arXiv**：[2512.04629v1](https://arxiv.org/abs/2512.04629) · [PDF](https://arxiv.org/pdf/2512.04629.pdf)  
**作者**：Chenyang Zuo, Siqi Fan, Zaiqing Nie  

**一句话要点**：提出BioMedGPT-Mol，通过多任务学习框架将通用推理模型高效适配于分子理解与生成任务。

**关键词**：分子语言模型, 多任务学习, 分子理解, 分子生成, 逆合成规划, 生物医学应用

## 3 点简述
- 核心问题：探索如何将通用语言模型高效适配于分子科学应用，以支持分子理解与生成。
- 方法要点：通过整合公共指令数据集构建大规模高质量训练集，并设计多任务学习框架进行微调。
- 实验或效果：在LlaSMol、TOMG-Bench和MuMOInstruct基准上表现优异，并展示在逆合成规划任务中的竞争力。

## 摘要（原文）

> Molecules play a crucial role in biomedical research and discovery, particularly in the field of small molecule drug development. Given the rapid advancements in large language models, especially the recent emergence of reasoning models, it is natural to explore how a general-purpose language model can be efficiently adapted for molecular science applications. In this work, we introduce BioMedGPT-Mol, a molecular language model designed to support molecular understanding and generation tasks. By curating and unifying existing public instruction datasets, we have assembled a large-scale, comprehensive, and high-quality training dataset. The model is then fine-tuned through a meticulously designed multi-task learning framework. On a consolidated benchmark derived from LlaSMol, TOMG-Bench, and MuMOInstruct, BioMedGPT-Mol achieves remarkable performance. Our experimental results demonstrate that a general-purpose reasoning model can be effectively and efficiently post-trained into a professional molecular language model through a well-structured multi-task curriculum. Leveraging the power of it, we further explore retrosynthetic planning task, and the performance on RetroBench demonstrates its competitive capability of acting as an end-to-end retrosynthetic planner. We anticipate that our approach can be extended to other biomedical scientific domains.

