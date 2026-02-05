---
layout: default
title: Identifying Intervenable and Interpretable Features via Orthogonality Regularization
---

# Identifying Intervenable and Interpretable Features via Orthogonality Regularization
**arXiv**：[2602.04718v1](https://arxiv.org/abs/2602.04718) · [PDF](https://arxiv.org/pdf/2602.04718.pdf)  
**作者**：Moritz Miller, Florent Draye, Bernhard Schölkopf  

**一句话要点**：提出正交正则化方法以识别可干预和可解释特征，应用于语言模型微调场景。

**关键词**：正交正则化, 特征解耦, 可解释性, 因果干预, 语言模型微调, 稀疏自编码器

## 3 点简述
- 核心问题：语言模型特征存在干扰和叠加，影响可解释性和干预能力。
- 方法要点：通过正交正则化使解码器矩阵特征几乎正交，减少干扰并确保分解唯一性。
- 实验或效果：正交化特征提升解释距离，支持孤立干预，性能基本保持不变。

## 摘要（原文）

> With recent progress on fine-tuning language models around a fixed sparse autoencoder, we disentangle the decoder matrix into almost orthogonal features. This reduces interference and superposition between the features, while keeping performance on the target dataset essentially unchanged. Our orthogonality penalty leads to identifiable features, ensuring the uniqueness of the decomposition. Further, we find that the distance between embedded feature explanations increases with stricter orthogonality penalty, a desirable property for interpretability. Invoking the $\textit{Independent Causal Mechanisms}$ principle, we argue that orthogonality promotes modular representations amenable to causal intervention. We empirically show that these increasingly orthogonalized features allow for isolated interventions. Our code is available under $\texttt{https://github.com/mrtzmllr/sae-icm}$.

