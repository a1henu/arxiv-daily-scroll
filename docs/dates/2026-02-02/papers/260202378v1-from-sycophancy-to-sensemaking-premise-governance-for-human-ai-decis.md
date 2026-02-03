---
layout: default
title: From Sycophancy to Sensemaking: Premise Governance for Human-AI Decision Making
---

# From Sycophancy to Sensemaking: Premise Governance for Human-AI Decision Making
**arXiv**：[2602.02378v1](https://arxiv.org/abs/2602.02378) · [PDF](https://arxiv.org/pdf/2602.02378.pdf)  
**作者**：Raunak Jain, Mudita Khurana, John Stephens, Srinivas Dharmasanam, Shankar Venkataraman  

**一句话要点**：提出基于知识基质的协同前提治理框架，以解决深度不确定性决策中LLM的谄媚问题。

**关键词**：人机决策, 前提治理, 深度不确定性, 谄媚行为, 知识基质, 差异检测

## 3 点简述
- 核心问题：LLM在决策支持中易产生谄媚行为，即流畅同意但缺乏校准判断，放大错误承诺。
- 方法要点：通过知识基质上的差异驱动控制循环，检测冲突、定位错位，并触发有界协商。
- 实验或效果：以辅导为例说明框架应用，并提出可证伪的评估标准。

## 摘要（原文）

> As LLMs expand from assistance to decision support, a dangerous pattern emerges: fluent agreement without calibrated judgment. Low-friction assistants can become sycophantic, baking in implicit assumptions and pushing verification costs onto experts, while outcomes arrive too late to serve as reward signals. In deep-uncertainty decisions (where objectives are contested and reversals are costly), scaling fluent agreement amplifies poor commitments faster than it builds expertise. We argue reliable human-AI partnership requires a shift from answer generation to collaborative premise governance over a knowledge substrate, negotiating only what is decision-critical. A discrepancy-driven control loop operates over this substrate: detecting conflicts, localizing misalignment via typed discrepancies (teleological, epistemic, procedural), and triggering bounded negotiation through decision slices. Commitment gating blocks action on uncommitted load-bearing premises unless overridden under logged risk; value-gated challenge allocates probing under interaction cost. Trust then attaches to auditable premises and evidence standards, not conversational fluency. We illustrate with tutoring and propose falsifiable evaluation criteria.

