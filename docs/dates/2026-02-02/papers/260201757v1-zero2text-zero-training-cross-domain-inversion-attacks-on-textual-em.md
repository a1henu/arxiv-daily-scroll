---
layout: default
title: Zero2Text: Zero-Training Cross-Domain Inversion Attacks on Textual Embeddings
---

# Zero2Text: Zero-Training Cross-Domain Inversion Attacks on Textual Embeddings
**arXiv**：[2602.01757v1](https://arxiv.org/abs/2602.01757) · [PDF](https://arxiv.org/pdf/2602.01757.pdf)  
**作者**：Doohyun Kim, Donghwa Kang, Kyungjae Lee, Hyeongboo Baek, Brent Byunghoon Kang  

**一句话要点**：提出Zero2Text框架，通过递归在线对齐实现零训练跨域嵌入反转攻击，解决黑盒场景下隐私风险问题。

**关键词**：嵌入反转攻击, 跨域隐私风险, 零训练框架, 递归在线对齐, 向量数据库安全, 黑盒攻击

## 3 点简述
- 核心问题：向量数据库在检索增强生成中引入隐私风险，现有方法在计算成本或数据可访问性上受限，难以应对严格黑盒和跨域设置。
- 方法要点：基于递归在线对齐，结合LLM先验和动态岭回归机制，无需训练数据，迭代对齐生成与目标嵌入。
- 实验或效果：在MS MARCO等基准上验证，相比基线显著提升ROUGE-L和BLEU-2分数，未知域句子恢复效果突出，标准防御如差分隐私无效。

## 摘要（原文）

> The proliferation of retrieval-augmented generation (RAG) has established vector databases as critical infrastructure, yet they introduce severe privacy risks via embedding inversion attacks. Existing paradigms face a fundamental trade-off: optimization-based methods require computationally prohibitive queries, while alignment-based approaches hinge on the unrealistic assumption of accessible in-domain training data. These constraints render them ineffective in strict black-box and cross-domain settings. To dismantle these barriers, we introduce Zero2Text, a novel training-free framework based on recursive online alignment. Unlike methods relying on static datasets, Zero2Text synergizes LLM priors with a dynamic ridge regression mechanism to iteratively align generation to the target embedding on-the-fly. We further demonstrate that standard defenses, such as differential privacy, fail to effectively mitigate this adaptive threat. Extensive experiments across diverse benchmarks validate Zero2Text; notably, on MS MARCO against the OpenAI victim model, it achieves 1.8x higher ROUGE-L and 6.4x higher BLEU-2 scores compared to baselines, recovering sentences from unknown domains without a single leaked data pair.

