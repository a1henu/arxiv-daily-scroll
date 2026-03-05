---
layout: default
title: Underrepresented in Foundation Model Pretraining Data? A One-Shot Probe
---

# Underrepresented in Foundation Model Pretraining Data? A One-Shot Probe
**arXiv**：[2603.04346v1](https://arxiv.org/abs/2603.04346) · [PDF](https://arxiv.org/pdf/2603.04346.pdf)  
**作者**：Chris Vorster, Mayug Maniparambil, Noel E. O'Connor, Noel Murphy, Derek Molloy  

**一句话要点**：提出单样本探针方法以预测视觉语言基础模型在未标注领域的零样本准确率

**关键词**：视觉语言基础模型, 零样本评估, 单样本学习, 反事实生成, 嵌入空间分析, 数据高效方法

## 3 点简述
- 核心问题：视觉语言基础模型在未标注或代表性不足领域性能评估困难，缺乏标注测试集
- 方法要点：利用大语言模型生成反事实描述，基于嵌入空间相似度特征预测零样本准确率
- 实验或效果：在五个数据集上实现皮尔逊相关系数0.96，包括非洲代表性不足数据集

## 摘要（原文）

> Large-scale Vision-Language Foundation Models (VLFMs), such as CLIP, now underpin a wide range of computer vision research and applications. VLFMs are often adapted to various domain-specific tasks. However, VLFM performance on novel, specialised, or underrepresented domains remains inconsistent. Evaluating VLFMs typically requires labelled test sets, which are often unavailable for niche domains of interest, particularly those from the Global South. We address this gap by proposing a highly data-efficient method to predict a VLFM's zero-shot accuracy on a target domain using only a single labelled image per class. Our approach uses a Large Language Model to generate plausible counterfactual descriptions of a given image. By measuring the VLFM's ability to distinguish the correct description from these hard negatives, we engineer features that capture the VLFM's discriminative power in its shared embedding space. A linear regressor trained on these similarity scores estimates the VLFM's zero-shot test accuracy across various visual domains with a Pearson-r correlation of 0.96. We demonstrate our method's performance across five diverse datasets, including standard benchmark datasets and underrepresented datasets from Africa. Our work provides a low-cost, reliable tool for probing VLFMs, enabling researchers and practitioners to make informed decisions about data annotation efforts before committing significant resources. The model training code, generated captions and counterfactuals are released here: https://github.com/chris-vorster/PreLabellingProbe.

