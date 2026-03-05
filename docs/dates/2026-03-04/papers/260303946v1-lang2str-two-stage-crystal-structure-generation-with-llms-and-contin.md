---
layout: default
title: Lang2Str: Two-Stage Crystal Structure Generation with LLMs and Continuous Flow Models
---

# Lang2Str: Two-Stage Crystal Structure Generation with LLMs and Continuous Flow Models
**arXiv**：[2603.03946v1](https://arxiv.org/abs/2603.03946) · [PDF](https://arxiv.org/pdf/2603.03946.pdf)  
**作者**：Cong Liu, Chengyue Gong, Zhenyu Liu, Jiale Zhao, Yuxuan Zhang  

**一句话要点**：提出Lang2Str两阶段框架，结合LLM与流模型以灵活生成晶体结构

**关键词**：晶体结构生成, 两阶段生成, 大语言模型, 流模型, 材料设计, 条件生成

## 3 点简述
- 生成模型在材料发现中受限，因单阶段过程难以保证有效性与多样性
- 方法分两阶段：LLM生成几何布局描述，流模型解码为精确坐标与参数
- 实验显示在材料生成与结构预测任务中性能优越，几何与能量更接近真实

## 摘要（原文）

> Generative models hold great promise for accelerating material discovery but are often limited by their inflexible single-stage generative process in designing valid and diverse materials. To address this, we propose a two-stage generative framework, Lang2Str, that combines the strengths of large language models (LLMs) and flow-based models for flexible and precise material generation. Our method frames the generative process as a conditional generative task, where an LLM provides high-level conditions by generating descriptions of material unit cells' geometric layouts and properties. These descriptions, informed by the LLM's extensive background knowledge, ensure reasonable structure designs. A conditioned flow model then decodes these textual conditions into precise continuous coordinates and unit cell parameters. This staged approach combines the structured reasoning of LLMs and the distribution modeling capabilities of flow models. Experimental results show that our method achieves competitive performance on \textit{ab initio} material generation and crystal structure prediction tasks, with generated structures exhibiting closer alignment to ground truth in both geometry and energy levels, surpassing state-of-the-art models. The flexibility and modularity of our framework further enable fine-grained control over the generation process, potentially leading to more efficient and customizable material design.

