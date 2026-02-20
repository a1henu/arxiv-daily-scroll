---
layout: default
title: KLong: Training LLM Agent for Extremely Long-horizon Tasks
---

# KLong: Training LLM Agent for Extremely Long-horizon Tasks
**arXiv**：[2602.17547v1](https://arxiv.org/abs/2602.17547) · [PDF](https://arxiv.org/pdf/2602.17547.pdf)  
**作者**：Yue Liu, Zhiyuan Hu, Flood Sung, Jiaheng Zhang, Bryan Hooi  

**一句话要点**：提出KLong LLM代理，通过轨迹分割SFT和渐进式RL训练解决极长视野任务。

**关键词**：长视野任务, 轨迹分割SFT, 渐进式强化学习, LLM代理训练, 自动化数据生成, 研究论文分析

## 3 点简述
- 核心问题：训练LLM代理处理极长视野任务，如研究论文分析，面临轨迹过长和训练效率挑战。
- 方法要点：采用轨迹分割SFT激活基础能力，结合Research-Factory自动生成高质量数据，并通过渐进式RL分阶段扩展训练超时。
- 实验或效果：KLong在PaperBench上超越Kimi K2 Thinking 11.28%，并在SWE-bench Verified和MLE-bench等编码基准上展现泛化性能。

## 摘要（原文）

> This paper introduces KLong, an open-source LLM agent trained to solve extremely long-horizon tasks. The principle is to first cold-start the model via trajectory-splitting SFT, then scale it via progressive RL training. Specifically, we first activate basic agentic abilities of a base model with a comprehensive SFT recipe. Then, we introduce Research-Factory, an automated pipeline that generates high-quality training data by collecting research papers and constructing evaluation rubrics. Using this pipeline, we build thousands of long-horizon trajectories distilled from Claude 4.5 Sonnet (Thinking). To train with these extremely long trajectories, we propose a new trajectory-splitting SFT, which preserves early context, progressively truncates later context, and maintains overlap between sub-trajectories. In addition, to further improve long-horizon task-solving capability, we propose a novel progressive RL, which schedules training into multiple stages with progressively extended timeouts. Experiments demonstrate the superiority and generalization of KLong, as shown in Figure 1. Notably, our proposed KLong (106B) surpasses Kimi K2 Thinking (1T) by 11.28% on PaperBench, and the performance improvement generalizes to other coding benchmarks like SWE-bench Verified and MLE-bench.

