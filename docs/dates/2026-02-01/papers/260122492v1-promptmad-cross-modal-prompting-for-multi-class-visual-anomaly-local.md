---
layout: default
title: PromptMAD: Cross-Modal Prompting for Multi-Class Visual Anomaly Localization
---

# PromptMAD: Cross-Modal Prompting for Multi-Class Visual Anomaly Localization
**arXiv**：[2601.22492v1](https://arxiv.org/abs/2601.22492) · [PDF](https://arxiv.org/pdf/2601.22492.pdf)  
**作者**：Duncan McCain, Hossein Kashiani, Fatemeh Afghah  

**一句话要点**：提出PromptMAD跨模态提示框架，以解决多类视觉异常检测与定位中的语义引导和类不平衡问题。

**关键词**：跨模态提示, 视觉异常定位, 语义引导, Focal损失, 多尺度特征融合, Transformer注意力

## 3 点简述
- 核心问题：多类视觉异常检测面临类别多样性、异常样本稀缺和伪装缺陷等挑战。
- 方法要点：利用CLIP编码的文本提示，结合语义上下文增强视觉重建，并集成Focal损失和融合多尺度特征的监督分割器。
- 实验或效果：在MVTec-AD数据集上实现像素级SOTA性能，平均AUC达98.35%，AP达66.54%。

## 摘要（原文）

> Visual anomaly detection in multi-class settings poses significant challenges due to the diversity of object categories, the scarcity of anomalous examples, and the presence of camouflaged defects. In this paper, we propose PromptMAD, a cross-modal prompting framework for unsupervised visual anomaly detection and localization that integrates semantic guidance through vision-language alignment. By leveraging CLIP-encoded text prompts describing both normal and anomalous class-specific characteristics, our method enriches visual reconstruction with semantic context, improving the detection of subtle and textural anomalies. To further address the challenge of class imbalance at the pixel level, we incorporate Focal loss function, which emphasizes hard-to-detect anomalous regions during training. Our architecture also includes a supervised segmentor that fuses multi-scale convolutional features with Transformer-based spatial attention and diffusion iterative refinement, yielding precise and high-resolution anomaly maps. Extensive experiments on the MVTec-AD dataset demonstrate that our method achieves state-of-the-art pixel-level performance, improving mean AUC to 98.35% and AP to 66.54%, while maintaining efficiency across diverse categories.

