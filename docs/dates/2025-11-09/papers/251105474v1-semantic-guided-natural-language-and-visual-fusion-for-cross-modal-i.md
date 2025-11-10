---
layout: default
title: Semantic-Guided Natural Language and Visual Fusion for Cross-Modal Interaction Based on Tiny Object Detection
---

# Semantic-Guided Natural Language and Visual Fusion for Cross-Modal Interaction Based on Tiny Object Detection
**arXiv**：[2511.05474v1](https://arxiv.org/abs/2511.05474) · [PDF](https://arxiv.org/pdf/2511.05474.pdf)  
**作者**：Xian-Hong Huang, Hui-Kai Su, Chi-Chia Sun, Jun-Wei Hsieh  

**一句话要点**：提出语义引导的自然语言与视觉融合方法，以解决小物体检测中的跨模态交互问题。

**关键词**：小物体检测, 跨模态交互, 语义引导融合, BERT模型, 特征金字塔网络, 骨干网络优化

## 3 点简述
- 核心问题：小物体检测精度低，需融合自然语言与视觉信息以提升性能。
- 方法要点：集成BERT与PRB-FPN-Net，采用ELAN等骨干网络优化特征提取与融合。
- 实验或效果：在COCO数据集上AP达52.6%，优于YOLO-World，参数消耗减半。

## 摘要（原文）

> This paper introduces a cutting-edge approach to cross-modal interaction for
> tiny object detection by combining semantic-guided natural language processing
> with advanced visual recognition backbones. The proposed method integrates the
> BERT language model with the CNN-based Parallel Residual Bi-Fusion Feature
> Pyramid Network (PRB-FPN-Net), incorporating innovative backbone architectures
> such as ELAN, MSP, and CSP to optimize feature extraction and fusion. By
> employing lemmatization and fine-tuning techniques, the system aligns semantic
> cues from textual inputs with visual features, enhancing detection precision
> for small and complex objects. Experimental validation using the COCO and
> Objects365 datasets demonstrates that the model achieves superior performance.
> On the COCO2017 validation set, it attains a 52.6% average precision (AP),
> outperforming YOLO-World significantly while maintaining half the parameter
> consumption of Transformer-based models like GLIP. Several test on different of
> backbones such ELAN, MSP, and CSP further enable efficient handling of
> multi-scale objects, ensuring scalability and robustness in
> resource-constrained environments. This study underscores the potential of
> integrating natural language understanding with advanced backbone
> architectures, setting new benchmarks in object detection accuracy, efficiency,
> and adaptability to real-world challenges.

