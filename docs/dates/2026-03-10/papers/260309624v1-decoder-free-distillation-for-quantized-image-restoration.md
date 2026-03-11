---
layout: default
title: Decoder-Free Distillation for Quantized Image Restoration
---

# Decoder-Free Distillation for Quantized Image Restoration
**arXiv**：[2603.09624v1](https://arxiv.org/abs/2603.09624) · [PDF](https://arxiv.org/pdf/2603.09624.pdf)  
**作者**：S. M. A. Sharif, Abdur Rehman, Seongwan Kim, Jaeho Lee  

**一句话要点**：提出QDR框架以解决量化图像恢复中的教师-学生能力不匹配、解码器蒸馏误差放大和优化冲突问题。

**关键词**：图像恢复, 量化感知训练, 知识蒸馏, 边缘部署, 解码器自由蒸馏, 可学习幅度重加权

## 3 点简述
- 核心问题：量化感知训练与知识蒸馏在图像恢复中面临能力不匹配、空间误差放大和优化冲突。
- 方法要点：采用FP32自蒸馏消除能力不匹配，解码器自由蒸馏纠正瓶颈误差，可学习幅度重加权平衡梯度。
- 实验或效果：Int8模型恢复96.5% FP32性能，在NVIDIA Jetson Orin上达442 FPS，提升下游检测16.3 mAP。

## 摘要（原文）

> Quantization-Aware Training (QAT), combined with Knowledge Distillation (KD), holds immense promise for compressing models for edge deployment. However, joint optimization for precision-sensitive image restoration (IR) to recover visual quality from degraded images remains largely underexplored. Directly adapting QAT-KD to low-level vision reveals three critical bottlenecks: teacher-student capacity mismatch, spatial error amplification during decoder distillation, and an optimization "tug-of-war" between reconstruction and distillation losses caused by quantization noise. To tackle these, we introduce Quantization-aware Distilled Restoration (QDR), a framework for edge-deployed IR. QDR eliminates capacity mismatch via FP32 self-distillation and prevents error amplification through Decoder-Free Distillation (DFD), which corrects quantization errors strictly at the network bottleneck. To stabilize the optimization tug-of-war, we propose a Learnable Magnitude Reweighting (LMR) that dynamically balances competing gradients. Finally, we design an Edge-Friendly Model (EFM) featuring a lightweight Learnable Degradation Gating (LDG) to dynamically modulate spatial degradation localization. Extensive experiments across four IR tasks demonstrate that our Int8 model recovers 96.5% of FP32 performance, achieves 442 frames per second (FPS) on an NVIDIA Jetson Orin, and boosts downstream object detection by 16.3 mAP

