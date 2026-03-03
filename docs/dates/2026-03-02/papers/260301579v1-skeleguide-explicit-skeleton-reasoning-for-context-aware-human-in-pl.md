---
layout: default
title: SkeleGuide: Explicit Skeleton Reasoning for Context-Aware Human-in-Place Image Synthesis
---

# SkeleGuide: Explicit Skeleton Reasoning for Context-Aware Human-in-Place Image Synthesis
**arXiv**：[2603.01579v1](https://arxiv.org/abs/2603.01579) · [PDF](https://arxiv.org/pdf/2603.01579.pdf)  
**作者**：Chuqiao Wu, Jin Song, Yiyun Fei  

**一句话要点**：提出SkeleGuide框架，通过显式骨骼推理解决场景中人像合成的结构失真问题

**关键词**：人像合成, 骨骼推理, 结构先验, 姿态编辑, 上下文感知

## 3 点简述
- 核心问题：现有生成模型在场景中人像合成中常产生肢体扭曲和姿态不自然等结构失真
- 方法要点：基于显式骨骼推理，联合训练推理与渲染阶段，生成内部姿态作为结构先验
- 实验或效果：在生成高保真、上下文感知的人像方面显著优于专业和通用模型

## 摘要（原文）

> Generating realistic and structurally plausible human images into existing scenes remains a significant challenge for current generative models, which often produce artifacts like distorted limbs and unnatural poses. We attribute this systemic failure to an inability to perform explicit reasoning over human skeletal structure. To address this, we introduce SkeleGuide, a novel framework built upon explicit skeletal reasoning. Through joint training of its reasoning and rendering stages, SkeleGuide learns to produce an internal pose that acts as a strong structural prior, guiding the synthesis towards high structural integrity. For fine-grained user control, we introduce PoseInverter, a module that decodes this internal latent pose into an explicit and editable format. Extensive experiments demonstrate that SkeleGuide significantly outperforms both specialized and general-purpose models in generating high-fidelity, contextually-aware human images. Our work provides compelling evidence that explicitly modeling skeletal structure is a fundamental step towards robust and plausible human image synthesis.

