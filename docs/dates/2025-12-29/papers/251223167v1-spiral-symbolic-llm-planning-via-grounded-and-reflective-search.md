---
layout: default
title: SPIRAL: Symbolic LLM Planning via Grounded and Reflective Search
---

# SPIRAL: Symbolic LLM Planning via Grounded and Reflective Search
**arXiv**：[2512.23167v1](https://arxiv.org/abs/2512.23167) · [PDF](https://arxiv.org/pdf/2512.23167.pdf)  
**作者**：Yifan Zhang, Giridhar Ganapavarapu, Srideepika Jayaraman, Bhavna Agrawal, Dhaval Patel, Achille Fokoue  

**一句话要点**：提出SPIRAL框架，通过集成三个LLM代理到MCTS循环中，以解决复杂规划任务中LLM探索和自我纠正的不足。

**关键词**：符号规划, LLM代理, 蒙特卡洛树搜索, 自纠正推理, 密集奖励, 复杂任务规划

## 3 点简述
- 核心问题：LLM在复杂规划任务中因线性推理易犯早期错误，且搜索算法如MCTS在稀疏奖励下效果有限。
- 方法要点：SPIRAL嵌入三个LLM代理（规划者、模拟器、批评者）到MCTS，实现引导式、自纠正的搜索过程。
- 实验或效果：在DailyLifeAPIs和HuggingFace数据集上，SPIRAL显著优于默认Chain-of-Thought方法和其他先进代理，准确率提升超过16个百分点。

## 摘要（原文）

> Large Language Models (LLMs) often falter at complex planning tasks that require exploration and self-correction, as their linear reasoning process struggles to recover from early mistakes. While search algorithms like Monte Carlo Tree Search (MCTS) can explore alternatives, they are often ineffective when guided by sparse rewards and fail to leverage the rich semantic capabilities of LLMs. We introduce SPIRAL (Symbolic LLM Planning via Grounded and Reflective Search), a novel framework that embeds a cognitive architecture of three specialized LLM agents into an MCTS loop. SPIRAL's key contribution is its integrated planning pipeline where a Planner proposes creative next steps, a Simulator grounds the search by predicting realistic outcomes, and a Critic provides dense reward signals through reflection. This synergy transforms MCTS from a brute-force search into a guided, self-correcting reasoning process. On the DailyLifeAPIs and HuggingFace datasets, SPIRAL consistently outperforms the default Chain-of-Thought planning method and other state-of-the-art agents. More importantly, it substantially surpasses other state-of-the-art agents; for example, SPIRAL achieves 83.6% overall accuracy on DailyLifeAPIs, an improvement of over 16 percentage points against the next-best search framework, while also demonstrating superior token efficiency. Our work demonstrates that structuring LLM reasoning as a guided, reflective, and grounded search process yields more robust and efficient autonomous planners. The source code, full appendices, and all experimental data are available for reproducibility at the official project repository.

