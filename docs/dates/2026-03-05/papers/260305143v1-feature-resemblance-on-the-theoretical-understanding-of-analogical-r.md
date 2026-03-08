---
layout: default
title: Feature Resemblance: On the Theoretical Understanding of Analogical Reasoning in Transformers
---

# Feature Resemblance: On the Theoretical Understanding of Analogical Reasoning in Transformers
**arXiv**：[2603.05143v1](https://arxiv.org/abs/2603.05143) · [PDF](https://arxiv.org/pdf/2603.05143.pdf)  
**作者**：Ruichen Xu, Wenjing Yan, Ying-Jun Angela Zhang  

**一句话要点**：提出特征相似性理论，解释Transformer中类比推理的机制与训练条件

**关键词**：类比推理, Transformer理论, 表示对齐, 训练课程, 特征相似性, 归纳推理

## 3 点简述
- 核心问题：隔离类比推理，分析其在Transformer中的涌现机制
- 方法要点：理论证明联合训练、顺序训练和两跳推理的数学条件
- 实验或效果：在1.5B参数架构上验证理论，展示表示几何如何塑造推理能力

## 摘要（原文）

> Understanding reasoning in large language models is complicated by evaluations that conflate multiple reasoning types. We isolate analogical reasoning (inferring shared properties between entities based on known similarities) and analyze its emergence in transformers. We theoretically prove three key results: (1) Joint training on similarity and attribution premises enables analogical reasoning through aligned representations; (2) Sequential training succeeds only when similarity structure is learned before specific attributes, revealing a necessary curriculum; (3) Two-hop reasoning ($a \to b, b \to c \implies a \to c$) reduces to analogical reasoning with identity bridges ($b = b$), which must appear explicitly in training data. These results reveal a unified mechanism: transformers encode entities with similar properties into similar representations, enabling property transfer through feature alignment. Experiments with architectures up to 1.5B parameters validate our theory and demonstrate how representational geometry shapes inductive reasoning capabilities.

