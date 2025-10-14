---
layout: default
title: Connecting Giants: Synergistic Knowledge Transfer of Large Multimodal Models for Few-Shot Learning
---

# Connecting Giants: Synergistic Knowledge Transfer of Large Multimodal Models for Few-Shot Learning
**arXiv**：[2510.11115v1](https://arxiv.org/abs/2510.11115) · [PDF](https://arxiv.org/pdf/2510.11115.pdf)  
**作者**：Hao Tang, Shengfeng He, Jing Qin  

**一句话要点**：提出SynTrans框架，通过大模型知识转移增强少样本学习性能

**关键词**：少样本学习, 知识蒸馏, 多模态模型, 视觉语义桥接, 分类器构建

## 3 点简述
- 少样本学习面临数据稀缺和噪声问题，现有方法易引入偏差
- 利用CLIP作为教师模型，通过无监督代理任务蒸馏视觉知识
- 在四个数据集上实验，显著优于当前最优方法

## 摘要（原文）

> Few-shot learning (FSL) addresses the challenge of classifying novel classes
> with limited training samples. While some methods leverage semantic knowledge
> from smaller-scale models to mitigate data scarcity, these approaches often
> introduce noise and bias due to the data's inherent simplicity. In this paper,
> we propose a novel framework, Synergistic Knowledge Transfer (SynTrans), which
> effectively transfers diverse and complementary knowledge from large multimodal
> models to empower the off-the-shelf few-shot learner. Specifically, SynTrans
> employs CLIP as a robust teacher and uses a few-shot vision encoder as a weak
> student, distilling semantic-aligned visual knowledge via an unsupervised proxy
> task. Subsequently, a training-free synergistic knowledge mining module
> facilitates collaboration among large multimodal models to extract high-quality
> semantic knowledge. Building upon this, a visual-semantic bridging module
> enables bi-directional knowledge transfer between visual and semantic spaces,
> transforming explicit visual and implicit semantic knowledge into
> category-specific classifier weights. Finally, SynTrans introduces a visual
> weight generator and a semantic weight reconstructor to adaptively construct
> optimal multimodal FSL classifiers. Experimental results on four FSL datasets
> demonstrate that SynTrans, even when paired with a simple few-shot vision
> encoder, significantly outperforms current state-of-the-art methods.

