---
layout: default
title: Cross-Space Synergy: A Unified Framework for Multimodal Emotion Recognition in Conversation
---

# Cross-Space Synergy: A Unified Framework for Multimodal Emotion Recognition in Conversation
**arXiv**：[2512.03521v1](https://arxiv.org/abs/2512.03521) · [PDF](https://arxiv.org/pdf/2512.03521.pdf)  
**作者**：Xiaosen Lyu, Jiayu Xiong, Yuren Chen, Wanlong Wang, Xiaoqing Dai, Jing Wang  

**一句话要点**：提出Cross-Space Synergy框架，通过协同表示与优化解决多模态对话情感识别中的交互与训练问题。

**关键词**：多模态情感识别, 对话情感分析, 跨模态交互, 梯度优化, 帕累托最优, 低秩张量分解

## 3 点简述
- 核心问题：现有方法难以捕捉复杂跨模态交互，且深层架构易导致梯度冲突与训练不稳定。
- 方法要点：结合Synergistic Polynomial Fusion高效建模高阶跨模态交互，Pareto Gradient Modulator沿帕累托最优方向优化以缓解梯度冲突。
- 实验或效果：在IEMOCAP和MELD数据集上超越现有方法，提升准确率与训练稳定性。

## 摘要（原文）

> Multimodal Emotion Recognition in Conversation (MERC) aims to predict speakers' emotions by integrating textual, acoustic, and visual cues. Existing approaches either struggle to capture complex cross-modal interactions or experience gradient conflicts and unstable training when using deeper architectures. To address these issues, we propose Cross-Space Synergy (CSS), which couples a representation component with an optimization component. Synergistic Polynomial Fusion (SPF) serves the representation role, leveraging low-rank tensor factorization to efficiently capture high-order cross-modal interactions. Pareto Gradient Modulator (PGM) serves the optimization role, steering updates along Pareto-optimal directions across competing objectives to alleviate gradient conflicts and improve stability. Experiments show that CSS outperforms existing representative methods on IEMOCAP and MELD in both accuracy and training stability, demonstrating its effectiveness in complex multimodal scenarios.

