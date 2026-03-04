---
layout: default
title: Chain of World: World Model Thinking in Latent Motion
---

# Chain of World: World Model Thinking in Latent Motion
**arXiv**：[2603.03195v1](https://arxiv.org/abs/2603.03195) · [PDF](https://arxiv.org/pdf/2603.03195.pdf)  
**作者**：Fuxiang Yang, Donglin Di, Lulu Tang, Xuancheng Zhang, Lei Fan, Hao Li, Chen Wei, Tonghua Su, Baorui Ma  

**一句话要点**：提出CoWVLA范式，通过解耦潜在运动链统一世界模型推理与紧凑表示，以提升具身智能的视觉语言动作模型性能。

**关键词**：视觉语言动作模型, 世界模型, 潜在运动表示, 解耦学习, 自回归解码, 具身智能

## 3 点简述
- 问题：现有VLA模型忽视视觉动态的预测与因果结构，世界模型方法冗余重建背景，潜在动作方法缺乏连续动态建模。
- 方法：使用预训练视频VAE提取解耦的结构与运动潜在变量，通过自回归解码器学习连续潜在运动链并预测关键帧，对齐动作序列。
- 效果：在机器人仿真基准测试中优于现有方法，实现中等计算效率，验证了作为有效VLA预训练范式的潜力。

## 摘要（原文）

> Vision-Language-Action (VLA) models are a promising path toward embodied intelligence, yet they often overlook the predictive and temporal-causal structure underlying visual dynamics. World-model VLAs address this by predicting future frames, but waste capacity reconstructing redundant backgrounds. Latent-action VLAs encode frame-to-frame transitions compactly, but lack temporally continuous dynamic modeling and world knowledge. To overcome these limitations, we introduce CoWVLA (Chain-of-World VLA), a new "Chain of World" paradigm that unifies world-model temporal reasoning with a disentangled latent motion representation. First, a pretrained video VAE serves as a latent motion extractor, explicitly factorizing video segments into structure and motion latents. Then, during pre-training, the VLA learns from an instruction and an initial frame to infer a continuous latent motion chain and predict the segment's terminal frame. Finally, during co-fine-tuning, this latent dynamic is aligned with discrete action prediction by jointly modeling sparse keyframes and action sequences in a unified autoregressive decoder. This design preserves the world-model benefits of temporal reasoning and world knowledge while retaining the compactness and interpretability of latent actions, enabling efficient visuomotor learning. Extensive experiments on robotic simulation benchmarks show that CoWVLA outperforms existing world-model and latent-action approaches and achieves moderate computational efficiency, highlighting its potential as a more effective VLA pretraining paradigm. The project website can be found at https://fx-hit.github.io/cowvla-io.

