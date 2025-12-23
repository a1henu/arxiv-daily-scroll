---
layout: default
title: SAP: Syntactic Attention Pruning for Transformer-based Language Models
---

# SAP: Syntactic Attention Pruning for Transformer-based Language Models
**arXiv**：[2512.19125v1](https://arxiv.org/abs/2512.19125) · [PDF](https://arxiv.org/pdf/2512.19125.pdf)  
**作者**：Tzu-Yun Lee, Ding-Yong Hong, Jan-Jan Wu  

**一句话要点**：提出SAP方法，结合句法结构与注意力模式，有效剪枝Transformer模型注意力头。

**关键词**：注意力头剪枝, Transformer模型, 句法结构, 模型压缩, 可解释性

## 3 点简述
- 核心问题：传统剪枝方法依赖数学分析，忽略语言特征，可能影响模型性能与可解释性。
- 方法要点：SAP利用句法结构和注意力模式指导剪枝，并引入候选过滤机制提升鲁棒性。
- 实验或效果：在免重训练设置下，SAP优于现有方法，保留关键注意力头，性能与先进方法相当。

## 摘要（原文）

> This paper introduces Syntactic Attention Pruning (SAP), a novel method for effectively pruning attention heads in Transformer models. Unlike conventional approaches that rely solely on mathematical analysis of model weights and activations, SAP incorporates both the syntactic structure and attention patterns of sentences to guide the pruning process. By leveraging these linguistic features, SAP not only achieves performance comparable to state-of-the-art methods but also enhances the interpretability of model behavior. To further improve robustness, we propose Candidate Filtering (CF), a mechanism that prioritizes heads based on their contribution to model performance, mitigating degradation during pruning. Experimental results indicate that SAP effectively preserves critical heads of a high density of strong attention values, outperforming existing head pruning strategies in retrain-free settings. These findings position SAP as a promising foundation for a new direction in model compression research, offering high flexibility for pruning across all transformer-based language models.

