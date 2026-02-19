---
layout: default
title: Team of Thoughts: Efficient Test-time Scaling of Agentic Systems through Orchestrated Tool Calling
---

# Team of Thoughts: Efficient Test-time Scaling of Agentic Systems through Orchestrated Tool Calling
**arXiv**：[2602.16485v1](https://arxiv.org/abs/2602.16485) · [PDF](https://arxiv.org/pdf/2602.16485.pdf)  
**作者**：Jeffrey T. H. Wong, Zixi Zhang, Junyi Liu, Yiren Zhao  

**一句话要点**：提出Team-of-Thoughts架构，通过编排异构代理解决多智能体系统静态同质化问题。

**关键词**：多智能体系统, 异构代理, 编排器校准, 自评估协议, 推理基准, 代码生成

## 3 点简述
- 现有MAS依赖静态同质模型，无法利用不同后训练模型的优势。
- 引入编排器校准和自评估协议，动态激活最合适的工具代理。
- 在推理和代码生成基准上表现优于同质基线，如AIME24准确率达96.67%。

## 摘要（原文）

> Existing Multi-Agent Systems (MAS) typically rely on static, homogeneous model configurations, limiting their ability to exploit the distinct strengths of differently post-trained models. To address this, we introduce Team-of-Thoughts, a novel MAS architecture that leverages the complementary capabilities of heterogeneous agents via an orchestrator-tool paradigm. Our framework introduces two key mechanisms to optimize performance: (1) an orchestrator calibration scheme that identifies models with superior coordination capabilities, and (2) a self-assessment protocol where tool agents profile their own domain expertise to account for variations in post-training skills. During inference, the orchestrator dynamically activates the most suitable tool agents based on these proficiency profiles. Experiments on five reasoning and code generation benchmarks show that Team-of-Thoughts delivers consistently superior task performance. Notably, on AIME24 and LiveCodeBench, our approach achieves accuracies of 96.67% and 72.53%, respectively, substantially outperforming homogeneous role-play baselines, which score 80% and 65.93%.

