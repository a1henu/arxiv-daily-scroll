---
layout: default
title: Surgery: Mitigating Harmful Fine-Tuning for Large Language Models via Attention Sink
---

# Surgery: Mitigating Harmful Fine-Tuning for Large Language Models via Attention Sink
**arXiv**：[2602.05228v1](https://arxiv.org/abs/2602.05228) · [PDF](https://arxiv.org/pdf/2602.05228.pdf)  
**作者**：Guozhi Liu, Weiwei Lin, Tiansheng Huang, Ruichao Mo, Qi Mu, Xiumin Wang, Li Shen  

**一句话要点**：提出Surgery方法，利用注意力汇机制缓解大语言模型有害微调的安全风险。

**关键词**：大语言模型安全, 有害微调防御, 注意力汇机制, 汇散度, 正则化方法, 安全对齐

## 3 点简述
- 有害微调会破坏大语言模型的安全对齐，导致显著安全风险。
- 基于注意力汇机制，提出可分离汇散度假设，并设计Surgery正则化抑制有害模式学习。
- 实验在BeaverTails等基准上提升防御性能5.90%至11.25%。

## 摘要（原文）

> Harmful fine-tuning can invalidate safety alignment of large language models, exposing significant safety risks. In this paper, we utilize the attention sink mechanism to mitigate harmful fine-tuning. Specifically, we first measure a statistic named \emph{sink divergence} for each attention head and observe that \emph{different attention heads exhibit two different signs of sink divergence}. To understand its safety implications, we conduct experiments and find that the number of attention heads of positive sink divergence increases along with the increase of the model's harmfulness when undergoing harmful fine-tuning. Based on this finding, we propose a separable sink divergence hypothesis -- \emph{attention heads associating with learning harmful patterns during fine-tuning are separable by their sign of sink divergence}. Based on the hypothesis, we propose a fine-tuning-stage defense, dubbed Surgery. Surgery utilizes a regularizer for sink divergence suppression, which steers attention heads toward the negative sink divergence group, thereby reducing the model's tendency to learn and amplify harmful patterns. Extensive experiments demonstrate that Surgery improves defense performance by 5.90\%, 11.25\%, and 9.55\% on the BeaverTails, HarmBench, and SorryBench benchmarks, respectively. Source code is available on https://github.com/Lslland/Surgery.

