---
layout: default
title: AI Agents for Inventory Control: Human-LLM-OR Complementarity
---

# AI Agents for Inventory Control: Human-LLM-OR Complementarity
**arXiv**：[2602.12631v1](https://arxiv.org/abs/2602.12631) · [PDF](https://arxiv.org/pdf/2602.12631.pdf)  
**作者**：Jackie Baek, Yaopeng Fu, Will Ma, Tianyi Peng  

**一句话要点**：提出人-LLM-OR互补框架以优化多周期库存控制决策

**关键词**：库存控制, 大语言模型, 人机协作, 操作研究, 基准测试, 决策优化

## 3 点简述
- 研究库存控制中OR算法与LLM的互补性，解决需求分布变化和上下文信息缺失问题
- 构建InventoryBench基准，包含1000多个实例，测试需求变化、季节性和不确定提前期下的决策规则
- 通过课堂实验验证人-AI团队平均利润高于单独决策，并量化个体受益比例

## 摘要（原文）

> Inventory control is a fundamental operations problem in which ordering decisions are traditionally guided by theoretically grounded operations research (OR) algorithms. However, such algorithms often rely on rigid modeling assumptions and can perform poorly when demand distributions shift or relevant contextual information is unavailable. Recent advances in large language models (LLMs) have generated interest in AI agents that can reason flexibly and incorporate rich contextual signals, but it remains unclear how best to incorporate LLM-based methods into traditional decision-making pipelines.
>   We study how OR algorithms, LLMs, and humans can interact and complement each other in a multi-period inventory control setting. We construct InventoryBench, a benchmark of over 1,000 inventory instances spanning both synthetic and real-world demand data, designed to stress-test decision rules under demand shifts, seasonality, and uncertain lead times. Through this benchmark, we find that OR-augmented LLM methods outperform either method in isolation, suggesting that these methods are complementary rather than substitutes.
>   We further investigate the role of humans through a controlled classroom experiment that embeds LLM recommendations into a human-in-the-loop decision pipeline. Contrary to prior findings that human-AI collaboration can degrade performance, we show that, on average, human-AI teams achieve higher profits than either humans or AI agents operating alone. Beyond this population-level finding, we formalize an individual-level complementarity effect and derive a distribution-free lower bound on the fraction of individuals who benefit from AI collaboration; empirically, we find this fraction to be substantial.

