---
layout: default
title: RACA: Representation-Aware Coverage Criteria for LLM Safety Testing
---

# RACA: Representation-Aware Coverage Criteria for LLM Safety Testing
**arXiv**：[2602.02280v1](https://arxiv.org/abs/2602.02280) · [PDF](https://arxiv.org/pdf/2602.02280.pdf)  
**作者**：Zeming Wei, Zhixin Zhang, Chengcan Wu, Yihao Zhang, Xiaokun Luan, Meng Sun  

**一句话要点**：提出RACA覆盖准则以解决LLM安全测试中缺乏系统性评估标准的问题

**关键词**：LLM安全测试, 覆盖准则, 表示工程, 越狱攻击, 测试评估

## 3 点简述
- 核心问题：LLM安全测试依赖静态数据集，缺乏评估测试质量和充分性的系统标准
- 方法要点：利用表示工程聚焦安全关键概念，通过三阶段框架计算覆盖结果
- 实验或效果：RACA能识别高质量越狱提示，优于传统神经元级准则，并展示实际应用

## 摘要（原文）

> Recent advancements in LLMs have led to significant breakthroughs in various AI applications. However, their sophisticated capabilities also introduce severe safety concerns, particularly the generation of harmful content through jailbreak attacks. Current safety testing for LLMs often relies on static datasets and lacks systematic criteria to evaluate the quality and adequacy of these tests. While coverage criteria have been effective for smaller neural networks, they are not directly applicable to LLMs due to scalability issues and differing objectives. To address these challenges, this paper introduces RACA, a novel set of coverage criteria specifically designed for LLM safety testing. RACA leverages representation engineering to focus on safety-critical concepts within LLMs, thereby reducing dimensionality and filtering out irrelevant information. The framework operates in three stages: first, it identifies safety-critical representations using a small, expert-curated calibration set of jailbreak prompts. Second, it calculates conceptual activation scores for a given test suite based on these representations. Finally, it computes coverage results using six sub-criteria that assess both individual and compositional safety concepts. We conduct comprehensive experiments to validate RACA's effectiveness, applicability, and generalization, where the results demonstrate that RACA successfully identifies high-quality jailbreak prompts and is superior to traditional neuron-level criteria. We also showcase its practical application in real-world scenarios, such as test set prioritization and attack prompt sampling. Furthermore, our findings confirm RACA's generalization to various scenarios and its robustness across various configurations. Overall, RACA provides a new framework for evaluating the safety of LLMs, contributing a valuable technique to the field of testing for AI.

