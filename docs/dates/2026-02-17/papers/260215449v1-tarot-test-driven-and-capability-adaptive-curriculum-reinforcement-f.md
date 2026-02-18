---
layout: default
title: TAROT: Test-driven and Capability-adaptive Curriculum Reinforcement Fine-tuning for Code Generation with Large Language Models
---

# TAROT: Test-driven and Capability-adaptive Curriculum Reinforcement Fine-tuning for Code Generation with Large Language Models
**arXiv**：[2602.15449v1](https://arxiv.org/abs/2602.15449) · [PDF](https://arxiv.org/pdf/2602.15449.pdf)  
**作者**：Chansung Park, Juyong Jiang, Fan Wang, Sayak Paul, Jiasi Shen, Jing Tang, Jianguo Li  

**一句话要点**：提出TAROT方法，通过测试驱动和能力自适应课程强化微调，提升大语言模型代码生成的功能正确性和鲁棒性。

**关键词**：代码生成, 强化微调, 课程学习, 大语言模型, 测试驱动

## 3 点简述
- 核心问题：现有强化微调方法忽视测试用例的异质难度和粒度，导致奖励信号分布不均和训练梯度偏差。
- 方法要点：TAROT为每个问题构建四层测试套件，并基于模型能力自适应选择课程策略，实现稳定优化。
- 实验或效果：实验表明，课程设计需适配模型能力，TAROT能一致改进生成代码的功能正确性和鲁棒性。

## 摘要（原文）

> Large Language Models (LLMs) are changing the coding paradigm, known as vibe coding, yet synthesizing algorithmically sophisticated and robust code still remains a critical challenge. Incentivizing the deep reasoning capabilities of LLMs is essential to overcoming this hurdle. Reinforcement Fine-Tuning (RFT) has emerged as a promising strategy to address this need. However, most existing approaches overlook the heterogeneous difficulty and granularity inherent in test cases, leading to an imbalanced distribution of reward signals and consequently biased gradient updates during training. To address this, we propose Test-driven and cApability-adaptive cuRriculum reinfOrcement fine-Tuning (TAROT). TAROT systematically constructs, for each problem, a four-tier test suite (basic, intermediate, complex, edge), providing a controlled difficulty landscape for curriculum design and evaluation. Crucially, TAROT decouples curriculum progression from raw reward scores, enabling capability-conditioned evaluation and principled selection from a portfolio of curriculum policies rather than incidental test-case difficulty composition. This design fosters stable optimization and more efficient competency acquisition. Extensive experimental results reveal that the optimal curriculum for RFT in code generation is closely tied to a model's inherent capability, with less capable models achieving greater gains with an easy-to-hard progression, whereas more competent models excel under a hard-first curriculum. TAROT provides a reproducible method that adaptively tailors curriculum design to a model's capability, thereby consistently improving the functional correctness and robustness of the generated code. All code and data are released to foster reproducibility and advance community research at https://github.com/deep-diver/TAROT.

