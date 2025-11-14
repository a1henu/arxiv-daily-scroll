---
layout: default
title: Next-Frame Feature Prediction for Multimodal Deepfake Detection and Temporal Localization
---

# Next-Frame Feature Prediction for Multimodal Deepfake Detection and Temporal Localization
**arXiv**：[2511.10212v1](https://arxiv.org/abs/2511.10212) · [PDF](https://arxiv.org/pdf/2511.10212.pdf)  
**作者**：Ashutosh Anshul, Shreyas Gopal, Deepu Rajan, Eng Siong Chng  

**一句话要点**：提出基于下一帧预测的单阶段训练框架，以提升多模态深度伪造检测的泛化能力和时序定位精度。

**关键词**：多模态深度伪造检测, 下一帧预测, 时序定位, 窗口级注意力, 泛化性增强

## 3 点简述
- 核心问题：现有方法泛化性差，依赖预训练，且易忽略模态内伪影。
- 方法要点：引入下一帧预测和窗口级注意力机制，捕获预测与实际帧差异。
- 实验或效果：在多个基准数据集上验证了强泛化性和精确时序定位。

## 摘要（原文）

> Recent multimodal deepfake detection methods designed for generalization conjecture that single-stage supervised training struggles to generalize across unseen manipulations and datasets. However, such approaches that target generalization require pretraining over real samples. Additionally, these methods primarily focus on detecting audio-visual inconsistencies and may overlook intra-modal artifacts causing them to fail against manipulations that preserve audio-visual alignment. To address these limitations, we propose a single-stage training framework that enhances generalization by incorporating next-frame prediction for both uni-modal and cross-modal features. Additionally, we introduce a window-level attention mechanism to capture discrepancies between predicted and actual frames, enabling the model to detect local artifacts around every frame, which is crucial for accurately classifying fully manipulated videos and effectively localizing deepfake segments in partially spoofed samples. Our model, evaluated on multiple benchmark datasets, demonstrates strong generalization and precise temporal localization.

