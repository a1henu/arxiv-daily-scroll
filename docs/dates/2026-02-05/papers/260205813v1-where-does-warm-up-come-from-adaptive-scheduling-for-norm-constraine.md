---
layout: default
title: Where Does Warm-Up Come From? Adaptive Scheduling for Norm-Constrained Optimizers
---

# Where Does Warm-Up Come From? Adaptive Scheduling for Norm-Constrained Optimizers
**arXiv**：[2602.05813v1](https://arxiv.org/abs/2602.05813) · [PDF](https://arxiv.org/pdf/2602.05813.pdf)  
**作者**：Artem Riabinin, Andrey Veprikov, Arman Bolatov, Martin Takáč, Aleksandr Beznosikov  

**一句话要点**：提出自适应学习率调度器以优化范数约束优化器的预热阶段

**关键词**：自适应学习率调度, 范数约束优化器, 预热策略, 收敛理论, 大语言模型预训练

## 3 点简述
- 研究范数约束优化器（如Muon和Lion）的预热问题，基于局部曲率随次优性间隙减小的假设
- 建立收敛理论，证明预热后衰减的学习率调度自然产生，而非启发式设定
- 开发自适应预热调度器，在LLaMA架构预训练中优于手动调优，无需额外超参数搜索

## 摘要（原文）

> We study adaptive learning rate scheduling for norm-constrained optimizers (e.g., Muon and Lion). We introduce a generalized smoothness assumption under which local curvature decreases with the suboptimality gap and empirically verify that this behavior holds along optimization trajectories. Under this assumption, we establish convergence guarantees under an appropriate choice of learning rate, for which warm-up followed by decay arises naturally from the proof rather than being imposed heuristically.
>   Building on this theory, we develop a practical learning rate scheduler that relies only on standard hyperparameters and adapts the warm-up duration automatically at the beginning of training. We evaluate this method on large language model pretraining with LLaMA architectures and show that our adaptive warm-up selection consistently outperforms or at least matches the best manually tuned warm-up schedules across all considered setups, without additional hyperparameter search. Our source code is available at https://github.com/brain-lab-research/llm-baselines/tree/warmup

