---
layout: default
title: GRAB: An LLM-Inspired Sequence-First Click-Through Rate Prediction Modeling Paradigm
---

# GRAB: An LLM-Inspired Sequence-First Click-Through Rate Prediction Modeling Paradigm
**arXiv**：[2602.01865v1](https://arxiv.org/abs/2602.01865) · [PDF](https://arxiv.org/pdf/2602.01865.pdf)  
**作者**：Shaopeng Chen, Chuyue Xie, Huimin Ren, Shaozong Zhang, Han Zhang, Ruobing Cheng, Zhiqiang Cao, Zehao Ju, Gao Yu, Jie Ding, Xiaodong Chen, Xuewu Jiao, Shuanglong Li, Liu Lin  

**一句话要点**：提出GRAB生成式框架，利用因果动作感知多通道注意力机制改进点击率预测中的长序列建模问题。

**关键词**：点击率预测, 长序列建模, 生成式框架, 注意力机制, 在线部署, 扩展行为

## 3 点简述
- 传统深度学习推荐模型在泛化和长序列建模方面面临性能瓶颈。
- 引入因果动作感知多通道注意力机制，有效捕捉用户行为序列的时序动态和动作信号。
- 在线部署显示，GRAB显著提升收入和点击率，并展示随序列长度增长的线性扩展能力。

## 摘要（原文）

> Traditional Deep Learning Recommendation Models (DLRMs) face increasing bottlenecks in performance and efficiency, often struggling with generalization and long-sequence modeling. Inspired by the scaling success of Large Language Models (LLMs), we propose Generative Ranking for Ads at Baidu (GRAB), an end-to-end generative framework for Click-Through Rate (CTR) prediction. GRAB integrates a novel Causal Action-aware Multi-channel Attention (CamA) mechanism to effectively capture temporal dynamics and specific action signals within user behavior sequences. Full-scale online deployment demonstrates that GRAB significantly outperforms established DLRMs, delivering a 3.05% increase in revenue and a 3.49% rise in CTR. Furthermore, the model demonstrates desirable scaling behavior: its expressive power shows a monotonic and approximately linear improvement as longer interaction sequences are utilized.

