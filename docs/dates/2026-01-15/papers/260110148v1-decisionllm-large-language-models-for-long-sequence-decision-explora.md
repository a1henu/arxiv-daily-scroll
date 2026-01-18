---
layout: default
title: DecisionLLM: Large Language Models for Long Sequence Decision Exploration
---

# DecisionLLM: Large Language Models for Long Sequence Decision Exploration
**arXiv**：[2601.10148v1](https://arxiv.org/abs/2601.10148) · [PDF](https://arxiv.org/pdf/2601.10148.pdf)  
**作者**：Xiaowei Lv, Zhilin Zhang, Yijun Li, Yusen Huo, Siyuan Ju, Xuyan Li, Chunxiang Hong, Tianyu Wang, Yongcai Wang, Peng Sun, Chuan Yu, Jian Xu, Bo Zheng  

**一句话要点**：提出DecisionLLM，将轨迹作为模态对齐语言，以解决LLMs在长序列离线决策中处理连续值的挑战。

**关键词**：长序列决策, 离线强化学习, 轨迹模态对齐, 大语言模型应用, 缩放定律, 实时竞价

## 3 点简述
- 核心问题：LLMs无法原生理解连续数值，阻碍其在长序列决策任务中的应用。
- 方法要点：将轨迹数据视为独立模态，通过对齐自然语言描述实现自回归决策预测。
- 实验或效果：在离线基准和竞价场景中，DecisionLLM-3B优于传统Decision Transformer，并建立了缩放定律。

## 摘要（原文）

> Long-sequence decision-making, which is usually addressed through reinforcement learning (RL), is a critical component for optimizing strategic operations in dynamic environments, such as real-time bidding in computational advertising. The Decision Transformer (DT) introduced a powerful paradigm by framing RL as an autoregressive sequence modeling problem. Concurrently, Large Language Models (LLMs) have demonstrated remarkable success in complex reasoning and planning tasks. This inspires us whether LLMs, which share the same Transformer foundation, but operate at a much larger scale, can unlock new levels of performance in long-horizon sequential decision-making problem. This work investigates the application of LLMs to offline decision making tasks. A fundamental challenge in this domain is the LLMs' inherent inability to interpret continuous values, as they lack a native understanding of numerical magnitude and order when values are represented as text strings. To address this, we propose treating trajectories as a distinct modality. By learning to align trajectory data with natural language task descriptions, our model can autoregressively predict future decisions within a cohesive framework we term DecisionLLM. We establish a set of scaling laws governing this paradigm, demonstrating that performance hinges on three factors: model scale, data volume, and data quality. In offline experimental benchmarks and bidding scenarios, DecisionLLM achieves strong performance. Specifically, DecisionLLM-3B outperforms the traditional Decision Transformer (DT) by 69.4 on Maze2D umaze-v1 and by 0.085 on AuctionNet. It extends the AIGB paradigm and points to promising directions for future exploration in online bidding.

