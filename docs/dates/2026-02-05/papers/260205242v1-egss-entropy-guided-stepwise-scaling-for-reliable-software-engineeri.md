---
layout: default
title: EGSS: Entropy-guided Stepwise Scaling for Reliable Software Engineering
---

# EGSS: Entropy-guided Stepwise Scaling for Reliable Software Engineering
**arXiv**：[2602.05242v1](https://arxiv.org/abs/2602.05242) · [PDF](https://arxiv.org/pdf/2602.05242.pdf)  
**作者**：Chenhui Mao, Yuanting Lei, Zhixiang Wei, Ming Liang, Zhixiang Wang, Jingxuan Xu, Dajun Chen, Wei Jiang, Yong Li  

**一句话要点**：提出EGSS框架以解决Agentic TTS在软件工程任务中的计算开销和候选选择问题

**关键词**：软件工程, 测试时缩放, 熵引导搜索, 计算效率, 代码生成, 集成学习

## 3 点简述
- 核心问题：Agentic TTS因大集成部署成本高和缺乏可靠候选选择机制，导致计算开销大且性能受限
- 方法要点：EGSS通过熵引导自适应搜索和鲁棒测试套件增强，动态平衡效率与效果
- 实验或效果：在SWE-Bench-Verified上提升性能5-10%，减少推理令牌使用超28%，实现效果与效率双重提升

## 摘要（原文）

> Agentic Test-Time Scaling (TTS) has delivered state-of-the-art (SOTA) performance on complex software engineering tasks such as code generation and bug fixing. However, its practical adoption remains limited due to significant computational overhead, primarily driven by two key challenges: (1) the high cost associated with deploying excessively large ensembles, and (2) the lack of a reliable mechanism for selecting the optimal candidate solution, ultimately constraining the performance gains that can be realized. To address these challenges, we propose Entropy-Guided Stepwise Scaling (EGSS), a novel TTS framework that dynamically balances efficiency and effectiveness through entropy-guided adaptive search and robust test-suite augmentation. Extensive experiments on SWE-Bench-Verified demonstrate that EGSS consistently boosts performance by 5-10% across all evaluated models. Specifically, it increases the resolved ratio of Kimi-K2-Intruct from 63.2% to 72.2%, and GLM-4.6 from 65.8% to 74.6%. Furthermore, when paired with GLM-4.6, EGSS achieves a new state-of-the-art among open-source large language models. In addition to these accuracy improvements, EGSS reduces inference-time token usage by over 28% compared to existing TTS methods, achieving simultaneous gains in both effectiveness and computational efficiency.

