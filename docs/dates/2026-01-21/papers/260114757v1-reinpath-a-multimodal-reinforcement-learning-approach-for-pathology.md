---
layout: default
title: ReinPath: A Multimodal Reinforcement Learning Approach for Pathology
---

# ReinPath: A Multimodal Reinforcement Learning Approach for Pathology
**arXiv**：[2601.14757v1](https://arxiv.org/abs/2601.14757) · [PDF](https://arxiv.org/pdf/2601.14757.pdf)  
**作者**：Kangcheng Zhou, Jun Jiang, Qing Zhang, Shuang Zheng, Qingli Li, Shugong Xu  

**一句话要点**：提出ReinPath多模态强化学习模型，以增强病理学中的推理能力和可解释性。

**关键词**：病理学多模态学习, 强化学习, 视觉问答, 可解释性, 语义奖励策略, 零样本分类

## 3 点简述
- 核心问题：现有病理学多模态方法因缺乏高质量数据集和简单推理过程，可解释性有限。
- 方法要点：设计语义奖励策略结合群体相对策略优化，提升文本描述的准确性和上下文相关性。
- 实验或效果：在自建高质量病理VQA数据集上，仅用20%数据训练即超越先进方法，零样本图像分类任务性能与CLIP相当。

## 摘要（原文）

> Interpretability is significant in computational pathology, leading to the development of multimodal information integration from histopathological image and corresponding text data.However, existing multimodal methods have limited interpretability due to the lack of high-quality dataset that support explicit reasoning and inference and simple reasoning process.To address the above problems, we introduce a novel multimodal pathology large language model with strong reasoning capabilities.To improve the generation of accurate and contextually relevant textual descriptions, we design a semantic reward strategy integrated with group relative policy optimization.We construct a high-quality pathology visual question answering (VQA) dataset, specifically designed to support complex reasoning tasks.Comprehensive experiments conducted on this dataset demonstrate that our method outperforms state-of-the-art methods, even when trained with only 20% of the data.Our method also achieves comparable performance on downstream zero-shot image classification task compared with CLIP.

