---
layout: default
title: JADE: Expert-Grounded Dynamic Evaluation for Open-Ended Professional Tasks
---

# JADE: Expert-Grounded Dynamic Evaluation for Open-Ended Professional Tasks
**arXiv**：[2602.06486v1](https://arxiv.org/abs/2602.06486) · [PDF](https://arxiv.org/pdf/2602.06486.pdf)  
**作者**：Lanbo Lin, Jiayao Liu, Tianyuan Yang, Li Cai, Yuanwu Xu, Lei Wei, Sicong Xie, Guannan Zhang  

**一句话要点**：提出JADE框架以解决开放专业任务中评估的严谨性与灵活性矛盾

**关键词**：开放专业任务评估, 专家知识编码, 动态声明级评估, 证据依赖门控, 评估稳定性, 跨领域迁移

## 3 点简述
- 核心问题：开放专业任务评估面临静态标准与动态响应策略的冲突，现有方法在严谨性和适应性上存在不足
- 方法要点：JADE采用双层框架，结合专家知识编码和动态声明级评估，通过证据依赖门控提高评估稳定性
- 实验或效果：在BizBench上验证JADE提升评估稳定性并揭示关键失败模式，在医疗领域基准上展示有效迁移

## 摘要（原文）

> Evaluating agentic AI on open-ended professional tasks faces a fundamental dilemma between rigor and flexibility. Static rubrics provide rigorous, reproducible assessment but fail to accommodate diverse valid response strategies, while LLM-as-a-judge approaches adapt to individual responses yet suffer from instability and bias. Human experts address this dilemma by combining domain-grounded principles with dynamic, claim-level assessment. Inspired by this process, we propose JADE, a two-layer evaluation framework. Layer 1 encodes expert knowledge as a predefined set of evaluation skills, providing stable evaluation criteria. Layer 2 performs report-specific, claim-level evaluation to flexibly assess diverse reasoning strategies, with evidence-dependency gating to invalidate conclusions built on refuted claims. Experiments on BizBench show that JADE improves evaluation stability and reveals critical agent failure modes missed by holistic LLM-based evaluators. We further demonstrate strong alignment with expert-authored rubrics and effective transfer to a medical-domain benchmark, validating JADE across professional domains. Our code is publicly available at https://github.com/smiling-world/JADE.

