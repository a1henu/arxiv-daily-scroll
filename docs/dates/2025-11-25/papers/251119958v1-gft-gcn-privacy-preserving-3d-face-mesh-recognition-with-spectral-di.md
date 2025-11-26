---
layout: default
title: GFT-GCN: Privacy-Preserving 3D Face Mesh Recognition with Spectral Diffusion
---

# GFT-GCN: Privacy-Preserving 3D Face Mesh Recognition with Spectral Diffusion
**arXiv**：[2511.19958v1](https://arxiv.org/abs/2511.19958) · [PDF](https://arxiv.org/pdf/2511.19958.pdf)  
**作者**：Hichem Felouat, Hanrui Wang, Isao Echizen  

**一句话要点**：提出GFT-GCN框架，结合谱图学习与扩散机制，实现隐私保护的3D人脸识别。

**关键词**：3D人脸识别, 隐私保护, 图卷积网络, 谱扩散, 生物特征模板

## 3 点简述
- 核心问题：3D人脸识别需保护存储的生物特征模板，防止隐私泄露。
- 方法要点：集成GFT和GCN提取谱特征，并应用谱扩散机制生成不可逆模板。
- 实验效果：在BU-3DFE和FaceScape数据集上验证高识别精度和抗重建攻击能力。

## 摘要（原文）

> 3D face recognition offers a robust biometric solution by capturing facial geometry, providing resilience to variations in illumination, pose changes, and presentation attacks. Its strong spoof resistance makes it suitable for high-security applications, but protecting stored biometric templates remains critical. We present GFT-GCN, a privacy-preserving 3D face recognition framework that combines spectral graph learning with diffusion-based template protection. Our approach integrates the Graph Fourier Transform (GFT) and Graph Convolutional Networks (GCN) to extract compact, discriminative spectral features from 3D face meshes. To secure these features, we introduce a spectral diffusion mechanism that produces irreversible, renewable, and unlinkable templates. A lightweight client-server architecture ensures that raw biometric data never leaves the client device. Experiments on the BU-3DFE and FaceScape datasets demonstrate high recognition accuracy and strong resistance to reconstruction attacks. Results show that GFT-GCN effectively balances privacy and performance, offering a practical solution for secure 3D face authentication.

