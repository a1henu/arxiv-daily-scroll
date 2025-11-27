---
layout: default
title: ToolOrchestra: Elevating Intelligence via Efficient Model and Tool Orchestration
---

# ToolOrchestra: Elevating Intelligence via Efficient Model and Tool Orchestration
**arXiv**：[2511.21689v1](https://arxiv.org/abs/2511.21689) · [PDF](https://arxiv.org/pdf/2511.21689.pdf)  
**作者**：Hongjin Su, Shizhe Diao, Ximing Lu, Mingjie Liu, Jiacheng Xu, Xin Dong, Yonggan Fu, Peter Belcak, Hanrong Ye, Hongxu Yin, Yi Dong, Evelina Bakhturina, Tao Yu, Yejin Choi, Jan Kautz, Pavlo Molchanov  

**一句话要点**：提出ToolOrchestra方法，通过小模型协调工具以高效解决复杂智能任务

**关键词**：模型协调, 工具使用, 强化学习, 效率优化, 智能代理

## 3 点简述
- 核心问题：大语言模型解决复杂任务时概念挑战高且计算成本大
- 方法要点：使用强化学习训练小协调器，结合结果、效率和用户偏好奖励
- 实验或效果：在HLE等基准上超越GPT-5，成本降低2.5倍以上

## 摘要（原文）

> Large language models are powerful generalists, yet solving deep and complex problems such as those of the Humanity's Last Exam (HLE) remains both conceptually challenging and computationally expensive. We show that small orchestrators managing other models and a variety of tools can both push the upper bound of intelligence and improve efficiency in solving difficult agentic tasks. We introduce ToolOrchestra, a method for training small orchestrators that coordinate intelligent tools. ToolOrchestra explicitly uses reinforcement learning with outcome-, efficiency-, and user-preference-aware rewards. Using ToolOrchestra, we produce Orchestrator, an 8B model that achieves higher accuracy at lower cost than previous tool-use agents while aligning with user preferences on which tools are to be used for a given query. On HLE, Orchestrator achieves a score of 37.1%, outperforming GPT-5 (35.1%) while being 2.5x more efficient. On tau2-Bench and FRAMES, Orchestrator surpasses GPT-5 by a wide margin while using only about 30% of the cost. Extensive analysis shows that Orchestrator achieves the best trade-off between performance and cost under multiple metrics, and generalizes robustly to unseen tools. These results demonstrate that composing diverse tools with a lightweight orchestration model is both more efficient and more effective than existing methods, paving the way for practical and scalable tool-augmented reasoning systems.

