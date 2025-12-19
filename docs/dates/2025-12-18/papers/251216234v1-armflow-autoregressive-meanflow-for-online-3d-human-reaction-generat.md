---
layout: default
title: ARMFlow: AutoRegressive MeanFlow for Online 3D Human Reaction Generation
---

# ARMFlow: AutoRegressive MeanFlow for Online 3D Human Reaction Generation
**arXiv**：[2512.16234v1](https://arxiv.org/abs/2512.16234) · [PDF](https://arxiv.org/pdf/2512.16234.pdf)  
**作者**：Zichen Geng, Zeeshan Hayder, Wei Liu, Hesheng Wang, Ajmal Mian  

**一句话要点**：提出ARMFlow自回归框架，用于在线3D人体反应生成，解决高保真、实时和自回归适应性问题。

**关键词**：3D人体反应生成, 自回归模型, 在线推理, 误差累积缓解, 实时运动生成, 因果编码

## 3 点简述
- 核心问题：在线3D人体反应生成需同时满足高运动保真度、实时推理和自回归适应性，现有方法难以兼顾。
- 方法要点：基于MeanFlow的自回归框架，包含因果上下文编码器和MLP速度预测器，引入Bootstrap Contextual Encoding减轻误差累积。
- 实验或效果：在线生成在InterHuman和InterX数据集上FID提升超40%，单步推理匹配离线最优性能，延迟低。

## 摘要（原文）

> 3D human reaction generation faces three main challenges:(1) high motion fidelity, (2) real-time inference, and (3) autoregressive adaptability for online scenarios. Existing methods fail to meet all three simultaneously. We propose ARMFlow, a MeanFlow-based autoregressive framework that models temporal dependencies between actor and reactor motions. It consists of a causal context encoder and an MLP-based velocity predictor. We introduce Bootstrap Contextual Encoding (BSCE) in training, encoding generated history instead of the ground-truth ones, to alleviate error accumulation in autoregressive generation. We further introduce the offline variant ReMFlow, achieving state-of-the-art performance with the fastest inference among offline methods. Our ARMFlow addresses key limitations of online settings by: (1) enhancing semantic alignment via a global contextual encoder; (2) achieving high accuracy and low latency in a single-step inference; and (3) reducing accumulated errors through BSCE. Our single-step online generation surpasses existing online methods on InterHuman and InterX by over 40% in FID, while matching offline state-of-the-art performance despite using only partial sequence conditions.

