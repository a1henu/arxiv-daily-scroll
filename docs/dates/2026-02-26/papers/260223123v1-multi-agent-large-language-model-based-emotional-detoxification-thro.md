---
layout: default
title: Multi-Agent Large Language Model Based Emotional Detoxification Through Personalized Intensity Control for Consumer Protection
---

# Multi-Agent Large Language Model Based Emotional Detoxification Through Personalized Intensity Control for Consumer Protection
**arXiv**：[2602.23123v1](https://arxiv.org/abs/2602.23123) · [PDF](https://arxiv.org/pdf/2602.23123.pdf)  
**作者**：Keito Inoshita  

**一句话要点**：提出多智能体LLM情感去毒系统MALLET，通过个性化强度控制保护消费者免受过度情绪刺激。

**关键词**：情感去毒, 多智能体系统, 个性化控制, 消费者保护, 语义保持, 情绪分析

## 3 点简述
- 核心问题：注意力经济中煽情内容导致消费者情绪过载，影响冷静决策。
- 方法要点：基于四智能体系统分析、调整情绪，提供平衡或冷却模式文本。
- 实验或效果：在AG News数据集上实现刺激分数显著降低，语义保持独立可控。

## 摘要（原文）

> In the attention economy, sensational content exposes consumers to excessive emotional stimulation, hindering calm decision-making. This study proposes Multi-Agent LLM-based Emotional deToxification (MALLET), a multi-agent information sanitization system consisting of four agents: Emotion Analysis, Emotion Adjustment, Balance Monitoring, and Personal Guide. The Emotion Analysis Agent quantifies stimulus intensity using a 6-emotion BERT classifier, and the Emotion Adjustment Agent rewrites texts into two presentation modes, BALANCED (neutralized text) and COOL (neutralized text + supplementary text), using an LLM. The Balance Monitoring Agent aggregates weekly information consumption patterns and generates personalized advice, while the Personal Guide Agent recommends a presentation mode according to consumer sensitivity. Experiments on 800 AG News articles demonstrated significant stimulus score reduction (up to 19.3%) and improved emotion balance while maintaining semantic preservation. Near-zero correlation between stimulus reduction and semantic preservation confirmed that the two are independently controllable. Category-level analysis revealed substantial reduction (17.8-33.8%) in Sports, Business, and Sci/Tech, whereas the effect was limited in the World category, where facts themselves are inherently high-stimulus. The proposed system provides a framework for supporting calm information reception of consumers without restricting access to the original text.

