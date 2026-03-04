---
layout: default
title: Seeing Clearly without Training: Mitigating Hallucinations in Multimodal LLMs for Remote Sensing
---

# Seeing Clearly without Training: Mitigating Hallucinations in Multimodal LLMs for Remote Sensing
**arXiv**：[2603.02754v1](https://arxiv.org/abs/2603.02754) · [PDF](https://arxiv.org/pdf/2603.02754.pdf)  
**作者**：Yi Liu, Jing Zhang, Di Wang, Xiaoyu Tian, Haonan Guo, Bo Du  

**一句话要点**：提出RADAR方法以缓解遥感视觉问答中多模态大模型的幻觉问题

**关键词**：遥感视觉问答, 多模态大模型, 幻觉缓解, 无训练推理, 视觉定位, 细粒度分析

## 3 点简述
- 核心问题：多模态大模型在遥感视觉问答中因视觉定位失败或细粒度目标误读产生显著幻觉
- 方法要点：RADAR利用模型内在注意力进行无训练推理，通过渐进定位和细粒度局部推理缓解幻觉
- 实验或效果：在多种多模态大模型上验证，RADAR能提升性能并减少事实和逻辑幻觉

## 摘要（原文）

> Multimodal large language models (MLLMs) suffer from pronounced hallucinations in remote sensing visual question-answering (RS-VQA), primarily caused by visual grounding failures in large-scale scenes or misinterpretation of fine-grained small targets. To systematically analyze these issues, we introduce RSHBench, a protocol-based benchmark for fine-grained diagnosis of factual and logical hallucinations. To mitigate grounding-induced factual hallucinations, we further propose Relative Attention-Driven Actively Reasoning (RADAR), a training-free inference method that leverages intrinsic attention in MLLMs to guide progressive localization and fine-grained local reasoning at test time. Extensive experiments across diverse MLLMs demonstrate that RADAR consistently improves RS-VQA performance and reduces both factual and logical hallucinations. Code and data will be publicly available at: https://github.com/MiliLab/RADAR

