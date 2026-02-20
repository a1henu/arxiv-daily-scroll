---
layout: default
title: RetouchIQ: MLLM Agents for Instruction-Based Image Retouching with Generalist Reward
---

# RetouchIQ: MLLM Agents for Instruction-Based Image Retouching with Generalist Reward
**arXiv**：[2602.17558v1](https://arxiv.org/abs/2602.17558) · [PDF](https://arxiv.org/pdf/2602.17558.pdf)  
**作者**：Qiucheng Wu, Jing Shi, Simon Jenni, Kushal Kafle, Tianyu Wang, Shiyu Chang, Handong Zhao  

**一句话要点**：提出RetouchIQ框架，通过通用奖励模型驱动的MLLM代理实现基于指令的图像精修。

**关键词**：多模态大语言模型, 强化学习, 图像编辑, 奖励模型, 指令执行, 专业软件集成

## 3 点简述
- 核心问题：专业图像编辑中缺乏可靠奖励信号，难以训练MLLM代理进行主观性编辑。
- 方法要点：引入通用奖励模型，基于多模态推理生成案例特定指标，提供高质量强化学习梯度。
- 实验或效果：在19万指令-推理对数据集上验证，显著提升语义一致性和感知质量。

## 摘要（原文）

> Recent advances in multimodal large language models (MLLMs) have shown great potential for extending vision-language reasoning to professional tool-based image editing, enabling intuitive and creative editing. A promising direction is to use reinforcement learning (RL) to enable MLLMs to reason about and execute optimal tool-use plans within professional image-editing software. However, training remains challenging due to the lack of reliable, verifiable reward signals that can reflect the inherently subjective nature of creative editing. In this work, we introduce RetouchIQ, a framework that performs instruction-based executable image editing through MLLM agents guided by a generalist reward model. RetouchIQ interprets user-specified editing intentions and generates corresponding, executable image adjustments, bridging high-level aesthetic goals with precise parameter control. To move beyond conventional, rule-based rewards that compute similarity against a fixed reference image using handcrafted metrics, we propose a generalist reward model, an RL fine-tuned MLLM that evaluates edited results through a set of generated metrics on a case-by-case basis. Then, the reward model provides scalar feedback through multimodal reasoning, enabling reinforcement learning with high-quality, instruction-consistent gradients. We curate an extended dataset with 190k instruction-reasoning pairs and establish a new benchmark for instruction-based image editing. Experiments show that RetouchIQ substantially improves both semantic consistency and perceptual quality over previous MLLM-based and diffusion-based editing systems. Our findings demonstrate the potential of generalist reward-driven MLLM agents as flexible, explainable, and executable assistants for professional image editing.

