---
layout: default
title: Breaking Contextual Inertia: Reinforcement Learning with Single-Turn Anchors for Stable Multi-Turn Interaction
---

# Breaking Contextual Inertia: Reinforcement Learning with Single-Turn Anchors for Stable Multi-Turn Interaction
**arXiv**：[2603.04783v1](https://arxiv.org/abs/2603.04783) · [PDF](https://arxiv.org/pdf/2603.04783.pdf)  
**作者**：Xingwu Chen, Zhanqiu Zhang, Yiwen Guo, Difan Zou  

**一句话要点**：提出RLSTA方法，利用单轮锚点强化学习以稳定多轮交互中的模型推理

**关键词**：上下文惯性, 强化学习, 多轮交互, 单轮锚点, 跨领域泛化

## 3 点简述
- 核心问题：LLMs在多轮交互中因上下文惯性而忽略新信息，导致性能下降
- 方法要点：利用模型单轮能力作为锚点，通过强化学习对齐多轮响应以打破惯性
- 实验或效果：RLSTA显著优于标准微调，展现跨领域泛化能力且无需外部验证器

## 摘要（原文）

> While LLMs demonstrate strong reasoning capabilities when provided with full information in a single turn, they exhibit substantial vulnerability in multi-turn interactions. Specifically, when information is revealed incrementally or requires updates, models frequently fail to integrate new constraints, leading to a collapse in performance compared to their single-turn baselines. We term the root cause as \emph{Contextual Inertia}: a phenomenon where models rigidly adhere to previous reasoning traces. Even when users explicitly provide corrections or new data in later turns, the model ignores them, preferring to maintain consistency with its previous (incorrect) reasoning path. To address this, we introduce \textbf{R}einforcement \textbf{L}earning with \textbf{S}ingle-\textbf{T}urn \textbf{A}nchors (\textbf{RLSTA}), a generalizable training approach designed to stabilize multi-turn interaction across diverse scenarios and domains. RLSTA leverages the model's superior single-turn capabilities as stable internal anchors to provide reward signals. By aligning multi-turn responses with these anchors, RLSTA empowers models to break contextual inertia and self-calibrate their reasoning based on the latest information. Experiments show that RLSTA significantly outperforms standard fine-tuning and abstention-based methods. Notably, our method exhibits strong cross-domain generalization (e.g., math to code) and proves effective even without external verifiers, highlighting its potential for general-domain applications.

