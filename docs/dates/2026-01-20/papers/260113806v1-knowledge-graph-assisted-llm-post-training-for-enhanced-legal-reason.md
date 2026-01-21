---
layout: default
title: Knowledge Graph-Assisted LLM Post-Training for Enhanced Legal Reasoning
---

# Knowledge Graph-Assisted LLM Post-Training for Enhanced Legal Reasoning
**arXiv**：[2601.13806v1](https://arxiv.org/abs/2601.13806) · [PDF](https://arxiv.org/pdf/2601.13806.pdf)  
**作者**：Dezhao Song, Guglielmo Bonifazi, Frank Schilder, Jonathan Richard Schwarz  

**一句话要点**：提出知识图谱辅助LLM后训练方法，以增强法律推理能力

**关键词**：知识图谱, LLM后训练, 法律推理, IRAC框架, 直接偏好优化

## 3 点简述
- 问题：LLM后训练缺乏领域知识结构，导致复杂推理任务表现不佳
- 方法：基于IRAC框架构建知识图谱，生成训练数据并进行SFT和DPO
- 效果：在多个法律基准测试中优于基线，70B DPO模型在推理任务上表现最佳

## 摘要（原文）

> LLM post-training has primarily relied on large text corpora and human feedback, without capturing the structure of domain knowledge. This has caused models to struggle dealing with complex reasoning tasks, especially for high-stakes professional domains. In Law, reasoning requires deep understanding of the relations between various legal concepts, a key component missing in current LLM post-training. In this paper, we propose a knowledge graph (KG)-assisted approach for enhancing LLMs' reasoning capability in Legal that is generalizable to other high-stakes domains. We model key legal concepts by following the \textbf{IRAC} (Issue, Rule, Analysis and Conclusion) framework, and construct a KG with 12K legal cases. We then produce training data using our IRAC KG, and conduct both Supervised Fine-Tuning (SFT) and Direct Preference Optimization (DPO) with three state-of-the-art (SOTA) LLMs (30B, 49B and 70B), varying architecture and base model family. Our post-trained models obtained better average performance on 4/5 diverse legal benchmarks (14 tasks) than baselines. In particular, our 70B DPO model achieved the best score on 4/6 reasoning tasks, among baselines and a 141B SOTA legal LLM, demonstrating the effectiveness of our KG for enhancing LLMs' legal reasoning capability.

