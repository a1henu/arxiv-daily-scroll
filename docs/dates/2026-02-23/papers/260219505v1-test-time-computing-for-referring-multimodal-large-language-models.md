---
layout: default
title: Test-Time Computing for Referring Multimodal Large Language Models
---

# Test-Time Computing for Referring Multimodal Large Language Models
**arXiv**：[2602.19505v1](https://arxiv.org/abs/2602.19505) · [PDF](https://arxiv.org/pdf/2602.19505.pdf)  
**作者**：Mingrui Wu, Hao Chen, Jiayi Ji, Xiaoshuai Sun, Zhiyuan Liu, Liujuan Cao, Ming-Ming Cheng, Rongrong Ji  

**一句话要点**：提出ControlMLLM++，通过测试时注入可学习视觉提示，实现无需重训练的多模态大语言模型细粒度区域推理。

**关键词**：测试时适应, 多模态大语言模型, 视觉提示, 区域推理, 注意力引导, 跨模态对应

## 3 点简述
- 核心问题：多模态大语言模型在测试时难以进行细粒度区域视觉推理，需避免模型重训练或微调。
- 方法要点：利用跨模态注意力图编码语义对应，优化潜在视觉令牌修饰符，结合改进优化策略和提示去偏机制。
- 实验或效果：支持多种视觉提示类型，展示强域外泛化能力和可解释性，代码已开源。

## 摘要（原文）

> We propose ControlMLLM++, a novel test-time adaptation framework that injects learnable visual prompts into frozen multimodal large language models (MLLMs) to enable fine-grained region-based visual reasoning without any model retraining or fine-tuning. Leveraging the insight that cross-modal attention maps intrinsically encode semantic correspondences between textual tokens and visual regions, ControlMLLM++ optimizes a latent visual token modifier during inference via a task-specific energy function to steer model attention towards user-specified areas. To enhance optimization stability and mitigate language prompt biases, ControlMLLM++ incorporates an improved optimization strategy (Optim++) and a prompt debiasing mechanism (PromptDebias). Supporting diverse visual prompt types including bounding boxes, masks, scribbles, and points, our method demonstrates strong out-of-domain generalization and interpretability. The code is available at https://github.com/mrwu-mac/ControlMLLM.

