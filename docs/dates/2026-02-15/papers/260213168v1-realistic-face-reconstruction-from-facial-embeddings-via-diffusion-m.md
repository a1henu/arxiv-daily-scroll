---
layout: default
title: Realistic Face Reconstruction from Facial Embeddings via Diffusion Models
---

# Realistic Face Reconstruction from Facial Embeddings via Diffusion Models
**arXiv**：[2602.13168v1](https://arxiv.org/abs/2602.13168) · [PDF](https://arxiv.org/pdf/2602.13168.pdf)  
**作者**：Dong Han, Yong Li, Joachim Denzler  

**一句话要点**：提出基于扩散模型的面部嵌入映射框架，以评估人脸识别系统的隐私泄露风险。

**关键词**：人脸重建, 隐私保护人脸识别, 扩散模型, 嵌入攻击, Kolmogorov-Arnold网络, 隐私评估

## 3 点简述
- 核心问题：从隐私保护人脸识别系统的嵌入中重建高分辨率人脸图像，验证隐私风险。
- 方法要点：利用Kolmogorov-Arnold网络和预训练扩散模型，实现嵌入到人脸的攻击。
- 实验或效果：重建人脸可访问其他真实系统，对部分和保护嵌入具有鲁棒性，作为评估工具。

## 摘要（原文）

> With the advancement of face recognition (FR) systems, privacy-preserving face recognition (PPFR) systems have gained popularity for their accurate recognition, enhanced facial privacy protection, and robustness to various attacks. However, there are limited studies to further verify privacy risks by reconstructing realistic high-resolution face images from embeddings of these systems, especially for PPFR. In this work, we propose the face embedding mapping (FEM), a general framework that explores Kolmogorov-Arnold Network (KAN) for conducting the embedding-to-face attack by leveraging pre-trained Identity-Preserving diffusion model against state-of-the-art (SOTA) FR and PPFR systems. Based on extensive experiments, we verify that reconstructed faces can be used for accessing other real-word FR systems. Besides, the proposed method shows the robustness in reconstructing faces from the partial and protected face embeddings. Moreover, FEM can be utilized as a tool for evaluating safety of FR and PPFR systems in terms of privacy leakage. All images used in this work are from public datasets.

