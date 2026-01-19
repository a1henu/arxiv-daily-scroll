---
layout: default
title: Institutional AI: Governing LLM Collusion in Multi-Agent Cournot Markets via Public Governance Graphs
---

# Institutional AI: Governing LLM Collusion in Multi-Agent Cournot Markets via Public Governance Graphs
**arXiv**：[2601.11369v1](https://arxiv.org/abs/2601.11369) · [PDF](https://arxiv.org/pdf/2601.11369.pdf)  
**作者**：Marcantonio Bracale Syrnikov, Federico Pierucci, Marcello Galisai, Matteo Prandi, Piercosma Bisconti, Francesco Giarrusso, Olga Sorokoletova, Vincenzo Suriani, Daniele Nardi  

**一句话要点**：提出基于治理图的制度AI框架以治理多智能体古诺市场中的LLM合谋

**关键词**：多智能体对齐, 制度AI, 治理图, 古诺市场, LLM合谋, 机制设计

## 3 点简述
- 核心问题：多智能体LLM集成可能收敛于协调、有害社会的均衡，需系统级对齐方法。
- 方法要点：引入治理图作为公开、不可变的制度声明，结合Oracle/Controller运行时执行制裁与审计。
- 实验效果：制度AI显著降低合谋水平，平均层级从3.1降至1.8，严重合谋发生率从50%降至5.6%。

## 摘要（原文）

> Multi-agent LLM ensembles can converge on coordinated, socially harmful equilibria. This paper advances an experimental framework for evaluating Institutional AI, our system-level approach to AI alignment that reframes alignment from preference engineering in agent-space to mechanism design in institution-space. Central to this approach is the governance graph, a public, immutable manifest that declares legal states, transitions, sanctions, and restorative paths; an Oracle/Controller runtime interprets this manifest, attaching enforceable consequences to evidence of coordination while recording a cryptographically keyed, append-only governance log for audit and provenance. We apply the Institutional AI framework to govern the Cournot collusion case documented by prior work and compare three regimes: Ungoverned (baseline incentives from the structure of the Cournot market), Constitutional (a prompt-only policy-as-prompt prohibition implemented as a fixed written anti-collusion constitution, and Institutional (governance-graph-based). Across six model configurations including cross-provider pairs (N=90 runs/condition), the Institutional regime produces large reductions in collusion: mean tier falls from 3.1 to 1.8 (Cohen's d=1.28), and severe-collusion incidence drops from 50% to 5.6%. The prompt-only Constitutional baseline yields no reliable improvement, illustrating that declarative prohibitions do not bind under optimisation pressure. These results suggest that multi-agent alignment may benefit from being framed as an institutional design problem, where governance graphs can provide a tractable abstraction for alignment-relevant collective behavior.

