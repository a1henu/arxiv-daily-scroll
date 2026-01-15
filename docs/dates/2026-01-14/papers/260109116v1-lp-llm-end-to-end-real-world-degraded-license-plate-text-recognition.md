---
layout: default
title: LP-LLM: End-to-End Real-World Degraded License Plate Text Recognition via Large Multimodal Models
---

# LP-LLM: End-to-End Real-World Degraded License Plate Text Recognition via Large Multimodal Models
**arXiv**：[2601.09116v1](https://arxiv.org/abs/2601.09116) · [PDF](https://arxiv.org/pdf/2601.09116.pdf)  
**作者**：Haoyan Gong, Hongbin Liu  

**一句话要点**：提出基于Qwen3-VL的端到端结构感知多模态推理框架，以解决真实世界车牌识别中的严重退化问题。

**关键词**：车牌识别, 多模态推理, 端到端学习, 结构感知建模, 参数高效微调, 退化文本识别

## 3 点简述
- 核心问题：真实世界车牌识别面临运动模糊、低分辨率等退化，现有两阶段方法因像素级优化与语义目标不匹配导致误差累积。
- 方法要点：引入字符感知多模态推理模块，通过可学习字符槽查询实现细粒度证据检索，结合残差调制注入结构先验，并采用LoRA进行参数高效微调。
- 实验或效果：在合成和真实严重退化数据集上显著优于现有方法，验证了结构推理在大模型中处理低质量文本识别的优势。

## 摘要（原文）

> Real-world License Plate Recognition (LPR) faces significant challenges from severe degradations such as motion blur, low resolution, and complex illumination. The prevailing "restoration-then-recognition" two-stage paradigm suffers from a fundamental flaw: the pixel-level optimization objectives of image restoration models are misaligned with the semantic goals of character recognition, leading to artifact interference and error accumulation. While Vision-Language Models (VLMs) have demonstrated powerful general capabilities, they lack explicit structural modeling for license plate character sequences (e.g., fixed length, specific order). To address this, we propose an end-to-end structure-aware multimodal reasoning framework based on Qwen3-VL. The core innovation lies in the Character-Aware Multimodal Reasoning Module (CMRM), which introduces a set of learnable Character Slot Queries. Through a cross-attention mechanism, these queries actively retrieve fine-grained evidence corresponding to character positions from visual features. Subsequently, we inject these character-aware representations back into the visual tokens via residual modulation, enabling the language model to perform autoregressive generation based on explicit structural priors. Furthermore, combined with the LoRA parameter-efficient fine-tuning strategy, the model achieves domain adaptation while retaining the generalization capabilities of the large model. Extensive experiments on both synthetic and real-world severely degraded datasets demonstrate that our method significantly outperforms existing restoration-recognition combinations and general VLMs, validating the superiority of incorporating structured reasoning into large models for low-quality text recognition tasks.

