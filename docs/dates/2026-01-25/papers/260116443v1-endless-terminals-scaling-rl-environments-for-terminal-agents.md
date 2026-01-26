---
layout: default
title: Endless Terminals: Scaling RL Environments for Terminal Agents
---

# Endless Terminals: Scaling RL Environments for Terminal Agents
**arXiv**：[2601.16443v1](https://arxiv.org/abs/2601.16443) · [PDF](https://arxiv.org/pdf/2601.16443.pdf)  
**作者**：Kanishk Gandhi, Shivam Garg, Noah D. Goodman, Dimitris Papailiopoulos  

**一句话要点**：提出Endless Terminals以解决终端代理训练环境可扩展性瓶颈问题

**关键词**：终端代理, 强化学习, 程序化生成, 环境可扩展性, 任务自动化, 基准测试迁移

## 3 点简述
- 核心问题：现有终端基准测试仅用于评估，缺乏可扩展训练环境，阻碍自改进代理发展。
- 方法要点：构建全自动流水线，通过程序化生成任务描述、容器化环境、测试验证和可解性过滤，无需人工标注。
- 实验或效果：在生成任务上训练简单PPO代理，模型性能显著提升，并在人类基准测试中展现迁移优势。

## 摘要（原文）

> Environments are the bottleneck for self-improving agents. Current terminal benchmarks were built for evaluation, not training; reinforcement learning requires a scalable pipeline, not just a dataset. We introduce Endless Terminals, a fully autonomous pipeline that procedurally generates terminal-use tasks without human annotation. The pipeline has four stages: generating diverse task descriptions, building and validating containerized environments, producing completion tests, and filtering for solvability. From this pipeline we obtain 3255 tasks spanning file operations, log management, data processing, scripting, and database operations. We train agents using vanilla PPO with binary episode level rewards and a minimal interaction loop: no retrieval, multi-agent coordination, or specialized tools. Despite this simplicity, models trained on Endless Terminals show substantial gains: on our held-out dev set, Llama-3.2-3B improves from 4.0% to 18.2%, Qwen2.5-7B from 10.7% to 53.3%, and Qwen3-8B-openthinker-sft from 42.6% to 59.0%. These improvements transfer to human-curated benchmarks: models trained on Endless Terminals show substantial gains on held out human curated benchmarks: on TerminalBench 2.0, Llama-3.2-3B improves from 0.0% to 2.2%, Qwen2.5-7B from 2.2% to 3.4%, and Qwen3-8B-openthinker-sft from 1.1% to 6.7%, in each case outperforming alternative approaches including models with more complex agentic scaffolds. These results demonstrate that simple RL succeeds when environments scale.

