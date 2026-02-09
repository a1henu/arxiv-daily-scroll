---
layout: default
title: Wild Guesses and Mild Guesses in Active Concept Learning
---

# Wild Guesses and Mild Guesses in Active Concept Learning
**arXiv**：[2602.06818v1](https://arxiv.org/abs/2602.06818) · [PDF](https://arxiv.org/pdf/2602.06818.pdf)  
**作者**：Anirudh Chari, Neil Pattanaik  

**一句话要点**：提出神经符号贝叶斯学习器，分析主动概念学习中理性策略与人类策略的权衡

**关键词**：主动概念学习, 神经符号学习, 贝叶斯推理, 大语言模型, 查询策略, 认知偏差

## 3 点简述
- 研究主动概念学习中查询信息性与假设稳定性的权衡问题
- 采用LLM生成可执行程序作为假设，通过贝叶斯更新重加权
- 在Number Game任务中比较EIG与PTS策略，揭示支持不匹配陷阱

## 摘要（原文）

> Human concept learning is typically active: learners choose which instances to query or test in order to reduce uncertainty about an underlying rule or category. Active concept learning must balance informativeness of queries against the stability of the learner that generates and scores hypotheses. We study this trade-off in a neuro-symbolic Bayesian learner whose hypotheses are executable programs proposed by a large language model (LLM) and reweighted by Bayesian updating. We compare a Rational Active Learner that selects queries to maximize approximate expected information gain (EIG) and the human-like Positive Test Strategy (PTS) that queries instances predicted to be positive under the current best hypothesis. Across concept-learning tasks in the classic Number Game, EIG is effective when falsification is necessary (e.g., compound or exception-laden rules), but underperforms on simple concepts. We trace this failure to a support mismatch between the EIG policy and the LLM proposal distribution: highly diagnostic boundary queries drive the posterior toward regions where the generator produces invalid or overly specific programs, yielding a support-mismatch trap in the particle approximation. PTS is information-suboptimal but tends to maintain proposal validity by selecting "safe" queries, leading to faster convergence on simple rules. Our results suggest that "confirmation bias" may not be a cognitive error, but rather a rational adaptation for maintaining tractable inference in the sparse, open-ended hypothesis spaces characteristic of human thought.

