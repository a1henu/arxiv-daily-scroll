---
layout: default
title: The Potential of CoT for Reasoning: A Closer Look at Trace Dynamics
---

# The Potential of CoT for Reasoning: A Closer Look at Trace Dynamics
**arXiv**：[2602.14903v1](https://arxiv.org/abs/2602.14903) · [PDF](https://arxiv.org/pdf/2602.14903.pdf)  
**作者**：Gregor Bachmann, Yichen Jiang, Seyed Mohsen Moosavi Dezfooli, Moin Nabi  

**一句话要点**：提出潜在概念量化CoT推理贡献，分析竞赛数学问题中的推理动态与可转移性。

**关键词**：链式思维推理, 推理动态分析, 潜在量化, 模型可转移性, 竞赛数学问题

## 3 点简述
- 核心问题：探究CoT推理成功背后的驱动因素，特别是推理步骤如何影响最终答案。
- 方法要点：引入潜在概念量化CoT各部分对正确完成概率的贡献，分析推理轨迹中的模式。
- 实验或效果：发现潜在的非单调性、尖锐峰值和幸运猜测，并验证CoT可转移性，弱模型可借助部分强模型CoT解锁性能。

## 摘要（原文）

> Chain-of-thought (CoT) prompting is a de-facto standard technique to elicit reasoning-like responses from large language models (LLMs), allowing them to spell out individual steps before giving a final answer. While the resemblance to human-like reasoning is undeniable, the driving forces underpinning the success of CoT reasoning still remain largely unclear. In this work, we perform an in-depth analysis of CoT traces originating from competition-level mathematics questions, with the aim of better understanding how, and which parts of CoT actually contribute to the final answer. To this end, we introduce the notion of a potential, quantifying how much a given part of CoT increases the likelihood of a correct completion. Upon examination of reasoning traces through the lens of the potential, we identify surprising patterns including (1) its often strong non-monotonicity (due to reasoning tangents), (2) very sharp but sometimes tough to interpret spikes (reasoning insights and jumps) as well as (3) at times lucky guesses, where the model arrives at the correct answer without providing any relevant justifications before. While some of the behaviours of the potential are readily interpretable and align with human intuition (such as insights and tangents), others remain difficult to understand from a human perspective. To further quantify the reliance of LLMs on reasoning insights, we investigate the notion of CoT transferability, where we measure the potential of a weaker model under the partial CoT from another, stronger model. Indeed aligning with our previous results, we find that as little as 20% of partial CoT can ``unlock'' the performance of the weaker model on problems that were previously unsolvable for it, highlighting that a large part of the mechanics underpinning CoT are transferable.

