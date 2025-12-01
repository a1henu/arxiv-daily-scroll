---
layout: default
title: Do We Need Perfect Data? Leveraging Noise for Domain Generalized Segmentation
---

# Do We Need Perfect Data? Leveraging Noise for Domain Generalized Segmentation
**arXiv**：[2511.22948v1](https://arxiv.org/abs/2511.22948) · [PDF](https://arxiv.org/pdf/2511.22948.pdf)  
**作者**：Taeyeong Kim, SeungJoon Lee, Jung Uk Kim, MyeongAh Cho  

**一句话要点**：提出FLEX-Seg框架，利用合成数据中的噪声提升语义分割的领域泛化能力。

**关键词**：语义分割, 领域泛化, 噪声利用, 自适应学习, 边界处理

## 3 点简述
- 核心问题：扩散生成数据存在图像与语义掩码错位，影响领域泛化。
- 方法要点：通过多尺度边界原型、不确定性边界强调和难度感知采样，自适应处理噪声。
- 实验或效果：在五个真实数据集上优于现有方法，ACDC和Dark Zurich的mIoU提升超2%。

## 摘要（原文）

> Domain generalization in semantic segmentation faces challenges from domain shifts, particularly under adverse conditions. While diffusion-based data generation methods show promise, they introduce inherent misalignment between generated images and semantic masks. This paper presents FLEX-Seg (FLexible Edge eXploitation for Segmentation), a framework that transforms this limitation into an opportunity for robust learning. FLEX-Seg comprises three key components: (1) Granular Adaptive Prototypes that captures boundary characteristics across multiple scales, (2) Uncertainty Boundary Emphasis that dynamically adjusts learning emphasis based on prediction entropy, and (3) Hardness-Aware Sampling that progressively focuses on challenging examples. By leveraging inherent misalignment rather than enforcing strict alignment, FLEX-Seg learns robust representations while capturing rich stylistic variations. Experiments across five real-world datasets demonstrate consistent improvements over state-of-the-art methods, achieving 2.44% and 2.63% mIoU gains on ACDC and Dark Zurich. Our findings validate that adaptive strategies for handling imperfect synthetic data lead to superior domain generalization. Code is available at https://github.com/VisualScienceLab-KHU/FLEX-Seg.

