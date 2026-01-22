---
layout: default
title: IntelliSA: An Intelligent Static Analyzer for IaC Security Smell Detection Using Symbolic Rules and Neural Inference
---

# IntelliSA: An Intelligent Static Analyzer for IaC Security Smell Detection Using Symbolic Rules and Neural Inference
**arXiv**：[2601.14595v1](https://arxiv.org/abs/2601.14595) · [PDF](https://arxiv.org/pdf/2601.14595.pdf)  
**作者**：Qiyue Mei, Michael Fu  

**一句话要点**：提出IntelliSA智能静态分析器，结合符号规则与神经推理检测IaC安全异味，以降低误报。

**关键词**：IaC安全检测, 静态分析, 符号规则, 神经推理, 知识蒸馏, 误报过滤

## 3 点简述
- IaC脚本安全异味检测中，基于符号规则的方法易产生高误报，增加人工检查负担。
- IntelliSA集成符号规则进行过近似检测，再通过知识蒸馏训练的小型学生模型过滤误报。
- 在真实数据集上评估，IntelliSA达到最高F1分数83%，成本效益最优，检测60%异味仅检查2%代码。

## 摘要（原文）

> Infrastructure as Code (IaC) enables automated provisioning of large-scale cloud and on-premise environments, reducing the need for repetitive manual setup. However, this automation is a double-edged sword: a single misconfiguration in IaC scripts can propagate widely, leading to severe system downtime and security risks. Prior studies have shown that IaC scripts often contain security smells--bad coding patterns that may introduce vulnerabilities--and have proposed static analyzers based on symbolic rules to detect them. Yet, our preliminary analysis reveals that rule-based detection alone tends to over-approximate, producing excessive false positives and increasing the burden of manual inspection. In this paper, we present IntelliSA, an intelligent static analyzer for IaC security smell detection that integrates symbolic rules with neural inference. IntelliSA applies symbolic rules to over-approximate potential smells for broad coverage, then employs neural inference to filter false positives. While an LLM can effectively perform this filtering, reliance on LLM APIs introduces high cost and latency, raises data governance concerns, and limits reproducibility and offline deployment. To address the challenges, we adopt a knowledge distillation approach: an LLM teacher generates pseudo-labels to train a compact student model--over 500x smaller--that learns from the teacher's knowledge and efficiently classifies false positives. We evaluate IntelliSA against two static analyzers and three LLM baselines (Claude-4, Grok-4, and GPT-5) using a human-labeled dataset including 241 security smells across 11,814 lines of real-world IaC code. Experimental results show that IntelliSA achieves the highest F1 score (83%), outperforming baselines by 7-42%. Moreover, IntelliSA demonstrates the best cost-effectiveness, detecting 60% of security smells while inspecting less than 2% of the codebase.

