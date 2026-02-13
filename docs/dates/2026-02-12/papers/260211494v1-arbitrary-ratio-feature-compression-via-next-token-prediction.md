---
layout: default
title: Arbitrary Ratio Feature Compression via Next Token Prediction
---

# Arbitrary Ratio Feature Compression via Next Token Prediction
**arXiv**：[2602.11494v1](https://arxiv.org/abs/2602.11494) · [PDF](https://arxiv.org/pdf/2602.11494.pdf)  
**作者**：Yufan Liu, Daoyuan Ren, Zhipeng Zhang, Wenyang Luo, Bing Li, Weiming Hu, Stephen Maybank  

**一句话要点**：提出任意比率特征压缩框架，通过下一令牌预测实现单模型灵活压缩

**关键词**：特征压缩, 自回归模型, 跨模态检索, 实体关系图, 任意压缩比, 下一令牌预测

## 3 点简述
- 现有特征压缩方法需针对不同压缩比训练专用模型，缺乏灵活性
- 核心为自回归压缩器，通过调整生成令牌数控制压缩比，并引入混合解和实体关系图约束提升质量
- 在跨模态检索等任务中，多数据集实验显示优于现有方法，有时甚至超越未压缩特征

## 摘要（原文）

> Feature compression is increasingly important for improving the efficiency of downstream tasks, especially in applications involving large-scale or multi-modal data. While existing methods typically rely on dedicated models for achieving specific compression ratios, they are often limited in flexibility and generalization. In particular, retraining is necessary when adapting to a new compression ratio. To address this limitation, we propose a novel and flexible Arbitrary Ratio Feature Compression (ARFC) framework, which supports any compression ratio with a single model, eliminating the need for multiple specialized models. At its core, the Arbitrary Ratio Compressor (ARC) is an auto-regressive model that performs compression via next-token prediction. This allows the compression ratio to be controlled at inference simply by adjusting the number of generated tokens. To enhance the quality of the compressed features, two key modules are introduced. The Mixture of Solutions (MoS) module refines the compressed tokens by utilizing multiple compression results (solutions), reducing uncertainty and improving robustness. The Entity Relation Graph Constraint (ERGC) is integrated into the training process to preserve semantic and structural relationships during compression. Extensive experiments on cross-modal retrieval, image classification, and image retrieval tasks across multiple datasets demonstrate that our method consistently outperforms existing approaches at various compression ratios. Notably, in some cases, it even surpasses the performance of the original, uncompressed features. These results validate the effectiveness and versatility of ARFC for practical, resource-constrained scenarios.

