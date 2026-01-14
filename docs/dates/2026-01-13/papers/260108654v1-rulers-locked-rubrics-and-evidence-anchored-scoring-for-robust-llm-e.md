---
layout: default
title: RULERS: Locked Rubrics and Evidence-Anchored Scoring for Robust LLM Evaluation
---

# RULERS: Locked Rubrics and Evidence-Anchored Scoring for Robust LLM Evaluation
**arXiv**：[2601.08654v1](https://arxiv.org/abs/2601.08654) · [PDF](https://arxiv.org/pdf/2601.08654.pdf)  
**作者**：Yihan Hong, Huaiyuan Yao, Bolin Shen, Wanpeng Xu, Hua Wei, Yushun Dong  

**一句话要点**：提出RULERS框架以解决LLM作为评估者时的标准对齐与稳定性问题

**关键词**：LLM评估, 标准对齐, 结构化解码, 可验证推理, 评分校准, 编译器框架

## 3 点简述
- 核心问题：LLM评估存在标准不稳定、推理不可验证和评分尺度错配等失败模式
- 方法要点：通过编译-执行框架将自然语言标准转化为可执行规范，包括锁定标准、结构化解码和校准
- 实验或效果：在文章和摘要基准上显著提升人类一致性，对抗扰动稳定，小模型可媲美大模型

## 摘要（原文）

> The LLM-as-a-Judge paradigm promises scalable rubric-based evaluation, yet aligning frozen black-box models with human standards remains a challenge due to inherent generation stochasticity. We reframe judge alignment as a criteria transfer problem and isolate three recurrent failure modes: rubric instability caused by prompt sensitivity, unverifiable reasoning that lacks auditable evidence, and scale misalignment with human grading boundaries. To address these issues, we introduce RULERS (Rubric Unification, Locking, and Evidence-anchored Robust Scoring), a compiler-executor framework that transforms natural language rubrics into executable specifications. RULERS operates by compiling criteria into versioned immutable bundles, enforcing structured decoding with deterministic evidence verification, and applying lightweight Wasserstein-based post-hoc calibration, all without updating model parameters. Extensive experiments on essay and summarization benchmarks demonstrate that RULERS significantly outperforms representative baselines in human agreement, maintains strong stability against adversarial rubric perturbations, and enables smaller models to rival larger proprietary judges. Overall, our results suggest that reliable LLM judging requires executable rubrics, verifiable evidence, and calibrated scales rather than prompt phrasing alone. Code is available at https://github.com/LabRAI/Rulers.git.

