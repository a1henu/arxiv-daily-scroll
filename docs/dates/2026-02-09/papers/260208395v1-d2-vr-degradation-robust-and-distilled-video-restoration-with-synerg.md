---
layout: default
title: D$^2$-VR: Degradation-Robust and Distilled Video Restoration with Synergistic Optimization Strategy
---

# D$^2$-VR: Degradation-Robust and Distilled Video Restoration with Synergistic Optimization Strategy
**arXiv**：[2602.08395v1](https://arxiv.org/abs/2602.08395) · [PDF](https://arxiv.org/pdf/2602.08395.pdf)  
**作者**：Jianfeng Liang, Shaocheng Shen, Botao Xu, Qiang Hu, Xiaoyun Zhang  

**一句话要点**：提出D²-VR框架以解决视频修复中推理延迟高和时序不稳定问题

**关键词**：视频修复, 扩散模型, 时序对齐, 对抗蒸馏, 退化鲁棒性

## 3 点简述
- 核心问题：扩散先验与时间对齐结合的视频修复框架存在高推理延迟和复杂退化下的时序不稳定
- 方法要点：设计退化鲁棒流对齐模块过滤不可靠运动线索，采用对抗蒸馏压缩采样轨迹
- 实验或效果：在实验中实现12倍加速，达到先进性能，提升感知质量和时序一致性

## 摘要（原文）

> The integration of diffusion priors with temporal alignment has emerged as a transformative paradigm for video restoration, delivering fantastic perceptual quality, yet the practical deployment of such frameworks is severely constrained by prohibitive inference latency and temporal instability when confronted with complex real-world degradations. To address these limitations, we propose \textbf{D$^2$-VR}, a single-image diffusion-based video-restoration framework with low-step inference. To obtain precise temporal guidance under severe degradation, we first design a Degradation-Robust Flow Alignment (DRFA) module that leverages confidence-aware attention to filter unreliable motion cues. We then incorporate an adversarial distillation paradigm to compress the diffusion sampling trajectory into a rapid few-step regime. Finally, a synergistic optimization strategy is devised to harmonize perceptual quality with rigorous temporal consistency. Extensive experiments demonstrate that D$^2$-VR achieves state-of-the-art performance while accelerating the sampling process by \textbf{12$\times$}

