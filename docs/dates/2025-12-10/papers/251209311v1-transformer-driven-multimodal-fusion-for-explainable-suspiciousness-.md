---
layout: default
title: Transformer-Driven Multimodal Fusion for Explainable Suspiciousness Estimation in Visual Surveillance
---

# Transformer-Driven Multimodal Fusion for Explainable Suspiciousness Estimation in Visual Surveillance
**arXiv**：[2512.09311v1](https://arxiv.org/abs/2512.09311) · [PDF](https://arxiv.org/pdf/2512.09311.pdf)  
**作者**：Kuldeep Singh Yadav, Lalan Kumar  

**一句话要点**：提出DeepUSEvision框架和USE50k数据集，用于视觉监控中的实时可疑性估计与解释性分析。

**关键词**：可疑性估计, 多模态融合, Transformer网络, 视觉监控, 实时分析, 可解释性AI

## 3 点简述
- 核心问题：在复杂环境中实现实时可疑性估计，以支持主动威胁检测和公共安全。
- 方法要点：基于增强YOLOv12的物体检测器、双DCNN的面部表情与身体语言识别，以及Transformer驱动的多模态融合网络。
- 实验或效果：在USE50k数据集上验证了框架的准确性、鲁棒性和可解释性，优于现有方法。

## 摘要（原文）

> Suspiciousness estimation is critical for proactive threat detection and ensuring public safety in complex environments. This work introduces a large-scale annotated dataset, USE50k, along with a computationally efficient vision-based framework for real-time suspiciousness analysis. The USE50k dataset contains 65,500 images captured from diverse and uncontrolled environments, such as airports, railway stations, restaurants, parks, and other public areas, covering a broad spectrum of cues including weapons, fire, crowd density, abnormal facial expressions, and unusual body postures. Building on this dataset, we present DeepUSEvision, a lightweight and modular system integrating three key components, i.e., a Suspicious Object Detector based on an enhanced YOLOv12 architecture, dual Deep Convolutional Neural Networks (DCNN-I and DCNN-II) for facial expression and body-language recognition using image and landmark features, and a transformer-based Discriminator Network that adaptively fuses multimodal outputs to yield an interpretable suspiciousness score. Extensive experiments confirm the superior accuracy, robustness, and interpretability of the proposed framework compared to state-of-the-art approaches. Collectively, the USE50k dataset and the DeepUSEvision framework establish a strong and scalable foundation for intelligent surveillance and real-time risk assessment in safety-critical applications.

