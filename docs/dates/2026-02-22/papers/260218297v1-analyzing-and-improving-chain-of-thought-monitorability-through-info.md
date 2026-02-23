---
layout: default
title: Analyzing and Improving Chain-of-Thought Monitorability Through Information Theory
---

# Analyzing and Improving Chain-of-Thought Monitorability Through Information Theory
**arXiv**：[2602.18297v1](https://arxiv.org/abs/2602.18297) · [PDF](https://arxiv.org/pdf/2602.18297.pdf)  
**作者**：Usman Anwar, Tim Bakker, Dana Kianfar, Cristina Pinneri, Christos Louizos  

**一句话要点**：提出信息论分析与训练方法以改进链式思维监控性能

**关键词**：链式思维监控, 信息论分析, 训练优化, 监控准确性, 互信息

## 3 点简述
- 核心问题：链式思维监控中互信息非零是必要非充分条件，存在信息差距和激发误差
- 方法要点：基于信息论分析，提出两种训练方法优化监控准确性
- 实验或效果：在多种环境中显著提升监控准确性，防止链式思维退化

## 摘要（原文）

> Chain-of-thought (CoT) monitors are LLM-based systems that analyze reasoning traces to detect when outputs may exhibit attributes of interest, such as test-hacking behavior during code generation. In this paper, we use information-theoretic analysis to show that non-zero mutual information between CoT and output is a necessary but not sufficient condition for CoT monitorability. We identify two sources of approximation error that may undermine the performance of CoT monitors in practice: information gap, which measures the extent to which the monitor can extract the information available in CoT, and elicitation error, which measures the extent to which the monitor approximates the optimal monitoring function. We further demonstrate that CoT monitorability can be systematically improved through targeted training objectives. To this end, we propose two complementary approaches: (a) an oracle-based method that directly rewards the monitored model for producing CoTs that maximize monitor accuracy, and (b) a more practical, label-free approach that maximizes conditional mutual information between outputs and CoTs. Across multiple different environments, we show both methods significantly improve monitor accuracy while preventing CoT degeneration even when training against a monitor, thereby mitigating reward hacking when the task reward is imperfectly specified.

