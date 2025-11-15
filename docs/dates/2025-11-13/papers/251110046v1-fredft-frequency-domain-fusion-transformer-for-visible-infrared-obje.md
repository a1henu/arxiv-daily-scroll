---
layout: default
title: FreDFT: Frequency Domain Fusion Transformer for Visible-Infrared Object Detection
---

# FreDFT: Frequency Domain Fusion Transformer for Visible-Infrared Object Detection
**arXiv**：[2511.10046v1](https://arxiv.org/abs/2511.10046) · [PDF](https://arxiv.org/pdf/2511.10046.pdf)  
**作者**：Wencong Wu, Xiuwei Zhang, Hanlin Yin, Shun Dai, Hongxi Zhang, Yanning Zhang  

**一句话要点**：提出频率域融合Transformer以解决可见光-红外目标检测中的信息不平衡问题

**关键词**：可见光-红外目标检测, 频率域Transformer, 多模态融合, 注意力机制, 特征增强

## 3 点简述
- 核心问题：可见光与红外模态在复杂场景中存在信息不平衡，导致跨模态融合不足。
- 方法要点：使用多模态频率域注意力和频率域前馈层挖掘互补信息。
- 实验或效果：在多个公共数据集上验证了优于现有方法的性能。

## 摘要（原文）

> Visible-infrared object detection has gained sufficient attention due to its detection performance in low light, fog, and rain conditions. However, visible and infrared modalities captured by different sensors exist the information imbalance problem in complex scenarios, which can cause inadequate cross-modal fusion, resulting in degraded detection performance. \textcolor{red}{Furthermore, most existing methods use transformers in the spatial domain to capture complementary features, ignoring the advantages of developing frequency domain transformers to mine complementary information.} To solve these weaknesses, we propose a frequency domain fusion transformer, called FreDFT, for visible-infrared object detection. The proposed approach employs a novel multimodal frequency domain attention (MFDA) to mine complementary information between modalities and a frequency domain feed-forward layer (FDFFL) via a mixed-scale frequency feature fusion strategy is designed to better enhance multimodal features. To eliminate the imbalance of multimodal information, a cross-modal global modeling module (CGMM) is constructed to perform pixel-wise inter-modal feature interaction in a spatial and channel manner. Moreover, a local feature enhancement module (LFEM) is developed to strengthen multimodal local feature representation and promote multimodal feature fusion by using various convolution layers and applying a channel shuffle. Extensive experimental results have verified that our proposed FreDFT achieves excellent performance on multiple public datasets compared with other state-of-the-art methods. The code of our FreDFT is linked at https://github.com/WenCongWu/FreDFT.

