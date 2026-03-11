---
layout: default
title: GAST: Gradient-aligned Sparse Tuning of Large Language Models with Data-layer Selection
---

# GAST: Gradient-aligned Sparse Tuning of Large Language Models with Data-layer Selection
**arXiv**：[2603.09865v1](https://arxiv.org/abs/2603.09865) · [PDF](https://arxiv.org/pdf/2603.09865.pdf)  
**作者**：Kai Yao, Zhenghan Song, Kaixin Wu, Mingjie Zhong, Danzhao Cheng, Zhaorui Tan, Yixin Ji, Penglei Gao  

**一句话要点**：提出GAST方法，通过梯度对齐的稀疏调优和数据层选择，统一优化大语言模型的高效微调。

**关键词**：参数高效微调, 稀疏调优, 数据选择, 层选择, 大语言模型, 梯度对齐

## 3 点简述
- 现有参数高效微调方法常忽略数据点对不同模型层的贡献差异，导致信息冗余或丢失。
- GAST结合数据选择和层稀疏策略，自适应选择每层最有效的数据点，实现统一优化。
- 实验表明GAST优于基线方法，为参数高效微调提供了新方向。

## 摘要（原文）

> Parameter-Efficient Fine-Tuning (PEFT) has become a key strategy for adapting large language models, with recent advances in sparse tuning reducing overhead by selectively updating key parameters or subsets of data. Existing approaches generally focus on two distinct paradigms: layer-selective methods aiming to fine-tune critical layers to minimize computational load, and data-selective methods aiming to select effective training subsets to boost training. However, current methods typically overlook the fact that different data points contribute varying degrees to distinct model layers, and they often discard potentially valuable information from data perceived as of low quality. To address these limitations, we propose Gradient-aligned Sparse Tuning (GAST), an innovative method that simultaneously performs selective fine-tuning at both data and layer dimensions as integral components of a unified optimization strategy. GAST specifically targets redundancy in information by employing a layer-sparse strategy that adaptively selects the most impactful data points for each layer, providing a more comprehensive and sophisticated solution than approaches restricted to a single dimension. Experiments demonstrate that GAST consistently outperforms baseline methods, establishing a promising direction for future research in PEFT strategies.

