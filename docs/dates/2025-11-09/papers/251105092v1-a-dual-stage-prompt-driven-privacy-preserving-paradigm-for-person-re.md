---
layout: default
title: A Dual-stage Prompt-driven Privacy-preserving Paradigm for Person Re-Identification
---

# A Dual-stage Prompt-driven Privacy-preserving Paradigm for Person Re-Identification
**arXiv**：[2511.05092v1](https://arxiv.org/abs/2511.05092) · [PDF](https://arxiv.org/pdf/2511.05092.pdf)  
**作者**：Ruolin Li, Min Liu, Yuan Bian, Zhaoyang Li, Yuzhen Li, Xueping Wang, Yaonan Wang  

**一句话要点**：提出双阶段提示驱动隐私保护范式，解决行人重识别中虚拟数据构建与泛化难题

**关键词**：行人重识别, 隐私保护, 扩散模型, 提示驱动, 域泛化, 对比学习

## 3 点简述
- 核心问题：虚拟数据集构建复杂且泛化能力差，难以用于实际行人重识别场景
- 方法要点：首阶段用多维提示驱动扩散模型合成多样数据；次阶段通过提示驱动解耦机制学习域不变特征
- 实验或效果：在GenePerson数据集上训练模型，泛化性能达到最先进水平，超越真实和虚拟数据集

## 摘要（原文）

> With growing concerns over data privacy, researchers have started using
> virtual data as an alternative to sensitive real-world images for training
> person re-identification (Re-ID) models. However, existing virtual datasets
> produced by game engines still face challenges such as complex construction and
> poor domain generalization, making them difficult to apply in real scenarios.
> To address these challenges, we propose a Dual-stage Prompt-driven
> Privacy-preserving Paradigm (DPPP). In the first stage, we generate rich
> prompts incorporating multi-dimensional attributes such as pedestrian
> appearance, illumination, and viewpoint that drive the diffusion model to
> synthesize diverse data end-to-end, building a large-scale virtual dataset
> named GenePerson with 130,519 images of 6,641 identities. In the second stage,
> we propose a Prompt-driven Disentanglement Mechanism (PDM) to learn
> domain-invariant generalization features. With the aid of contrastive learning,
> we employ two textual inversion networks to map images into pseudo-words
> representing style and content, respectively, thereby constructing
> style-disentangled content prompts to guide the model in learning
> domain-invariant content features at the image level. Experiments demonstrate
> that models trained on GenePerson with PDM achieve state-of-the-art
> generalization performance, surpassing those on popular real and virtual Re-ID
> datasets.

