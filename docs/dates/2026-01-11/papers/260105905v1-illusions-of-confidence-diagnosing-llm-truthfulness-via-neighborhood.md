---
layout: default
title: Illusions of Confidence? Diagnosing LLM Truthfulness via Neighborhood Consistency
---

# Illusions of Confidence? Diagnosing LLM Truthfulness via Neighborhood Consistency
**arXiv**：[2601.05905v1](https://arxiv.org/abs/2601.05905) · [PDF](https://arxiv.org/pdf/2601.05905.pdf)  
**作者**：Haoming Xu, Ningyuan Zhao, Yunzhi Yao, Weihong Xu, Hongru Wang, Xinle Deng, Shumin Deng, Jeff Z. Pan, Huajun Chen, Ningyu Zhang  

**一句话要点**：提出邻居一致性信念以评估大语言模型在上下文扰动下的信念鲁棒性。

**关键词**：大语言模型, 信念鲁棒性, 邻居一致性, 认知压力测试, 结构感知训练

## 3 点简述
- 核心问题：现有评估依赖点状置信度，可能掩盖信念脆弱性，需在上下文干扰下保持真实信念。
- 方法要点：引入邻居一致性信念作为结构度量，通过概念邻域评估响应一致性，并设计认知压力测试协议。
- 实验或效果：实验显示高邻居一致性信念数据更抗干扰，结构感知训练减少长尾知识脆弱性约30%。

## 摘要（原文）

> As Large Language Models (LLMs) are increasingly deployed in real-world settings, correctness alone is insufficient. Reliable deployment requires maintaining truthful beliefs under contextual perturbations. Existing evaluations largely rely on point-wise confidence like Self-Consistency, which can mask brittle belief. We show that even facts answered with perfect self-consistency can rapidly collapse under mild contextual interference. To address this gap, we propose Neighbor-Consistency Belief (NCB), a structural measure of belief robustness that evaluates response coherence across a conceptual neighborhood. To validate the efficiency of NCB, we introduce a new cognitive stress-testing protocol that probes outputs stability under contextual interference. Experiments across multiple LLMs show that the performance of high-NCB data is relatively more resistant to interference. Finally, we present Structure-Aware Training (SAT), which optimizes context-invariant belief structure and reduces long-tail knowledge brittleness by approximately 30%. Code will be available at https://github.com/zjunlp/belief.

