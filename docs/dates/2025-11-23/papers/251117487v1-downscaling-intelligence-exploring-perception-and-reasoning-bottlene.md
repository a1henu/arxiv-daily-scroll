---
layout: default
title: Downscaling Intelligence: Exploring Perception and Reasoning Bottlenecks in Small Multimodal Models
---

# Downscaling Intelligence: Exploring Perception and Reasoning Bottlenecks in Small Multimodal Models
**arXiv**：[2511.17487v1](https://arxiv.org/abs/2511.17487) · [PDF](https://arxiv.org/pdf/2511.17487.pdf)  
**作者**：Mark Endo, Serena Yeung-Levy  

**一句话要点**：提出Extract+Think方法以解决小多模态模型中感知与推理瓶颈问题

**关键词**：小多模态模型, 视觉提取调优, 逐步推理, 感知瓶颈, LLM缩小化

## 3 点简述
- 核心问题：LLM缩小化导致视觉能力下降，可能影响感知而非仅推理
- 方法要点：引入视觉提取调优，训练模型提取指令相关视觉细节
- 实验或效果：结合逐步推理，提升小模型效率与性能，设定新标准

## 摘要（原文）

> Scaling up multimodal models has enabled remarkable advances in visual understanding and reasoning, but practical demands call for smaller, efficient systems. In this work, we conduct a principled analysis of downscaling intelligence in multimodal models, examining how reduced large language model (LLM) capacity affects multimodal capabilities. Our initial findings reveal an interesting trend: LLM downscaling disproportionately affects visual capabilities, rather than abilities inherited from the LLM. We then examine whether this drop mainly reflects the expected decline in visual reasoning or a more fundamental loss of perceptual abilities. Isolating the effect of LLM downscaling on perception, we find performance still drops sharply, often matching or exceeding the impact on reasoning. To address this bottleneck, we introduce visual extraction tuning, which explicitly trains the model to extract instruction-relevant visual details consistently across tasks. With these extracted visual details, we then apply step-by-step reasoning to generate answers. Together, these components form our Extract+Think approach, setting a new standard for efficiency and performance in this space.

