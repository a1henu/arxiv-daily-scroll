---
layout: default
title: Boule or Baguette? A Study on Task Topology, Length Generalization, and the Benefit of Reasoning Traces
---

# Boule or Baguette? A Study on Task Topology, Length Generalization, and the Benefit of Reasoning Traces
**arXiv**：[2602.14404v1](https://arxiv.org/abs/2602.14404) · [PDF](https://arxiv.org/pdf/2602.14404.pdf)  
**作者**：William L. Tong, Ege Cakar, Cengiz Pehlevan  

**一句话要点**：提出PITA数据集与任务拓扑理论，揭示推理轨迹模型在长度泛化中的优势与局限

**关键词**：推理轨迹模型, 长度泛化, 任务拓扑, 命题逻辑, PITA数据集, 深度与广度分析

## 3 点简述
- 研究推理轨迹模型在长度泛化中的表现，聚焦任务深度与广度的影响
- 引入PITA大规模命题逻辑数据集，包含超过2300万语句及其证明
- 实验表明推理轨迹模型在广而浅任务中泛化良好，在窄而深任务中相对退化

## 摘要（原文）

> Recent years have witnessed meteoric progress in reasoning models: neural networks that generate intermediate reasoning traces (RTs) before producing a final output. Despite the rapid advancement, our understanding of how RTs support reasoning, and the limits of this paradigm, remain incomplete. To promote greater clarity, we introduce PITA: a novel large-scale dataset of over 23 million statements in propositional logic and their corresponding proofs. As a benchmark for robust reasoning, we focus on length generalization: if a model is trained to determine truth or falsity on statements with proofs up to fixed length, how well does it generalize to statements requiring longer proofs? We propose notions of (1) task depth and (2) task breadth, which measure respectively (1) the number of steps required to solve an example from a task and (2) the number of unique examples across a task. We vary these quantities across subsets of PITA, and find that RT models generalize well on broad and shallow subsets, while deteriorating on narrow and deep subsets relative to non-RT baselines. To determine whether our results are idiosyncratic to PITA or indicative of general phenomena, we compare our results to a simple synthetic task based on syllogisms. Our resulting theory suggests fundamental scalings that limit how well RT models perform on deep tasks, and highlights their generalization strengths on broad tasks. Our findings overall identify fundamental benefits and limitations inherent in using reasoning traces.

