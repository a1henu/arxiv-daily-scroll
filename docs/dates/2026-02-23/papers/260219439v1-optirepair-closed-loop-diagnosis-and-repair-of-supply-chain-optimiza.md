---
layout: default
title: OptiRepair: Closed-Loop Diagnosis and Repair of Supply Chain Optimization Models with LLM Agents
---

# OptiRepair: Closed-Loop Diagnosis and Repair of Supply Chain Optimization Models with LLM Agents
**arXiv**：[2602.19439v1](https://arxiv.org/abs/2602.19439) · [PDF](https://arxiv.org/pdf/2602.19439.pdf)  
**作者**：Ruicheng Ao, David Simchi-Levi, Xinshang Wang  

**一句话要点**：提出OptiRepair框架，利用LLM代理闭环诊断与修复供应链优化模型的不可行性问题

**关键词**：供应链优化, 模型修复, LLM代理, 不可行性诊断, 自学习推理, 库存理论

## 3 点简述
- 核心问题：供应链优化模型常因建模错误不可行，诊断修复需稀缺运筹学专业知识，AI代理能力未知
- 方法要点：分两阶段处理，通用可行性修复与基于库存理论的领域特定验证，训练自学习推理模型
- 实验或效果：在976个多级供应链问题上测试，训练模型达到81.7%理性恢复率，显著优于API模型

## 摘要（原文）

> Problem Definition. Supply chain optimization models frequently become infeasible because of modeling errors. Diagnosis and repair require scarce OR expertise: analysts must interpret solver diagnostics, trace root causes across echelons, and fix formulations without sacrificing operational soundness. Whether AI agents can perform this task remains untested.
>   Methodology/Results. OptiRepair splits this task into a domain-agnostic feasibility phase (iterative IIS-guided repair of any LP) and a domain-specific validation phase (five rationality checks grounded in inventory theory). We test 22 API models from 7 families on 976 multi-echelon supply chain problems and train two 8B-parameter models using self-taught reasoning with solver-verified rewards. The trained models reach 81.7% Rational Recovery Rate (RRR) -- the fraction of problems resolved to both feasibility and operational rationality -- versus 42.2% for the best API model and 21.3% on average. The gap concentrates in Phase 1 repair: API models average 27.6% recovery rate versus 97.2% for trained models.
>   Managerial Implications. Two gaps separate current AI from reliable model repair: solver interaction (API models restore only 27.6% of infeasible formulations) and operational rationale (roughly one in four feasible repairs violate supply chain theory). Each requires a different intervention: solver interaction responds to targeted training; operational rationale requires explicit specification as solver-verifiable checks. For organizations adopting AI in operational planning, formalizing what "rational" means in their context is the higher-return investment.

