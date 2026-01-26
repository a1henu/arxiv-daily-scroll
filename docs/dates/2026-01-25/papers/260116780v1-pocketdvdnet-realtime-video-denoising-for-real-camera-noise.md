---
layout: default
title: PocketDVDNet: Realtime Video Denoising for Real Camera Noise
---

# PocketDVDNet: Realtime Video Denoising for Real Camera Noise
**arXiv**：[2601.16780v1](https://arxiv.org/abs/2601.16780) · [PDF](https://arxiv.org/pdf/2601.16780.pdf)  
**作者**：Crispian Morris, Imogen Dexter, Fan Zhang, David R. Bull, Nantheera Anantrasirichai  

**一句话要点**：提出PocketDVDNet以解决实时视频去噪中资源需求高的问题

**关键词**：视频去噪, 模型压缩, 知识蒸馏, 实时处理, 传感器噪声

## 3 点简述
- 核心问题：真实多分量传感器噪声下的实时视频去噪挑战，如自动对焦和自动驾驶应用
- 方法要点：结合稀疏引导结构化剪枝、物理噪声模型和知识蒸馏的轻量化模型压缩框架
- 实验或效果：模型大小减少74%，去噪质量提升，实时处理5帧补丁

## 摘要（原文）

> Live video denoising under realistic, multi-component sensor noise remains challenging for applications such as autofocus, autonomous driving, and surveillance. We propose PocketDVDNet, a lightweight video denoiser developed using our model compression framework that combines sparsity-guided structured pruning, a physics-informed noise model, and knowledge distillation to achieve high-quality restoration with reduced resource demands. Starting from a reference model, we induce sparsity, apply targeted channel pruning, and retrain a teacher on realistic multi-component noise. The student network learns implicit noise handling, eliminating the need for explicit noise-map inputs. PocketDVDNet reduces the original model size by 74% while improving denoising quality and processing 5-frame patches in real-time. These results demonstrate that aggressive compression, combined with domain-adapted distillation, can reconcile performance and efficiency for practical, real-time video denoising.

