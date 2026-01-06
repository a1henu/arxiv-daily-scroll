---
layout: default
title: Exploring Approaches for Detecting Memorization of Recommender System Data in Large Language Models
---

# Exploring Approaches for Detecting Memorization of Recommender System Data in Large Language Models
**arXiv**：[2601.02002v1](https://arxiv.org/abs/2601.02002) · [PDF](https://arxiv.org/pdf/2601.02002.pdf)  
**作者**：Antonio Colacicco, Vito Guida, Dario Di Palma, Fedelucio Narducci, Tommaso Di Noia  

**一句话要点**：评估三种方法以检测大型语言模型在推荐系统中的数据记忆问题

**关键词**：数据记忆检测, 推荐系统, 大型语言模型, 自动提示工程, 无监督学习

## 3 点简述
- 核心问题：LLMs在推荐场景中可能记忆训练数据，引发数据泄露担忧，需自动化检测方法。
- 方法要点：比较越狱提示工程、无监督潜在知识发现（CCS和Cluster-Norm）和自动提示工程（APE）。
- 实验效果：APE在提取记忆项信息上表现最佳，但数值数据恢复仍具挑战；CCS可区分真假电影标题。

## 摘要（原文）

> Large Language Models (LLMs) are increasingly applied in recommendation scenarios due to their strong natural language understanding and generation capabilities. However, they are trained on vast corpora whose contents are not publicly disclosed, raising concerns about data leakage. Recent work has shown that the MovieLens-1M dataset is memorized by both the LLaMA and OpenAI model families, but the extraction of such memorized data has so far relied exclusively on manual prompt engineering. In this paper, we pose three main questions: Is it possible to enhance manual prompting? Can LLM memorization be detected through methods beyond manual prompting? And can the detection of data leakage be automated? To address these questions, we evaluate three approaches: (i) jailbreak prompt engineering; (ii) unsupervised latent knowledge discovery, probing internal activations via Contrast-Consistent Search (CCS) and Cluster-Norm; and (iii) Automatic Prompt Engineering (APE), which frames prompt discovery as a meta-learning process that iteratively refines candidate instructions. Experiments on MovieLens-1M using LLaMA models show that jailbreak prompting does not improve the retrieval of memorized items and remains inconsistent; CCS reliably distinguishes genuine from fabricated movie titles but fails on numerical user and rating data; and APE retrieves item-level information with moderate success yet struggles to recover numerical interactions. These findings suggest that automatically optimizing prompts is the most promising strategy for extracting memorized samples.

