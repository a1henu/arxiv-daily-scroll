---
layout: default
title: Towards Selection as Power: Bounding Decision Authority in Autonomous Agents
---

# Towards Selection as Power: Bounding Decision Authority in Autonomous Agents
**arXiv**：[2602.14606v1](https://arxiv.org/abs/2602.14606) · [PDF](https://arxiv.org/pdf/2602.14606.pdf)  
**作者**：Jose Manuel de la Chica Rodriguez, Juan Manuel Vera Díaz  

**一句话要点**：提出基于选择权限制的治理架构，以在受监管高风险场景中部署自主代理系统。

**关键词**：自主代理治理, 选择权限制, 机械执行架构, 受监管场景, 安全评估

## 3 点简述
- 核心问题：现有安全方法未直接治理选择权，即决定选项生成、呈现和框架的权威。
- 方法要点：将认知、选择和行动分离，通过机械执行原语限制选择和行动自主权，集成外部候选生成等组件。
- 实验或效果：在受监管金融场景中评估，结果显示架构可实施、可审计，能防止确定性结果捕获并保持推理能力。

## 摘要（原文）

> Autonomous agentic systems are increasingly deployed in regulated, high-stakes domains where decisions may be irreversible and institutionally constrained. Existing safety approaches emphasize alignment, interpretability, or action-level filtering. We argue that these mechanisms are necessary but insufficient because they do not directly govern selection power: the authority to determine which options are generated, surfaced, and framed for decision. We propose a governance architecture that separates cognition, selection, and action into distinct domains and models autonomy as a vector of sovereignty. Cognitive autonomy remains unconstrained, while selection and action autonomy are bounded through mechanically enforced primitives operating outside the agent's optimization space. The architecture integrates external candidate generation (CEFL), a governed reducer, commit-reveal entropy isolation, rationale validation, and fail-loud circuit breakers. We evaluate the system across multiple regulated financial scenarios under adversarial stress targeting variance manipulation, threshold gaming, framing skew, ordering effects, and entropy probing. Metrics quantify selection concentration, narrative diversity, governance activation cost, and failure visibility. Results show that mechanical selection governance is implementable, auditable, and prevents deterministic outcome capture while preserving reasoning capacity. Although probabilistic concentration remains, the architecture measurably bounds selection authority relative to conventional scalar pipelines. This work reframes governance as bounded causal power rather than internal intent alignment, offering a foundation for deploying autonomous agents where silent failure is unacceptable.

