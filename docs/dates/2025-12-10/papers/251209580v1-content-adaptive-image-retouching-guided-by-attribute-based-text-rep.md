---
layout: default
title: Content-Adaptive Image Retouching Guided by Attribute-Based Text Representation
---

# Content-Adaptive Image Retouching Guided by Attribute-Based Text Representation
**arXiv**：[2512.09580v1](https://arxiv.org/abs/2512.09580) · [PDF](https://arxiv.org/pdf/2512.09580.pdf)  
**作者**：Hancheng Zhu, Xinyu Liu, Rui Yao, Kunyang Sun, Leida Li, Abdulmotaleb El Saddik  

**一句话要点**：提出内容自适应图像润色方法CA-ATP，通过属性文本表示指导，解决现有方法忽略内容颜色变化和用户风格偏好的问题。

**关键词**：图像润色, 内容自适应, 属性文本表示, 多模态模型, 颜色映射

## 3 点简述
- 核心问题：现有图像润色方法采用统一像素级颜色映射，忽略图像内容引起的颜色变化，难以适应多样颜色分布和用户风格偏好。
- 方法要点：设计内容自适应曲线映射模块，利用基础曲线和权重图实现内容感知颜色调整；提出属性文本预测模块，从图像属性生成文本表示，通过多模态模型整合视觉特征，提供用户友好指导。
- 实验或效果：在多个公共数据集上实验，CA-ATP方法达到最先进性能，验证了其自适应润色能力。

## 摘要（原文）

> Image retouching has received significant attention due to its ability to achieve high-quality visual content. Existing approaches mainly rely on uniform pixel-wise color mapping across entire images, neglecting the inherent color variations induced by image content. This limitation hinders existing approaches from achieving adaptive retouching that accommodates both diverse color distributions and user-defined style preferences. To address these challenges, we propose a novel Content-Adaptive image retouching method guided by Attribute-based Text Representation (CA-ATP). Specifically, we propose a content-adaptive curve mapping module, which leverages a series of basis curves to establish multiple color mapping relationships and learns the corresponding weight maps, enabling content-aware color adjustments. The proposed module can capture color diversity within the image content, allowing similar color values to receive distinct transformations based on their spatial context. In addition, we propose an attribute text prediction module that generates text representations from multiple image attributes, which explicitly represent user-defined style preferences. These attribute-based text representations are subsequently integrated with visual features via a multimodal model, providing user-friendly guidance for image retouching. Extensive experiments on several public datasets demonstrate that our method achieves state-of-the-art performance.

