---
layout: default
title: CORE-Acu: Structured Reasoning Traces and Knowledge Graph Safety Verification for Acupuncture Clinical Decision Support
---

# CORE-Acu: Structured Reasoning Traces and Knowledge Graph Safety Verification for Acupuncture Clinical Decision Support
**arXiv**：[2603.08321v1](https://arxiv.org/abs/2603.08321) · [PDF](https://arxiv.org/pdf/2603.08321.pdf)  
**作者**：Liuyi Xu, Yun Guo, Ming Chen, Zihan Dun, Yining Qian, An-Yang Lu, Shuang Li, Lijun Liu  

**一句话要点**：提出CORE-Acu神经符号框架，结合结构化思维链与知识图谱安全验证，以解决针灸临床决策支持中LLM黑盒性与安全性问题。

**关键词**：针灸临床决策支持, 神经符号框架, 结构化思维链, 知识图谱安全验证, 术语校正损失

## 3 点简述
- 针灸临床决策支持中，LLM的黑盒推理和幻觉问题严重，需提升可解释性与安全性。
- 方法包括构建结构化推理轨迹数据集、知识图谱安全验证闭环系统，以及术语校正损失函数。
- 实验在1000例病例上验证，CORE-Acu实现零安全违规，优于GPT-4o的8.5%违规率。

## 摘要（原文）

> Large language models (LLMs) show significant potential for clinical decision support (CDS), yet their black-box nature -- characterized by untraceable reasoning and probabilistic hallucinations -- poses severe challenges in acupuncture, a field demanding rigorous interpretability and safety. To address this, we propose CORE-Acu, a neuro-symbolic framework for acupuncture clinical decision support that integrates Structured Chain-of-Thought (S-CoT) with knowledge graph (KG) safety verification. First, we construct the first acupuncture Structured Reasoning Trace dataset and a schema-constrained fine-tuning framework. By enforcing an explicit causal chain from pattern identification to treatment principles, treatment plans, and acupoint selection, we transform implicit Traditional Chinese Medicine (TCM) reasoning into interpretable generation constraints, mitigating the opacity of LLM-based CDS. Furthermore, we construct a TCM safety knowledge graph and establish a ``Generate--Verify--Revise'' closed-loop inference system based on a Symbolic Veto Mechanism, employing deterministic rules to intercept hallucinations and enforce hard safety boundaries. Finally, we introduce the Lexicon-Matched Entity-Reweighted Loss (LMERL), which corrects terminology drift caused by the frequency--importance mismatch in general optimization by adaptively amplifying gradient contributions of high-risk entities during fine-tuning. Experiments on 1,000 held-out cases demonstrate CORE-Acu's superior entity fidelity and reasoning quality. Crucially, CORE-Acu achieved 0/1,000 observed safety violations (95\% CI: 0--0.37\%), whereas GPT-4o exhibited an 8.5\% violation rate under identical rules. These results establish CORE-Acu as a robust neuro-symbolic framework for acupuncture clinical decision support, guaranteeing both reasoning auditability and strict safety compliance.

