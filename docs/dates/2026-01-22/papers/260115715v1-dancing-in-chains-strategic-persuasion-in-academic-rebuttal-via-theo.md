---
layout: default
title: Dancing in Chains: Strategic Persuasion in Academic Rebuttal via Theory of Mind
---

# Dancing in Chains: Strategic Persuasion in Academic Rebuttal via Theory of Mind
**arXiv**：[2601.15715v1](https://arxiv.org/abs/2601.15715) · [PDF](https://arxiv.org/pdf/2601.15715.pdf)  
**作者**：Zhitao He, Zongwei Lyu, Yi R Fung  

**一句话要点**：提出基于心智理论的学术反驳框架RebuttalAgent，以解决信息不对称下的战略沟通挑战。

**关键词**：学术反驳, 心智理论, 战略沟通, 强化学习, 自动评估, 数据集构建

## 3 点简述
- 核心问题：学术反驳是信息不对称下的战略沟通，现有方法因缺乏视角采能力而受限。
- 方法要点：通过ToM-策略-响应管道建模审稿人心态、制定说服策略并生成基于策略的回应。
- 实验或效果：在自动指标上平均提升18.3%，并在自动和人工评估中超越先进专有模型。

## 摘要（原文）

> Although artificial intelligence (AI) has become deeply integrated into various stages of the research workflow and achieved remarkable advancements, academic rebuttal remains a significant and underexplored challenge. This is because rebuttal is a complex process of strategic communication under severe information asymmetry rather than a simple technical debate. Consequently, current approaches struggle as they largely imitate surface-level linguistics, missing the essential element of perspective-taking required for effective persuasion. In this paper, we introduce RebuttalAgent, the first framework to ground academic rebuttal in Theory of Mind (ToM), operationalized through a ToM-Strategy-Response (TSR) pipeline that models reviewer mental state, formulates persuasion strategy, and generates strategy-grounded response. To train our agent, we construct RebuttalBench, a large-scale dataset synthesized via a novel critique-and-refine approach. Our training process consists of two stages, beginning with a supervised fine-tuning phase to equip the agent with ToM-based analysis and strategic planning capabilities, followed by a reinforcement learning phase leveraging the self-reward mechanism for scalable self-improvement. For reliable and efficient automated evaluation, we further develop Rebuttal-RM, a specialized evaluator trained on over 100K samples of multi-source rebuttal data, which achieves scoring consistency with human preferences surpassing powerful judge GPT-4.1. Extensive experiments show RebuttalAgent significantly outperforms the base model by an average of 18.3% on automated metrics, while also outperforming advanced proprietary models across both automated and human evaluations. Disclaimer: the generated rebuttal content is for reference only to inspire authors and assist in drafting. It is not intended to replace the author's own critical analysis and response.

