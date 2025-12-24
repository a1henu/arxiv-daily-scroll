---
layout: default
title: KnowVal: A Knowledge-Augmented and Value-Guided Autonomous Driving System
---

# KnowVal: A Knowledge-Augmented and Value-Guided Autonomous Driving System
**arXiv**：[2512.20299v1](https://arxiv.org/abs/2512.20299) · [PDF](https://arxiv.org/pdf/2512.20299.pdf)  
**作者**：Zhongyu Xia, Wenhao Chen, Yongtao Wang, Ming-Hsuan Yang  

**一句话要点**：提出KnowVal系统，通过知识增强与价值引导提升自动驾驶决策性能

**关键词**：自动驾驶系统, 知识图谱, 视觉-语言推理, 价值对齐, 轨迹评估

## 3 点简述
- 现有方法依赖数据驱动，难以捕捉复杂决策逻辑，导致性能受限
- 构建驾驶知识图谱并集成检索机制，实现视觉-语言推理与知识增强
- 在nuScenes和Bench2Drive上验证，显著降低碰撞率并达到先进水平

## 摘要（原文）

> Visual-language reasoning, driving knowledge, and value alignment are essential for advanced autonomous driving systems. However, existing approaches largely rely on data-driven learning, making it difficult to capture the complex logic underlying decision-making through imitation or limited reinforcement rewards. To address this, we propose KnowVal, a new autonomous driving system that enables visual-language reasoning through the synergistic integration of open-world perception and knowledge retrieval. Specifically, we construct a comprehensive driving knowledge graph that encodes traffic laws, defensive driving principles, and ethical norms, complemented by an efficient LLM-based retrieval mechanism tailored for driving scenarios. Furthermore, we develop a human-preference dataset and train a Value Model to guide interpretable, value-aligned trajectory assessment. Experimental results show that our method substantially improves planning performance while remaining compatible with existing architectures. Notably, KnowVal achieves the lowest collision rate on nuScenes and state-of-the-art results on Bench2Drive.

