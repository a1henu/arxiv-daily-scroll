---
layout: default
title: AMAP Agentic Planning Technical Report
---

# AMAP Agentic Planning Technical Report
**arXiv**：[2512.24957v1](https://arxiv.org/abs/2512.24957) · [PDF](https://arxiv.org/pdf/2512.24957.pdf)  
**作者**：Yulan Hu, Xiangwen Zhang, Sheng Ouyang, Hao Yi, Lu Xu, Qinglin Lang, Lide Tan, Xiang Cheng, Tianchen Ye, Zhicong Li, Ge Chen, Wenjin Yang, Zheng Pan, Shaopan Xiong, Siran Yang, Ju Huang, Yan Zhang, Jiamang Wang, Yong Liu, Yinfeng Huang, Tucheng Lin, Xin Li, Ning Guo  

**一句话要点**：提出STAgent代理大语言模型，用于时空场景下的复杂任务解决，如兴趣点发现和行程规划。

**关键词**：时空理解, 代理大语言模型, 工具交互, 分层数据筛选, 级联训练

## 3 点简述
- 核心问题：针对时空理解，设计代理模型以处理约束性兴趣点发现和行程规划等复杂任务。
- 方法要点：通过稳定工具环境、分层数据筛选和级联训练方法，增强模型在时空场景中的交互与推理能力。
- 实验或效果：在TravelBench上表现良好，同时保持广泛通用基准上的能力，验证了代理模型的有效性。

## 摘要（原文）

> We present STAgent, an agentic large language model tailored for spatio-temporal understanding, designed to solve complex tasks such as constrained point-of-interest discovery and itinerary planning. STAgent is a specialized model capable of interacting with ten distinct tools within spatio-temporal scenarios, enabling it to explore, verify, and refine intermediate steps during complex reasoning. Notably, STAgent effectively preserves its general capabilities. We empower STAgent with these capabilities through three key contributions: (1) a stable tool environment that supports over ten domain-specific tools, enabling asynchronous rollout and training; (2) a hierarchical data curation framework that identifies high-quality data like a needle in a haystack, curating high-quality queries with a filter ratio of 1:10,000, emphasizing both diversity and difficulty; and (3) a cascaded training recipe that starts with a seed SFT stage acting as a guardian to measure query difficulty, followed by a second SFT stage fine-tuned on queries with high certainty, and an ultimate RL stage that leverages data of low certainty. Initialized with Qwen3-30B-A3B to establish a strong SFT foundation and leverage insights into sample difficulty, STAgent yields promising performance on TravelBench while maintaining its general capabilities across a wide range of general benchmarks, thereby demonstrating the effectiveness of our proposed agentic model.

