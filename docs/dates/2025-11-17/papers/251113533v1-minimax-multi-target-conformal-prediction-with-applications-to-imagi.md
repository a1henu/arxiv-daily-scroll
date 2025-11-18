---
layout: default
title: Minimax Multi-Target Conformal Prediction with Applications to Imaging Inverse Problems
---

# Minimax Multi-Target Conformal Prediction with Applications to Imaging Inverse Problems
**arXiv**：[2511.13533v1](https://arxiv.org/abs/2511.13533) · [PDF](https://arxiv.org/pdf/2511.13533.pdf)  
**作者**：Jeffrey Wen, Rizwan Ahmad, Philip Schniter  

**一句话要点**：提出渐近极小极大多目标共形预测方法，以解决不适定成像逆问题中的不确定性量化挑战。

**关键词**：共形预测, 成像逆问题, 不确定性量化, 多目标预测, 极小极大优化, 盲图像质量评估

## 3 点简述
- 核心问题：不适定成像逆问题中多目标不确定性量化困难，尤其在安全关键应用。
- 方法要点：渐近极小极大方法确保联合边际覆盖，提供紧密预测区间。
- 实验或效果：在合成和MRI数据上验证优于现有方法，应用于多指标盲图像质量评估等。

## 摘要（原文）

> In ill-posed imaging inverse problems, uncertainty quantification remains a fundamental challenge, especially in safety-critical applications. Recently, conformal prediction has been used to quantify the uncertainty that the inverse problem contributes to downstream tasks like image classification, image quality assessment, fat mass quantification, etc. While existing works handle only a scalar estimation target, practical applications often involve multiple targets. In response, we propose an asymptotically minimax approach to multi-target conformal prediction that provides tight prediction intervals while ensuring joint marginal coverage. We then outline how our minimax approach can be applied to multi-metric blind image quality assessment, multi-task uncertainty quantification, and multi-round measurement acquisition. Finally, we numerically demonstrate the benefits of our minimax method, relative to existing multi-target conformal prediction methods, using both synthetic and magnetic resonance imaging (MRI) data.

