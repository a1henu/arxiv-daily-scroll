---
layout: default
title: VLM-NCD:Novel Class Discovery with Vision-Based Large Language Models
---

# VLM-NCD:Novel Class Discovery with Vision-Based Large Language Models
**arXiv**：[2512.10262v1](https://arxiv.org/abs/2512.10262) · [PDF](https://arxiv.org/pdf/2512.10262.pdf)  
**作者**：Yuetong Su, Baoguo Wei, Xinyu Wang, Xu Li, Lixin Li  

**一句话要点**：提出VLM-NCD框架，融合视觉-文本语义与原型聚类，以解决图像新类发现中特征判别性不足和长尾分布问题。

**关键词**：新类发现, 视觉-语言模型, 原型聚类, 长尾分布, 语义融合, 双阶段发现

## 3 点简述
- 核心问题：图像新类发现依赖视觉特征，存在特征判别性不足和数据长尾分布限制。
- 方法要点：通过联合优化已知类图像和文本特征建模聚类中心与语义原型，采用双阶段发现机制动态分离样本。
- 实验或效果：在CIFAR-100数据集上，未知类准确率提升达25.3%，首次展示对长尾分布的鲁棒性。

## 摘要（原文）

> Novel Class Discovery aims to utilise prior knowledge of known classes to classify and discover unknown classes from unlabelled data. Existing NCD methods for images primarily rely on visual features, which suffer from limitations such as insufficient feature discriminability and the long-tail distribution of data. We propose LLM-NCD, a multimodal framework that breaks this bottleneck by fusing visual-textual semantics and prototype guided clustering. Our key innovation lies in modelling cluster centres and semantic prototypes of known classes by jointly optimising known class image and text features, and a dualphase discovery mechanism that dynamically separates known or novel samples via semantic affinity thresholds and adaptive clustering. Experiments on the CIFAR-100 dataset show that compared to the current methods, this method achieves up to 25.3% improvement in accuracy for unknown classes. Notably, our method shows unique resilience to long tail distributions, a first in NCD literature.

