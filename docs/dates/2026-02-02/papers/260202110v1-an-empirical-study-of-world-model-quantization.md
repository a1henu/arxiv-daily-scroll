---
layout: default
title: An Empirical Study of World Model Quantization
---

# An Empirical Study of World Model Quantization
**arXiv**：[2602.02110v1](https://arxiv.org/abs/2602.02110) · [PDF](https://arxiv.org/pdf/2602.02110.pdf)  
**作者**：Zhongqian Fu, Tianyi Zhao, Kai Han, Hang Zhou, Xinghao Chen, Yunhe Wang  

**一句话要点**：实证研究世界模型量化，揭示量化对规划任务的影响与部署指导

**关键词**：世界模型量化, 后训练量化, 视觉规划, 模型部署, 计算效率

## 3 点简述
- 核心问题：世界模型量化效果未充分研究，量化可能影响规划性能与任务对齐
- 方法要点：以DINO-WM为例，系统评估后训练量化方法，涵盖权重与激活量化设置
- 实验或效果：量化导致规划失败模式，如低比特下稳定性差和模块敏感度不对称

## 摘要（原文）

> World models learn an internal representation of environment dynamics, enabling agents to simulate and reason about future states within a compact latent space for tasks such as planning, prediction, and inference. However, running world models rely on hevay computational cost and memory footprint, making model quantization essential for efficient deployment. To date, the effects of post-training quantization (PTQ) on world models remain largely unexamined. In this work, we present a systematic empirical study of world model quantization using DINO-WM as a representative case, evaluating diverse PTQ methods under both weight-only and joint weight-activation settings. We conduct extensive experiments on different visual planning tasks across a wide range of bit-widths, quantization granularities, and planning horizons up to 50 iterations. Our results show that quantization effects in world models extend beyond standard accuracy and bit-width trade-offs: group-wise weight quantization can stabilize low-bit rollouts, activation quantization granularity yields inconsistent benefits, and quantization sensitivity is highly asymmetric between encoder and predictor modules. Moreover, aggressive low-bit quantization significantly degrades the alignment between the planning objective and task success, leading to failures that cannot be remedied by additional optimization. These findings reveal distinct quantization-induced failure modes in world model-based planning and provide practical guidance for deploying quantized world models under strict computational constraints. The code will be available at https://github.com/huawei-noah/noah-research/tree/master/QuantWM.

