---
layout: default
title: DeepFact: Co-Evolving Benchmarks and Agents for Deep Research Factuality
---

# DeepFact: Co-Evolving Benchmarks and Agents for Deep Research Factuality
**arXiv**：[2603.05912v1](https://arxiv.org/abs/2603.05912) · [PDF](https://arxiv.org/pdf/2603.05912.pdf)  
**作者**：Yukun Huang, Leonardo F. R. Ribeiro, Momchil Hardalov, Bhuwan Dhingra, Markus Dreyer, Venkatesh Saligrama  

**一句话要点**：提出AtS方法构建DeepFact-Bench基准和DeepFact-Eval代理，以解决深度研究报告事实性验证的挑战。

**关键词**：深度研究报告事实性, 动态基准构建, 审计-评分方法, 文档级验证代理, 事实核查基准

## 3 点简述
- 核心问题：现有事实核查器不适用于深度研究报告，且缺乏相关基准。
- 方法要点：采用AtS方法，通过审计-评分循环动态更新基准标签和理由。
- 实验或效果：AtS将专家准确率从60.8%提升至90.9%，DeepFact-Eval在基准上优于现有验证器。

## 摘要（原文）

> Search-augmented LLM agents can produce deep research reports (DRRs), but verifying claim-level factuality remains challenging. Existing fact-checkers are primarily designed for general-domain, factoid-style atomic claims, and there is no benchmark to test whether such verifiers transfer to DRRs. Yet building such a benchmark is itself difficult. We first show that static expert-labeled benchmarks are brittle in this setting: in a controlled study with PhD-level specialists, unassisted experts achieve only 60.8% accuracy on a hidden micro-gold set of verifiable claims. We propose Evolving Benchmarking via Audit-then-Score (AtS), where benchmark labels and rationales are explicitly revisable: when a verifier disagrees with the current benchmark, it must submit evidence; an auditor adjudicates the dispute; and accepted revisions update the benchmark before models are scored. Across four AtS rounds, expert micro-gold accuracy rises to 90.9%, indicating experts are substantially more reliable as auditors than as one-shot labelers. We instantiate AtS as DeepFact-Bench, a versioned DRR factuality benchmark with auditable rationales, and DeepFact-Eval, a document-level verification agent (with a grouped lite variant) that outperforms existing verifiers on DeepFact-Bench and transfers well to external factuality datasets.

