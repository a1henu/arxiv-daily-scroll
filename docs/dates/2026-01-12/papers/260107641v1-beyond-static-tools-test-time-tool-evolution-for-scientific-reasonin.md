---
layout: default
title: Beyond Static Tools: Test-Time Tool Evolution for Scientific Reasoning
---

# Beyond Static Tools: Test-Time Tool Evolution for Scientific Reasoning
**arXiv**：[2601.07641v1](https://arxiv.org/abs/2601.07641) · [PDF](https://arxiv.org/pdf/2601.07641.pdf)  
**作者**：Jiaxuan Lu, Ziyu Kong, Yemin Wang, Rong Fu, Haiyuan Wan, Cheng Yang, Wenjie Lou, Haoran Sun, Lilong Wang, Yankai Jiang, Xiaosong Wang, Xiao Sun, Dongzhan Zhou  

**一句话要点**：提出测试时工具演化以解决科学推理中静态工具库的局限性

**关键词**：科学推理, 工具演化, LLM代理, 测试时学习, 跨域适应

## 3 点简述
- 核心问题：现有LLM代理依赖静态预定义工具库，在科学领域工具稀疏、异构且不完整时失效
- 方法要点：在推理过程中合成、验证和演化可执行工具，将工具从固定资源转化为问题驱动产物
- 实验或效果：在SciEvo基准上实现最先进性能，支持跨领域工具适应，代码和基准已开源

## 摘要（原文）

> The central challenge of AI for Science is not reasoning alone, but the ability to create computational methods in an open-ended scientific world. Existing LLM-based agents rely on static, pre-defined tool libraries, a paradigm that fundamentally fails in scientific domains where tools are sparse, heterogeneous, and intrinsically incomplete. In this paper, we propose Test-Time Tool Evolution (TTE), a new paradigm that enables agents to synthesize, verify, and evolve executable tools during inference. By transforming tools from fixed resources into problem-driven artifacts, TTE overcomes the rigidity and long-tail limitations of static tool libraries. To facilitate rigorous evaluation, we introduce SciEvo, a benchmark comprising 1,590 scientific reasoning tasks supported by 925 automatically evolved tools. Extensive experiments show that TTE achieves state-of-the-art performance in both accuracy and tool efficiency, while enabling effective cross-domain adaptation of computational tools. The code and benchmark have been released at https://github.com/lujiaxuan0520/Test-Time-Tool-Evol.

