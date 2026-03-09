---
layout: default
title: Spectral and Trajectory Regularization for Diffusion Transformer Super-Resolution
---

# Spectral and Trajectory Regularization for Diffusion Transformer Super-Resolution
**arXiv**：[2603.06275v1](https://arxiv.org/abs/2603.06275) · [PDF](https://arxiv.org/pdf/2603.06275.pdf)  
**作者**：Jingkai Wang, Yixin Tang, Jue Gong, Jiatong Li, Shu Li, Libo Liu, Jianliang Lan, Yutong Liu, Yulun Zhang  

**一句话要点**：提出StrSR框架，通过谱和轨迹正则化解决扩散变压器在真实图像超分辨率中的一步蒸馏问题。

**关键词**：扩散变压器, 图像超分辨率, 一步蒸馏, 谱正则化, 轨迹正则化, 对抗蒸馏

## 3 点简述
- 核心问题：扩散变压器在真实图像超分辨率中，一步蒸馏方法存在轨迹不匹配和周期性网格伪影。
- 方法要点：设计非对称判别蒸馏架构以弥合轨迹差距，并采用频率分布匹配策略抑制谱泄漏伪影。
- 实验或效果：在真实图像超分辨率任务中，StrSR在定量指标和视觉感知上达到最先进性能。

## 摘要（原文）

> Diffusion transformer (DiT) architectures show great potential for real-world image super-resolution (Real-ISR). However, their computationally expensive iterative sampling necessitates one-step distillation. Existing one-step distillation methods struggle with Real-ISR on DiT. They suffer from fundamental trajectory mismatch and generate severe grid-like periodic artifacts. To tackle these challenges, we propose StrSR, a novel one-step adversarial distillation framework featuring spectral and trajectory regularization. Specifically, we propose an asymmetric discriminative distillation architecture to bridge the trajectory gap. Additionally, we design a frequency distribution matching strategy to effectively suppress DiT-specific periodic artifacts caused by high-frequency spectral leakage. Extensive experiments demonstrate that StrSR achieves state-of-the-art performance in Real-ISR, across both quantitative metrics and visual perception. The code and models will be released at https://github.com/jkwang28/StrSR .

