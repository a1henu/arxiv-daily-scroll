---
layout: default
title: Are Object-Centric Representations Better At Compositional Generalization?
---

# Are Object-Centric Representations Better At Compositional Generalization?
**arXiv**：[2602.16689v1](https://arxiv.org/abs/2602.16689) · [PDF](https://arxiv.org/pdf/2602.16689.pdf)  
**作者**：Ferdinand Kapl, Amir Mohammad Karimi Mamaghan, Maximilian Seitzer, Karl Henrik Johansson, Carsten Marr, Stefan Bauer, Andrea Dittadi  

**一句话要点**：提出视觉问答基准，评估对象中心表示在组合泛化中的优势与限制。

**关键词**：组合泛化, 对象中心表示, 视觉问答, 基准评估, 视觉编码器

## 3 点简述
- 核心问题：对象中心表示是否在视觉丰富场景中支持组合泛化。
- 方法要点：在三个可控视觉世界构建基准，公平比较密集与对象中心编码器。
- 实验或效果：对象中心表示在困难设置中更优，但密集表示在数据充足时可能超越。

## 摘要（原文）

> Compositional generalization, the ability to reason about novel combinations of familiar concepts, is fundamental to human cognition and a critical challenge for machine learning. Object-centric (OC) representations, which encode a scene as a set of objects, are often argued to support such generalization, but systematic evidence in visually rich settings is limited. We introduce a Visual Question Answering benchmark across three controlled visual worlds (CLEVRTex, Super-CLEVR, and MOVi-C) to measure how well vision encoders, with and without object-centric biases, generalize to unseen combinations of object properties. To ensure a fair and comprehensive comparison, we carefully account for training data diversity, sample size, representation size, downstream model capacity, and compute. We use DINOv2 and SigLIP2, two widely used vision encoders, as the foundation models and their OC counterparts. Our key findings reveal that (1) OC approaches are superior in harder compositional generalization settings; (2) original dense representations surpass OC only on easier settings and typically require substantially more downstream compute; and (3) OC models are more sample efficient, achieving stronger generalization with fewer images, whereas dense encoders catch up or surpass them only with sufficient data and diversity. Overall, object-centric representations offer stronger compositional generalization when any one of dataset size, training data diversity, or downstream compute is constrained.

