---
layout: default
title: Proof of Time: A Benchmark for Evaluating Scientific Idea Judgments
---

# Proof of Time: A Benchmark for Evaluating Scientific Idea Judgments
**arXiv**：[2601.07606v1](https://arxiv.org/abs/2601.07606) · [PDF](https://arxiv.org/pdf/2601.07606.pdf)  
**作者**：Bingyang Ye, Shan Chen, Jingxuan Tu, Chen Liu, Zidi Xiong, Samuel Schmidgall, Danielle S. Bitterman  

**一句话要点**：提出PoT基准框架以评估大语言模型对科学想法的判断质量

**关键词**：科学想法评估, 基准框架, 大语言模型, 代理研究, 时间分区验证, 离线沙箱

## 3 点简述
- 核心问题：缺乏可扩展方法评估大语言模型对科学想法的判断质量。
- 方法要点：引入半可验证基准框架，链接科学想法判断与下游可观测信号（如引用）。
- 实验或效果：在30,000+实例中，发现交互预算提升代理性能，工具使用效果依赖任务。

## 摘要（原文）

> Large language models are increasingly being used to assess and forecast research ideas, yet we lack scalable ways to evaluate the quality of models' judgments about these scientific ideas. Towards this goal, we introduce PoT, a semi-verifiable benchmarking framework that links scientific idea judgments to downstream signals that become observable later (e.g., citations and shifts in researchers' agendas). PoT freezes a pre-cutoff snapshot of evidence in an offline sandbox and asks models to forecast post-cutoff outcomes, enabling verifiable evaluation when ground truth arrives, scalable benchmarking without exhaustive expert annotation, and analysis of human-model misalignment against signals such as peer-review awards. In addition, PoT provides a controlled testbed for agent-based research judgments that evaluate scientific ideas, comparing tool-using agents to non-agent baselines under prompt ablations and budget scaling. Across 30,000+ instances spanning four benchmark domains, we find that, compared with non-agent baselines, higher interaction budgets generally improve agent performance, while the benefit of tool use is strongly task-dependent. By combining time-partitioned, future-verifiable targets with an offline sandbox for tool use, PoT supports scalable evaluation of agents on future-facing scientific idea judgment tasks.

