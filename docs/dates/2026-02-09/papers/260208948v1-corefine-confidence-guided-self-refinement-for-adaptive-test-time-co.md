---
layout: default
title: CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute
---

# CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute
**arXiv**：[2602.08948v1](https://arxiv.org/abs/2602.08948) · [PDF](https://arxiv.org/pdf/2602.08948.pdf)  
**作者**：Chen Jin, Ryutaro Tanno, Tom Diethe, Philip Teare  

**一句话要点**：提出CoRefine方法，通过置信度引导的自精炼减少大语言模型推理时的计算开销。

**关键词**：大语言模型, 推理优化, 置信度引导, 自精炼, 计算效率

## 3 点简述
- 核心问题：大语言模型依赖并行解码提升推理精度，但计算成本高。
- 方法要点：在冻结大语言模型上添加轻量控制器，基于置信度动态决策精炼步骤。
- 实验或效果：平均2.7步精炼，减少约190倍token，置信度停止时精度达92.6%。

## 摘要（原文）

> Large Language Models (LLMs) often rely on test-time scaling via parallel decoding (for example, 512 samples) to boost reasoning accuracy, but this incurs substantial compute. We introduce CoRefine, a confidence-guided self-refinement method that achieves competitive accuracy using a fraction of the tokens via a lightweight 211k-parameter Conv1D controller atop a frozen LLM. The controller consumes full-trace confidence to decide whether to halt, re-examine, or try a different approach, enabling targeted self-correction with an average of 2.7 refinement steps per problem and roughly 190-fold token reduction relative to 512-sample baselines. Across diverse reasoning benchmarks and three open-source models, the controller achieves 92.6 percent precision when it confidently halts, indicating that confidence dynamics reliably signal correctness without ground-truth verification. We extend this to CoRefine-Tree, a hybrid sequential-parallel variant that adaptively balances exploration and exploitation, with easy serving integration and verifier compatibility. By treating confidence as a control signal rather than a correctness guarantee, CoRefine provides a modular primitive for scalable reasoning and agentic settings with imperfect verifiers.

