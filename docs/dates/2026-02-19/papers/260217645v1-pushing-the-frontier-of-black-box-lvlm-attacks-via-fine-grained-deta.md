---
layout: default
title: Pushing the Frontier of Black-Box LVLM Attacks via Fine-Grained Detail Targeting
---

# Pushing the Frontier of Black-Box LVLM Attacks via Fine-Grained Detail Targeting
**arXiv**：[2602.17645v1](https://arxiv.org/abs/2602.17645) · [PDF](https://arxiv.org/pdf/2602.17645.pdf)  
**作者**：Xiaohan Zhao, Zhaoyi Li, Yaxin Luo, Jiacheng Cui, Zhiqiang Shen  

**一句话要点**：提出M-Attack-V2以提升黑盒大视觉语言模型攻击的迁移成功率

**关键词**：黑盒对抗攻击, 大视觉语言模型, 梯度去噪, 迁移攻击, 局部对齐

## 3 点简述
- 核心问题：现有迁移攻击方法因ViT平移敏感性和结构不对称导致梯度高方差，破坏局部对齐稳定性。
- 方法要点：通过多裁剪对齐和辅助目标对齐降低梯度方差，结合补丁动量和改进的补丁大小集成增强可迁移方向。
- 实验或效果：在Claude-4.0、Gemini-2.5-Pro和GPT-5上显著提升攻击成功率，优于先前黑盒LVLM攻击方法。

## 摘要（原文）

> Black-box adversarial attacks on Large Vision-Language Models (LVLMs) are challenging due to missing gradients and complex multimodal boundaries. While prior state-of-the-art transfer-based approaches like M-Attack perform well using local crop-level matching between source and target images, we find this induces high-variance, nearly orthogonal gradients across iterations, violating coherent local alignment and destabilizing optimization. We attribute this to (i) ViT translation sensitivity that yields spike-like gradients and (ii) structural asymmetry between source and target crops. We reformulate local matching as an asymmetric expectation over source transformations and target semantics, and build a gradient-denoising upgrade to M-Attack. On the source side, Multi-Crop Alignment (MCA) averages gradients from multiple independently sampled local views per iteration to reduce variance. On the target side, Auxiliary Target Alignment (ATA) replaces aggressive target augmentation with a small auxiliary set from a semantically correlated distribution, producing a smoother, lower-variance target manifold. We further reinterpret momentum as Patch Momentum, replaying historical crop gradients; combined with a refined patch-size ensemble (PE+), this strengthens transferable directions. Together these modules form M-Attack-V2, a simple, modular enhancement over M-Attack that substantially improves transfer-based black-box attacks on frontier LVLMs: boosting success rates on Claude-4.0 from 8% to 30%, Gemini-2.5-Pro from 83% to 97%, and GPT-5 from 98% to 100%, outperforming prior black-box LVLM attacks. Code and data are publicly available at: https://github.com/vila-lab/M-Attack-V2.

