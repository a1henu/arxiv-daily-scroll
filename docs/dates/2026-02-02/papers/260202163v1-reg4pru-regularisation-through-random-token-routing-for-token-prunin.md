---
layout: default
title: Reg4Pru: Regularisation Through Random Token Routing for Token Pruning
---

# Reg4Pru: Regularisation Through Random Token Routing for Token Pruning
**arXiv**：[2602.02163v1](https://arxiv.org/abs/2602.02163) · [PDF](https://arxiv.org/pdf/2602.02163.pdf)  
**作者**：Julian Wyatt, Ronald Clark, Irina Voiculescu  

**一句话要点**：提出Reg4Pru正则化方法，通过随机令牌路由缓解令牌剪枝在分割任务中的性能损失。

**关键词**：令牌剪枝, 正则化训练, 随机路由, 分割任务, 计算效率

## 3 点简述
- 核心问题：Transformer令牌剪枝提高计算效率但导致深层表示不稳定，降低密集预测性能。
- 方法要点：引入训练正则化技术，通过随机令牌路由来稳定剪枝后的表示。
- 实验或效果：在FIVES血管分割数据集上，平均精度绝对提升46%，同时实现29%的相对加速。

## 摘要（原文）

> Transformers are widely adopted in modern vision models due to their strong ability to scale with dataset size and generalisability. However, this comes with a major drawback: computation scales quadratically to the total number of tokens. Numerous methods have been proposed to mitigate this. For example, we consider token pruning with reactivating tokens from preserved representations, but the increased computational efficiency of this method results in decreased stability from the preserved representations, leading to poorer dense prediction performance at deeper layers. In this work, we introduce Reg4Pru, a training regularisation technique that mitigates token-pruning performance loss for segmentation. We compare our models on the FIVES blood vessel segmentation dataset and find that Reg4Pru improves average precision by an absolute 46% compared to the same model trained without routing. This increase is observed using a configuration that achieves a 29% relative speedup in wall-clock time compared to the non-pruned baseline. These findings indicate that Reg4Pru is a valuable regulariser for token reduction strategies.

