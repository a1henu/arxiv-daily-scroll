---
layout: default
title: AVP-Pro: An Adaptive Multi-Modal Fusion and Contrastive Learning Approach for Comprehensive Two-Stage Antiviral Peptide Identification
---

# AVP-Pro: An Adaptive Multi-Modal Fusion and Contrastive Learning Approach for Comprehensive Two-Stage Antiviral Peptide Identification
**arXiv**：[2601.11028v1](https://arxiv.org/abs/2601.11028) · [PDF](https://arxiv.org/pdf/2601.11028.pdf)  
**作者**：Xinru Wen, Weizhong Lin, zi liu, Xuan Xiao  

**一句话要点**：提出AVP-Pro，一种自适应多模态融合与对比学习框架，用于两阶段抗病毒肽识别

**关键词**：抗病毒肽识别, 多模态融合, 对比学习, 自适应门控, 两阶段预测, 小样本学习

## 3 点简述
- 核心问题：现有方法难以捕获复杂序列依赖和区分高相似度样本，影响抗病毒肽识别准确性。
- 方法要点：构建全景特征空间，结合自注意力和自适应门控机制动态融合CNN和BiLSTM特征，并采用OHEM驱动的对比学习增强判别力。
- 实验或效果：在通用识别阶段准确率达0.9531，MCC为0.9064，优于现有方法；在功能亚型预测阶段实现小样本下6个病毒家族和8种特定病毒的准确分类。

## 摘要（原文）

> The accurate identification of antiviral peptides (AVPs) is crucial for novel drug development. However, existing methods still have limitations in capturing complex sequence dependencies and distinguishing confusing samples with high similarity. To address these challenges, we propose AVP-Pro, a novel two-stage predictive framework that integrates adaptive feature fusion and contrastive learning. To comprehensively capture the physicochemical properties and deep-seated patterns of peptide sequences, we constructed a panoramic feature space encompassing 10 distinct descriptors and designed a hierarchical fusion architecture. This architecture integrates self-attention and adaptive gating mechanisms to dynamically modulate the weights of local motifs extracted by CNNs and global dependencies captured by BiLSTMs based on sequence context. Targeting the blurred decision boundary caused by the high similarity between positive and negative sample sequences, we adopted an Online Hard Example Mining (OHEM)-driven contrastive learning strategy enhanced by BLOSUM62. This approach significantly sharpened the model's discriminative power. Model evaluation results show that in the first stage of general AVP identification, the model achieved an accuracy of 0.9531 and an MCC of 0.9064, outperforming existing state-of-the-art (SOTA) methods. In the second stage of functional subtype prediction, combined with a transfer learning strategy, the model realized accurate classification of 6 viral families and 8 specific viruses under small-sample conditions. AVP-Pro provides a powerful and interpretable new tool for the high-throughput screening of antiviral drugs. To further enhance accessibility for users, we have developed a user-friendly web interface, which is available at https://wwwy1031-avp-pro.hf.space.

