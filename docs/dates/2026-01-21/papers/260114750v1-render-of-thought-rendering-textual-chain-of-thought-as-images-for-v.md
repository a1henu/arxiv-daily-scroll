---
layout: default
title: Render-of-Thought: Rendering Textual Chain-of-Thought as Images for Visual Latent Reasoning
---

# Render-of-Thought: Rendering Textual Chain-of-Thought as Images for Visual Latent Reasoning
**arXiv**：[2601.14750v1](https://arxiv.org/abs/2601.14750) · [PDF](https://arxiv.org/pdf/2601.14750.pdf)  
**作者**：Yifan Wang, Shiyu Li, Peiming Li, Xiaochen Yang, Yang Tang, Zheng Wei  

**一句话要点**：提出Render-of-Thought框架，通过将文本推理链渲染为图像以解决视觉潜在推理中的计算开销和可分析性问题。

**关键词**：推理链可视化, 视觉语言模型, 计算效率优化, 潜在推理分析, 令牌压缩

## 3 点简述
- 核心问题：CoT提示冗长导致计算开销大，且中间推理过程缺乏监督，影响潜在推理链的可分析性。
- 方法要点：利用现有视觉语言模型的视觉编码器作为语义锚点，将文本推理步骤渲染为图像，实现即插即用。
- 实验或效果：在数学和逻辑推理基准测试中，实现3-4倍令牌压缩和显著推理加速，性能保持竞争力。

## 摘要（原文）

> Chain-of-Thought (CoT) prompting has achieved remarkable success in unlocking the reasoning capabilities of Large Language Models (LLMs). Although CoT prompting enhances reasoning, its verbosity imposes substantial computational overhead. Recent works often focus exclusively on outcome alignment and lack supervision on the intermediate reasoning process. These deficiencies obscure the analyzability of the latent reasoning chain. To address these challenges, we introduce Render-of-Thought (RoT), the first framework to reify the reasoning chain by rendering textual steps into images, making the latent rationale explicit and traceable. Specifically, we leverage the vision encoders of existing Vision Language Models (VLMs) as semantic anchors to align the vision embeddings with the textual space. This design ensures plug-and-play implementation without incurring additional pre-training overhead. Extensive experiments on mathematical and logical reasoning benchmarks demonstrate that our method achieves 3-4x token compression and substantial inference acceleration compared to explicit CoT. Furthermore, it maintains competitive performance against other methods, validating the feasibility of this paradigm. Our code is available at https://github.com/TencentBAC/RoT

