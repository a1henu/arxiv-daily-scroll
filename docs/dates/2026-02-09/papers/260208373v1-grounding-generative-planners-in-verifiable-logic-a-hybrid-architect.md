---
layout: default
title: Grounding Generative Planners in Verifiable Logic: A Hybrid Architecture for Trustworthy Embodied AI
---

# Grounding Generative Planners in Verifiable Logic: A Hybrid Architecture for Trustworthy Embodied AI
**arXiv**：[2602.08373v1](https://arxiv.org/abs/2602.08373) · [PDF](https://arxiv.org/pdf/2602.08373.pdf)  
**作者**：Feiyu Wu, Xu Zheng, Yue Qu, Zhuocheng Wang, Zicheng Feng, Hui Li  

**一句话要点**：提出可验证迭代精炼框架，通过逻辑导师与LLM协作实现可信实体AI规划

**关键词**：实体AI规划, 神经符号架构, 可验证安全, 逻辑导师, 知识获取管道, 计划修复

## 3 点简述
- 问题：LLM规划器缺乏形式化推理，无法保证实体AI部署的严格安全性
- 方法：引入神经符号架构，基于形式安全本体提供因果和教学反馈以修复计划
- 效果：在家庭安全任务中实现零危险行动率和最高目标条件率，平均仅需1.1次迭代

## 摘要（原文）

> Large Language Models (LLMs) show promise as planners for embodied AI, but their stochastic nature lacks formal reasoning, preventing strict safety guarantees for physical deployment. Current approaches often rely on unreliable LLMs for safety checks or simply reject unsafe plans without offering repairs. We introduce the Verifiable Iterative Refinement Framework (VIRF), a neuro-symbolic architecture that shifts the paradigm from passive safety gatekeeping to active collaboration. Our core contribution is a tutor-apprentice dialogue where a deterministic Logic Tutor, grounded in a formal safety ontology, provides causal and pedagogical feedback to an LLM planner. This enables intelligent plan repairs rather than mere avoidance. We also introduce a scalable knowledge acquisition pipeline that synthesizes safety knowledge bases from real-world documents, correcting blind spots in existing benchmarks. In challenging home safety tasks, VIRF achieves a perfect 0 percent Hazardous Action Rate (HAR) and a 77.3 percent Goal-Condition Rate (GCR), which is the highest among all baselines. It is highly efficient, requiring only 1.1 correction iterations on average. VIRF demonstrates a principled pathway toward building fundamentally trustworthy and verifiably safe embodied agents.

