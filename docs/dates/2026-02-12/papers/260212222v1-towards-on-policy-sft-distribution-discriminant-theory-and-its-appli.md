---
layout: default
title: Towards On-Policy SFT: Distribution Discriminant Theory and its Applications in LLM Training
---

# Towards On-Policy SFT: Distribution Discriminant Theory and its Applications in LLM Training
**arXiv**：[2602.12222v1](https://arxiv.org/abs/2602.12222) · [PDF](https://arxiv.org/pdf/2602.12222.pdf)  
**作者**：Miaosen Zhang, Yishan Liu, Shuxia Lin, Xu Yang, Qi Dai, Chong Luo, Weihao Jiang, Peng Hou, Anxiang Zeng, Xin Geng, Baining Guo  

**一句话要点**：提出分布判别理论与On-Policy SFT框架，以提升监督微调在LLM训练中的泛化能力。

**关键词**：监督微调, 分布判别理论, On-Policy SFT, 大语言模型训练, 泛化能力提升

## 3 点简述
- 核心问题：监督微调（SFT）计算高效但泛化能力常弱于强化学习（RL），主要因RL使用在线策略数据。
- 方法要点：引入分布判别理论（DDT）量化数据与模型分布对齐，并开发In-Distribution Finetuning和Hinted Decoding技术。
- 实验或效果：框架在泛化性能上媲美DPO和SimPO等离线RL算法，同时保持SFT的高效性。

## 摘要（原文）

> Supervised fine-tuning (SFT) is computationally efficient but often yields inferior generalization compared to reinforcement learning (RL). This gap is primarily driven by RL's use of on-policy data. We propose a framework to bridge this chasm by enabling On-Policy SFT. We first present \textbf{\textit{Distribution Discriminant Theory (DDT)}}, which explains and quantifies the alignment between data and the model-induced distribution. Leveraging DDT, we introduce two complementary techniques: (i) \textbf{\textit{In-Distribution Finetuning (IDFT)}}, a loss-level method to enhance generalization ability of SFT, and (ii) \textbf{\textit{Hinted Decoding}}, a data-level technique that can re-align the training corpus to the model's distribution. Extensive experiments demonstrate that our framework achieves generalization performance on par with prominent offline RL algorithms, including DPO and SimPO, while maintaining the efficiency of an SFT pipeline. The proposed framework thus offers a practical alternative in domains where RL is infeasible. We open-source the code here: https://github.com/zhangmiaosen2000/Towards-On-Policy-SFT

