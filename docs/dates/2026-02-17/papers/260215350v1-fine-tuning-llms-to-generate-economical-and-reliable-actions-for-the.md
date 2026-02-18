---
layout: default
title: Fine-Tuning LLMs to Generate Economical and Reliable Actions for the Power Grid
---

# Fine-Tuning LLMs to Generate Economical and Reliable Actions for the Power Grid
**arXiv**：[2602.15350v1](https://arxiv.org/abs/2602.15350) · [PDF](https://arxiv.org/pdf/2602.15350.pdf)  
**作者**：Mohamad Chehade, Hao Zhu  

**一句话要点**：提出可验证的多阶段微调流程，使LLM在预算约束下为电网PSPS场景生成经济可靠的开关动作计划。

**关键词**：电网优化, 大语言模型微调, 传输开关, 电压感知, 可验证生成

## 3 点简述
- 核心问题：PSPS导致电网拓扑快速变化，需快速生成减少负荷削减并维持电压的开关动作计划。
- 方法要点：通过监督微调和直接偏好优化，将DC-OPF MILP蒸馏为约束动作语法，并注入电压感知。
- 实验效果：在IEEE 118-bus场景中，微调显著提升DC目标值，降低AC潮流失败率，改善电压惩罚指标。

## 摘要（原文）

> Public Safety Power Shutoffs (PSPS) force rapid topology changes that can render standard operating points infeasible, requiring operators to quickly identify corrective transmission switching actions that reduce load shedding while maintaining acceptable voltage behavior. We present a verifiable, multi-stage adaptation pipeline that fine-tunes an instruction-tuned large language model (LLM) to generate \emph{open-only} corrective switching plans from compact PSPS scenario summaries under an explicit switching budget. First, supervised fine-tuning distills a DC-OPF MILP oracle into a constrained action grammar that enables reliable parsing and feasibility checks. Second, direct preference optimization refines the policy using AC-evaluated preference pairs ranked by a voltage-penalty metric, injecting voltage-awareness beyond DC imitation. Finally, best-of-$N$ selection provides an inference-time addition by choosing the best feasible candidate under the target metric. On IEEE 118-bus PSPS scenarios, fine-tuning substantially improves DC objective values versus zero-shot generation, reduces AC power-flow failure from 50\% to single digits, and improves voltage-penalty outcomes on the common-success set. Code and data-generation scripts are released to support reproducibility.

