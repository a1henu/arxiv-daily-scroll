---
layout: default
title: Spatial Chain-of-Thought: Bridging Understanding and Generation Models for Spatial Reasoning Generation
---

# Spatial Chain-of-Thought: Bridging Understanding and Generation Models for Spatial Reasoning Generation
**arXiv**：[2602.11980v1](https://arxiv.org/abs/2602.11980) · [PDF](https://arxiv.org/pdf/2602.11980.pdf)  
**作者**：Wei Chen, Yancheng Long, Mingqiao Liu, Haojie Ding, Yankai Yang, Hongyang Wei, Yi-Fan Zhang, Bin Wen, Fan Yang, Tingting Gao, Han Li, Long Chen  

**一句话要点**：提出空间思维链框架，以增强扩散模型在复杂空间推理生成中的能力。

**关键词**：空间推理生成, 扩散模型增强, 多模态大语言模型, 布局规划, 图像生成, 图像编辑

## 3 点简述
- 核心问题：扩散模型在复杂空间理解和推理方面存在不足，现有方法计算成本高或信息损失。
- 方法要点：通过文本-坐标指令训练增强布局感知，利用多模态大语言模型作为规划器生成布局计划。
- 实验或效果：在图像生成基准上达到先进性能，复杂推理任务显著优于基线，图像编辑场景有效。

## 摘要（原文）

> While diffusion models have shown exceptional capabilities in aesthetic image synthesis, they often struggle with complex spatial understanding and reasoning. Existing approaches resort to Multimodal Large Language Models (MLLMs) to enhance this capability. However, they either incur high computational costs through joint training or suffer from spatial information loss when relying solely on textual prompts. To alleviate these limitations, we propose a Spatial Chain-of-Thought (SCoT) framework, a plug-and-play approach that effectively bridges the reasoning capabilities of MLLMs with the generative power of diffusion models. Specifically, we first enhance the diffusion model's layout awareness by training it on an interleaved text-coordinate instruction format. We then leverage state-of-the-art MLLMs as planners to generate comprehensive layout plans, transferring their spatial planning capabilities directly to the generation process. Extensive experiments demonstrate that our method achieves state-of-the-art performance on image generation benchmarks and significantly outperforms baselines on complex reasoning tasks, while also showing strong efficacy in image editing scenarios.

