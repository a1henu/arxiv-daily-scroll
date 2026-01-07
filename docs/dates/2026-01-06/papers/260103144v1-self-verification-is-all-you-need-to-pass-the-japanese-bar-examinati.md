---
layout: default
title: Self-Verification is All You Need To Pass The Japanese Bar Examination
---

# Self-Verification is All You Need To Pass The Japanese Bar Examination
**arXiv**：[2601.03144v1](https://arxiv.org/abs/2601.03144) · [PDF](https://arxiv.org/pdf/2601.03144.pdf)  
**作者**：Andrew Shin  

**一句话要点**：提出自验证模型以通过日本司法考试，首次在原始格式下超越及格线。

**关键词**：自验证模型, 日本司法考试, 格式忠实监督, 法律推理, 大语言模型评估

## 3 点简述
- 核心问题：LLMs在专业结构化考试中可靠性能不足，日本司法考试需高级法律推理和严格格式遵循。
- 方法要点：构建忠实复制考试格式的数据集，训练自验证模型，强调格式忠实监督和一致性验证。
- 实验或效果：模型在原始考试评分下超越及格分数，优于多智能体推理和分解监督等替代策略。

## 摘要（原文）

> Despite rapid advances in large language models (LLMs), achieving reliable performance on highly professional and structured examinations remains a significant challenge. The Japanese bar examination is a particularly demanding benchmark, requiring not only advanced legal reasoning but also strict adherence to complex answer formats that involve joint evaluation of multiple propositions. While recent studies have reported improvements by decomposing such questions into simpler true--false judgments, these approaches have not been systematically evaluated under the original exam format and scoring scheme, leaving open the question of whether they truly capture exam-level competence. In this paper, we present a self-verification model trained on a newly constructed dataset that faithfully replicates the authentic format and evaluation scale of the exam. Our model is able to exceed the official passing score when evaluated on the actual exam scale, marking the first demonstration, to our knowledge, of an LLM passing the Japanese bar examination without altering its original question structure or scoring rules. We further conduct extensive comparisons with alternative strategies, including multi-agent inference and decomposition-based supervision, and find that these methods fail to achieve comparable performance. Our results highlight the importance of format-faithful supervision and consistency verification, and suggest that carefully designed single-model approaches can outperform more complex systems in high-stakes professional reasoning tasks. Our dataset and codes are publicly available.

