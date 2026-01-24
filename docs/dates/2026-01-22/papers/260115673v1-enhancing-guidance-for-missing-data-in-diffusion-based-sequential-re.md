---
layout: default
title: Enhancing guidance for missing data in diffusion-based sequential recommendation
---

# Enhancing guidance for missing data in diffusion-based sequential recommendation
**arXiv**：[2601.15673v1](https://arxiv.org/abs/2601.15673) · [PDF](https://arxiv.org/pdf/2601.15673.pdf)  
**作者**：Qilong Yan, Yifei Xing, Dugang Liu, Jingpu Duan, Jian Yin  

**一句话要点**：提出CARD模型以解决序列推荐中缺失数据导致的引导质量下降问题。

**关键词**：序列推荐, 扩散模型, 缺失数据处理, 注意力机制, 兴趣转折点, 反事实学习

## 3 点简述
- 核心问题：序列推荐中用户信息缺失影响扩散模型引导质量，忽略兴趣转折点。
- 方法要点：使用双面汤普森采样识别兴趣转折序列，结合反事实注意力机制重加权项目重要性。
- 实验或效果：在真实数据上表现良好，计算成本低，代码已开源。

## 摘要（原文）

> Contemporary sequential recommendation methods are becoming more complex, shifting from classification to a diffusion-guided generative paradigm. However, the quality of guidance in the form of user information is often compromised by missing data in the observed sequences, leading to suboptimal generation quality. Existing methods address this by removing locally similar items, but overlook ``critical turning points'' in user interest, which are crucial for accurately predicting subsequent user intent. To address this, we propose a novel Counterfactual Attention Regulation Diffusion model (CARD), which focuses on amplifying the signal from key interest-turning-point items while concurrently identifying and suppressing noise within the user sequence. CARD consists of (1) a Dual-side Thompson Sampling method to identify sequences undergoing significant interest shift, and (2) a counterfactual attention mechanism for these sequences to quantify the importance of each item. In this manner, CARD provides the diffusion model with a high-quality guidance signal composed of dynamically re-weighted interaction vectors to enable effective generation. Experiments show our method works well on real-world data without being computationally expensive. Our code is available at https://github.com/yanqilong3321/CARD.

