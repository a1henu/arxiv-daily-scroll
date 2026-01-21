---
layout: default
title: OmniOVCD: Streamlining Open-Vocabulary Change Detection with SAM 3
---

# OmniOVCD: Streamlining Open-Vocabulary Change Detection with SAM 3
**arXiv**：[2601.13895v1](https://arxiv.org/abs/2601.13895) · [PDF](https://arxiv.org/pdf/2601.13895.pdf)  
**作者**：Xu Zhang, Danyang Li, Yingjie Xia, Xiaohang Dong, Hualong Yu, Jianye Wang, Qicheng Li  

**一句话要点**：提出OmniOVCD框架，利用SAM 3的分离输出头实现开放词汇变化检测，提升准确性和稳定性。

**关键词**：开放词汇变化检测, SAM 3, 实例解耦, 遥感图像分析, 免训练方法

## 3 点简述
- 核心问题：现有免训练开放词汇变化检测方法依赖多模型组合，导致特征匹配问题和系统不稳定。
- 方法要点：基于SAM 3的分离输出头，设计协同融合到实例解耦策略，融合语义、实例和存在输出以构建地物掩码并分解为实例掩码进行比较。
- 实验或效果：在四个公开基准测试中实现SOTA性能，IoU分数分别为67.2、66.5、24.5和27.1，超越所有先前方法。

## 摘要（原文）

> Change Detection (CD) is a fundamental task in remote sensing. It monitors the evolution of land cover over time. Based on this, Open-Vocabulary Change Detection (OVCD) introduces a new requirement. It aims to reduce the reliance on predefined categories. Existing training-free OVCD methods mostly use CLIP to identify categories. These methods also need extra models like DINO to extract features. However, combining different models often causes problems in matching features and makes the system unstable. Recently, the Segment Anything Model 3 (SAM 3) is introduced. It integrates segmentation and identification capabilities within one promptable model, which offers new possibilities for the OVCD task. In this paper, we propose OmniOVCD, a standalone framework designed for OVCD. By leveraging the decoupled output heads of SAM 3, we propose a Synergistic Fusion to Instance Decoupling (SFID) strategy. SFID first fuses the semantic, instance, and presence outputs of SAM 3 to construct land-cover masks, and then decomposes them into individual instance masks for change comparison. This design preserves high accuracy in category recognition and maintains instance-level consistency across images. As a result, the model can generate accurate change masks. Experiments on four public benchmarks (LEVIR-CD, WHU-CD, S2Looking, and SECOND) demonstrate SOTA performance, achieving IoU scores of 67.2, 66.5, 24.5, and 27.1 (class-average), respectively, surpassing all previous methods.

