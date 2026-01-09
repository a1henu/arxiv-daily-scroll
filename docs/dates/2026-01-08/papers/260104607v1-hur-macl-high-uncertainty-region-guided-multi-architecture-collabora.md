---
layout: default
title: HUR-MACL: High-Uncertainty Region-Guided Multi-Architecture Collaborative Learning for Head and Neck Multi-Organ Segmentation
---

# HUR-MACL: High-Uncertainty Region-Guided Multi-Architecture Collaborative Learning for Head and Neck Multi-Organ Segmentation
**arXiv**：[2601.04607v1](https://arxiv.org/abs/2601.04607) · [PDF](https://arxiv.org/pdf/2601.04607.pdf)  
**作者**：Xiaoyu Liu, Siwen Wei, Linhao Qu, Mingyuan Pan, Chengsheng Zhang, Yonghong Shi, Zhijian Song  

**一句话要点**：提出高不确定性区域引导的多架构协同学习模型，以提升头颈部多器官分割精度。

**关键词**：头颈部多器官分割, 高不确定性区域引导, 多架构协同学习, Vision Mamba, Deformable CNN, 特征蒸馏损失

## 3 点简述
- 核心问题：现有混合架构在头颈部小器官分割中功能重叠，导致准确性受限。
- 方法要点：自适应识别高不确定性区域，结合Vision Mamba和Deformable CNN协同提升分割。
- 实验或效果：在公开和私有数据集上实现SOTA结果，验证方法有效性。

## 摘要（原文）

> Accurate segmentation of organs at risk in the head and neck is essential for radiation therapy, yet deep learning models often fail on small, complexly shaped organs. While hybrid architectures that combine different models show promise, they typically just concatenate features without exploiting the unique strengths of each component. This results in functional overlap and limited segmentation accuracy. To address these issues, we propose a high uncertainty region-guided multi-architecture collaborative learning (HUR-MACL) model for multi-organ segmentation in the head and neck. This model adaptively identifies high uncertainty regions using a convolutional neural network, and for these regions, Vision Mamba as well as Deformable CNN are utilized to jointly improve their segmentation accuracy. Additionally, a heterogeneous feature distillation loss was proposed to promote collaborative learning between the two architectures in high uncertainty regions to further enhance performance. Our method achieves SOTA results on two public datasets and one private dataset.

