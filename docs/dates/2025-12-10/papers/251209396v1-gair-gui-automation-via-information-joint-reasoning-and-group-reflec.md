---
layout: default
title: GAIR: GUI Automation via Information-Joint Reasoning and Group Reflection
---

# GAIR: GUI Automation via Information-Joint Reasoning and Group Reflection
**arXiv**：[2512.09396v1](https://arxiv.org/abs/2512.09396) · [PDF](https://arxiv.org/pdf/2512.09396.pdf)  
**作者**：Zishu Wei, Qixiang Ma, Xavier Hu, Yuhang Liu, Hui Zang, Yudong Zhao, Tao Wang, Shengyu Zhang, Fei Wu  

**一句话要点**：提出GAIR框架，通过信息联合推理与群体反思提升GUI自动化任务性能

**关键词**：GUI自动化, 多模态大语言模型, 异构模型集成, 信息联合推理, 群体反思

## 3 点简述
- 核心问题：GUI自动化任务多样，需异构模型能力，构建高性能系统困难
- 方法要点：引入通用MLLM联合处理多GUI专用模型信息，决策时触发群体反思优化信息收集
- 实验或效果：在GUI基准测试中验证了框架的有效性和可靠性

## 摘要（原文）

> Building AI systems for GUI automation task has attracted remarkable research efforts, where MLLMs are leveraged for processing user requirements and give operations. However, GUI automation includes a wide range of tasks, from document processing to online shopping, from CAD to video editing. Diversity between particular tasks requires MLLMs for GUI automation to have heterogeneous capabilities and master multidimensional expertise, raising problems on constructing such a model. To address such challenge, we propose GAIR: GUI Automation via Information-Joint Reasoning and Group Reflection, a novel MLLM-based GUI automation agent framework designed for integrating knowledge and combining capabilities from heterogeneous models to build GUI automation agent systems with higher performance. Since different GUI-specific MLLMs are trained on different dataset and thus have different strengths, GAIR introduced a general-purpose MLLM for jointly processing the information from multiple GUI-specific models, further enhancing performance of the agent framework. The general-purpose MLLM also serves as decision maker, trying to execute a reasonable operation based on previously gathered information. When the general-purpose model thinks that there isn't sufficient information for a reasonable decision, GAIR would transit into group reflection status, where the general-purpose model would provide GUI-specific models with different instructions and hints based on their strengths and weaknesses, driving them to gather information with more significance and accuracy that can support deeper reasoning and decision. We evaluated the effectiveness and reliability of GAIR through extensive experiments on GUI benchmarks.

