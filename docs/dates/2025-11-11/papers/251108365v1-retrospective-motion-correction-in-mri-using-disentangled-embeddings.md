---
layout: default
title: Retrospective motion correction in MRI using disentangled embeddings
---

# Retrospective motion correction in MRI using disentangled embeddings
**arXiv**：[2511.08365v1](https://arxiv.org/abs/2511.08365) · [PDF](https://arxiv.org/pdf/2511.08365.pdf)  
**作者**：Qi Wang, Veronika Ecker, Marcel Früh, Sergios Gatidis, Thomas Küstner  

**一句话要点**：提出分层VQ-VAE以解决MRI中生理运动伪影的泛化校正问题

**关键词**：MRI运动校正, 解耦嵌入, 分层VQ-VAE, 自回归模型, 泛化学习

## 3 点简述
- 生理运动影响MRI诊断质量，现有方法难以泛化不同运动类型和身体区域
- 使用分层VQ-VAE学习运动与干净图像特征的解耦嵌入，结合自回归模型引导校正
- 在模拟全身运动伪影上验证，模型能泛化未见运动模式，提升图像质量

## 摘要（原文）

> Physiological motion can affect the diagnostic quality of magnetic resonance imaging (MRI). While various retrospective motion correction methods exist, many struggle to generalize across different motion types and body regions. In particular, machine learning (ML)-based corrections are often tailored to specific applications and datasets. We hypothesize that motion artifacts, though diverse, share underlying patterns that can be disentangled and exploited. To address this, we propose a hierarchical vector-quantized (VQ) variational auto-encoder that learns a disentangled embedding of motion-to-clean image features. A codebook is deployed to capture finite collection of motion patterns at multiple resolutions, enabling coarse-to-fine correction. An auto-regressive model is trained to learn the prior distribution of motion-free images and is used at inference to guide the correction process. Unlike conventional approaches, our method does not require artifact-specific training and can generalize to unseen motion patterns. We demonstrate the approach on simulated whole-body motion artifacts and observe robust correction across varying motion severity. Our results suggest that the model effectively disentangled physical motion of the simulated motion-effective scans, therefore, improving the generalizability of the ML-based MRI motion correction. Our work of disentangling the motion features shed a light on its potential application across anatomical regions and motion types.

