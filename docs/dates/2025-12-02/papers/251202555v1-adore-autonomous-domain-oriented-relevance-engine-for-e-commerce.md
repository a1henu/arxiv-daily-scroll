---
layout: default
title: ADORE: Autonomous Domain-Oriented Relevance Engine for E-commerce
---

# ADORE: Autonomous Domain-Oriented Relevance Engine for E-commerce
**arXiv**：[2512.02555v1](https://arxiv.org/abs/2512.02555) · [PDF](https://arxiv.org/pdf/2512.02555.pdf)  
**作者**：Zheng Fang, Donghao Xie, Ming Pang, Chunyuan Yuan, Xue Jiang, Changping Peng, Zhangang Lin, Zheng Luo  

**一句话要点**：提出ADORE框架以解决电商搜索中语义鸿沟和数据稀缺问题，实现自动化标注与推理增强。

**关键词**：电商搜索, 相关性建模, 知识蒸馏, 自动化标注, 对抗生成, 认知对齐

## 3 点简述
- 核心问题：电商搜索相关性建模面临术语匹配方法的语义鸿沟和神经模型对领域特定硬样本的依赖。
- 方法要点：结合规则感知相关性判别、错误类型感知数据合成和关键属性增强知识蒸馏，自动化生成训练数据。
- 实验或效果：通过大规模实验和在线A/B测试验证了ADORE的有效性，提升了资源效率和认知对齐。

## 摘要（原文）

> Relevance modeling in e-commerce search remains challenged by semantic gaps in term-matching methods (e.g., BM25) and neural models' reliance on the scarcity of domain-specific hard samples. We propose ADORE, a self-sustaining framework that synergizes three innovations: (1) A Rule-aware Relevance Discrimination module, where a Chain-of-Thought LLM generates intent-aligned training data, refined via Kahneman-Tversky Optimization (KTO) to align with user behavior; (2) An Error-type-aware Data Synthesis module that auto-generates adversarial examples to harden robustness; and (3) A Key-attribute-enhanced Knowledge Distillation module that injects domain-specific attribute hierarchies into a deployable student model. ADORE automates annotation, adversarial generation, and distillation, overcoming data scarcity while enhancing reasoning. Large-scale experiments and online A/B testing verify the effectiveness of ADORE. The framework establishes a new paradigm for resource-efficient, cognitively aligned relevance modeling in industrial applications.

