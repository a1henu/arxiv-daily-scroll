---
layout: default
title: SkipCat: Rank-Maximized Low-Rank Compression of Large Language Models via Shared Projection and Block Skipping
---

# SkipCat: Rank-Maximized Low-Rank Compression of Large Language Models via Shared Projection and Block Skipping
**arXiv**：[2512.13494v1](https://arxiv.org/abs/2512.13494) · [PDF](https://arxiv.org/pdf/2512.13494.pdf)  
**作者**：Yu-Chen Lu, Sheng-Feng Yu, Hui-Hsien Weng, Pei-Shuo Wang, Yu-Fang Hu, Liang Hung-Chun, Hung-Yueh Chiang, Kai-Chiang Wu  

**一句话要点**：提出SkipCat框架，通过共享投影和块跳过实现大语言模型的高效低秩压缩

**关键词**：大语言模型压缩, 低秩分解, 共享投影, 块跳过, 资源受限部署, 零样本性能

## 3 点简述
- 核心问题：低秩压缩需大幅降低秩以节省资源，但导致性能显著下降
- 方法要点：引入层内共享低秩投影和块跳过技术，在相同压缩率下保留更多有效秩
- 实验或效果：在零样本任务上，相同压缩率下准确率提升7%，无需额外微调

## 摘要（原文）

> Large language models (LLM) have achieved remarkable performance across a wide range of tasks. However, their substantial parameter sizes pose significant challenges for deployment on edge devices with limited computational and memory resources. Low-rank compression is a promising approach to address this issue, as it reduces both computational and memory costs, making LLM more suitable for resource-constrained environments. Nonetheless, naïve low-rank compression methods require a significant reduction in the retained rank to achieve meaningful memory and computation savings. For a low-rank model, the ranks need to be reduced by more than half to yield efficiency gains. Such aggressive truncation, however, typically results in substantial performance degradation. To address this trade-off, we propose SkipCat, a novel low-rank compression framework that enables the use of higher ranks while achieving the same compression rates. First, we introduce an intra-layer shared low-rank projection method, where multiple matrices that share the same input use a common projection. This reduces redundancy and improves compression efficiency. Second, we propose a block skipping technique that omits computations and memory transfers for selected sub-blocks within the low-rank decomposition. These two techniques jointly enable our compressed model to retain more effective ranks under the same compression budget. Experimental results show that, without any additional fine-tuning, our method outperforms previous low-rank compression approaches by 7% accuracy improvement on zero-shot tasks under the same compression rate. These results highlight the effectiveness of our rank-maximized compression strategy in preserving model performance under tight resource constraints.

