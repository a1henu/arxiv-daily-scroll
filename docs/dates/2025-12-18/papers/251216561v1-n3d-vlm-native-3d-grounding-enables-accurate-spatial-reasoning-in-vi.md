---
layout: default
title: N3D-VLM: Native 3D Grounding Enables Accurate Spatial Reasoning in Vision-Language Models
---

# N3D-VLM: Native 3D Grounding Enables Accurate Spatial Reasoning in Vision-Language Models
**arXiv**：[2512.16561v1](https://arxiv.org/abs/2512.16561) · [PDF](https://arxiv.org/pdf/2512.16561.pdf)  
**作者**：Yuxin Wang, Lei Ke, Boqiang Zhang, Tianyuan Qu, Hanxun Yu, Zhenpeng Huang, Meng Yu, Dan Xu, Dong Yu  

**一句话要点**：提出N3D-VLM框架，通过原生3D物体感知提升视觉语言模型的空间推理能力

**关键词**：3D物体感知, 空间推理, 视觉语言模型, 3D定位, 数据构造

## 3 点简述
- 当前多模态模型缺乏内在3D感知，限制其在3D场景中的空间关系理解能力
- N3D-VLM集成原生3D物体感知与3D感知视觉推理，实现精确3D定位和可解释空间理解
- 实验表明该框架在3D定位和空间推理任务上超越现有方法，达到最先进性能

## 摘要（原文）

> While current multimodal models can answer questions based on 2D images, they lack intrinsic 3D object perception, limiting their ability to comprehend spatial relationships and depth cues in 3D scenes. In this work, we propose N3D-VLM, a novel unified framework that seamlessly integrates native 3D object perception with 3D-aware visual reasoning, enabling both precise 3D grounding and interpretable spatial understanding. Unlike conventional end-to-end models that directly predict answers from RGB/RGB-D inputs, our approach equips the model with native 3D object perception capabilities, enabling it to directly localize objects in 3D space based on textual descriptions. Building upon accurate 3D object localization, the model further performs explicit reasoning in 3D, achieving more interpretable and structured spatial understanding. To support robust training for these capabilities, we develop a scalable data construction pipeline that leverages depth estimation to lift large-scale 2D annotations into 3D space, significantly increasing the diversity and coverage for 3D object grounding data, yielding over six times larger than the largest existing single-image 3D detection dataset. Moreover, the pipeline generates spatial question-answering datasets that target chain-of-thought (CoT) reasoning in 3D, facilitating joint training for both 3D object localization and 3D spatial reasoning. Experimental results demonstrate that our unified framework not only achieves state-of-the-art performance on 3D grounding tasks, but also consistently surpasses existing methods in 3D spatial reasoning in vision-language model.

