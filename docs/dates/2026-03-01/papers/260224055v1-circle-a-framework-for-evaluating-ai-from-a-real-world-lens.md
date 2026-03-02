---
layout: default
title: CIRCLE: A Framework for Evaluating AI from a Real-World Lens
---

# CIRCLE: A Framework for Evaluating AI from a Real-World Lens
**arXiv**：[2602.24055v1](https://arxiv.org/abs/2602.24055) · [PDF](https://arxiv.org/pdf/2602.24055.pdf)  
**作者**：Reva Schwartz, Carina Westling, Morgan Briggs, Marzieh Fadaee, Isar Nejadgholi, Matthew Holmes, Fariza Rashid, Maya Carlyle, Afaf Taïk, Kyra Wilson, Peter Douglas, Theodora Skeadas, Gabriella Waters, Rumman Chowdhury, Thiago Lacerda  

**一句话要点**：提出CIRCLE框架以解决AI模型性能指标与真实部署效果之间的差距

**关键词**：AI评估框架, 真实世界验证, 生命周期方法, TEVV操作化, 上下文敏感指标, 系统性知识生成

## 3 点简述
- 核心问题：现有AI评估框架如MLOps和基准测试难以捕捉真实世界用户变异和约束下的AI行为，导致决策者缺乏系统性证据。
- 方法要点：CIRCLE是一个六阶段、基于生命周期的框架，将TEVV中的验证阶段操作化，通过结构化协议将上下文敏感的定性洞察与可扩展的定量指标连接。
- 实验或效果：整合现场测试、红队演练和纵向研究等方法，生成跨站点可比且对本地上下文敏感的系统性知识，支持基于下游实际效果的治理。

## 摘要（原文）

> This paper proposes CIRCLE, a six-stage, lifecycle-based framework to bridge the reality gap between model-centric performance metrics and AI's materialized outcomes in deployment. While existing frameworks like MLOps focus on system stability and benchmarks measure abstract capabilities, decision-makers outside the AI stack lack systematic evidence about the behavior of AI technologies under real-world user variability and constraints. CIRCLE operationalizes the Validation phase of TEVV (Test, Evaluation, Verification, and Validation) by formalizing the translation of stakeholder concerns outside the stack into measurable signals. Unlike participatory design, which often remains localized, or algorithmic audits, which are often retrospective, CIRCLE provides a structured, prospective protocol for linking context-sensitive qualitative insights to scalable quantitative metrics. By integrating methods such as field testing, red teaming, and longitudinal studies into a coordinated pipeline, CIRCLE produces systematic knowledge: evidence that is comparable across sites yet sensitive to local context. This can enable governance based on materialized downstream effects rather than theoretical capabilities.

