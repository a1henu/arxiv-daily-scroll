---
layout: default
title: LawThinker: A Deep Research Legal Agent in Dynamic Environments
---

# LawThinker: A Deep Research Legal Agent in Dynamic Environments
**arXiv**：[2602.12056v1](https://arxiv.org/abs/2602.12056) · [PDF](https://arxiv.org/pdf/2602.12056.pdf)  
**作者**：Xinyu Yang, Chenlong Deng, Tongyu Wen, Binyu Xie, Zhicheng Dou  

**一句话要点**：提出LawThinker以解决动态司法环境中法律推理的中间步骤验证问题

**关键词**：法律推理, 动态环境, 验证机制, 知识检索, 过程合规

## 3 点简述
- 核心问题：现有法律推理方法缺乏中间步骤验证机制，导致错误传播
- 方法要点：采用探索-验证-记忆策略，通过DeepVerifier模块从准确性、相关性和合规性三方面验证检索结果
- 实验或效果：在动态基准J1-EVAL上比直接推理提升24%，在过程导向指标上表现突出

## 摘要（原文）

> Legal reasoning requires not only correct outcomes but also procedurally compliant reasoning processes. However, existing methods lack mechanisms to verify intermediate reasoning steps, allowing errors such as inapplicable statute citations to propagate undetected through the reasoning chain. To address this, we propose LawThinker, an autonomous legal research agent that adopts an Explore-Verify-Memorize strategy for dynamic judicial environments. The core idea is to enforce verification as an atomic operation after every knowledge exploration step. A DeepVerifier module examines each retrieval result along three dimensions of knowledge accuracy, fact-law relevance, and procedural compliance, with a memory module for cross-round knowledge reuse in long-horizon tasks. Experiments on the dynamic benchmark J1-EVAL show that LawThinker achieves a 24% improvement over direct reasoning and an 11% gain over workflow-based methods, with particularly strong improvements on process-oriented metrics. Evaluations on three static benchmarks further confirm its generalization capability. The code is available at https://github.com/yxy-919/LawThinker-agent .

