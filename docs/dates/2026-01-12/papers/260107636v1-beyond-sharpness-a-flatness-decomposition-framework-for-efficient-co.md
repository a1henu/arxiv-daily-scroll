---
layout: default
title: Beyond Sharpness: A Flatness Decomposition Framework for Efficient Continual Learning
---

# Beyond Sharpness: A Flatness Decomposition Framework for Efficient Continual Learning
**arXiv**：[2601.07636v1](https://arxiv.org/abs/2601.07636) · [PDF](https://arxiv.org/pdf/2601.07636.pdf)  
**作者**：Yanan Chen, Tieliang Gong, Yunjiao Zhang, Wen Wen  

**一句话要点**：提出FLAD框架，通过分解平坦度扰动以高效解决持续学习中的遗忘问题。

**关键词**：持续学习, 平坦度分解, 优化框架, 泛化提升, 计算效率

## 3 点简述
- 现有基于平坦度的持续学习方法未区分扰动成分，且计算开销大。
- FLAD将平坦度扰动分解为梯度对齐和随机噪声成分，仅保留噪声以提升泛化。
- 实验表明FLAD在多种持续学习场景中优于标准及平坦度感知优化器，计算高效。

## 摘要（原文）

> Continual Learning (CL) aims to enable models to sequentially learn multiple tasks without forgetting previous knowledge. Recent studies have shown that optimizing towards flatter loss minima can improve model generalization. However, existing sharpness-aware methods for CL suffer from two key limitations: (1) they treat sharpness regularization as a unified signal without distinguishing the contributions of its components. and (2) they introduce substantial computational overhead that impedes practical deployment. To address these challenges, we propose FLAD, a novel optimization framework that decomposes sharpness-aware perturbations into gradient-aligned and stochastic-noise components, and show that retaining only the noise component promotes generalization. We further introduce a lightweight scheduling scheme that enables FLAD to maintain significant performance gains even under constrained training time. FLAD can be seamlessly integrated into various CL paradigms and consistently outperforms standard and sharpness-aware optimizers in diverse experimental settings, demonstrating its effectiveness and practicality in CL.

