---
layout: default
title: Scalably Enhancing the Clinical Validity of a Task Benchmark with Physician Oversight
---

# Scalably Enhancing the Clinical Validity of a Task Benchmark with Physician Oversight
**arXiv**：[2512.19691v1](https://arxiv.org/abs/2512.19691) · [PDF](https://arxiv.org/pdf/2512.19691.pdf)  
**作者**：Junze Ye, Daniel Tawfik, Alex J. Goodell, Nikhil V. Kotha, Mark K. Buyyounouski, Mohsen Bayati  

**一句话要点**：提出医生监督的基准审计流程以提升临床风险评分任务基准的有效性

**关键词**：临床风险评分, 基准审计, 强化学习, 医生监督, 标签噪声, 模型评估

## 3 点简述
- 核心问题：模型生成的基准如MedCalc-Bench可能固化历史错误，影响评估和强化学习训练。
- 方法要点：引入医生参与的系统化审计流程，利用智能验证器自动筛选争议实例进行人工复审。
- 实验或效果：通过GRPO微调Qwen3-8B模型，修正标签后准确率提升8.7%，验证标签噪声对模型评估的影响。

## 摘要（原文）

> Automating the calculation of clinical risk scores offers a significant opportunity to reduce physician administrative burden and enhance patient care. The current standard for evaluating this capability is MedCalc-Bench, a large-scale dataset constructed using LLM-based feature extraction and rule-based aggregation. However, treating such model-generated benchmarks as static oracles risks enshrining historical model errors as evaluation gold standards, a problem dangerously amplified when these datasets serve as reward signals for Reinforcement Learning (RL). In this work, we propose viewing benchmarks for complex tasks such as clinical score computation as ''in-progress living documents'' that should be periodically re-evaluated as the processes for creating them improve. We introduce a systematic, physician-in-the-loop pipeline that leverages advanced agentic verifiers to audit and relabel MedCalc-Bench, utilizing automated triage to reserve scarce clinician attention for the most contentious instances. Our audit reveals that a notable fraction of original labels diverge from medical ground truth due to extraction errors, calculator logic mismatches, and clinical ambiguity. To study whether this label noise meaningfully impacts downstream RL training, we fine-tune a Qwen3-8B model via Group Relative Policy Optimization (GRPO) and demonstrate that training on corrected labels yields an 8.7% absolute improvement in accuracy over the original baseline -- validating that label noise materially affects model evaluation. These findings underscore that in safety-critical domains, rigorous benchmark maintenance is a prerequisite for genuine model alignment.

