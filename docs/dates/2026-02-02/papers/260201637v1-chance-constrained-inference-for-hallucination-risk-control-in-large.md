---
layout: default
title: Chance-Constrained Inference for Hallucination Risk Control in Large Language Models
---

# Chance-Constrained Inference for Hallucination Risk Control in Large Language Models
**arXiv**：[2602.01637v1](https://arxiv.org/abs/2602.01637) · [PDF](https://arxiv.org/pdf/2602.01637.pdf)  
**作者**：Sreenivasan Mohandas  

**一句话要点**：提出机会约束推理以控制大语言模型在重复使用中的幻觉风险

**关键词**：大语言模型, 幻觉控制, 机会约束推理, 风险保证, 序列推理, 问答系统

## 3 点简述
- 核心问题：现有方法降低平均错误率，但无法控制重复使用下幻觉的频率。
- 方法要点：将推理建模为部署时风险控制问题，引入机会约束直接限制接受生成中的幻觉概率。
- 实验或效果：在自然问题启发和多跳问答上验证可靠风险控制，早期检测不可行输入，安全组合使用。

## 摘要（原文）

> Large language models generate outputs stochastically and may produce fluent but invalid responses, including factual hallucinations. Existing mitigation strategies reduce average error rates but do not provide explicit control over the \emph{frequency} of such failures under repeated use. We formulate inference as a deployment-time risk control problem and introduce \emph{chance-constrained inference}, which directly bounds the probability of hallucinations among accepted generations. Hallucinations are modeled as stochastic constraint violations, and we show that confidence-based selective prediction does not, in general, imply probabilistic risk guarantees. To enforce chance constraints efficiently, we propose a sequential, anytime-valid inference procedure that adaptively certifies feasibility or infeasibility using finite samples, avoiding conservative fixed-sample bounds. Experiments on questions inspired by NaturalQuestions and controlled multi-hop question answering demonstrate reliable risk control, early detection of intrinsically infeasible inputs, and safe composition under repeated use, while confidence-based baselines fail to provide consistent guarantees.

