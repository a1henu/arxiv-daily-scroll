---
layout: default
title: AMEM4Rec: Leveraging Cross-User Similarity for Memory Evolution in Agentic LLM Recommenders
---

# AMEM4Rec: Leveraging Cross-User Similarity for Memory Evolution in Agentic LLM Recommenders
**arXiv**：[2602.08837v1](https://arxiv.org/abs/2602.08837) · [PDF](https://arxiv.org/pdf/2602.08837.pdf)  
**作者**：Minh-Duc Nguyen, Hai-Dang Kieu, Dung D. Le  

**一句话要点**：提出AMEM4Rec，通过跨用户记忆演化实现端到端协同过滤，以增强基于LLM的推荐系统。

**关键词**：LLM推荐系统, 协同过滤, 记忆演化, 跨用户相似性, 端到端学习

## 3 点简述
- 问题：现有基于LLM的推荐系统忽视协同过滤信号，且微调效率低、提示方法受限。
- 方法：利用全局记忆池存储用户行为模式，通过跨用户相似性迭代演化记忆以学习协同信号。
- 效果：在Amazon和MIND数据集上优于现有LLM推荐器，验证了记忆演化协同过滤的有效性。

## 摘要（原文）

> Agentic systems powered by Large Language Models (LLMs) have shown strong potential in recommender systems but remain hindered by several challenges. Fine-tuning LLMs is parameter-inefficient, and prompt-based agentic reasoning is limited by context length and hallucination risk. Moreover, existing agentic recommendation systems predominantly leverages semantic knowledge while neglecting the collaborative filtering (CF) signals essential for implicit preference modeling. To address these limitations, we propose AMEM4Rec, an agentic LLM-based recommender that learns collaborative signals in an end-to-end manner through cross-user memory evolution. AMEM4Rec stores abstract user behavior patterns from user histories in a global memory pool. Within this pool, memories are linked to similar existing ones and iteratively evolved to reinforce shared cross-user patterns, enabling the system to become aware of CF signals without relying on a pre-trained CF model. Extensive experiments on Amazon and MIND datasets show that AMEM4Rec consistently outperforms state-of-the-art LLM-based recommenders, demonstrating the effectiveness of evolving memory-guided collaborative filtering.

