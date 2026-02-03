---
layout: default
title: Live-Evo: Online Evolution of Agentic Memory from Continuous Feedback
---

# Live-Evo: Online Evolution of Agentic Memory from Continuous Feedback
**arXiv**：[2602.02369v1](https://arxiv.org/abs/2602.02369) · [PDF](https://arxiv.org/pdf/2602.02369.pdf)  
**作者**：Yaolun Zhang, Yiran Wu, Yijiong Yu, Qingyun Wu, Huazheng Wang  

**一句话要点**：提出Live-Evo在线自进化记忆系统，通过持续反馈优化LLM代理任务性能。

**关键词**：在线学习, 记忆系统, LLM代理, 自进化, 持续反馈

## 3 点简述
- 现有自进化系统依赖静态数据，难以应对真实分布偏移和连续反馈。
- Live-Evo解耦经验与元指导，在线更新记忆权重，强化有效经验并遗忘误导性经验。
- 在Prophet Arena基准上，Live-Evo显著提升Brier分数和市场回报，并迁移至深度研究基准。

## 摘要（原文）

> Large language model (LLM) agents are increasingly equipped with memory, which are stored experience and reusable guidance that can improve task-solving performance. Recent \emph{self-evolving} systems update memory based on interaction outcomes, but most existing evolution pipelines are developed for static train/test splits and only approximate online learning by folding static benchmarks, making them brittle under true distribution shift and continuous feedback. We introduce \textsc{Live-Evo}, an online self-evolving memory system that learns from a stream of incoming data over time. \textsc{Live-Evo} decouples \emph{what happened} from \emph{how to use it} via an Experience Bank and a Meta-Guideline Bank, compiling task-adaptive guidelines from retrieved experiences for each task. To manage memory online, \textsc{Live-Evo} maintains experience weights and updates them from feedback: experiences that consistently help are reinforced and retrieved more often, while misleading or stale experiences are down-weighted and gradually forgotten, analogous to reinforcement and decay in human memory. On the live \textit{Prophet Arena} benchmark over a 10-week horizon, \textsc{Live-Evo} improves Brier score by 20.8\% and increases market returns by 12.9\%, while also transferring to deep-research benchmarks with consistent gains over strong baselines. Our code is available at https://github.com/ag2ai/Live-Evo.

