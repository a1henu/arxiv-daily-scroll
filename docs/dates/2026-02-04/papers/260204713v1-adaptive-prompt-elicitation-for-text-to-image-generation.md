---
layout: default
title: Adaptive Prompt Elicitation for Text-to-Image Generation
---

# Adaptive Prompt Elicitation for Text-to-Image Generation
**arXiv**：[2602.04713v1](https://arxiv.org/abs/2602.04713) · [PDF](https://arxiv.org/pdf/2602.04713.pdf)  
**作者**：Xinyi Wen, Lena Hegemann, Xiaofu Jin, Shuai Ma, Antti Oulasvirta  

**一句话要点**：提出自适应提示引导技术，以解决文本到图像生成中用户意图对齐的挑战。

**关键词**：文本到图像生成, 意图对齐, 自适应提示, 信息论框架, 用户交互, 视觉查询

## 3 点简述
- 核心问题：用户输入模糊且难以适应模型特性，导致意图对齐困难。
- 方法要点：基于信息论框架，通过语言模型先验表示潜在意图，自适应生成视觉查询并编译为有效提示。
- 实验或效果：在IDEA-Bench和DesignBench评估中显示对齐增强且效率提升，用户研究任务对齐度提高19.8%。

## 摘要（原文）

> Aligning text-to-image generation with user intent remains challenging, for users who provide ambiguous inputs and struggle with model idiosyncrasies. We propose Adaptive Prompt Elicitation (APE), a technique that adaptively asks visual queries to help users refine prompts without extensive writing. Our technical contribution is a formulation of interactive intent inference under an information-theoretic framework. APE represents latent intent as interpretable feature requirements using language model priors, adaptively generates visual queries, and compiles elicited requirements into effective prompts. Evaluation on IDEA-Bench and DesignBench shows that APE achieves stronger alignment with improved efficiency. A user study with challenging user-defined tasks demonstrates 19.8% higher alignment without workload overhead. Our work contributes a principled approach to prompting that, for general users, offers an effective and efficient complement to the prevailing prompt-based interaction paradigm with text-to-image models.

