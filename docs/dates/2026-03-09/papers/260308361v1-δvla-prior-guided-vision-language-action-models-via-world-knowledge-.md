---
layout: default
title: $Δ$VLA: Prior-Guided Vision-Language-Action Models via World Knowledge Variation
---

# $Δ$VLA: Prior-Guided Vision-Language-Action Models via World Knowledge Variation
**arXiv**：[2603.08361v1](https://arxiv.org/abs/2603.08361) · [PDF](https://arxiv.org/pdf/2603.08361.pdf)  
**作者**：Yijie Zhu, Jie He, Rui Shao, Kaishen Yuan, Tao Tan, Xiaochen Yuan, Zitong Yu  

**一句话要点**：提出ΔVLA框架，通过建模世界知识变化来指导机器人动作生成

**关键词**：视觉-语言-动作模型, 机器人操作, 世界知识建模, 变化推理, 先验引导, 离散潜在空间

## 3 点简述
- 核心问题：现有视觉-语言-动作模型强调预测未来状态，而非推理变化过程，影响动作决策准确性。
- 方法要点：引入先验引导的世界知识提取器、潜在世界变化量化器和条件变化注意力，以建模世界知识变化。
- 实验或效果：在模拟基准和真实机器人任务中实现最先进性能，并提升效率，代码和视频已开源。

## 摘要（原文）

> Recent vision-language-action (VLA) models have significantly advanced robotic manipulation by unifying perception, reasoning, and control. To achieve such integration, recent studies adopt a predictive paradigm that models future visual states or world knowledge to guide action generation. However, these models emphasize forecasting outcomes rather than reasoning about the underlying process of change, which is essential for determining how to act. To address this, we propose $Δ$VLA, a prior-guided framework that models world-knowledge variations relative to an explicit current-world knowledge prior for action generation, rather than regressing absolute future world states. Specifically, 1) to construct the current world knowledge prior, we propose the Prior-Guided WorldKnowledge Extractor (PWKE). It extracts manipulable regions, spatial relations, and semantic cues from the visual input, guided by auxiliary heads and prior pseudo labels, thus reducing redundancy. 2) Building upon this, to represent how world knowledge evolves under actions, we introduce the Latent World Variation Quantization (LWVQ). It learns a discrete latent space via a VQ-VAE objective to encode world knowledge variations, shifting prediction from full modalities to compact latent. 3)Moreover, to mitigate interference during variation modeling, we design the Conditional Variation Attention (CV-Atten), whichpromotes disentangled learning and preserves the independence of knowledge representations. Extensive experiments on both simulated benchmarks and real-world robotic tasks demonstrate $Δ$VLA achieves state-of-the-art performance while improving efficiency. Code and real-world execution videos are available at https://github.com/JiuTian-VL/DeltaVLA.

