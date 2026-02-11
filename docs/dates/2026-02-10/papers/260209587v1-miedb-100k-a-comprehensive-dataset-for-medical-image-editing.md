---
layout: default
title: MieDB-100k: A Comprehensive Dataset for Medical Image Editing
---

# MieDB-100k: A Comprehensive Dataset for Medical Image Editing
**arXiv**：[2602.09587v1](https://arxiv.org/abs/2602.09587) · [PDF](https://arxiv.org/pdf/2602.09587.pdf)  
**作者**：Yongfan Lai, Wen Qian, Bo Liu, Hongyan Li, Hao Luo, Fan Wang, Bohan Zhuang, Shenda Hong  

**一句话要点**：提出MieDB-100k数据集以解决医学图像编辑中高质量数据稀缺问题

**关键词**：医学图像编辑, 多模态生成模型, 数据集构建, 文本引导编辑, 临床保真度

## 3 点简述
- 核心问题：现有医学图像编辑数据集多样性不足，忽视医学理解，难以平衡质量与规模。
- 方法要点：通过专家模型与规则合成构建大规模高质量数据集，涵盖感知、修改和转换任务。
- 实验或效果：基于该数据集训练的模型在实验中优于开源和专有模型，展现强泛化能力。

## 摘要（原文）

> The scarcity of high-quality data remains a primary bottleneck in adapting multimodal generative models for medical image editing. Existing medical image editing datasets often suffer from limited diversity, neglect of medical image understanding and inability to balance quality with scalability. To address these gaps, we propose MieDB-100k, a large-scale, high-quality and diverse dataset for text-guided medical image editing. It categorizes editing tasks into perspectives of Perception, Modification and Transformation, considering both understanding and generation abilities. We construct MieDB-100k via a data curation pipeline leveraging both modality-specific expert models and rule-based data synthetic methods, followed by rigorous manual inspection to ensure clinical fidelity. Extensive experiments demonstrate that model trained with MieDB-100k consistently outperform both open-source and proprietary models while exhibiting strong generalization ability. We anticipate that this dataset will serve as a cornerstone for future advancements in specialized medical image editing.

