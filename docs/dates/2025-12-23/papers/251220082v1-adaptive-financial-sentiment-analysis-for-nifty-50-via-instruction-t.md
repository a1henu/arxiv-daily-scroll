---
layout: default
title: Adaptive Financial Sentiment Analysis for NIFTY 50 via Instruction-Tuned LLMs , RAG and Reinforcement Learning Approaches
---

# Adaptive Financial Sentiment Analysis for NIFTY 50 via Instruction-Tuned LLMs , RAG and Reinforcement Learning Approaches
**arXiv**：[2512.20082v1](https://arxiv.org/abs/2512.20082) · [PDF](https://arxiv.org/pdf/2512.20082.pdf)  
**作者**：Chaithra, Kamesh Kadimisetty, Biju R Mohan  

**一句话要点**：提出自适应金融情感分析框架，结合指令调优LLM、RAG和强化学习，以提升印度股市NIFTY 50的情感分类性能。

**关键词**：金融情感分析, 指令调优大语言模型, 检索增强生成, 强化学习, 市场反馈适应, NIFTY 50

## 3 点简述
- 核心问题：现有金融情感分析未考虑股价或市场反馈对情感分析的影响。
- 方法要点：基于LLaMA 3.2 3B模型，通过指令调优、RAG动态检索多源上下文，并引入反馈驱动模块和PPO强化学习优化源权重。
- 实验或效果：在2024-2025年NIFTY 50新闻数据上，系统显著提升分类准确率、F1分数和市场对齐度。

## 摘要（原文）

> Financial sentiment analysis plays a crucial role in informing investment decisions, assessing market risk, and predicting stock price trends. Existing works in financial sentiment analysis have not considered the impact of stock prices or market feedback on sentiment analysis. In this paper, we propose an adaptive framework that integrates large language models (LLMs) with real-world stock market feedback to improve sentiment classification in the context of the Indian stock market. The proposed methodology fine-tunes the LLaMA 3.2 3B model using instruction-based learning on the SentiFin dataset. To enhance sentiment predictions, a retrieval-augmented generation (RAG) pipeline is employed that dynamically selects multi-source contextual information based on the cosine similarity of the sentence embeddings. Furthermore, a feedback-driven module is introduced that adjusts the reliability of the source by comparing predicted sentiment with actual next-day stock returns, allowing the system to iteratively adapt to market behavior. To generalize this adaptive mechanism across temporal data, a reinforcement learning agent trained using proximal policy optimization (PPO) is incorporated. The PPO agent learns to optimize source weighting policies based on cumulative reward signals from sentiment-return alignment. Experimental results on NIFTY 50 news headlines collected from 2024 to 2025 demonstrate that the proposed system significantly improves classification accuracy, F1-score, and market alignment over baseline models and static retrieval methods. The results validate the potential of combining instruction-tuned LLMs with dynamic feedback and reinforcement learning for robust, market-aware financial sentiment modeling.

