---
layout: default
title: Scaling Up AI-Generated Image Detection via Generator-Aware Prototypes
---

# Scaling Up AI-Generated Image Detection via Generator-Aware Prototypes
**arXiv**：[2512.12982v1](https://arxiv.org/abs/2512.12982) · [PDF](https://arxiv.org/pdf/2512.12982.pdf)  
**作者**：Ziheng Qin, Yuheng Ji, Renshuai Tao, Yuxuan Tian, Yuyang Liu, Yipu Wang, Xiaolong Zheng  

**一句话要点**：提出生成器感知原型学习以解决AI生成图像检测中的多样性与模型瓶颈问题

**关键词**：AI生成图像检测, 原型学习, 低秩适应, 特征空间统一, 生成器多样性

## 3 点简述
- 核心问题：检测器性能随生成器多样性增加而停滞或下降，源于数据异质性和固定编码器瓶颈
- 方法要点：通过结构化原型学习统一特征空间，结合低秩适应增强模型判别力
- 实验或效果：在多种生成器上实现最先进检测精度，代码开源

## 摘要（原文）

> The pursuit of a universal AI-generated image (AIGI) detector often relies on aggregating data from numerous generators to improve generalization. However, this paper identifies a paradoxical phenomenon we term the Benefit then Conflict dilemma, where detector performance stagnates and eventually degrades as source diversity expands. Our systematic analysis, diagnoses this failure by identifying two core issues: severe data-level heterogeneity, which causes the feature distributions of real and synthetic images to increasingly overlap, and a critical model-level bottleneck from fixed, pretrained encoders that cannot adapt to the rising complexity. To address these challenges, we propose Generator-Aware Prototype Learning (GAPL), a framework that constrain representation with a structured learning paradigm. GAPL learns a compact set of canonical forgery prototypes to create a unified, low-variance feature space, effectively countering data heterogeneity.To resolve the model bottleneck, it employs a two-stage training scheme with Low-Rank Adaptation, enhancing its discriminative power while preserving valuable pretrained knowledge. This approach establishes a more robust and generalizable decision boundary. Through extensive experiments, we demonstrate that GAPL achieves state-of-the-art performance, showing superior detection accuracy across a wide variety of GAN and diffusion-based generators. Code is available at https://github.com/UltraCapture/GAPL

