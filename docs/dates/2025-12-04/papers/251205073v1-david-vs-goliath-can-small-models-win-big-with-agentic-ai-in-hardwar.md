---
layout: default
title: David vs. Goliath: Can Small Models Win Big with Agentic AI in Hardware Design?
---

# David vs. Goliath: Can Small Models Win Big with Agentic AI in Hardware Design?
**arXiv**：[2512.05073v1](https://arxiv.org/abs/2512.05073) · [PDF](https://arxiv.org/pdf/2512.05073.pdf)  
**作者**：Shashwat Shankar, Subhranshu Pandey, Innocent Dengkhw Mochahari, Bhabesh Mali, Animesh Basak Chowdhury, Sukanta Bhattacharjee, Chandan Karfa  

**一句话要点**：提出小型模型结合代理AI框架，在硬件设计中实现高效性能

**关键词**：硬件设计, 小型语言模型, 代理AI框架, 任务分解, 迭代反馈, CVDP基准

## 3 点简述
- 核心问题：大型语言模型推理成本高，硬件设计任务需可持续解决方案
- 方法要点：使用小型模型与代理AI框架，通过任务分解和迭代反馈优化设计
- 实验或效果：在CVDP基准测试中，代理工作流以低成本实现接近LLM的性能

## 摘要（原文）

> Large Language Model(LLM) inference demands massive compute and energy, making domain-specific tasks expensive and unsustainable. As foundation models keep scaling, we ask: Is bigger always better for hardware design? Our work tests this by evaluating Small Language Models coupled with a curated agentic AI framework on NVIDIA's Comprehensive Verilog Design Problems(CVDP) benchmark. Results show that agentic workflows: through task decomposition, iterative feedback, and correction - not only unlock near-LLM performance at a fraction of the cost but also create learning opportunities for agents, paving the way for efficient, adaptive solutions in complex design tasks.

