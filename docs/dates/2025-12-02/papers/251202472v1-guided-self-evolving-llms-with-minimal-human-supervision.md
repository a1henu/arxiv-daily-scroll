---
layout: default
title: Guided Self-Evolving LLMs with Minimal Human Supervision
---

# Guided Self-Evolving LLMs with Minimal Human Supervision
**arXiv**：[2512.02472v1](https://arxiv.org/abs/2512.02472) · [PDF](https://arxiv.org/pdf/2512.02472.pdf)  
**作者**：Wenhao Yu, Zhenwen Liang, Chengsong Huang, Kishan Panaganti, Tianqing Fang, Haitao Mi, Dong Yu  

**一句话要点**：提出R-Few框架以解决LLM自进化中的不稳定问题，通过轻量人类监督实现可控改进。

**关键词**：自进化学习, 轻量监督, 挑战者-求解器框架, 上下文接地, 混合训练, 稳定性控制

## 3 点简述
- 核心问题：无指导自进化易导致概念漂移、多样性崩溃和误进化，模型性能停滞或下降。
- 方法要点：引入挑战者-求解器自博弈框架，结合上下文接地和混合训练，实现轻量人类监督下的稳定进化。
- 实验或效果：在数学和通用推理基准上实现迭代提升，Qwen3-8B-Base在数学任务上超越R-Zero，性能媲美使用20倍人类数据的模型。

## 摘要（原文）

> AI self-evolution has long been envisioned as a path toward superintelligence, where models autonomously acquire, refine, and internalize knowledge from their own learning experiences. Yet in practice, unguided self-evolving systems often plateau quickly or even degrade as training progresses. These failures arise from issues such as concept drift, diversity collapse, and mis-evolution, as models reinforce their own biases and converge toward low-entropy behaviors. To enable models to self-evolve in a stable and controllable manner while minimizing reliance on human supervision, we introduce R-Few, a guided Self-Play Challenger-Solver framework that incorporates lightweight human oversight through in-context grounding and mixed training. At each iteration, the Challenger samples a small set of human-labeled examples to guide synthetic question generation, while the Solver jointly trains on human and synthetic examples under an online, difficulty-based curriculum. Across math and general reasoning benchmarks, R-Few achieves consistent and iterative improvements. For example, Qwen3-8B-Base improves by +3.0 points over R-Zero on math tasks and achieves performance on par with General-Reasoner, despite the latter being trained on 20 times more human data. Ablation studies confirm the complementary contributions of grounded challenger training and curriculum-based solver training, and further analysis shows that R-Few mitigates drift, yielding more stable and controllable co-evolutionary dynamics.

