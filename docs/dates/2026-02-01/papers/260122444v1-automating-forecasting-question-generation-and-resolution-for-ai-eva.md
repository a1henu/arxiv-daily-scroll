---
layout: default
title: Automating Forecasting Question Generation and Resolution for AI Evaluation
---

# Automating Forecasting Question Generation and Resolution for AI Evaluation
**arXiv**：[2601.22444v1](https://arxiv.org/abs/2601.22444) · [PDF](https://arxiv.org/pdf/2601.22444.pdf)  
**作者**：Nikos I. Bosse, Peter Mühlbacher, Jack Wildman, Lawrence Phillips, Dan Schwarz  

**一句话要点**：提出基于LLM网络研究代理的自动化系统，用于大规模生成和解决高质量预测问题以评估AI。

**关键词**：预测问题生成, AI评估, LLM代理, 自动化系统, Brier分数

## 3 点简述
- 核心问题：自动化生成和解决多样化预测问题，以评估AI预测能力，克服传统依赖重复数据源的局限性。
- 方法要点：利用LLM驱动的网络研究代理自动生成和解决预测问题，提高问题多样性和准确性。
- 实验或效果：生成1499个问题，验证问题可验证性约96%，解决准确率约95%，并展示LLM性能差异和策略改进效果。

## 摘要（原文）

> Forecasting future events is highly valuable in decision-making and is a robust measure of general intelligence. As forecasting is probabilistic, developing and evaluating AI forecasters requires generating large numbers of diverse and difficult questions, and accurately resolving them. Previous efforts to automate this laborious work relied on recurring data sources (e.g., weather, stocks), limiting diversity and utility. In this work, we present a system for generating and resolving high-quality forecasting questions automatically and at scale using LLM-powered web research agents. We use this system to generate 1499 diverse, real-world forecasting questions, and to resolve them several months later. We estimate that our system produces verifiable, unambiguous questions approximately 96% of the time, exceeding the rate of Metaculus, a leading human-curated forecasting platform. We also find that our system resolves questions at approximately 95% accuracy. We verify that forecasting agents powered by more intelligent LLMs perform better on these questions (Brier score of 0.134 for Gemini 3 Pro, 0.149 for GPT-5, and 0.179 for Gemini 2.5 Flash). Finally, we demonstrate how our system can be leveraged to directly improve forecasting, by evaluating a question decomposition strategy on a generated question set, yielding a significant improvement in Brier scores (0.132 vs. 0.141).

