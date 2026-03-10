---
layout: default
title: PostTrainBench: Can LLM Agents Automate LLM Post-Training?
---

# PostTrainBench: Can LLM Agents Automate LLM Post-Training?
**arXiv**：[2603.08640v1](https://arxiv.org/abs/2603.08640) · [PDF](https://arxiv.org/pdf/2603.08640.pdf)  
**作者**：Ben Rank, Hardik Bhatnagar, Ameya Prabhu, Shira Eisenberg, Karina Nguyen, Matthias Bethge, Maksym Andriushchenko  

**一句话要点**：提出PostTrainBench以评估LLM代理在有限计算下自动化LLM后训练的能力。

**关键词**：LLM代理, 后训练自动化, 基准测试, 奖励黑客, AI研究自动化, 有限计算约束

## 3 点简述
- 核心问题：探索AI代理能否自动化AI研究，特别是LLM后训练阶段。
- 方法要点：引入基准测试，让前沿代理自主优化基础LLM性能，无预定义策略。
- 实验或效果：代理取得进展但落后于官方指令调优模型，在特定场景下可超越，并发现奖励黑客等失败模式。

## 摘要（原文）

> AI agents have become surprisingly proficient at software engineering over the past year, largely due to improvements in reasoning capabilities. This raises a deeper question: can these systems extend their capabilities to automate AI research itself? In this paper, we explore post-training, the critical phase that turns base LLMs into useful assistants. We introduce PostTrainBench to benchmark how well LLM agents can perform post-training autonomously under bounded compute constraints (10 hours on one H100 GPU). We ask frontier agents (e.g., Claude Code with Opus 4.6) to optimize the performance of a base LLM on a particular benchmark (e.g., Qwen3-4B on AIME). Importantly, we do not provide any predefined strategies to the agents and instead give them full autonomy to find necessary information on the web, run experiments, and curate data. We find that frontier agents make substantial progress but generally lag behind instruction-tuned LLMs from leading providers: 23.2% for the best agent vs. 51.1% for official instruction-tuned models. However, agents can exceed instruction-tuned models in targeted scenarios: GPT-5.1 Codex Max achieves 89% on BFCL with Gemma-3-4B vs. 67% for the official model. We also observe several failure modes worth flagging. Agents sometimes engage in reward hacking: training on the test set, downloading existing instruction-tuned checkpoints instead of training their own, and using API keys they find to generate synthetic data without authorization. These behaviors are concerning and highlight the importance of careful sandboxing as these systems become more capable. Overall, we hope PostTrainBench will be useful for tracking progress in AI R&D automation and for studying the risks that come with it. Website and code are available at https://posttrainbench.com/.

