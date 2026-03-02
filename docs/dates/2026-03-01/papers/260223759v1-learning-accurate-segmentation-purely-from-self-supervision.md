---
layout: default
title: Learning Accurate Segmentation Purely from Self-Supervision
---

# Learning Accurate Segmentation Purely from Self-Supervision
**arXiv**：[2602.23759v1](https://arxiv.org/abs/2602.23759) · [PDF](https://arxiv.org/pdf/2602.23759.pdf)  
**作者**：Zuyao You, Zuxuan Wu, Yu-Gang Jiang  

**一句话要点**：提出Selfment框架，通过完全自监督实现无标注图像的前景对象分割。

**关键词**：自监督分割, 图割优化, 零样本泛化, 前景检测, 无标注学习

## 3 点简述
- 核心问题：无需人工标注或预训练模型，实现准确的前景对象分割。
- 方法要点：基于自监督特征构建图，通过NCut和IPO迭代优化分割掩码。
- 实验或效果：在多个基准上达到SoTA，零样本泛化至伪装对象检测任务。

## 摘要（原文）

> Accurately segmenting objects without any manual annotations remains one of the core challenges in computer vision. In this work, we introduce Selfment, a fully self-supervised framework that segments foreground objects directly from raw images without human labels, pretrained segmentation models, or any post-processing. Selfment first constructs patch-level affinity graphs from self-supervised features and applies NCut to obtain an initial coarse foreground--background separation. We then introduce Iterative Patch Optimization (IPO), a feature-space refinement procedure that progressively enforces spatial coherence and semantic consistency through iterative patch clustering. The refined masks are subsequently used as supervisory signals to train a lightweight segmentation head with contrastive and region-consistency objectives, allowing the model to learn stable and transferable object representations. Despite its simplicity and complete absence of manual supervision, Selfment sets new state-of-the-art (SoTA) results across multiple benchmarks. It achieves substantial improvements on $F_{\max}$ over previous unsupervised saliency detection methods on ECSSD ($+4.0\%$), HKUIS ($+4.6\%$), and PASCAL-S ($+5.7\%$). Moreover, without any additional fine-tuning, Selfment demonstrates remarkable zero-shot generalization to camouflaged object detection tasks (e.g., $0.910$ $S_m$ on CHAMELEON and $0.792$ $F_β^ω$ on CAMO), outperforming all existing unsupervised approaches and even rivaling the SoTA fully supervised methods.

