---
layout: default
title: AgentsEval: Clinically Faithful Evaluation of Medical Imaging Reports via Multi-Agent Reasoning
---

# AgentsEval: Clinically Faithful Evaluation of Medical Imaging Reports via Multi-Agent Reasoning
**arXiv**：[2601.16685v1](https://arxiv.org/abs/2601.16685) · [PDF](https://arxiv.org/pdf/2601.16685.pdf)  
**作者**：Suzhong Fu, Jingqi Dong, Xuan Ding, Rui Sun, Yiming Yang, Shuguang Cui, Zhen Li  

**一句话要点**：提出AgentsEval多智能体推理框架，以解决医学影像报告自动生成的临床正确性评估难题。

**关键词**：医学影像报告评估, 多智能体推理, 临床正确性, 结构化诊断逻辑, 可解释评估, 大语言模型集成

## 3 点简述
- 核心问题：现有评估方法难以捕捉放射学解释的结构化诊断逻辑，导致临床相关性不足。
- 方法要点：通过多智能体流推理模拟放射科医生协作工作流，包括标准定义、证据提取、对齐和一致性评分步骤。
- 实验或效果：在基于扰动的多领域基准测试中，AgentsEval提供临床对齐、语义忠实且可解释的评估，对扰动保持稳健。

## 摘要（原文）

> Evaluating the clinical correctness and reasoning fidelity of automatically generated medical imaging reports remains a critical yet unresolved challenge. Existing evaluation methods often fail to capture the structured diagnostic logic that underlies radiological interpretation, resulting in unreliable judgments and limited clinical relevance. We introduce AgentsEval, a multi-agent stream reasoning framework that emulates the collaborative diagnostic workflow of radiologists. By dividing the evaluation process into interpretable steps including criteria definition, evidence extraction, alignment, and consistency scoring, AgentsEval provides explicit reasoning traces and structured clinical feedback. We also construct a multi-domain perturbation-based benchmark covering five medical report datasets with diverse imaging modalities and controlled semantic variations. Experimental results demonstrate that AgentsEval delivers clinically aligned, semantically faithful, and interpretable evaluations that remain robust under paraphrastic, semantic, and stylistic perturbations. This framework represents a step toward transparent and clinically grounded assessment of medical report generation systems, fostering trustworthy integration of large language models into clinical practice.

