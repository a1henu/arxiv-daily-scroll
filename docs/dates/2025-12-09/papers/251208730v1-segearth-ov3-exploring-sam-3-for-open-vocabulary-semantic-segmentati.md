---
layout: default
title: SegEarth-OV3: Exploring SAM 3 for Open-Vocabulary Semantic Segmentation in Remote Sensing Images
---

# SegEarth-OV3: Exploring SAM 3 for Open-Vocabulary Semantic Segmentation in Remote Sensing Images
**arXiv**：[2512.08730v1](https://arxiv.org/abs/2512.08730) · [PDF](https://arxiv.org/pdf/2512.08730.pdf)  
**作者**：Kaiyu Li, Shengqi Zhang, Yupeng Deng, Zhi Wang, Deyu Meng, Xiangyong Cao  

**一句话要点**：提出SegEarth-OV3，探索SAM 3在遥感图像开放词汇语义分割中的应用，无需训练。

**关键词**：开放词汇语义分割, 遥感图像, SAM 3, 掩码融合, 存在分数过滤, 无训练方法

## 3 点简述
- 核心问题：现有基于CLIP的开放词汇语义分割方法在遥感场景中定位不精确或流程复杂。
- 方法要点：结合SAM 3的语义分割头和Transformer解码器输出，并利用存在分数过滤不存在的类别。
- 实验或效果：在遥感数据集上评估，简单适应展现出有前景的性能，验证了SAM 3的潜力。

## 摘要（原文）

> Most existing methods for training-free Open-Vocabulary Semantic Segmentation (OVSS) are based on CLIP. While these approaches have made progress, they often face challenges in precise localization or require complex pipelines to combine separate modules, especially in remote sensing scenarios where numerous dense and small targets are present. Recently, Segment Anything Model 3 (SAM 3) was proposed, unifying segmentation and recognition in a promptable framework. In this paper, we present a preliminary exploration of applying SAM 3 to the remote sensing OVSS task without any training. First, we implement a mask fusion strategy that combines the outputs from SAM 3's semantic segmentation head and the Transformer decoder (instance head). This allows us to leverage the strengths of both heads for better land coverage. Second, we utilize the presence score from the presence head to filter out categories that do not exist in the scene, reducing false positives caused by the vast vocabulary sizes and patch-level processing in geospatial scenes. We evaluate our method on extensive remote sensing datasets. Experiments show that this simple adaptation achieves promising performance, demonstrating the potential of SAM 3 for remote sensing OVSS. Our code is released at https://github.com/earth-insights/SegEarth-OV-3.

