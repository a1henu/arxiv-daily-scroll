---
layout: default
title: FiDeSR: High-Fidelity and Detail-Preserving One-Step Diffusion Super-Resolution
---

# FiDeSR: High-Fidelity and Detail-Preserving One-Step Diffusion Super-Resolution
**arXiv**：[2603.02692v1](https://arxiv.org/abs/2603.02692) · [PDF](https://arxiv.org/pdf/2603.02692.pdf)  
**作者**：Aro Kim, Myeongjin Jang, Chaewon Moon, Youngjin Shin, Jinwoo Jeong, Sang-hyo Park  

**一句话要点**：提出FiDeSR以解决扩散超分辨率中细节保留与高保真重建的平衡问题

**关键词**：扩散超分辨率, 细节感知加权, 自适应增强, 噪声细化, 高保真重建

## 3 点简述
- 现有扩散超分辨率方法难以同时保持细节和高保真，导致视觉质量不佳
- 训练时采用细节感知加权策略，推理时使用自适应增强器，无需重训练即可灵活控制增强
- 通过残差中残差噪声细化纠正预测误差，提升细节恢复，实验显示优于现有方法

## 摘要（原文）

> Diffusion-based approaches have recently driven remarkable progress in real-world image super-resolution (SR). However, existing methods still struggle to simultaneously preserve fine details and ensure high-fidelity reconstruction, often resulting in suboptimal visual quality. In this paper, we propose FiDeSR, a high-fidelity and detail-preserving one-step diffusion super-resolution framework. During training, we introduce a detail-aware weighting strategy that adaptively emphasizes regions where the model exhibits higher prediction errors. During inference, low- and high-frequency adaptive enhancers further refine the reconstruction without requiring model retraining, enabling flexible enhancement control. To further improve the reconstruction accuracy, FiDeSR incorporates a residual-in-residual noise refinement, which corrects prediction errors in the diffusion noise and enhances fine detail recovery. FiDeSR achieves superior real-world SR performance compared to existing diffusion-based methods, producing outputs with both high perceptual quality and faithful content restoration. The source code will be released at: https://github.com/Ar0Kim/FiDeSR.

