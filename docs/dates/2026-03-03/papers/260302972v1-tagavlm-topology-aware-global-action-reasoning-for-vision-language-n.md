---
layout: default
title: TagaVLM: Topology-Aware Global Action Reasoning for Vision-Language Navigation
---

# TagaVLM: Topology-Aware Global Action Reasoning for Vision-Language Navigation
**arXiv**：[2603.02972v1](https://arxiv.org/abs/2603.02972) · [PDF](https://arxiv.org/pdf/2603.02972.pdf)  
**作者**：Jiaxing Liu, Zexi Zhang, Xiaoyan Li, Boyue Wang, Yongli Hu, Baocai Yin  

**一句话要点**：提出TagaVLM框架，通过拓扑感知增强视觉语言模型在导航任务中的全局动作推理能力。

**关键词**：视觉语言导航, 拓扑感知, 全局动作推理, 自注意力机制, 空间推理, 开源模型增强

## 3 点简述
- 核心问题：视觉语言模型在导航任务中存在架构不匹配，难以处理动态、具身和空间结构信息。
- 方法要点：引入STAR-Att机制和交错导航提示，显式注入拓扑结构到模型骨干，支持全局动作推理。
- 实验或效果：在R2R基准测试中，未见环境下的成功率达51.09%，优于先前方法，验证了针对性增强的有效性。

## 摘要（原文）

> Vision-Language Navigation (VLN) presents a unique challenge for Large Vision-Language Models (VLMs) due to their inherent architectural mismatch: VLMs are primarily pretrained on static, disembodied vision-language tasks, which fundamentally clash with the dynamic, embodied, and spatially-structured nature of navigation. Existing large-model-based methods often resort to converting rich visual and spatial information into text, forcing models to implicitly infer complex visual-topological relationships or limiting their global action capabilities. To bridge this gap, we propose TagaVLM (Topology-Aware Global Action reasoning), an end-to-end framework that explicitly injects topological structures into the VLM backbone. To introduce topological edge information, Spatial Topology Aware Residual Attention (STAR-Att) directly integrates it into the VLM's self-attention mechanism, enabling intrinsic spatial reasoning while preserving pretrained knowledge. To enhance topological node information, an Interleaved Navigation Prompt strengthens node-level visual-text alignment. Finally, with the embedded topological graph, the model is capable of global action reasoning, allowing for robust path correction. On the R2R benchmark, TagaVLM achieves state-of-the-art performance among large-model-based methods, with a Success Rate (SR) of 51.09% and SPL of 47.18 in unseen environments, outperforming prior work by 3.39% in SR and 9.08 in SPL. This demonstrates that, for embodied spatial reasoning, targeted enhancements on smaller open-source VLMs can be more effective than brute-force model scaling. The code will be released upon publication.Project page: https://apex-bjut.github.io/Taga-VLM

