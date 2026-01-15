---
layout: default
title: Bridging Semantic Understanding and Popularity Bias with LLMs
---

# Bridging Semantic Understanding and Popularity Bias with LLMs
**arXiv**：[2601.09478v1](https://arxiv.org/abs/2601.09478) · [PDF](https://arxiv.org/pdf/2601.09478.pdf)  
**作者**：Renqiang Luo, Dong Zhang, Yupeng Gao, Wen Shi, Mingliang Hou, Jiaying Liu, Zhe Wang, Shuo Yu  

**一句话要点**：提出FairLRM框架，利用大语言模型增强推荐系统中流行度偏差的语义理解与公平性。

**关键词**：推荐系统, 流行度偏差, 大语言模型, 语义理解, 公平性, 去偏方法

## 3 点简述
- 核心问题：现有方法忽视流行度偏差的深层语义因果，导致去偏效果和推荐准确性受限。
- 方法要点：FairLRM分解偏差为物品侧和用户侧，通过结构化提示增强大语言模型对全局分布和个体偏好的理解。
- 实验或效果：实证评估显示FairLRM显著提升公平性和推荐准确性，提供更语义感知的解决方案。

## 摘要（原文）

> Semantic understanding of popularity bias is a crucial yet underexplored challenge in recommender systems, where popular items are often favored at the expense of niche content. Most existing debiasing methods treat the semantic understanding of popularity bias as a matter of diversity enhancement or long-tail coverage, neglecting the deeper semantic layer that embodies the causal origins of the bias itself. Consequently, such shallow interpretations limit both their debiasing effectiveness and recommendation accuracy. In this paper, we propose FairLRM, a novel framework that bridges the gap in the semantic understanding of popularity bias with Recommendation via Large Language Model (RecLLM). FairLRM decomposes popularity bias into item-side and user-side components, using structured instruction-based prompts to enhance the model's comprehension of both global item distributions and individual user preferences. Unlike traditional methods that rely on surface-level features such as "diversity" or "debiasing", FairLRM improves the model's ability to semantically interpret and address the underlying bias. Through empirical evaluation, we show that FairLRM significantly enhances both fairness and recommendation accuracy, providing a more semantically aware and trustworthy approach to enhance the semantic understanding of popularity bias. The implementation is available at https://github.com/LuoRenqiang/FairLRM.

