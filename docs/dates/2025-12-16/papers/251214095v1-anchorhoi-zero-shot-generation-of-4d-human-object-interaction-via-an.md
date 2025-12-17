---
layout: default
title: AnchorHOI: Zero-shot Generation of 4D Human-Object Interaction via Anchor-based Prior Distillation
---

# AnchorHOI: Zero-shot Generation of 4D Human-Object Interaction via Anchor-based Prior Distillation
**arXiv**：[2512.14095v1](https://arxiv.org/abs/2512.14095) · [PDF](https://arxiv.org/pdf/2512.14095.pdf)  
**作者**：Sisi Dai, Kai Xu  

**一句话要点**：提出AnchorHOI框架，通过锚点先验蒸馏解决零样本4D人-物交互生成中的交互线索不足问题。

**关键词**：4D人-物交互生成, 零样本学习, 先验蒸馏, 锚点引导, 视频扩散模型, 神经辐射场

## 3 点简述
- 核心问题：现有零样本4D HOI生成方法因交互线索蒸馏不足，限制了多样场景的适用性。
- 方法要点：引入锚点先验蒸馏策略，设计锚点NeRF和关键点，分两步引导生成以优化高维4D HOI。
- 实验或效果：实验显示AnchorHOI在多样性和泛化性上优于先前方法，但具体数据集和指标未知。

## 摘要（原文）

> Despite significant progress in text-driven 4D human-object interaction (HOI) generation with supervised methods, the scalability remains limited by the scarcity of large-scale 4D HOI datasets. To overcome this, recent approaches attempt zero-shot 4D HOI generation with pre-trained image diffusion models. However, interaction cues are minimally distilled during the generation process, restricting their applicability across diverse scenarios. In this paper, we propose AnchorHOI, a novel framework that thoroughly exploits hybrid priors by incorporating video diffusion models beyond image diffusion models, advancing 4D HOI generation. Nevertheless, directly optimizing high-dimensional 4D HOI with such priors remains challenging, particularly for human pose and compositional motion. To address this challenge, AnchorHOI introduces an anchor-based prior distillation strategy, which constructs interaction-aware anchors and then leverages them to guide generation in a tractable two-step process. Specifically, two tailored anchors are designed for 4D HOI generation: anchor Neural Radiance Fields (NeRFs) for expressive interaction composition, and anchor keypoints for realistic motion synthesis. Extensive experiments demonstrate that AnchorHOI outperforms previous methods with superior diversity and generalization.

