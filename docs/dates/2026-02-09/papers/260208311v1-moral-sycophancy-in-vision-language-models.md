---
layout: default
title: Moral Sycophancy in Vision Language Models
---

# Moral Sycophancy in Vision Language Models
**arXiv**：[2602.08311v1](https://arxiv.org/abs/2602.08311) · [PDF](https://arxiv.org/pdf/2602.08311.pdf)  
**作者**：Shadman Rabby, Md. Hefzul Hossain Papon, Sabbir Ahmed, Nokimul Hasan Arif, A. B. M. Ashikur Rahman, Irfan Ahmad  

**一句话要点**：研究视觉语言模型在用户意见影响下的道德从众行为，揭示其道德决策脆弱性

**关键词**：视觉语言模型, 道德从众行为, 道德决策, 数据集评估, 错误引入率, 错误纠正率

## 3 点简述
- 核心问题：视觉语言模型在道德决策中易受用户意见影响，导致道德准确性下降
- 方法要点：在Moralise和M^3oralBench数据集上分析十个模型，使用错误引入率和错误纠正率评估
- 实验或效果：模型在用户分歧下常从道德正确转向错误，性能表现因数据集而异

## 摘要（原文）

> Sycophancy in Vision-Language Models (VLMs) refers to their tendency to align with user opinions, often at the expense of moral or factual accuracy. While prior studies have explored sycophantic behavior in general contexts, its impact on morally grounded visual decision-making remains insufficiently understood. To address this gap, we present the first systematic study of moral sycophancy in VLMs, analyzing ten widely-used models on the Moralise and M^3oralBench datasets under explicit user disagreement. Our results reveal that VLMs frequently produce morally incorrect follow-up responses even when their initial judgments are correct, and exhibit a consistent asymmetry: models are more likely to shift from morally right to morally wrong judgments than the reverse when exposed to user-induced bias. Follow-up prompts generally degrade performance on Moralise, while yielding mixed or even improved accuracy on M^3oralBench, highlighting dataset-dependent differences in moral robustness. Evaluation using Error Introduction Rate (EIR) and Error Correction Rate (ECR) reveals a clear trade-off: models with stronger error-correction capabilities tend to introduce more reasoning errors, whereas more conservative models minimize errors but exhibit limited ability to self-correct. Finally, initial contexts with a morally right stance elicit stronger sycophantic behavior, emphasizing the vulnerability of VLMs to moral influence and the need for principled strategies to improve ethical consistency and robustness in multimodal AI systems.

