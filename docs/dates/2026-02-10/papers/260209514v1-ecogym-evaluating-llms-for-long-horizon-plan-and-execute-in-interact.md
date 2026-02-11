---
layout: default
title: EcoGym: Evaluating LLMs for Long-Horizon Plan-and-Execute in Interactive Economies
---

# EcoGym: Evaluating LLMs for Long-Horizon Plan-and-Execute in Interactive Economies
**arXiv**：[2602.09514v1](https://arxiv.org/abs/2602.09514) · [PDF](https://arxiv.org/pdf/2602.09514.pdf)  
**作者**：Xavier Hu, Jinxiang Xia, Shengze Xu, Kangqi Song, Yishuo Yuan, Guibin Zhang, Jincheng Ren, Boyu Feng, Li Lu, Tieyong Zeng, Jiaheng Liu, Minghao Liu, Yuchen Elenor Jiang, Wei Wang, He Zhu, Wangchunshu Zhou  

**一句话要点**：提出EcoGym基准以评估LLM在交互经济中的长时程规划与执行能力

**关键词**：长时程规划, 交互经济, 基准测试, LLM评估, 决策制定, 经济模拟

## 3 点简述
- 当前LLM代理评估框架多为片段化、领域特定或缺乏持久经济动态基础
- EcoGym包含三个多样化环境，提供统一决策接口和预算化动作，支持1000+步长时程评估
- 实验显示11个领先LLM在策略与执行间存在系统性张力，无单一模型在所有场景中占优

## 摘要（原文）

> Long-horizon planning is widely recognized as a core capability of autonomous LLM-based agents; however, current evaluation frameworks suffer from being largely episodic, domain-specific, or insufficiently grounded in persistent economic dynamics. We introduce EcoGym, a generalizable benchmark for continuous plan-and-execute decision making in interactive economies. EcoGym comprises three diverse environments: Vending, Freelance, and Operation, implemented in a unified decision-making process with standardized interfaces, and budgeted actions over an effectively unbounded horizon (1000+ steps if 365 day-loops for evaluation). The evaluation of EcoGym is based on business-relevant outcomes (e.g., net worth, income, and DAU), targeting long-term strategic coherence and robustness under partial observability and stochasticity. Experiments across eleven leading LLMs expose a systematic tension: no single model dominates across all three scenarios. Critically, we find that models exhibit significant suboptimality in either high-level strategies or efficient actions executions. EcoGym is released as an open, extensible testbed for transparent long-horizon agent evaluation and for studying controllability-utility trade-offs in realistic economic settings.

