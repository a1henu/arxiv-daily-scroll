---
layout: default
title: How2Everything: Mining the Web for How-To Procedures to Evaluate and Improve LLMs
---

# How2Everything: Mining the Web for How-To Procedures to Evaluate and Improve LLMs
**arXiv**：[2602.08808v1](https://arxiv.org/abs/2602.08808) · [PDF](https://arxiv.org/pdf/2602.08808.pdf)  
**作者**：Yapei Chang, Kyle Lo, Mohit Iyyer, Luca Soldaini  

**一句话要点**：提出How2Everything框架，通过挖掘网络过程数据评估和改进LLM过程生成能力

**关键词**：过程生成评估, 网络数据挖掘, 强化学习优化, LLM评判协议, 蒸馏训练

## 3 点简述
- 核心问题：LLM生成真实世界任务的过程有效性评估与改进缺乏大规模方法
- 方法要点：从网络挖掘35.1万过程构建评估集，开发基于LLM评判的评分协议
- 实验或效果：RL使用评分作为奖励提升性能超10点，蒸馏模型与人类标注一致性达80.5%

## 摘要（原文）

> Generating step-by-step "how-to" procedures is a key LLM capability: how-to advice is commonly requested in chatbots, and step-by-step planning is critical for reasoning over complex tasks. Yet, measuring and improving procedural validity at scale on real-world tasks remains challenging and understudied. To address this, we introduce How2Everything, a scalable framework to evaluate and improve goal-conditioned procedure generation. Our framework includes How2Mine, which mines 351K procedures from 980K web pages across 14 topics and readily scales to larger corpora. From this pool we build How2Bench, a 7K-example evaluation set balanced across topics. To reliably score model outputs, we develop How2Score, an evaluation protocol that uses an LLM judge to detect whether a generation contains any critical failure that would prevent achieving the goal. For low-cost, reproducible evaluation, we distill a frontier model into an open 8B model, achieving 80.5% agreement with human annotators. How2Bench reveals clear scaling trends across model sizes and training stages, providing signal early in pretraining. Finally, RL using How2Score as a reward improves performance on How2Bench by >10 points across three models without systematic regressions on standard benchmarks, with gains robust to superficial source-document memorization or format compliance. Taken together, How2Everything shows how pretraining web data can support a closed loop of capability evaluation and improvement at scale.

