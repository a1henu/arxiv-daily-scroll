---
layout: default
title: PEGAsus: 3D Personalization of Geometry and Appearance
---

# PEGAsus: 3D Personalization of Geometry and Appearance
**arXiv**：[2602.08198v1](https://arxiv.org/abs/2602.08198) · [PDF](https://arxiv.org/pdf/2602.08198.pdf)  
**作者**：Jingyu Hu, Bin Hu, Ka-Hei Hui, Haipeng Li, Zhengzhe Liu, Daniel Cohen-Or, Chi-Wing Fu  

**一句话要点**：提出PEGAsus框架，通过几何与外观概念学习实现个性化3D形状生成。

**关键词**：3D形状生成, 个性化建模, 几何外观解耦, 概念学习, 跨类别合成

## 3 点简述
- 核心问题：从参考形状中提取可重用、类别无关的几何与外观属性，并与文本结合生成新形状。
- 方法要点：采用渐进优化策略，解耦几何与外观概念学习，并支持区域级概念提取。
- 实验或效果：在跨类别场景中实现细粒度控制，定量与定性实验优于现有方法。

## 摘要（原文）

> We present PEGAsus, a new framework capable of generating Personalized 3D shapes by learning shape concepts at both Geometry and Appearance levels. First, we formulate 3D shape personalization as extracting reusable, category-agnostic geometric and appearance attributes from reference shapes, and composing these attributes with text to generate novel shapes. Second, we design a progressive optimization strategy to learn shape concepts at both the geometry and appearance levels, decoupling the shape concept learning process. Third, we extend our approach to region-wise concept learning, enabling flexible concept extraction, with context-aware and context-free losses. Extensive experimental results show that PEGAsus is able to effectively extract attributes from a wide range of reference shapes and then flexibly compose these concepts with text to synthesize new shapes. This enables fine-grained control over shape generation and supports the creation of diverse, personalized results, even in challenging cross-category scenarios. Both quantitative and qualitative experiments demonstrate that our approach outperforms existing state-of-the-art solutions.

