---
layout: default
title: Multi-Round Human-AI Collaboration with User-Specified Requirements
---

# Multi-Round Human-AI Collaboration with User-Specified Requirements
**arXiv**：[2602.17646v1](https://arxiv.org/abs/2602.17646) · [PDF](https://arxiv.org/pdf/2602.17646.pdf)  
**作者**：Sima Noorani, Shayan Kiyani, Hamed Hassani, George Pappas  

**一句话要点**：提出基于用户定义规则的多轮人机协作框架，以提升高风险决策质量。

**关键词**：多轮人机协作, 反事实伤害, 互补性, 在线算法, 用户定义规则, 决策质量

## 3 点简述
- 核心问题：多轮对话AI需确保不损害人类优势并补充其弱点，以可靠改进决策。
- 方法要点：通过用户指定规则形式化反事实伤害和互补性，并设计在线无分布算法强制执行约束。
- 实验或效果：在医疗诊断和图像推理任务中验证算法能维持约束违反率，约束调整可预测影响人类准确性。

## 摘要（原文）

> As humans increasingly rely on multiround conversational AI for high stakes decisions, principled frameworks are needed to ensure such interactions reliably improve decision quality. We adopt a human centric view governed by two principles: counterfactual harm, ensuring the AI does not undermine human strengths, and complementarity, ensuring it adds value where the human is prone to err. We formalize these concepts via user defined rules, allowing users to specify exactly what harm and complementarity mean for their specific task. We then introduce an online, distribution free algorithm with finite sample guarantees that enforces the user-specified constraints over the collaboration dynamics. We evaluate our framework across two interactive settings: LLM simulated collaboration on a medical diagnostic task and a human crowdsourcing study on a pictorial reasoning task. We show that our online procedure maintains prescribed counterfactual harm and complementarity violation rates even under nonstationary interaction dynamics. Moreover, tightening or loosening these constraints produces predictable shifts in downstream human accuracy, confirming that the two principles serve as practical levers for steering multi-round collaboration toward better decision quality without the need to model or constrain human behavior.

