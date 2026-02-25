---
layout: default
title: LongVideo-R1: Smart Navigation for Low-cost Long Video Understanding
---

# LongVideo-R1: Smart Navigation for Low-cost Long Video Understanding
**arXiv**：[2602.20913v1](https://arxiv.org/abs/2602.20913) · [PDF](https://arxiv.org/pdf/2602.20913.pdf)  
**作者**：Jihao Qiu, Lingxi Xie, Xinyue Huo, Qi Tian, Qixiang Ye  

**一句话要点**：提出LongVideo-R1以解决低计算预算下的长视频理解挑战，通过智能导航避免冗余搜索。

**关键词**：长视频理解, 智能导航, 多模态大语言模型, 强化学习, 计算效率

## 3 点简述
- 核心问题：长视频理解在低计算预算下存在挑战，现有方法常需冗余搜索，效率低下。
- 方法要点：基于Qwen-3-8B模型，构建推理模块，利用高层视觉线索迭代导航，通过两阶段微调（SFT和RL）优化选择性剪辑处理。
- 实验或效果：在多个长视频基准测试中验证有效性，实现问答准确性与效率的优越权衡，数据和代码已公开。

## 摘要（原文）

> This paper addresses the critical and underexplored challenge of long video understanding with low computational budgets. We propose LongVideo-R1, an active, reasoning-equipped multimodal large language model (MLLM) agent designed for efficient video context navigation, avoiding the redundancy of exhaustive search. At the core of LongVideo-R1 lies a reasoning module that leverages high-level visual cues to infer the most informative video clip for subsequent processing. During inference, the agent initiates traversal from top-level visual summaries and iteratively refines its focus, immediately halting the exploration process upon acquiring sufficient knowledge to answer the query. To facilitate training, we first extract hierarchical video captions from CGBench, a video corpus with grounding annotations, and guide GPT-5 to generate 33K high-quality chain-of-thought-with-tool trajectories. The LongVideo-R1 agent is fine-tuned upon the Qwen-3-8B model through a two-stage paradigm: supervised fine-tuning (SFT) followed by reinforcement learning (RL), where RL employs a specifically designed reward function to maximize selective and efficient clip navigation. Experiments on multiple long video benchmarks validate the effectiveness of name, which enjoys superior tradeoff between QA accuracy and efficiency. All curated data and source code are provided in the supplementary material and will be made publicly available. Code and data are available at: https://github.com/qiujihao19/LongVideo-R1

