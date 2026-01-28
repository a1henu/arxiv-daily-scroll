---
layout: default
title: Speed is Confidence
---

# Speed is Confidence
**arXiv**：[2601.19085v1](https://arxiv.org/abs/2601.19085) · [PDF](https://arxiv.org/pdf/2601.19085.pdf)  
**作者**：Joshua V. Dillon  

**一句话要点**：提出基于首个停止的集成预测方法，以低计算成本实现高精度数独求解

**关键词**：集成学习, 推理效率, 置信度估计, 数独求解, 训练优化

## 3 点简述
- 核心问题：生物神经系统的快速性与能量约束，启发将推理速度作为置信度指标
- 方法要点：使用Tiny Recursive Models集成，仅基于首个停止的模型进行预测，避免平均预测
- 实验或效果：在Sudoku-Extreme上达到97.2%准确率，计算量比基线减少10倍

## 摘要（原文）

> Biological neural systems must be fast but are energy-constrained. Evolution's solution: act on the first signal. Winner-take-all circuits and time-to-first-spike coding implicitly treat when a neuron fires as an expression of confidence. We apply this principle to ensembles of Tiny Recursive Models (TRM). By basing the ensemble prediction solely on the first to halt rather than averaging predictions, we achieve 97.2% puzzle accuracy on Sudoku-Extreme while using 10x less compute than test-time augmentation (the baseline achieves 86.1% single-pass, 97.3% with TTA). Inference speed is an implicit indication of confidence. But can this capability be manifested as a training-only cost? Evidently yes: by maintaining K = 4 parallel latent states during training but backpropping only through the lowest-loss "winner," a single model achieves 96.9% +/- 0.6% puzzle accuracy with a single forward pass-matching TTA performance without any test-time augmentation. As in nature, this work was also resource constrained: all experimentation used a single RTX 5090. This necessitated efficiency and compelled our invention of a modified SwiGLU which made Muon viable. With Muon and K = 1 training, we exceed TRM baseline performance in 7k steps (40 min). Higher accuracy requires 36k steps: 1.5 hours for K = 1, 6 hours for K = 4.

