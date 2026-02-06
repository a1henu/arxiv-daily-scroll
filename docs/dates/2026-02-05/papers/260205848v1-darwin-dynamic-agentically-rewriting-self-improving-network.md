---
layout: default
title: DARWIN: Dynamic Agentically Rewriting Self-Improving Network
---

# DARWIN: Dynamic Agentically Rewriting Self-Improving Network
**arXiv**：[2602.05848v1](https://arxiv.org/abs/2602.05848) · [PDF](https://arxiv.org/pdf/2602.05848.pdf)  
**作者**：Henry Jiang  

**一句话要点**：提出DARWIN框架，通过遗传算法优化GPT代理以提升训练效率与性能。

**关键词**：进化式GPT训练, 遗传算法优化, 代码自动修改, 模型性能提升, 人工干预接口

## 3 点简述
- 核心问题：如何自动化改进GPT模型训练代码以提升性能与效率。
- 方法要点：使用遗传算法，多个GPT代理相互修改训练代码，结合持久记忆和人工干预接口。
- 实验或效果：在5次迭代中，模型FLOPS利用率提升1.26%，困惑度改善2.07%。

## 摘要（原文）

> DARWIN is an evolutionary GPT model, utilizing a genetic-algorithm like optimization structure with several independent GPT agents being trained individually using unique training code. Each iteration, the GPT models are prompted to modify the training code of one another in an attempt to improve their performance in a mutation-like manner, and the best GPT agents are then benchmarked and selected for the next iteration by genetic algorithm. For demonstration purposes and due to budget and time constraints, OpenAI API is used to prompt training code improvements and the nanoGPT framework is used as the training code. DARWIN also utilizes persistent JSON-based memory files to track previous reasoning and changes to code to correlate with improvement to model performance. and a bidirectional interface for HITL intervention allowing the model to request upgrades such as additional datasets, training scripts, and restructuring of file hierarchies. In experiments, DARWIN achieved a 1.26 percent improvement in model FLOPS utilization (MFU) and a 2.07 percent improvement to perplexity in 5 iterations of training over baseline configurations, demonstrating promising capabilities as a foundation for scaling evolutionary GPT training.

