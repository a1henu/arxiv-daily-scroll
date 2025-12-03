---
layout: default
title: VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling
---

# VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling
**arXiv**：[2512.02902v1](https://arxiv.org/abs/2512.02902) · [PDF](https://arxiv.org/pdf/2512.02902.pdf)  
**作者**：Weiqi Li, Quande Zhang, Ruifeng Zhai, Liang Lin, Guangrun Wang  

**一句话要点**：提出轻量级视觉适应框架，通过特征校准解决VLA模型视角泛化问题

**关键词**：视觉语言动作模型, 空间建模, 视角泛化, 轻量级适应, 特征校准

## 3 点简述
- 核心问题：VLA模型在视角变化下性能骤降，源于空间建模而非物理建模的错位
- 方法要点：提出FTM全局仿射变换和FLA低秩更新，实现轻量级视觉表征重校准
- 实验效果：FTM仅用4K参数将Libero视角准确率从48.5%提升至87.1%，FLA达90.8%

## 摘要（原文）

> Vision-language-action (VLA) models achieve strong in-distribution performance but degrade sharply under novel camera viewpoints and visual perturbations. We show that this brittleness primarily arises from misalignment in Spatial Modeling, rather than Physical Modeling. To address this, we propose a one-shot adaptation framework that recalibrates visual representations through lightweight, learnable updates. Our first method, Feature Token Modulation (FTM), applies a global affine transformation to visual tokens and improves Libero viewpoint accuracy from 48.5% to 87.1% with only 4K parameters. Building on this, Feature Linear Adaptation (FLA) introduces low-rank updates to the ViT encoder, achieving 90.8% success with 4.7M parameters -- matching LoRA-scale finetuning at far lower cost. Together, these results reveal substantial untapped robustness in pretrained VLA models and demonstrate that targeted, minimal visual adaptation is sufficient to restore viewpoint generalization.

