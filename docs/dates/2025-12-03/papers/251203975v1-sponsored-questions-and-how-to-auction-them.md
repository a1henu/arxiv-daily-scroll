---
layout: default
title: Sponsored Questions and How to Auction Them
---

# Sponsored Questions and How to Auction Them
**arXiv**：[2512.03975v1](https://arxiv.org/abs/2512.03975) · [PDF](https://arxiv.org/pdf/2512.03975.pdf)  
**作者**：Kshipra Bhawalkar, Alexandros Psomas, Di Wang  

**一句话要点**：提出基于VCG机制的联合优化模型，以解决LLM交互中赞助建议与广告拍卖的分配问题。

**关键词**：赞助建议, 广告拍卖, VCG机制, 战略无效率, 联合优化, LLM交互

## 3 点简述
- 核心问题：LLM交互中赞助建议的分配与传统广告拍卖的交互机制设计。
- 方法要点：采用VCG机制联合优化赞助建议和后续广告，实现高效和真实。
- 实验或效果：证明模块化方法存在战略无效率，其无政府价格无界。

## 摘要（原文）

> Online platforms connect users with relevant products and services using ads. A key challenge is that a user's search query often leaves their true intent ambiguous. Typically, platforms passively predict relevance based on available signals and in some cases offer query refinements. The shift from traditional search to conversational AI provides a new approach. When a user's query is ambiguous, a Large Language Model (LLM) can proactively offer several clarifying follow-up prompts. In this paper we consider the following: what if some of these follow-up prompts can be ``sponsored,'' i.e., selected for their advertising potential. How should these ``suggestion slots'' be allocated? And, how does this new mechanism interact with the traditional ad auction that might follow?
>   This paper introduces a formal model for designing and analyzing these interactive platforms. We use this model to investigate a critical engineering choice: whether it is better to build an end-to-end pipeline that jointly optimizes the user interaction and the final ad auction, or to decouple them into separate mechanisms for the suggestion slots and another for the subsequent ad slot. We show that the VCG mechanism can be adopted to jointly optimize the sponsored suggestion and the ads that follow; while this mechanism is more complex, it achieves outcomes that are efficient and truthful. On the other hand, we prove that the simple-to-implement modular approach suffers from strategic inefficiency: its Price of Anarchy is unbounded.

