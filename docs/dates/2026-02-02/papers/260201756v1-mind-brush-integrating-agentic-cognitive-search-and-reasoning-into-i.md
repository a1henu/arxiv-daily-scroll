---
layout: default
title: Mind-Brush: Integrating Agentic Cognitive Search and Reasoning into Image Generation
---

# Mind-Brush: Integrating Agentic Cognitive Search and Reasoning into Image Generation
**arXiv**：[2602.01756v1](https://arxiv.org/abs/2602.01756) · [PDF](https://arxiv.org/pdf/2602.01756.pdf)  
**作者**：Jun He, Junyan Ye, Zilong Huang, Dongzhi Jiang, Chenjue Zhang, Leqi Zhu, Renrui Zhang, Xiang Zhang, Weijia Li  

**一句话要点**：提出Mind-Brush框架，通过动态知识检索与推理增强图像生成中的意图理解

**关键词**：文本到图像生成, 知识驱动推理, 多模态检索, 意图理解, 基准评估

## 3 点简述
- 现有文本到图像模型难以理解隐含意图和进行复杂知识推理
- Mind-Brush采用类人'思考-研究-创作'范式，集成多模态检索和推理工具
- 在Mind-Bench基准上显著提升Qwen-Image基线性能，并在WISE和RISE基准取得优越结果

## 摘要（原文）

> While text-to-image generation has achieved unprecedented fidelity, the vast majority of existing models function fundamentally as static text-to-pixel decoders. Consequently, they often fail to grasp implicit user intentions. Although emerging unified understanding-generation models have improved intent comprehension, they still struggle to accomplish tasks involving complex knowledge reasoning within a single model. Moreover, constrained by static internal priors, these models remain unable to adapt to the evolving dynamics of the real world. To bridge these gaps, we introduce Mind-Brush, a unified agentic framework that transforms generation into a dynamic, knowledge-driven workflow. Simulating a human-like 'think-research-create' paradigm, Mind-Brush actively retrieves multimodal evidence to ground out-of-distribution concepts and employs reasoning tools to resolve implicit visual constraints. To rigorously evaluate these capabilities, we propose Mind-Bench, a comprehensive benchmark comprising 500 distinct samples spanning real-time news, emerging concepts, and domains such as mathematical and Geo-Reasoning. Extensive experiments demonstrate that Mind-Brush significantly enhances the capabilities of unified models, realizing a zero-to-one capability leap for the Qwen-Image baseline on Mind-Bench, while achieving superior results on established benchmarks like WISE and RISE.

