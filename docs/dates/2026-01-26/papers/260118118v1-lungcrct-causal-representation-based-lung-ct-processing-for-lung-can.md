---
layout: default
title: LungCRCT: Causal Representation based Lung CT Processing for Lung Cancer Treatment
---

# LungCRCT: Causal Representation based Lung CT Processing for Lung Cancer Treatment
**arXiv**：[2601.18118v1](https://arxiv.org/abs/2601.18118) · [PDF](https://arxiv.org/pdf/2601.18118.pdf)  
**作者**：Daeyoung Kim  

**一句话要点**：提出LungCRCT框架，基于因果表示学习分析肺癌治疗，提升可解释性与下游任务性能。

**关键词**：肺癌分析, 因果表示学习, 图自编码器, 低剂量CT, 因果干预, 肿瘤分类

## 3 点简述
- 核心问题：现有深度学习模型在肺癌治疗分析和因果干预模拟中受限，因相关性依赖和低可解释性。
- 方法要点：使用图自编码器因果发现算法，结合距离相关解缠和熵基图像重建优化，提取肺癌进展的因果表示。
- 实验或效果：在恶性肿瘤分类任务中实现AUC 93.91%，支持因果干预分析并构建轻量下游模型。

## 摘要（原文）

> Due to silence in early stages, lung cancer has been one of the most leading causes of mortality in cancer patients world-wide. Moreover, major symptoms of lung cancer are hard to differentiate with other respiratory disease symptoms such as COPD, further leading patients to overlook cancer progression in early stages. Thus, to enhance survival rates in lung cancer, early detection from consistent proactive respiratory system monitoring becomes crucial. One of the most prevalent and effective methods for lung cancer monitoring would be low-dose computed tomography(LDCT) chest scans, which led to remarkable enhancements in lung cancer detection or tumor classification tasks under rapid advancements and applications of computer vision based AI models such as EfficientNet or ResNet in image processing. However, though advanced CNN models under transfer learning or ViT based models led to high performing lung cancer detections, due to its intrinsic limitations in terms of correlation dependence and low interpretability due to complexity, expansions of deep learning models to lung cancer treatment analysis or causal intervention analysis simulations are still limited. Therefore, this research introduced LungCRCT: a latent causal representation learning based lung cancer analysis framework that retrieves causal representations of factors within the physical causal mechanism of lung cancer progression. With the use of advanced graph autoencoder based causal discovery algorithms with distance Correlation disentanglement and entropy-based image reconstruction refinement, LungCRCT not only enables causal intervention analysis for lung cancer treatments, but also leads to robust, yet extremely light downstream models in malignant tumor classification tasks with an AUC score of 93.91%.

