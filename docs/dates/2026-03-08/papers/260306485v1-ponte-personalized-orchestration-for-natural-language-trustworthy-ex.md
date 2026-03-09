---
layout: default
title: PONTE: Personalized Orchestration for Natural Language Trustworthy Explanations
---

# PONTE: Personalized Orchestration for Natural Language Trustworthy Explanations
**arXiv**：[2603.06485v1](https://arxiv.org/abs/2603.06485) · [PDF](https://arxiv.org/pdf/2603.06485.pdf)  
**作者**：Vittoria Vineis, Matteo Silvestri, Lorenzo Antonelli, Filippo Betello, Gabriele Tolomei  

**一句话要点**：提出PONTE框架以解决可解释AI中个性化与可信度不足的问题

**关键词**：可解释人工智能, 个性化解释, 闭环验证, 自然语言生成, 用户反馈, 可信度评估

## 3 点简述
- 核心问题：现有可解释AI方法忽视用户差异，且大语言模型生成解释时存在不忠实和幻觉问题
- 方法要点：PONTE通过闭环验证与适应过程，结合偏好建模、条件生成和验证模块实现个性化可信解释
- 实验或效果：在医疗和金融领域评估显示，验证-精炼循环显著提升解释的完整性和风格对齐，用户研究证实偏好感知与质量提升

## 摘要（原文）

> Explainable Artificial Intelligence (XAI) seeks to enhance the transparency and accountability of machine learning systems, yet most methods follow a one-size-fits-all paradigm that neglects user differences in expertise, goals, and cognitive needs. Although Large Language Models can translate technical explanations into natural language, they introduce challenges related to faithfulness and hallucinations. To address these challenges, we present PONTE (Personalized Orchestration for Natural language Trustworthy Explanations), a human-in-the-loop framework for adaptive and reliable XAI narratives. PONTE models personalization as a closed-loop validation and adaptation process rather than prompt engineering. It combines: (i) a low-dimensional preference model capturing stylistic requirements; (ii) a preference-conditioned generator grounded in structured XAI artifacts; and (iii) verification modules enforcing numerical faithfulness, informational completeness, and stylistic alignment, optionally supported by retrieval-grounded argumentation. User feedback iteratively updates the preference state, enabling quick personalization. Automatic and human evaluations across healthcare and finance domains show that the verification-refinement loop substantially improves completeness and stylistic alignment over validation-free generation. Human studies further confirm strong agreement between intended preference vectors and perceived style, robustness to generation stochasticity, and consistently positive quality assessments.

