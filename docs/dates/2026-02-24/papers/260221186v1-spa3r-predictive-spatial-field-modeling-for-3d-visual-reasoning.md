---
layout: default
title: Spa3R: Predictive Spatial Field Modeling for 3D Visual Reasoning
---

# Spa3R: Predictive Spatial Field Modeling for 3D Visual Reasoning
**arXiv**：[2602.21186v1](https://arxiv.org/abs/2602.21186) · [PDF](https://arxiv.org/pdf/2602.21186.pdf)  
**作者**：Haoyi Jiang, Liu Liu, Xinjie Wang, Yonghao He, Wei Sui, Zhizhong Su, Wenyu Liu, Xinggang Wang  

**一句话要点**：提出Spa3R框架，通过预测性空间场建模从2D图像学习统一空间表示，以提升3D视觉推理能力。

**关键词**：3D视觉推理, 预测性空间场建模, 自监督学习, 视图不变表示, 视觉语言模型增强, 空间智能

## 3 点简述
- 核心问题：现有视觉语言模型在3D空间理解上表现浅层，依赖显式3D模态或几何先验，导致可扩展性差和语言模型负担重。
- 方法要点：基于预测性空间场建模范式，从无姿态多视图图像自监督学习视图不变空间表示，通过轻量适配器集成到视觉语言模型中。
- 实验或效果：在VSI-Bench上，Spa3-VLM达到58.6%的3D视觉问答准确率，优于先前方法，验证了方法的有效性。

## 摘要（原文）

> While Vision-Language Models (VLMs) exhibit exceptional 2D visual understanding, their ability to comprehend and reason about 3D space--a cornerstone of spatial intelligence--remains superficial. Current methodologies attempt to bridge this domain gap either by relying on explicit 3D modalities or by augmenting VLMs with partial, view-conditioned geometric priors. However, such approaches hinder scalability and ultimately burden the language model with the ill-posed task of implicitly reconstructing holistic 3D geometry from sparse cues. In this paper, we argue that spatial intelligence can emerge inherently from 2D vision alone, rather than being imposed via explicit spatial instruction tuning. To this end, we introduce Spa3R, a self-supervised framework that learns a unified, view-invariant spatial representation directly from unposed multi-view images. Spa3R is built upon the proposed Predictive Spatial Field Modeling (PSFM) paradigm, where Spa3R learns to synthesize feature fields for arbitrary unseen views conditioned on a compact latent representation, thereby internalizing a holistic and coherent understanding of the underlying 3D scene. We further integrate the pre-trained Spa3R Encoder into existing VLMs via a lightweight adapter to form Spa3-VLM, effectively grounding language reasoning in a global spatial context. Experiments on the challenging VSI-Bench demonstrate that Spa3-VLM achieves state-of-the-art accuracy of 58.6% on 3D VQA, significantly outperforming prior methods. These results highlight PSFM as a scalable path toward advancing spatial intelligence. Code is available at https://github.com/hustvl/Spa3R.

