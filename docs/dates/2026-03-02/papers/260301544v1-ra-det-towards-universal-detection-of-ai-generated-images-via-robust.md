---
layout: default
title: RA-Det: Towards Universal Detection of AI-Generated Images via Robustness Asymmetry
---

# RA-Det: Towards Universal Detection of AI-Generated Images via Robustness Asymmetry
**arXiv**：[2603.01544v1](https://arxiv.org/abs/2603.01544) · [PDF](https://arxiv.org/pdf/2603.01544.pdf)  
**作者**：Xinchang Wang, Yunhao Chen, Yuechen Zhang, Congcong Bian, Zihao Guo, Xingjun Ma, Hui Li  

**一句话要点**：提出RA-Det框架，利用鲁棒性不对称性实现AI生成图像的通用检测

**关键词**：AI生成图像检测, 鲁棒性不对称性, 行为驱动检测, 通用检测框架, 特征漂移分析

## 3 点简述
- 核心问题：AI生成图像外观逼真，传统基于外观的检测器稳定性下降
- 方法要点：从外观转向行为，利用自然与生成图像在扰动下的特征漂移差异
- 实验或效果：在14个生成模型上评估，平均性能提升7.81%，无需生成器指纹

## 摘要（原文）

> Recent image generators produce photo-realistic content that undermines the reliability of downstream recognition systems. As visual appearance cues become less pronounced, appearance-driven detectors that rely on forensic cues or high-level representations lose stability. This motivates a shift from appearance to behavior, focusing on how images respond to controlled perturbations rather than how they look. In this work, we identify a simple and universal behavioral signal. Natural images preserve stable semantic representations under small, structured perturbations, whereas generated images exhibit markedly larger feature drift. We refer to this phenomenon as robustness asymmetry and provide a theoretical analysis that establishes a lower bound connecting this asymmetry to memorization tendencies in generative models, explaining its prevalence across architectures. Building on this insight, we introduce Robustness Asymmetry Detection (RA-Det), a behavior-driven detection framework that converts robustness asymmetry into a reliable decision signal. Evaluated across 14 diverse generative models and against more than 10 strong detectors, RA-Det achieves superior performance, improving the average performance by 7.81 percent. The method is data- and model-agnostic, requires no generator fingerprints, and transfers across unseen generators. Together, these results indicate that robustness asymmetry is a stable, general cue for synthetic-image detection and that carefully designed probing can turn this cue into a practical, universal detector. The source code is publicly available at Github.

