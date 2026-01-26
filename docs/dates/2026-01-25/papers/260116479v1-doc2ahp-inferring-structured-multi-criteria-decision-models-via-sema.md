---
layout: default
title: Doc2AHP: Inferring Structured Multi-Criteria Decision Models via Semantic Trees with LLMs
---

# Doc2AHP: Inferring Structured Multi-Criteria Decision Models via Semantic Trees with LLMs
**arXiv**：[2601.16479v1](https://arxiv.org/abs/2601.16479) · [PDF](https://arxiv.org/pdf/2601.16479.pdf)  
**作者**：Hongjia Wu, Shuai Zhou, Hongxin Zhang, Wei Chen  

**一句话要点**：提出Doc2AHP框架，利用LLMs从文档中自动构建结构化多准则决策模型

**关键词**：结构化推理, 多准则决策, 大语言模型, 层次分析法, 文档理解, 一致性优化

## 3 点简述
- 核心问题：LLMs在复杂决策任务中结构一致性和推理可靠性不足，而传统AHP方法依赖专家知识，存在可扩展性瓶颈。
- 方法要点：基于AHP原则引导LLMs进行约束搜索，结合多智能体权重机制和自适应一致性优化，确保逻辑和数值一致性。
- 实验或效果：Doc2AHP使非专家用户能从头构建高质量决策模型，在逻辑完整性和下游任务准确性上显著优于直接生成基线。

## 摘要（原文）

> While Large Language Models (LLMs) demonstrate remarkable proficiency in semantic understanding, they often struggle to ensure structural consistency and reasoning reliability in complex decision-making tasks that demand rigorous logic. Although classical decision theories, such as the Analytic Hierarchy Process (AHP), offer systematic rational frameworks, their construction relies heavily on labor-intensive domain expertise, creating an "expert bottleneck" that hinders scalability in general scenarios. To bridge the gap between the generalization capabilities of LLMs and the rigor of decision theory, we propose Doc2AHP, a novel structured inference framework guided by AHP principles. Eliminating the need for extensive annotated data or manual intervention, our approach leverages the structural principles of AHP as constraints to direct the LLM in a constrained search within the unstructured document space, thereby enforcing the logical entailment between parent and child nodes. Furthermore, we introduce a multi-agent weighting mechanism coupled with an adaptive consistency optimization strategy to ensure the numerical consistency of weight allocation. Empirical results demonstrate that Doc2AHP not only empowers non-expert users to construct high-quality decision models from scratch but also significantly outperforms direct generative baselines in both logical completeness and downstream task accuracy.

