---
layout: default
title: Resisting Manipulative Bots in Memecoin Copy Trading: A Multi-Agent Approach with Chain-of-Thought Reasoning
---

# Resisting Manipulative Bots in Memecoin Copy Trading: A Multi-Agent Approach with Chain-of-Thought Reasoning
**arXiv**：[2601.08641v1](https://arxiv.org/abs/2601.08641) · [PDF](https://arxiv.org/pdf/2601.08641.pdf)  
**作者**：Yichen Luo, Yebo Feng, Jiahua Xu, Yang Liu  

**一句话要点**：提出基于多智能体与思维链推理的可解释系统，以应对模因币跟单交易中的操纵机器人问题。

**关键词**：模因币交易, 多智能体系统, 思维链推理, 可解释人工智能, 跟单交易, 加密货币市场

## 3 点简述
- 核心问题：模因币跟单交易面临操纵机器人泛滥、被跟钱包未来表现不确定及交易执行延迟等挑战，导致盈利无保障。
- 方法要点：受资产管理团队结构启发，将复杂任务分解为子任务，协调专业智能体协作，采用少样本思维链提示获取知识并生成可解释决策。
- 实验或效果：在1000个模因币项目数据集上评估，系统在识别高质量项目和关键意见领袖钱包上分别达到73%和70%精确度，所选领袖总利润达50万美元。

## 摘要（原文）

> The launch of \$Trump coin ignited a wave in meme coin investment. Copy trading, as a strategy-agnostic approach that eliminates the need for deep trading knowledge, quickly gains widespread popularity in the meme coin market. However, copy trading is not a guarantee of profitability due to the prevalence of manipulative bots, the uncertainty of the followed wallets' future performance, and the lag in trade execution. Recently, large language models (LLMs) have shown promise in financial applications by effectively understanding multi-modal data and producing explainable decisions. However, a single LLM struggles with complex, multi-faceted tasks such as asset allocation. These challenges are even more pronounced in cryptocurrency markets, where LLMs often lack sufficient domain-specific knowledge in their training data.
>   To address these challenges, we propose an explainable multi-agent system for meme coin copy trading. Inspired by the structure of an asset management team, our system decomposes the complex task into subtasks and coordinates specialized agents to solve them collaboratively. Employing few-shot chain-of-though (CoT) prompting, each agent acquires professional meme coin trading knowledge, interprets multi-modal data, and generates explainable decisions. Using a dataset of 1,000 meme coin projects' transaction data, our empirical evaluation shows that the proposed multi-agent system outperforms both traditional machine learning models and single LLMs, achieving 73% and 70% precision in identifying high-quality meme coin projects and key opinion leader (KOL) wallets, respectively. The selected KOLs collectively generated a total profit of \$500,000 across these projects.

