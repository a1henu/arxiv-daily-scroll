---
layout: default
title: Adapter-Augmented Bandits for Online Multi-Constrained Multi-Modal Inference Scheduling
---

# Adapter-Augmented Bandits for Online Multi-Constrained Multi-Modal Inference Scheduling
**arXiv**：[2603.06403v1](https://arxiv.org/abs/2603.06403) · [PDF](https://arxiv.org/pdf/2603.06403.pdf)  
**作者**：Xianzhi Zhang, Yue Xu, Yinlin Zhu, Di Wu, Yipeng Zhou, Miao Hu, Guocong Quan  

**一句话要点**：提出M-CMAB框架以解决多模态大模型在线推理调度中的多约束多模态任务表示与决策挑战

**关键词**：多模态大模型, 在线调度, 上下文多臂老虎机, 多约束优化, 适配器增强, 推理成本控制

## 3 点简述
- 核心问题：在线多模态大模型推理调度面临任务模态组成和推理难度多变、后端成本时变的不确定性，需在不可逆预算下进行低开销决策。
- 方法要点：采用多适配器增强的上下文多臂老虎机框架，包括预测器提取任务表示、约束器维护拉格朗日乘子、调度器平衡探索与利用。
- 实验或效果：在异构后端多模态基准上，M-CMAB优于现有基线，奖励提升最高达14.18%，接近理论上界。

## 摘要（原文）

> Multi-modal large language model (MLLM) inference scheduling enables strong response quality under practical and heterogeneous budgets, beyond what a homogeneous single-backend setting can offer. Yet online MLLM task scheduling is nontrivial, as requests vary sharply in modality composition and latent reasoning difficulty, while execution backends incur distinct, time-varying costs due to system jitter and network variation. These coupled uncertainties pose two core challenges: deriving semantically faithful yet scheduling-relevant multi-modal task representations, and making low-overhead online decisions over irreversible multi-dimensional budgets. Accordingly, we propose \emph{M-CMAB} (\underline{M}ulti-modal \underline{M}ulti-constraint \underline{C}ontextual \underline{M}ulti-\underline{A}rmed \underline{B}andit), a multi-adapter-enhanced MLLM inference scheduling framework with three components: (i) a CLS-attentive, frozen-backbone \emph{Predictor} that extracts compact task representations and updates only lightweight adapters for action-specific estimation; (ii) a primal-dual \emph{Constrainer} that maintains online Lagrange multipliers to enforce long-horizon constraints via per-round objectives; and (iii) a two-phase \emph{Scheduler} that balances exploration and exploitation under irreversible budgets. We establish a regret guarantee under multi-dimensional knapsack constraints. On a composite multimodal benchmark with heterogeneous backends, \emph{M-CMAB} consistently outperforms state-of-the-art baselines across budget regimes, achieving up to 14.18% higher reward and closely tracking an oracle-aided upper bound. Codes are available at https://anonymous.4open.science/r/M2CMAB/.

