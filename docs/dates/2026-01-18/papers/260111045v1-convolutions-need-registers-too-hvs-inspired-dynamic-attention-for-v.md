---
layout: default
title: Convolutions Need Registers Too: HVS-Inspired Dynamic Attention for Video Quality Assessment
---

# Convolutions Need Registers Too: HVS-Inspired Dynamic Attention for Video Quality Assessment
**arXiv**：[2601.11045v1](https://arxiv.org/abs/2601.11045) · [PDF](https://arxiv.org/pdf/2601.11045.pdf)  
**作者**：Mayesha Maliha R. Mithila, Mylene C. Q. Farias  

**一句话要点**：提出DAGR-VQA框架，通过集成寄存器令牌到卷积骨干中，实现动态注意力以提升无参考视频质量评估性能。

**关键词**：无参考视频质量评估, 动态注意力机制, 寄存器令牌, 时空显著性预测, 实时视频处理

## 3 点简述
- 核心问题：现有方法使用静态注意力图，未能将全局上下文嵌入视频序列的特征提取中。
- 方法要点：引入可学习寄存器令牌作为全局上下文载体，生成动态时空显著性图，无需显式运动估计。
- 实验或效果：在多个数据集上表现优异，计算效率达387.7 FPS，适用于实时多媒体流系统。

## 摘要（原文）

> No-reference video quality assessment (NR-VQA) estimates perceptual quality without a reference video, which is often challenging. While recent techniques leverage saliency or transformer attention, they merely address global context of the video signal by using static maps as auxiliary inputs rather than embedding context fundamentally within feature extraction of the video sequence. We present Dynamic Attention with Global Registers for Video Quality Assessment (DAGR-VQA), the first framework integrating register-token directly into a convolutional backbone for spatio-temporal, dynamic saliency prediction. By embedding learnable register tokens as global context carriers, our model enables dynamic, HVS-inspired attention, producing temporally adaptive saliency maps that track salient regions over time without explicit motion estimation. Our model integrates dynamic saliency maps with RGB inputs, capturing spatial data and analyzing it through a temporal transformer to deliver a perceptually consistent video quality assessment. Comprehensive tests conducted on the LSVQ, KonVid-1k, LIVE-VQC, and YouTube-UGC datasets show that the performance is highly competitive, surpassing the majority of top baselines. Research on ablation studies demonstrates that the integration of register tokens promotes the development of stable and temporally consistent attention mechanisms. Achieving an efficiency of 387.7 FPS at 1080p, DAGR-VQA demonstrates computational performance suitable for real-time applications like multimedia streaming systems.

