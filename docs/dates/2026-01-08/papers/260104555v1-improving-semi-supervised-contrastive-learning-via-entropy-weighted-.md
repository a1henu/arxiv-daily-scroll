---
layout: default
title: Improving Semi-Supervised Contrastive Learning via Entropy-Weighted Confidence Integration of Anchor-Positive Pairs
---

# Improving Semi-Supervised Contrastive Learning via Entropy-Weighted Confidence Integration of Anchor-Positive Pairs
**arXiv**：[2601.04555v1](https://arxiv.org/abs/2601.04555) · [PDF](https://arxiv.org/pdf/2601.04555.pdf)  
**作者**：Shogo Nakayama, Masahiro Okuda  

**一句话要点**：提出基于熵加权置信度整合锚点-正样本对的损失函数，以改进半监督对比学习在低标签条件下的性能。

**关键词**：半监督学习, 对比学习, 熵加权, 置信度估计, 伪标签分配, 低标签条件

## 3 点简述
- 传统半监督对比学习仅对高置信度样本分配伪标签，导致部分样本被排除训练。
- 新方法通过预测概率分布的熵估计样本置信度，并应用置信度自适应加权，实现更全面的伪标签分配。
- 实验表明，该方法在低标签条件下提高了分类准确率，并实现了更稳定的学习性能。

## 摘要（原文）

> Conventional semi-supervised contrastive learning methods assign pseudo-labels only to samples whose highest predicted class probability exceeds a predefined threshold, and then perform supervised contrastive learning using those selected samples. In this study, we propose a novel loss function that estimates the confidence of each sample based on the entropy of its predicted probability distribution and applies confidence-based adaptive weighting. This approach enables pseudo-label assignment even to samples that were previously excluded from training and facilitates contrastive learning that accounts for the confidence of both anchor and positive samples in a more principled manner. Experimental results demonstrate that the proposed method improves classification accuracy and achieves more stable learning performance even under low-label conditions.

