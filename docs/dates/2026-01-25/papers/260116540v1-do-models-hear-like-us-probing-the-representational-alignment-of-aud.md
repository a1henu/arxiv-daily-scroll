---
layout: default
title: Do Models Hear Like Us? Probing the Representational Alignment of Audio LLMs and Naturalistic EEG
---

# Do Models Hear Like Us? Probing the Representational Alignment of Audio LLMs and Naturalistic EEG
**arXiv**：[2601.16540v1](https://arxiv.org/abs/2601.16540) · [PDF](https://arxiv.org/pdf/2601.16540.pdf)  
**作者**：Haoyun Yang, Xin Xiao, Jiang Zhong, Yu Tian, Dong Xiaohua, Yu Mao, Hao Wu, Kaiwen Wei  

**一句话要点**：探究12个开源音频大语言模型与自然脑电信号在句子层面的表征对齐模式

**关键词**：音频大语言模型, 表征对齐, 脑电信号, 自然听音, 相似度分析, 神经动态

## 3 点简述
- 核心问题：音频大语言模型内部表征是否与人类自然听音时的神经动态对齐
- 方法要点：使用8种相似度指标（如基于Spearman的RSA）分析模型层间与脑电信号的表征几何
- 实验或效果：发现排名依赖分裂、时空对齐模式（如N400相关窗口）和情感解离现象

## 摘要（原文）

> Audio Large Language Models (Audio LLMs) have demonstrated strong capabilities in integrating speech perception with language understanding. However, whether their internal representations align with human neural dynamics during naturalistic listening remains largely unexplored. In this work, we systematically examine layer-wise representational alignment between 12 open-source Audio LLMs and Electroencephalogram (EEG) signals across 2 datasets. Specifically, we employ 8 similarity metrics, such as Spearman-based Representational Similarity Analysis (RSA), to characterize within-sentence representational geometry. Our analysis reveals 3 key findings: (1) we observe a rank-dependence split, in which model rankings vary substantially across different similarity metrics; (2) we identify spatio-temporal alignment patterns characterized by depth-dependent alignment peaks and a pronounced increase in RSA within the 250-500 ms time window, consistent with N400-related neural dynamics; (3) we find an affective dissociation whereby negative prosody, identified using a proposed Tri-modal Neighborhood Consistency (TNC) criterion, reduces geometric similarity while enhancing covariance-based dependence. These findings provide new neurobiological insights into the representational mechanisms of Audio LLMs.

