---
layout: default
title: On Conformant Planning and Model-Checking of $\exists^*\forall^*$ Hyperproperties
---

# On Conformant Planning and Model-Checking of $\exists^*\forall^*$ Hyperproperties
**arXiv**：[2512.23324v1](https://arxiv.org/abs/2512.23324) · [PDF](https://arxiv.org/pdf/2512.23324.pdf)  
**作者**：Raven Beutner, Bernd Finkbeiner  

**一句话要点**：建立符合规划与∃*∀*超属性模型检测的等价关系

**关键词**：符合规划, 超属性, 模型检测, 归约, 验证, 规划

## 3 点简述
- 研究符合规划与超属性模型检测两个问题的内在联系
- 证明∃*∀*超属性模型检测可高效归约为符合规划问题
- 反之，每个符合规划问题本身也是一个超属性模型检测任务

## 摘要（原文）

> We study the connection of two problems within the planning and verification community: Conformant planning and model-checking of hyperproperties. Conformant planning is the task of finding a sequential plan that achieves a given objective independent of non-deterministic action effects during the plan's execution. Hyperproperties are system properties that relate multiple execution traces of a system and, e.g., capture information-flow and fairness policies. In this paper, we show that model-checking of $\exists^*\forall^*$ hyperproperties is closely related to the problem of computing a conformant plan. Firstly, we show that we can efficiently reduce a hyperproperty model-checking instance to a conformant planning instance, and prove that our encoding is sound and complete. Secondly, we establish the converse direction: Every conformant planning problem is, itself, a hyperproperty model-checking task.

