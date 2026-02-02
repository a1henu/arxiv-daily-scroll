---
layout: default
title: RAudit: A Blind Auditing Protocol for Large Language Model Reasoning
---

# RAudit: A Blind Auditing Protocol for Large Language Model Reasoning
**arXiv**：[2601.23133v1](https://arxiv.org/abs/2601.23133) · [PDF](https://arxiv.org/pdf/2601.23133.pdf)  
**作者**：Edward Y. Chang, Longling Geng  

**一句话要点**：提出RAudit盲审协议以诊断大语言模型推理中的病理问题

**关键词**：大语言模型推理, 盲审协议, 推理病理诊断, CRIT评分, 社会框架影响, 模型鲁棒性

## 3 点简述
- 核心问题：推理时缩放会放大模型病理，如奉承、层级塌陷和过早确定性。
- 方法要点：基于盲审协议，通过CRIT评分评估推导步骤支持结论的合理性，无需真实标签。
- 实验效果：在数学和因果推理任务中揭示四种机制，挑战能力即鲁棒性和强反馈即优输出的假设。

## 摘要（原文）

> Inference-time scaling can amplify reasoning pathologies: sycophancy, rung collapse, and premature certainty. We present RAudit, a diagnostic protocol for auditing LLM reasoning without ground truth access. The key constraint is blindness: the auditor evaluates only whether derivation steps support conclusions, enabling detection of trace-output inconsistency and, when latent competence exists, its recovery. RAudit measures process quality via CRIT-based reasonableness scores and varies critique formulation to study how social framing affects model response. We prove bounded correction and $O(\log(1/ε))$ termination. Experiments on mathematical reasoning (CAP-GSM8K) and causal judgment (CausalL2) reveal four mechanisms explaining model unreliability: (1) Latent Competence Suppression, where models derive correct answers then overwrite them under social pressure; (2) The False Competence Trap, where weaker judges mask sycophancy that stronger judges expose; (3) The Complexity-Vulnerability Tradeoff, where causal tasks induce more than 10 times higher sycophancy than mathematical tasks; and (4) Iatrogenic Critique, where authoritative correction harms weaker models. These findings challenge assumptions that capability implies robustness and that stronger feedback yields better outputs.

