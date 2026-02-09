---
layout: default
title: A neuromorphic model of the insect visual system for natural image processing
---

# A neuromorphic model of the insect visual system for natural image processing
**arXiv**：[2602.06405v1](https://arxiv.org/abs/2602.06405) · [PDF](https://arxiv.org/pdf/2602.06405.pdf)  
**作者**：Adam D. Hines, Karin Nordström, Andrew B. Barron  

**一句话要点**：提出基于昆虫视觉系统的神经形态模型，用于自然图像处理与稀疏编码

**关键词**：昆虫视觉模型, 神经形态计算, 自监督学习, 稀疏编码, 生物启发视觉, 自然图像处理

## 3 点简述
- 核心问题：现有模型忽视生物处理路径，优先任务性能而非生物基础。
- 方法要点：采用自监督对比学习，模拟昆虫视觉系统生成稀疏判别性编码。
- 实验或效果：在花朵识别和自然图像基准测试中表现可靠，优于简单下采样基线。

## 摘要（原文）

> Insect vision supports complex behaviors including associative learning, navigation, and object detection, and has long motivated computational models for understanding biological visual processing. However, many contemporary models prioritize task performance while neglecting biologically grounded processing pathways. Here, we introduce a bio-inspired vision model that captures principles of the insect visual system to transform dense visual input into sparse, discriminative codes. The model is trained using a fully self-supervised contrastive objective, enabling representation learning without labeled data and supporting reuse across tasks without reliance on domain-specific classifiers. We evaluated the resulting representations on flower recognition tasks and natural image benchmarks. The model consistently produced reliable sparse codes that distinguish visually similar inputs. To support different modelling and deployment uses, we have implemented the model as both an artificial neural network and a spiking neural network. In a simulated localization setting, our approach outperformed a simple image downsampling comparison baseline, highlighting the functional benefit of incorporating neuromorphic visual processing pathways. Collectively, these results advance insect computational modelling by providing a generalizable bio-inspired vision model capable of sparse computation across diverse tasks.

