---
layout: default
title: Autoregressive Ranking: Bridging the Gap Between Dual and Cross Encoders
---

# Autoregressive Ranking: Bridging the Gap Between Dual and Cross Encoders
**arXiv**：[2601.05588v1](https://arxiv.org/abs/2601.05588) · [PDF](https://arxiv.org/pdf/2601.05588.pdf)  
**作者**：Benjamin Rozonoyer, Chong You, Michael Boratko, Himanshu Jain, Nilesh Gupta, Srinadh Bhojanapalli, Andrew McCallum, Felix Yu  

**一句话要点**：提出SToICaL损失函数以增强点式生成排序的排名感知能力

**关键词**：信息检索, 点式生成排序, 排名感知损失, LLM应用, 自回归模型

## 3 点简述
- 核心问题：LLM基于点式生成排序时，传统损失函数缺乏排名感知能力
- 方法要点：设计SToICaL损失，在项目和令牌级别融入排名监督
- 实验或效果：在WordNet和ESCI任务上提升排名指标，抑制无效docID生成

## 摘要（原文）

> Dual and cross encoders have long been mainstays of information retrieval (IR), but are being challenged by the emergent capabilities of LLMs. An LLM-based approach we term pointwise generative ranking - generating tokens the length of a single docID as opposed to a list in order to enable ranking via beam search - combines efficiency and expressivity benefits while leveraging the in-context capabilities of Causal Transformers. Although there is ample evidence to suggest that pretrained LLMs are well-suited for ranking, we find that the vast majority of LLM-based approaches rely on next-token prediction, a loss function which is fundamentally rank-agnostic (and especially so with pointwise supervision). In this paper, we first prove that the expressivity of pointwise generative ranking with multi-token docIDs is superior to that of dual encoders. We then propose SToICaL - a Simple Token-Item Calibrated Loss - which can incorporate rank-aware supervision at both the item and token levels within the pointwise setup. We run a suite of experiments on ranking tasks derived from WordNet (Fellbaum, 1998) and ESCI (Reddy et al., arXiv:2206.06588). Two variants of SToICaL successfully suppress the probability of invalid docID generations and improve on common ranking metrics beyond top-1 retrieval.

