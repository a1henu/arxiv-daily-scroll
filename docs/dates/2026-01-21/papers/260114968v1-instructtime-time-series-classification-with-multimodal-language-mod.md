---
layout: default
title: InstructTime++: Time Series Classification with Multimodal Language Modeling via Implicit Feature Enhancement
---

# InstructTime++: Time Series Classification with Multimodal Language Modeling via Implicit Feature Enhancement
**arXiv**：[2601.14968v1](https://arxiv.org/abs/2601.14968) · [PDF](https://arxiv.org/pdf/2601.14968.pdf)  
**作者**：Mingyue Cheng, Xiaoyu Tao, Huajian Zhang, Qi Liu, Enhong Chen  

**一句话要点**：提出InstructTime++框架，通过隐式特征增强的多模态语言建模解决时间序列分类问题。

**关键词**：时间序列分类, 多模态语言建模, 隐式特征增强, 生成式任务, 跨模态对齐

## 3 点简述
- 现有方法直接映射序列到标签，难以整合上下文特征和捕捉类别语义关系。
- 将分类重构为多模态生成任务，利用离散化、对齐和预训练策略桥接模态差异。
- 通过隐式特征建模增强语言模型，在多个基准数据集上展示优越性能。

## 摘要（原文）

> Most existing time series classification methods adopt a discriminative paradigm that maps input sequences directly to one-hot encoded class labels. While effective, this paradigm struggles to incorporate contextual features and fails to capture semantic relationships among classes. To address these limitations, we propose InstructTime, a novel framework that reformulates time series classification as a multimodal generative task. Specifically, continuous numerical sequences, contextual textual features, and task instructions are treated as multimodal inputs, while class labels are generated as textual outputs by tuned language models. To bridge the modality gap, InstructTime introduces a time series discretization module that converts continuous sequences into discrete temporal tokens, together with an alignment projection layer and a generative self-supervised pre-training strategy to enhance cross-modal representation alignment. Building upon this framework, we further propose InstructTime++, which extends InstructTime by incorporating implicit feature modeling to compensate for the limited inductive bias of language models. InstructTime++ leverages specialized toolkits to mine informative implicit patterns from raw time series and contextual inputs, including statistical feature extraction and vision-language-based image captioning, and translates them into textual descriptions for seamless integration. Extensive experiments on multiple benchmark datasets demonstrate the superior performance of InstructTime++.

