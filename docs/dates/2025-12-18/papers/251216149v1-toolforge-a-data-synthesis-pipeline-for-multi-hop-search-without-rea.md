---
layout: default
title: ToolForge: A Data Synthesis Pipeline for Multi-Hop Search without Real-World APIs
---

# ToolForge: A Data Synthesis Pipeline for Multi-Hop Search without Real-World APIs
**arXiv**：[2512.16149v1](https://arxiv.org/abs/2512.16149) · [PDF](https://arxiv.org/pdf/2512.16149.pdf)  
**作者**：Hao Chen, Zhexin Hu, Jiajun Chai, Haocheng Yang, Hang He, Xiaohan Wang, Wei Lin, Luhang Wang, Guojun Yin, Zhuofeng zhao  

**一句话要点**：提出ToolForge框架，通过虚拟工具合成多跳搜索数据，无需真实API调用。

**关键词**：工具调用, 数据合成, 多跳搜索, 自反思, 验证框架

## 3 点简述
- 核心问题：现有合成数据生成依赖大量真实API调用，成本高且缺乏多跳推理。
- 方法要点：基于（问题、黄金上下文、答案）三元组，结合多跳推理和自反思机制合成数据。
- 实验或效果：8B参数模型在合成数据上训练后，在多个基准上超越GPT-4o。

## 摘要（原文）

> Training LLMs to invoke tools and leverage retrieved information necessitates high-quality, diverse data. However, existing pipelines for synthetic data generation often rely on tens of thousands of real API calls to enhance generalization, incurring prohibitive costs while lacking multi-hop reasoning and self-reflection. To address these limitations, we introduce ToolForge, an automated synthesis framework that achieves strong real-world tool-calling performance by constructing only a small number of virtual tools, eliminating the need for real API calls. ToolForge leverages a (question, golden context, answer) triple to synthesize large-scale tool-learning data specifically designed for multi-hop search scenarios, further enriching the generated data through multi-hop reasoning and self-reflection mechanisms. To ensure data fidelity, we employ a Multi-Layer Validation Framework that integrates both rule-based and model-based assessments. Empirical results show that a model with only 8B parameters, when trained on our synthesized data, outperforms GPT-4o on multiple benchmarks. Our code and dataset are publicly available at https://github.com/Buycar-arb/ToolForge .

