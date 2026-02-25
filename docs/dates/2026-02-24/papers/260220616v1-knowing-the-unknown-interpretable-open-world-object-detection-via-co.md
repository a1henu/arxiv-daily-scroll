---
layout: default
title: Knowing the Unknown: Interpretable Open-World Object Detection via Concept Decomposition Model
---

# Knowing the Unknown: Interpretable Open-World Object Detection via Concept Decomposition Model
**arXiv**：[2602.20616v1](https://arxiv.org/abs/2602.20616) · [PDF](https://arxiv.org/pdf/2602.20616.pdf)  
**作者**：Xueqiang Lv, Shizhou Zhang, Yinghui Xing, Di Xu, Peng Wang, Yanning Zhang  

**一句话要点**：提出概念分解模型以增强开放世界目标检测的未知识别与可解释性

**关键词**：开放世界目标检测, 概念分解模型, 可解释性, 未知识别, 特征分解, 概念引导校正

## 3 点简述
- 核心问题：现有开放世界目标检测方法忽视可解释性，导致已知与未知类别混淆，降低预测可靠性。
- 方法要点：引入概念分解模型，将RoI特征分解为判别性、共享和背景概念，利用共享和背景概念泛化能力检测未知类别。
- 实验或效果：IPOW框架显著提升未知召回率，减少混淆，并为已知和未知预测提供概念级可解释性。

## 摘要（原文）

> Open-world object detection (OWOD) requires incrementally detecting known categories while reliably identifying unknown objects. Existing methods primarily focus on improving unknown recall, yet overlook interpretability, often leading to known-unknown confusion and reduced prediction reliability. This paper aims to make the entire OWOD framework interpretable, enabling the detector to truly "knowing the unknown". To this end, we propose a concept-driven InterPretable OWOD framework(IPOW) by introducing a Concept Decomposition Model (CDM) for OWOD, which explicitly decomposes the coupled RoI features in Faster R-CNN into discriminative, shared, and background concepts. Discriminative concepts identify the most discriminative features to enlarge the distances between known categories, while shared and background concepts, due to their strong generalization ability, can be readily transferred to detect unknown categories. Leveraging the interpretable framework, we identify that known-unknown confusion arises when unknown objects fall into the discriminative space of known classes. To address this, we propose Concept-Guided Rectification (CGR) to further resolve such confusion. Extensive experiments show that IPOW significantly improves unknown recall while mitigating confusion, and provides concept-level interpretability for both known and unknown predictions.

