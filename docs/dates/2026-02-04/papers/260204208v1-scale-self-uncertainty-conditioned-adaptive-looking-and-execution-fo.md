---
layout: default
title: SCALE: Self-uncertainty Conditioned Adaptive Looking and Execution for Vision-Language-Action Models
---

# SCALE: Self-uncertainty Conditioned Adaptive Looking and Execution for Vision-Language-Action Models
**arXiv**：[2602.04208v1](https://arxiv.org/abs/2602.04208) · [PDF](https://arxiv.org/pdf/2602.04208.pdf)  
**作者**：Hyeonbeom Choi, Daechul Ahn, Youhan Lee, Taewook Kang, Seongwon Cho, Jonghyun Choi  

**一句话要点**：提出SCALE以解决视觉-语言-动作模型在感知模糊下自适应执行的问题

**关键词**：视觉-语言-动作模型, 测试时缩放, 自不确定性, 自适应执行, 单次前向推理

## 3 点简述
- 现有测试时缩放方法需额外训练且仅干预动作解码，不适用于部署
- SCALE基于自不确定性联合调制视觉感知与动作，无需额外训练或验证器
- 实验表明SCALE提升先进模型性能，优于现有方法并保持单次前向效率

## 摘要（原文）

> Vision-Language-Action (VLA) models have emerged as a promising paradigm for general-purpose robotic control, with test-time scaling (TTS) gaining attention to enhance robustness beyond training. However, existing TTS methods for VLAs require additional training, verifiers, and multiple forward passes, making them impractical for deployment. Moreover, they intervene only at action decoding while keeping visual representations fixed-insufficient under perceptual ambiguity, where reconsidering how to perceive is as important as deciding what to do. To address these limitations, we propose SCALE, a simple inference strategy that jointly modulates visual perception and action based on 'self-uncertainty', inspired by uncertainty-driven exploration in Active Inference theory-requiring no additional training, no verifier, and only a single forward pass. SCALE broadens exploration in both perception and action under high uncertainty, while focusing on exploitation when confident-enabling adaptive execution across varying conditions. Experiments on simulated and real-world benchmarks demonstrate that SCALE improves state-of-the-art VLAs and outperforms existing TTS methods while maintaining single-pass efficiency.

