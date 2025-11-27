---
layout: default
title: $\mathcal{E}_0$: Enhancing Generalization and Fine-Grained Control in VLA Models via Continuized Discrete Diffusion
---

# $\mathcal{E}_0$: Enhancing Generalization and Fine-Grained Control in VLA Models via Continuized Discrete Diffusion
**arXiv**：[2511.21542v1](https://arxiv.org/abs/2511.21542) · [PDF](https://arxiv.org/pdf/2511.21542.pdf)  
**作者**：Zhihao Zhan, Jiaying Zhou, Likui Zhang, Qinhan Lv, Hao Liu, Jusheng Zhang, Weizheng Li, Ziliang Chen, Tianshui Chen, Keze Wang, Liang Lin, Guangrun Wang  

**一句话要点**：提出E0连续化离散扩散框架以增强VLA模型的泛化性和精细控制

**关键词**：视觉语言动作模型, 离散扩散, 机器人控制, 泛化性, 精细动作控制, 去噪策略

## 3 点简述
- 现有VLA模型泛化能力差，动作生成粗糙或不稳定
- E0将动作生成建模为量化动作令牌的迭代去噪，匹配机器人控制的离散特性
- 实验在多个基准上实现SOTA，平均提升10.7%，真实世界验证精确操控

## 摘要（原文）

> Vision-Language-Action (VLA) models offer a unified framework for robotic manipulation by integrating visual perception, language understanding, and control generation. Yet existing VLA models still struggle to generalize across diverse tasks, scenes, and camera viewpoints, and often produce coarse or unstable actions. We introduce E0, a continuized discrete diffusion framework that formulates action generation as iterative denoising over quantized action tokens. Compared with continuous diffusion policies, E0 offers two key advantages: (1) discrete action tokens align naturally with the symbolic structure of pretrained VLM/VLA backbones, enabling stronger semantic conditioning; and 2. discrete diffusion matches the true quantized nature of real-world robot control-whose hardware constraints (e.g., encoder resolution, control frequency, actuation latency) inherently discretize continuous signals-and therefore benefits from a Bayes-optimal denoiser that models the correct discrete action distribution, leading to stronger generalization. Compared with discrete autoregressive and mask-based discrete diffusion models, E0 supports a significantly larger and finer-grained action vocabulary and avoids the distributional mismatch introduced by masking-based corruptions-yielding more accurate fine-grained action control. We further introduce a spherical viewpoint perturbation augmentation method to improve robustness to camera shifts without additional data. Experiments on LIBERO, VLABench, and ManiSkill show that E0 achieves state-of-the-art performance across 14 diverse environments, outperforming strong baselines by 10.7% on average. Real-world evaluation on a Franka arm confirms that E0 delivers precise, robust, and transferable manipulation, establishing discrete diffusion as a promising direction for generalizable VLA policy learning.

