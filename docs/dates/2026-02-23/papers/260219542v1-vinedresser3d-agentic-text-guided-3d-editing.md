---
layout: default
title: Vinedresser3D: Agentic Text-guided 3D Editing
---

# Vinedresser3D: Agentic Text-guided 3D Editing
**arXiv**：[2602.19542v1](https://arxiv.org/abs/2602.19542) · [PDF](https://arxiv.org/pdf/2602.19542.pdf)  
**作者**：Yankuan Chi, Xiang Li, Zixuan Huang, James M. Rehg  

**一句话要点**：提出Vinedresser3D代理框架，用于高质量文本引导的3D编辑，直接操作于原生3D生成模型的潜在空间。

**关键词**：文本引导3D编辑, 代理框架, 潜在空间编辑, 多模态大语言模型, 反演修复流, 3D一致性

## 3 点简述
- 当前方法难以联合理解复杂提示、自动定位3D编辑区域并保留未编辑内容。
- 框架使用多模态大语言模型推断资产描述、识别编辑区域和类型，并生成分解的结构与外观文本指导。
- 实验表明，Vinedresser3D在自动指标和人类偏好研究中优于先前基线，实现精确、连贯且无需掩码的3D编辑。

## 摘要（原文）

> Text-guided 3D editing aims to modify existing 3D assets using natural-language instructions. Current methods struggle to jointly understand complex prompts, automatically localize edits in 3D, and preserve unedited content. We introduce Vinedresser3D, an agentic framework for high-quality text-guided 3D editing that operates directly in the latent space of a native 3D generative model. Given a 3D asset and an editing prompt, Vinedresser3D uses a multimodal large language model to infer rich descriptions of the original asset, identify the edit region and edit type (addition, modification, deletion), and generate decomposed structural and appearance-level text guidance. The agent then selects an informative view and applies an image editing model to obtain visual guidance. Finally, an inversion-based rectified-flow inpainting pipeline with an interleaved sampling module performs editing in the 3D latent space, enforcing prompt alignment while maintaining 3D coherence and unedited regions. Experiments on diverse 3D edits demonstrate that Vinedresser3D outperforms prior baselines in both automatic metrics and human preference studies, while enabling precise, coherent, and mask-free 3D editing.

