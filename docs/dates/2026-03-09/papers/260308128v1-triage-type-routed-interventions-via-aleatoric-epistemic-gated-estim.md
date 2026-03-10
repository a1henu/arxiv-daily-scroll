---
layout: default
title: TRIAGE: Type-Routed Interventions via Aleatoric-Epistemic Gated Estimation in Robotic Manipulation and Adaptive Perception -- Don't Treat All Uncertainty the Same
---

# TRIAGE: Type-Routed Interventions via Aleatoric-Epistemic Gated Estimation in Robotic Manipulation and Adaptive Perception -- Don't Treat All Uncertainty the Same
**arXiv**：[2603.08128v1](https://arxiv.org/abs/2603.08128) · [PDF](https://arxiv.org/pdf/2603.08128.pdf)  
**作者**：Divake Kumar, Sina Tayebati, Devashri Naik, Patrick Poggi, Amanda Sofie Rios, Nilesh Ahuja, Amit Ranjan Trivedi  

**一句话要点**：提出TRIAGE框架，通过分解不确定性为偶然与认知成分，在机器人操控与自适应感知中实现类型特定干预。

**关键词**：不确定性分解, 机器人操控, 自适应感知, 偶然不确定性, 认知不确定性, 类型特定干预

## 3 点简述
- 核心问题：现有系统将预测不确定性聚合为单一标量，导致无法区分观测损坏与模型失配，可能触发错误纠正。
- 方法要点：使用马氏密度模型估计偶然不确定性，噪声鲁棒前向动力学集成检测认知不确定性，两者在闭环中保持近似正交。
- 实验效果：在机器人操控任务中，任务成功率从59.4%提升至80.4%；在自适应跟踪中，计算量减少58.2%且检测质量保持。

## 摘要（原文）

> Most uncertainty-aware robotic systems collapse prediction uncertainty into a single scalar score and use it to trigger uniform corrective responses. This aggregation obscures whether uncertainty arises from corrupted observations or from mismatch between the learned model and the true system dynamics. As a result, corrective actions may be applied to the wrong component of the closed loop, degrading performance relative to leaving the policy unchanged. We introduce a lightweight post hoc framework that decomposes uncertainty into aleatoric and epistemic components and uses these signals to regulate system responses at inference time. Aleatoric uncertainty is estimated from deviations in the observation distribution using a Mahalanobis density model, while epistemic uncertainty is detected using a noise robust forward dynamics ensemble that isolates model mismatch from measurement corruption. The two signals remain empirically near orthogonal during closed loop execution and enable type specific responses. High aleatoric uncertainty triggers observation recovery, while high epistemic uncertainty moderates control actions. The same signals also regulate adaptive perception by guiding model capacity selection during tracking inference. Experiments demonstrate consistent improvements across both control and perception tasks. In robotic manipulation, the decomposed controller improves task success from 59.4% to 80.4% under compound perturbations and outperforms a combined uncertainty baseline by up to 21.0%. In adaptive tracking inference on MOT17, uncertainty-guided model selection reduces average compute by 58.2% relative to a fixed high capacity detector while preserving detection quality within 0.4%. Code and demo videos are available at https://divake.github.io/uncertainty-decomposition/.

